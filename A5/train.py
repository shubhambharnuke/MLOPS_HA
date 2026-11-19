import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    os.makedirs('A5/models', exist_ok=True)
    iris = load_iris()
    X, y = iris.data, iris.target
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Iris Model Trained - Accuracy: {acc:.4f}")
    
    model_data = {
        'model': model,
        'feature_names': list(iris.feature_names),
        'target_names': list(iris.target_names),
        'accuracy': acc
    }
    
    joblib.dump(model_data, 'A5/models/iris_model.pkl')
    print("Model serialized to A5/models/iris_model.pkl")

if __name__ == '__main__':
    train_model()
