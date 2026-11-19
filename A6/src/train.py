import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_and_export():
    os.makedirs('A6/models', exist_ok=True)
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )
    
    model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Model trained with Accuracy: {acc:.4f}")
    
    payload = {
        'model': model,
        'target_names': list(iris.target_names),
        'feature_names': list(iris.feature_names)
    }
    joblib.dump(payload, 'A6/models/model.joblib')
    print("Exported model to A6/models/model.joblib")

if __name__ == '__main__':
    train_and_export()
