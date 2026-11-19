from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
import joblib
import os
import numpy as np
from app.schemas import IrisInput, PredictionResponse, BatchIrisInput, BatchPredictionResponse, ModelInfoResponse

model_artifacts = {}

def load_iris_model():
    candidates = [
        os.path.join(os.path.dirname(__file__), '..', 'models', 'iris_model.pkl'),
        'A5/models/iris_model.pkl',
        os.path.abspath('A5/models/iris_model.pkl')
    ]
    for c in candidates:
        if os.path.exists(c):
            return joblib.load(c)
    return None

# Eagerly load model on module import so TestClient has access without lifespan context
model_bundle = load_iris_model()
if model_bundle is not None:
    model_artifacts['bundle'] = model_bundle

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_artifacts
    if 'bundle' not in model_artifacts:
        bundle = load_iris_model()
        if bundle:
            model_artifacts['bundle'] = bundle
    yield
    model_artifacts.clear()

app = FastAPI(
    title="Iris Classification Prediction Service",
    description="Production-grade REST API developed using FastAPI to serve real-time predictions from a trained ML model.",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/", status_code=status.HTTP_200_OK, tags=["General"])
def root():
    return {
        "service": "Iris Flower Classification API",
        "version": "1.0.0",
        "documentation": "/docs",
        "health_check": "/health",
        "model_info": "/model-info"
    }

@app.get("/health", status_code=status.HTTP_200_OK, tags=["Monitoring"])
def health():
    if 'bundle' not in model_artifacts:
        raise HTTPException(status_code=503, detail="Model is not ready.")
    return {
        "status": "HEALTHY",
        "model_loaded": True,
        "service_uptime": "active"
    }

@app.get("/model-info", response_model=ModelInfoResponse, tags=["Metadata"])
def model_info():
    if 'bundle' not in model_artifacts:
        raise HTTPException(status_code=503, detail="Model not loaded.")
    bundle = model_artifacts['bundle']
    return {
        "model_type": type(bundle['model']).__name__,
        "target_classes": bundle['target_names'],
        "features": bundle['feature_names'],
        "status": "ready"
    }

@app.post("/predict", response_model=PredictionResponse, status_code=status.HTTP_200_OK, tags=["Inference"])
def predict(payload: IrisInput):
    if 'bundle' not in model_artifacts:
        raise HTTPException(status_code=503, detail="Model not available.")
    
    bundle = model_artifacts['bundle']
    model = bundle['model']
    classes = bundle['target_names']
    
    features = np.array([[
        payload.sepal_length,
        payload.sepal_width,
        payload.petal_length,
        payload.petal_width
    ]])
    
    pred_id = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    confidence = float(probabilities[pred_id])
    
    return {
        "prediction_class": classes[pred_id],
        "class_id": pred_id,
        "confidence_score": round(confidence, 4),
        "model_version": "1.0.0"
    }

@app.post("/predict-batch", response_model=BatchPredictionResponse, status_code=status.HTTP_200_OK, tags=["Inference"])
def predict_batch(payload: BatchIrisInput):
    if 'bundle' not in model_artifacts:
        raise HTTPException(status_code=503, detail="Model not available.")
    
    bundle = model_artifacts['bundle']
    model = bundle['model']
    classes = bundle['target_names']
    
    results = []
    for item in payload.samples:
        features = np.array([[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]])
        pred_id = int(model.predict(features)[0])
        conf = float(model.predict_proba(features)[0][pred_id])
        results.append({
            "prediction_class": classes[pred_id],
            "class_id": pred_id,
            "confidence_score": round(conf, 4),
            "model_version": "1.0.0"
        })
        
    return {
        "predictions": results,
        "total_samples": len(results)
    }
