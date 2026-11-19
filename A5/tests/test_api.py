import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add A5 directory to sys.path
sys.path.insert(0, os.path.abspath('A5'))

from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Iris Flower Classification API" in response.json()["service"]

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "HEALTHY"
    assert response.json()["model_loaded"] is True

def test_model_info():
    response = client.get("/model-info")
    assert response.status_code == 200
    data = response.json()
    assert "RandomForestClassifier" in data["model_type"]
    assert "setosa" in data["target_classes"]

def test_predict_setosa():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["prediction_class"] == "setosa"
    assert data["class_id"] == 0
    assert data["confidence_score"] > 0.85

def test_predict_virginica():
    payload = {
        "sepal_length": 6.7,
        "sepal_width": 3.3,
        "petal_length": 5.7,
        "petal_width": 2.1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["prediction_class"] == "virginica"
    assert data["class_id"] == 2

def test_predict_validation_error():
    # Negative petal length should trigger Pydantic validation error (422)
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": -1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422

def test_predict_batch():
    payload = {
        "samples": [
            {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},
            {"sepal_length": 6.7, "sepal_width": 3.3, "petal_length": 5.7, "petal_width": 2.1}
        ]
    }
    response = client.post("/predict-batch", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["total_samples"] == 2
    assert len(data["predictions"]) == 2
