# Assignment 2: Track Machine Learning Experiments Using MLflow

**Course:** MLOps (AI3206C)  
**Student Name:** Shubham Bharnuke  
**PRN:** 12411834 | **Roll No:** 36 | **Class:** TY AI&DS (Div A)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  

---

## 1. Overview & Aim
The objective of this assignment is to develop machine learning models and implement comprehensive experiment tracking using **MLflow**. The system tracks multiple algorithms and hyperparameter variations by logging hyperparameters, evaluation metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC), diagnostic plots (Confusion Matrix, ROC Curve), and serializes models. The best-performing model is registered in the MLflow Model Registry and loaded for inference.

---

## 2. Dataset Description
- **Dataset:** Breast Cancer Wisconsin (Diagnostic)
- **Samples:** 569 instances
- **Features:** 30 numerical measurements (radius, texture, perimeter, area, smoothness, etc.)
- **Target:** Binary classification (Malignant vs. Benign)
- **Preprocessing:** 80/20 stratified split, StandardScaler feature normalization.

---

## 3. Directory Structure
```
A2/
├── INSTRUCTIONS.pdf              # Official Assignment Instruction Guide
├── README.md                     # Execution & Reproducibility Documentation
├── report.docx                   # Comprehensive Academic Submission Report
├── mlflow.db                     # SQLite database tracking server backend
├── src/
│   ├── dataset.py                # Data loading and preprocessing module
│   ├── train.py                  # MLflow experiment training, logging, & registry
│   ├── predict.py                # Model inference verification script
│   ├── generate_screenshots.py   # Visual evidence generation script
│   └── build_report.py           # Academic report generator
├── models/
│   └── best_model.joblib         # Exported best model (Logistic_Regression_Tuned)
├── artifacts/                    # Logged evaluation plots & summary
│   ├── Logistic_Regression_Tuned_cm.png
│   ├── Logistic_Regression_Tuned_roc.png
│   └── results_summary.json
└── screenshots/
    ├── mlflow_runs_table.png     # Experiment runs comparison
    ├── mlflow_tracking_terminal.png
    └── mlflow_inference_evidence.png
```

---

## 4. Experimental Results Summary
| Model / Run Name | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|
| Logistic_Regression | 0.9737 | 0.9726 | 0.9861 | 0.9793 | 0.9957 |
| **Logistic_Regression_Tuned** | **0.9825** | **0.9861** | **0.9861** | **0.9861** | **0.9954** |
| Decision_Tree | 0.9386 | 0.9589 | 0.9444 | 0.9510 | 0.9342 |
| Random_Forest_Base | 0.9474 | 0.9452 | 0.9722 | 0.9583 | 0.9904 |
| Random_Forest_Tuned | 0.9561 | 0.9583 | 0.9722 | 0.9655 | 0.9934 |
| Support_Vector_Machine | 0.9825 | 0.9861 | 0.9861 | 0.9861 | 0.9950 |

**Selected Model:** `Logistic_Regression_Tuned` registered as `BestClassificationModel` (v1).

---

## 5. Execution Instructions
```bash
# 1. Run experiment tracking pipeline
python A2/src/train.py

# 2. Test sample inference using registered model
python A2/src/predict.py

# 3. Launch MLflow UI (optional)
mlflow ui --backend-store-uri sqlite:///A2/mlflow.db --port 5000
```
