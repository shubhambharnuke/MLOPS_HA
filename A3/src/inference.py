import pandas as pd
import joblib

def test_inference():
    pipeline = joblib.load('A3/models/feature_pipeline.pkl')
    print("Loaded saved pipeline from A3/models/feature_pipeline.pkl")
    
    # Unseen sample data with missing values to test robust preprocessing
    new_samples = pd.DataFrame([
        {'Age': 22.0, 'Fare': 7.25, 'Sex': 'male', 'Pclass': 3, 'Embarked': 'S'},
        {'Age': None, 'Fare': 71.2833, 'Sex': 'female', 'Pclass': 1, 'Embarked': 'C'},
        {'Age': 38.0, 'Fare': None, 'Sex': 'female', 'Pclass': 2, 'Embarked': None}
    ])
    
    print("\n--- Unseen Raw Samples ---")
    print(new_samples)
    
    transformed = pipeline.transform(new_samples)
    print("\n--- Transformed Feature Vectors (Deterministic Output) ---")
    print(f"Output Matrix Shape: {transformed.shape}")
    print(transformed)
    print("\nPipeline Reuse Verification: SUCCESS")

if __name__ == '__main__':
    test_inference()
