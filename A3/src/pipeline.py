import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_classif
import joblib
import os

def build_feature_pipeline():
    numeric_features = ['Age', 'Fare']
    categorical_features = ['Sex', 'Pclass', 'Embarked']
    
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )
    
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('feature_selector', SelectKBest(score_func=f_classif, k='all'))
    ])
    
    return pipeline, numeric_features, categorical_features

def run_pipeline():
    os.makedirs('A3/models', exist_ok=True)
    os.makedirs('A3/output', exist_ok=True)
    
    df = pd.read_csv('A3/data/dataset.csv')
    print("Dataset Loaded Successfully")
    print(f"Original Dataset Shape: {df.shape}")
    
    features = ['Age', 'Fare', 'Sex', 'Pclass', 'Embarked']
    X = df[features]
    y = df['Survived']
    
    pipeline, num_feats, cat_feats = build_feature_pipeline()
    X_transformed = pipeline.fit_transform(X, y)
    
    # Extract feature names
    cat_encoder = pipeline.named_steps['preprocessor'].named_transformers_['cat'].named_steps['encoder']
    cat_columns = list(cat_encoder.get_feature_names_out(cat_feats))
    all_feature_names = num_feats + cat_columns
    
    transformed_df = pd.DataFrame(X_transformed, columns=all_feature_names)
    transformed_df['Survived'] = y.values
    transformed_df.to_csv('A3/output/transformed_data.csv', index=False)
    
    # Save Pipeline
    joblib.dump(pipeline, 'A3/models/feature_pipeline.pkl')
    
    print("\n--- Pipeline Transformation Summary ---")
    print(f"Missing Values Imputed: Yes")
    print(f"Categorical Features Encoded: {cat_feats}")
    print(f"Numerical Features Scaled: {num_feats}")
    print(f"Selected Features: {all_feature_names}")
    print(f"Transformed Dataset Shape: {transformed_df.shape}")
    print("Pipeline Saved Successfully to A3/models/feature_pipeline.pkl")
    print("Transformed data saved to A3/output/transformed_data.csv")
    
    return pipeline, transformed_df

if __name__ == '__main__':
    run_pipeline()
