from pydantic import BaseModel, Field
from typing import List, Optional

class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, lt=15, description="Sepal length in cm", example=5.1)
    sepal_width: float = Field(..., gt=0, lt=15, description="Sepal width in cm", example=3.5)
    petal_length: float = Field(..., gt=0, lt=15, description="Petal length in cm", example=1.4)
    petal_width: float = Field(..., gt=0, lt=15, description="Petal width in cm", example=0.2)

class PredictionResponse(BaseModel):
    prediction_class: str
    class_id: int
    confidence_score: float
    model_version: str

class BatchIrisInput(BaseModel):
    samples: List[IrisInput]

class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
    total_samples: int

class ModelInfoResponse(BaseModel):
    model_type: str
    target_classes: List[str]
    features: List[str]
    status: str
