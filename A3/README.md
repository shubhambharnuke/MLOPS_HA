# Assignment 3: Design and Implement a Feature Engineering Pipeline for Machine Learning

**Course:** MLOps (AI3206C)  
**Student Name:** Shubham Bharnuke  
**PRN:** 12411834 | **Roll No:** 36 | **Class:** TY AI&DS (Div A)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  

---

## 1. Overview & Aim
The objective of this assignment is to design, implement, persist, and reuse an automated **Feature Engineering Pipeline** for machine learning using industry-standard MLOps practices. Raw real-world datasets contain heterogeneous feature types (numerical and categorical) along with missing values and outliers. In this assignment, we build a reusable `scikit-learn` pipeline with `ColumnTransformer` that performs missing-value imputation, numerical scaling, categorical one-hot encoding, and feature selection, preventing training-serving skew and data leakage.

---

## 2. Dataset Description
- **Dataset:** Titanic Dataset
- **Original Samples:** 891 records, 12 raw columns
- **Selected Raw Features:** `Age`, `Fare` (Numerical), `Sex`, `Pclass`, `Embarked` (Categorical)
- **Target:** `Survived` (Binary Classification)

---

## 3. Directory Structure
```
A3/
├── INSTRUCTIONS.pdf              # Official Assignment Instruction Guide
├── README.md                     # Execution & Reproducibility Documentation
├── report.docx                   # Comprehensive Academic Submission Report
├── data/
│   └── dataset.csv               # Raw Titanic dataset (891 rows)
├── models/
│   └── feature_pipeline.pkl      # Serialized fitted pipeline
├── output/
│   └── transformed_data.csv      # Processed ML-ready dataset (891, 11)
├── src/
│   ├── inspect_data.py           # Data quality inspection
│   ├── preprocessing.py          # Custom transformation classes
│   ├── pipeline.py               # Unified ColumnTransformer & Pipeline builder
│   ├── inference.py              # Pipeline deserialization and inference verification
│   ├── generate_screenshots.py   # Visual evidence generator
│   └── build_report.py           # Academic report generator
└── screenshots/
    ├── pipeline_execution.png    # Pipeline fit and transform terminal output
    └── pipeline_inference_reuse.png # Inference verification on unseen data
```

---

## 4. Pipeline Execution Summary
- **Original Shape:** `(891, 12)`
- **Numerical Imputation:** Median imputation on `Age` and `Fare`.
- **Numerical Scaling:** `StandardScaler` (zero mean, unit variance).
- **Categorical Imputation:** Most frequent value on `Embarked`.
- **Categorical Encoding:** `OneHotEncoder(handle_unknown='ignore')` on `Sex`, `Pclass`, `Embarked`.
- **Transformed Feature Space:** 10 engineered features (`Age`, `Fare`, `Sex_female`, `Sex_male`, `Pclass_1`, `Pclass_2`, `Pclass_3`, `Embarked_C`, `Embarked_Q`, `Embarked_S`).
- **Transformed Dataset Shape:** `(891, 11)` including target.

---

## 5. Execution Instructions
```bash
# 1. Run pipeline training and data transformation
python A3/src/pipeline.py

# 2. Test pipeline inference on unseen test samples
python A3/src/inference.py
```
