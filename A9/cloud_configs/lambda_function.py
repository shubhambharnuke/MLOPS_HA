import json
import joblib
import numpy as np

# In AWS Lambda, boto3 client invokes SageMaker endpoint:
# sagemaker_runtime = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    """
    AWS Lambda proxy integration handler for SageMaker endpoint.
    Invoked via Amazon API Gateway POST /predict
    """
    try:
        # Parse body from API Gateway proxy event
        if isinstance(event.get('body'), str):
            body = json.loads(event['body'])
        else:
            body = event.get('body', {})
            
        features = body.get('features')
        if not features or not isinstance(features, list):
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"error": "Bad Request: 'features' list required."})
            }
            
        if len(features) != 30:
            return {
                "statusCode": 422,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"error": f"Validation Error: Expected 30 features, received {len(features)}"})
            }
            
        # Simulated InvokeEndpoint call:
        # response = sagemaker_runtime.invoke_endpoint(
        #     EndpointName=os.environ['ENDPOINT_NAME'],
        #     ContentType='application/json',
        #     Body=json.dumps({"features": features})
        # )
        
        # Local model inference simulation
        model = joblib.load('A9/models/model.joblib')
        X = np.array([features])
        pred_id = int(model.predict(X)[0])
        prob = float(model.predict_proba(X)[0][pred_id])
        diagnosis = "benign" if pred_id == 1 else "malignant"
        
        response_payload = {
            "prediction": pred_id,
            "diagnosis": diagnosis,
            "confidence": round(prob, 4),
            "endpoint_arn": "arn:aws:sagemaker:us-east-1:12411834:endpoint/breast-cancer-rf-endpoint",
            "status": "SUCCESS"
        }
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "X-SageMaker-Latency": "18ms"
            },
            "body": json.dumps(response_payload)
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }

if __name__ == '__main__':
    # Test Lambda handler with valid mock event
    sample_30_features = [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
                          1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
                          25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
    
    mock_event = {"body": json.dumps({"features": sample_30_features})}
    result = lambda_handler(mock_event, None)
    print("Lambda Function Test Execution Output:")
    print(f"Status: {result['statusCode']}")
    print(f"Body  : {result['body']}")
