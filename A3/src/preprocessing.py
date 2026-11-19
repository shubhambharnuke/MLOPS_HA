from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class MissingValueImputer(BaseEstimator, TransformerMixin):
    """Custom transformer to handle missing numerical and categorical values."""
    def __init__(self):
        self.age_median = None
        self.fare_median = None
        self.embarked_mode = None
        
    def fit(self, X, y=None):
        X_df = pd.DataFrame(X) if not isinstance(X, pd.DataFrame) else X.copy()
        if 'Age' in X_df.columns:
            self.age_median = X_df['Age'].median()
        if 'Fare' in X_df.columns:
            self.fare_median = X_df['Fare'].median()
        if 'Embarked' in X_df.columns:
            self.embarked_mode = X_df['Embarked'].mode()[0] if not X_df['Embarked'].mode().empty else 'S'
        return self
        
    def transform(self, X):
        X_df = pd.DataFrame(X) if not isinstance(X, pd.DataFrame) else X.copy()
        if 'Age' in X_df.columns and self.age_median is not None:
            X_df['Age'] = X_df['Age'].fillna(self.age_median)
        if 'Fare' in X_df.columns and self.fare_median is not None:
            X_df['Fare'] = X_df['Fare'].fillna(self.fare_median)
        if 'Embarked' in X_df.columns and self.embarked_mode is not None:
            X_df['Embarked'] = X_df['Embarked'].fillna(self.embarked_mode)
        return X_df
