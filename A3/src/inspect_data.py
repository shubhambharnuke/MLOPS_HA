import pandas as pd
import numpy as np

def inspect_raw_data(filepath='A3/data/dataset.csv'):
    df = pd.read_csv(filepath)
    print(f"Dataset Loaded Successfully from {filepath}")
    print(f"Original Dataset Shape: {df.shape}")
    print("\n--- Missing Values Count ---")
    print(df.isnull().sum()[df.isnull().sum() > 0])
    print("\n--- Column Data Types ---")
    print(df.dtypes)
    return df

if __name__ == '__main__':
    inspect_raw_data()
