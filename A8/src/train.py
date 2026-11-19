import os
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    os.makedirs('A8/models', exist_ok=True)
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, test_size=0.2, random_state=42, stratify=cancer.target
    )
    
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"A8 Model Trained - Accuracy: {acc:.4f}")
    
    payload = {
        'model': model,
        'feature_names': list(cancer.feature_names),
        'target_names': list(cancer.target_names)
    }
    joblib.dump(payload, 'A8/models/model.joblib')
    print("Model serialized to A8/models/model.joblib")

if __name__ == '__main__':
    train_model()
