import os
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import mlflow
import mlflow.sklearn
from dataset import get_data
import joblib

# Trusted types for skops in scikit-learn models
TRUSTED_TYPES = ["sklearn.tree._tree.Tree", "numpy.dtype", "numpy.core.multiarray.scalar"]

def train_and_log():
    mlflow.set_tracking_uri("sqlite:///A2/mlflow.db")
    experiment_name = "MLOps_Experiment_Tracking"
    mlflow.set_experiment(experiment_name)
    
    X_train, X_test, y_train, y_test, feature_names, target_names = get_data()
    
    os.makedirs("A2/artifacts", exist_ok=True)
    os.makedirs("A2/screenshots", exist_ok=True)
    os.makedirs("A2/models", exist_ok=True)
    
    models = [
        ("Logistic_Regression", LogisticRegression(C=0.1, max_iter=200, random_state=42), {"C": 0.1, "solver": "lbfgs"}),
        ("Logistic_Regression_Tuned", LogisticRegression(C=1.0, max_iter=200, random_state=42), {"C": 1.0, "solver": "lbfgs"}),
        ("Decision_Tree", DecisionTreeClassifier(max_depth=4, random_state=42), {"max_depth": 4, "criterion": "gini"}),
        ("Random_Forest_Base", RandomForestClassifier(n_estimators=50, max_depth=3, random_state=42), {"n_estimators": 50, "max_depth": 3}),
        ("Random_Forest_Tuned", RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42), {"n_estimators": 100, "max_depth": 5}),
        ("Support_Vector_Machine", SVC(C=1.0, kernel='rbf', probability=True, random_state=42), {"C": 1.0, "kernel": "rbf"})
    ]
    
    best_f1 = 0.0
    best_model_name = None
    best_model_obj = None
    best_run_id = None
    results_summary = []
    
    for name, model, params in models:
        with mlflow.start_run(run_name=name) as run:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
            
            acc = float(accuracy_score(y_test, y_pred))
            prec = float(precision_score(y_test, y_pred))
            rec = float(recall_score(y_test, y_pred))
            f1 = float(f1_score(y_test, y_pred))
            roc_auc = float(roc_auc_score(y_test, y_proba)) if y_proba is not None else 0.0
            
            # Log params
            mlflow.log_params(params)
            mlflow.log_param("model_type", type(model).__name__)
            
            # Log metrics
            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("precision", prec)
            mlflow.log_metric("recall", rec)
            mlflow.log_metric("f1_score", f1)
            mlflow.log_metric("roc_auc", roc_auc)
            
            # Confusion matrix plot
            cm = confusion_matrix(y_test, y_pred)
            plt.figure(figsize=(4.5, 3.5))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
            plt.title(f'CM: {name}')
            plt.ylabel('Actual')
            plt.xlabel('Predicted')
            plt.tight_layout()
            cm_path = f"A2/artifacts/{name}_cm.png"
            plt.savefig(cm_path)
            plt.close()
            mlflow.log_artifact(cm_path)
            
            # ROC curve plot
            if y_proba is not None:
                fpr, tpr, _ = roc_curve(y_test, y_proba)
                plt.figure(figsize=(4.5, 3.5))
                plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.3f}', color='darkorange')
                plt.plot([0, 1], [0, 1], 'k--', lw=1)
                plt.xlabel('FPR')
                plt.ylabel('TPR')
                plt.title(f'ROC: {name}')
                plt.legend(loc='lower right')
                plt.tight_layout()
                roc_path = f"A2/artifacts/{name}_roc.png"
                plt.savefig(roc_path)
                plt.close()
                mlflow.log_artifact(roc_path)
            
            # Log model artifact with skops_trusted_types
            try:
                mlflow.sklearn.log_model(model, name="model", skops_trusted_types=TRUSTED_TYPES)
            except Exception as e:
                # Fallback to direct joblib model artifact logging
                model_file = f"A2/models/{name}.joblib"
                joblib.dump(model, model_file)
                mlflow.log_artifact(model_file)
            
            results_summary.append({
                "Run_Name": name,
                "Accuracy": round(acc, 4),
                "Precision": round(prec, 4),
                "Recall": round(rec, 4),
                "F1_Score": round(f1, 4),
                "ROC_AUC": round(roc_auc, 4)
            })
            
            print(f"Logged {name} - Acc: {acc:.4f}, F1: {f1:.4f}, AUC: {roc_auc:.4f}")
            
            if f1 > best_f1:
                best_f1 = f1
                best_model_name = name
                best_model_obj = model
                best_run_id = run.info.run_id

    # Register best model
    print(f"\nBest Model: {best_model_name} with F1-Score: {best_f1:.4f}")
    try:
        model_uri = f"runs:/{best_run_id}/model"
        reg_model = mlflow.register_model(model_uri, "BestClassificationModel")
        print(f"Registered model as 'BestClassificationModel' (Version: {reg_model.version})")
    except Exception as e:
        print(f"Model registration notice: {e}")
    
    # Save standalone best model for fast inference
    joblib.dump(best_model_obj, "A2/models/best_model.joblib")
    
    # Save summary table JSON
    with open("A2/artifacts/results_summary.json", "w") as f:
        json.dump(results_summary, f, indent=4)
        
    print("All runs logged successfully.")
    return results_summary

if __name__ == '__main__':
    train_and_log()
