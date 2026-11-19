from flask import Flask, request, jsonify
import joblib
import os
import numpy as np

app = Flask(__name__)

model_path = os.environ.get('MODEL_PATH', 'models/model.joblib')
if not os.path.exists(model_path):
    model_path = 'A6/models/model.joblib'

bundle = joblib.load(model_path)
model = bundle['model']
classes = bundle['target_names']

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "service": "Containerized Iris Classification Model",
        "runtime": "Docker Container",
        "endpoints": ["/health", "/predict"]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "UP",
        "container": "mlops-docker-model",
        "model_loaded": True
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        # Expected features: sepal_length, sepal_width, petal_length, petal_width
        feats = [
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        ]
        X = np.array([feats])
        pred_id = int(model.predict(X)[0])
        prob = float(model.predict_proba(X)[0][pred_id])
        
        return jsonify({
            "prediction": classes[pred_id],
            "class_id": pred_id,
            "confidence": round(prob, 4),
            "status": "success"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
