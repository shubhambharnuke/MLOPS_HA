from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import PlainTextResponse
import time
import os
import joblib
import numpy as np
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# Prometheus Metrics Definitions
PREDICTION_REQUESTS = Counter(
    'ml_prediction_requests_total',
    'Total count of prediction requests received',
    ['endpoint', 'status']
)

PREDICTION_LATENCY = Histogram(
    'ml_prediction_latency_seconds',
    'Latency of prediction execution in seconds',
    ['endpoint'],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]
)

PREDICTION_ERRORS = Counter(
    'ml_prediction_errors_total',
    'Total count of prediction errors',
    ['endpoint', 'error_type']
)

PREDICTIONS_BY_CLASS = Counter(
    'ml_predictions_by_class_total',
    'Count of predictions broken down by target class',
    ['predicted_class']
)

app = FastAPI(title="ML Prediction Service with Prometheus Instrumentation")

model_path = os.environ.get('MODEL_PATH', 'A8/models/model.joblib')
bundle = joblib.load(model_path)
model = bundle['model']
classes = bundle['target_names']

@app.get('/metrics')
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get('/health')
def health():
    return {"status": "HEALTHY", "model_loaded": True}

@app.post('/predict')
async def predict(request: Request):
    start_time = time.time()
    try:
        body = await request.json()
        if 'features' not in body or not isinstance(body['features'], list):
            PREDICTION_ERRORS.labels(endpoint='/predict', error_type='invalid_schema').inc()
            PREDICTION_REQUESTS.labels(endpoint='/predict', status='400').inc()
            raise HTTPException(status_code=400, detail="Missing or invalid 'features' list in payload.")
            
        features = np.array([body['features']])
        if features.shape[1] != 30:
            PREDICTION_ERRORS.labels(endpoint='/predict', error_type='dimension_mismatch').inc()
            PREDICTION_REQUESTS.labels(endpoint='/predict', status='422').inc()
            raise HTTPException(status_code=422, detail=f"Expected 30 features, received {features.shape[1]}")
            
        pred_id = int(model.predict(features)[0])
        pred_class = classes[pred_id]
        prob = float(model.predict_proba(features)[0][pred_id])
        
        # Record operational metrics
        duration = time.time() - start_time
        PREDICTION_LATENCY.labels(endpoint='/predict').observe(duration)
        PREDICTION_REQUESTS.labels(endpoint='/predict', status='200').inc()
        PREDICTIONS_BY_CLASS.labels(predicted_class=pred_class).inc()
        
        return {
            "prediction": pred_class,
            "class_id": pred_id,
            "confidence": round(prob, 4),
            "latency_ms": round(duration * 1000, 2)
        }
    except HTTPException:
        raise
    except Exception as e:
        PREDICTION_ERRORS.labels(endpoint='/predict', error_type='server_error').inc()
        PREDICTION_REQUESTS.labels(endpoint='/predict', status='500').inc()
        raise HTTPException(status_code=500, detail=str(e))
