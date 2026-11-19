import os
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def get_data():
    cancer = load_breast_cancer()
    X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    y = pd.Series(cancer.target, name='target')
    
    # Train test split 80/20 stratified
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Standard scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    X_train_df = pd.DataFrame(X_train_scaled, columns=cancer.feature_names)
    X_test_df = pd.DataFrame(X_test_scaled, columns=cancer.feature_names)
    
    return X_train_df, X_test_df, y_train, y_test, cancer.feature_names, cancer.target_names

if __name__ == '__main__':
    X_train, X_test, y_train, y_test, fnames, tnames = get_data()
    print(f"Loaded dataset: Breast Cancer Wisconsin")
    print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")
    print(f"Target classes: {list(tnames)}")
