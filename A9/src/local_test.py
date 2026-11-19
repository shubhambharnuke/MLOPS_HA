"""
End-to-end Local Simulation and Validation Script for AWS SageMaker Workflow.
Validates:
1. Model loading (model_fn)
2. Input parsing (input_fn)
3. Prediction generation (predict_fn)
4. Output formatting (output_fn)
5. Lambda proxy invocation handler simulation
"""
import os
import sys
import json
import numpy as np
import pandas as pd

# Add src and cloud_configs to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.train import model_fn, predict_fn, input_fn, output_fn
from cloud_configs.lambda_function import lambda_handler

def main():
    print("=" * 70)
    print(">>> [AWS SageMaker Simulation] Local Inference Validation")
    print("=" * 70)

    # 1. Test model_fn
    models_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models"))
    print(f"[*] Loading model artifact from: {models_dir}")
    model = model_fn(models_dir)
    print(f"[*] Model loaded successfully: {type(model).__name__}")

    # 2. Test test data batch
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    test_csv = os.path.join(data_dir, "test.csv")
    test_df = pd.read_csv(test_csv)
    sample_row = test_df.iloc[0]
    true_label = int(sample_row["target"])
    features = sample_row.drop("target").tolist()

    print(f"\n[*] Sample Feature Vector (Length: {len(features)}):")
    print(f"    Features (first 5): {features[:5]} ...")
    print(f"    Ground Truth Label: {true_label} ({'Benign' if true_label == 1 else 'Malignant'})")

    # 3. Simulate input_fn & predict_fn & output_fn
    json_payload = json.dumps({"features": features})
    parsed_input = input_fn(json_payload, "application/json")
    raw_pred = predict_fn(parsed_input, model)
    output_response = output_fn(raw_pred, "application/json")
    parsed_output = json.loads(output_response)

    print(f"\n[*] SageMaker Container Inference Result:")
    print(f"    Predicted Class : {parsed_output['predictions'][0]} ({'Benign' if parsed_output['predictions'][0] == 1 else 'Malignant'})")
    print(f"    Class Probabilities: Malignant={parsed_output['probabilities'][0][0]:.4f}, Benign={parsed_output['probabilities'][0][1]:.4f}")

    # 4. Simulate Lambda Proxy Handler
    print("\n[*] Simulating AWS Lambda Function Integration:")
    lambda_event = {
        "body": json.dumps({"features": features})
    }
    lambda_res = lambda_handler(lambda_event, None)
    print(f"    Lambda Status Code: {lambda_res['statusCode']}")
    body_data = json.loads(lambda_res['body'])
    print(f"    Response Body: {json.dumps(body_data, indent=4)}")

    assert lambda_res['statusCode'] == 200
    assert body_data['diagnosis'] in ["Malignant", "Benign", "malignant", "benign"]
    print("\n[SUCCESS] Local SageMaker workflow simulation executed and verified perfectly!")

if __name__ == "__main__":
    main()
