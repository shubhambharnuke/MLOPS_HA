import os
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def prepare_data():
    os.makedirs('A9/data', exist_ok=True)
    cancer = load_breast_cancer()
    
    # SageMaker Scikit-learn CSV convention: Target column in first position
    df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    df.insert(0, 'target', cancer.target)
    
    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=42, stratify=df['target']
    )
    
    train_path = 'A9/data/train.csv'
    test_path = 'A9/data/test.csv'
    
    # Save headerless for SageMaker algorithm containers or with headers for script mode
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
    print(f"Prepared Breast Cancer Data for SageMaker:")
    print(f"Train samples: {len(train_df)} -> {train_path}")
    print(f"Test samples : {len(test_df)}  -> {test_path}")
    print(f"Features: 30 numeric | Target: binary (0=malignant, 1=benign)")

if __name__ == '__main__':
    prepare_data()
