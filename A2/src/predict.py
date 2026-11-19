import joblib
import pandas as pd
from dataset import get_data

def predict_sample():
    # Load best model
    model = joblib.load("A2/models/best_model.joblib")
    _, X_test, _, y_test, feature_names, target_names = get_data()
    
    sample = X_test.iloc[:5]
    actual = y_test.iloc[:5].values
    predictions = model.predict(sample)
    probabilities = model.predict_proba(sample)[:, 1] if hasattr(model, 'predict_proba') else [None]*5
    
    print("=== Model Inference Test ===")
    for i in range(5):
        pred_label = target_names[predictions[i]]
        act_label = target_names[actual[i]]
        prob = f"{probabilities[i]:.4f}" if probabilities[i] is not None else "N/A"
        print(f"Sample {i+1}: Actual='{act_label}', Predicted='{pred_label}', Confidence={prob}")
    
    print("\nInference verification: SUCCESS")

if __name__ == '__main__':
    predict_sample()
