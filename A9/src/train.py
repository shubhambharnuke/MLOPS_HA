import argparse
import os
import tarfile
import json
import io
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib

def model_fn(model_dir):
    """SageMaker hosting deserialization handler."""
    model_file = os.path.join(model_dir, "model.joblib")
    return joblib.load(model_file)

def input_fn(request_body, request_content_type):
    """SageMaker hosting deserialization of incoming payload."""
    if request_content_type == "application/json":
        data = json.loads(request_body)
        if isinstance(data, dict) and "features" in data:
            return np.array([data["features"]]) if np.ndim(data["features"]) == 1 else np.array(data["features"])
        elif isinstance(data, list):
            return np.array(data)
        else:
            raise ValueError("Invalid JSON payload structure")
    elif request_content_type == "text/csv":
        return pd.read_csv(io.StringIO(request_body), header=None).values
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    """SageMaker hosting prediction handler."""
    predictions = model.predict(input_data)
    probabilities = model.predict_proba(input_data)
    return {
        "predictions": predictions.tolist(),
        "probabilities": probabilities.tolist()
    }

def output_fn(prediction, accept):
    """SageMaker hosting formatting of response payload."""
    if accept == "application/json":
        return json.dumps(prediction)
    elif accept == "text/csv":
        return ",".join([str(p) for p in prediction["predictions"]])
    else:
        raise ValueError(f"Unsupported accept type: {accept}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # SageMaker hyperparameters
    parser.add_argument('--n-estimators', type=int, default=100)
    parser.add_argument('--max-depth', type=int, default=5)
    parser.add_argument('--random-state', type=int, default=42)
    
    # SageMaker environment directories
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR', 'A9/models'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN', 'A9/data'))
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST', 'A9/data'))
    
    args = parser.parse_args()
    
    os.makedirs(args.model_dir, exist_ok=True)
    
    # Load training and testing data
    train_file = os.path.join(args.train, 'train.csv')
    test_file = os.path.join(args.test, 'test.csv')
    
    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)
    
    # Target is in column 0
    y_train = train_df.iloc[:, 0]
    X_train = train_df.iloc[:, 1:]
    
    y_test = test_df.iloc[:, 0]
    X_test = test_df.iloc[:, 1:]
    
    print(f"Training Random Forest on SageMaker instance...")
    print(f"Hyperparameters: n_estimators={args.n_estimators}, max_depth={args.max_depth}")
    
    clf = RandomForestClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        random_state=args.random_state
    )
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    y_proba = clf.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    
    print("\n=== SageMaker Training Job Evaluation Metrics ===")
    print(f"Accuracy  : {acc:.4f}")
    print(f"Precision : {prec:.4f}")
    print(f"Recall    : {rec:.4f}")
    print(f"F1-Score  : {f1:.4f}")
    print(f"ROC-AUC   : {auc:.4f}")
    
    # Save model artifact inside model_dir
    model_output_path = os.path.join(args.model_dir, "model.joblib")
    joblib.dump(clf, model_output_path)
    print(f"\nModel artifact saved to {model_output_path}")
    
    # Package into model.tar.gz as required by SageMaker S3 storage
    tar_path = os.path.join(args.model_dir, "model.tar.gz")
    with tarfile.open(tar_path, "w:gz") as tar:
        tar.add(model_output_path, arcname="model.joblib")
    print(f"Packaged artifact for S3: {tar_path}")
