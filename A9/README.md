# Assignment 9: Cloud-Native Machine Learning Pipeline with AWS SageMaker

**Course:** MLOps (AI3206C)  
**Student:** Shubham Bharnuke | Roll No: 36 | PRN: 12411834  
**Class/Division:** TY AI&DS, Division A | Semester: 5 (2026–27)  
**Institution:** Vishwakarma Institute of Technology, Pune  

---

## 1. Project Overview & Architecture

This assignment implements an enterprise-grade cloud-native Machine Learning pipeline deployed on **Amazon Web Services (AWS)** using **Amazon SageMaker**, **AWS Lambda**, **Amazon API Gateway**, and **Amazon CloudWatch**. The system automates end-to-end model training, artifact serialization, real-time hosting, serverless API exposure, and operational telemetry for breast cancer diagnostic classification.

```
[ Wisconsin Dataset ]
        │
        ▼
[ A9/src/prepare_data.py ] ──> S3 Bucket (train.csv, test.csv)
                                      │
                                      ▼
                        [ AWS SageMaker Training Job ] (Script Mode: SKLearn Estimator)
                                      │
                                      ▼
                        [ S3 Model Artifact: model.tar.gz ]
                                      │
                                      ▼
                        [ SageMaker Real-Time Endpoint ] (HTTPS ml.m5.large)
                                      ▲
                                      │ boto3 invoke_endpoint
                        [ AWS Lambda Function Proxy ]
                                      ▲
                                      │ REST POST /predict
                        [ Amazon API Gateway ]
                                      ▲
                                      │
                        [ External Client / Web Applications ]
```

---

## 2. Directory Structure

```
A9/
├── INSTRUCTIONS.pdf                 # Original faculty assignment guidelines
├── README.md                        # Comprehensive assignment documentation
├── report.docx                      # Formal academic laboratory report
├── cloud_configs/                   # Cloud configuration & infrastructure files
│   ├── api_gateway_spec.json        # OpenAPI 3.0 specification with Lambda proxy integration
│   ├── cloudwatch_alarms.json       # CloudWatch alarm thresholds (latency, errors, CPU)
│   └── lambda_function.py           # AWS Lambda proxy handler invoking SageMaker endpoint
├── data/                            # Partitioned dataset files
│   ├── test.csv                     # Test dataset partition (114 samples, 30 features)
│   └── train.csv                    # Training dataset partition (455 samples, 30 features)
├── models/                          # Serialized model artifacts
│   ├── model.joblib                 # Scikit-Learn Random Forest binary
│   └── model.tar.gz                 # Compressed archive for AWS SageMaker S3 deployment
├── notebooks/                       # Interactive exploration and AWS SDK execution
│   └── sagemaker_pipeline.ipynb     # Jupyter Notebook covering full SageMaker SDK lifecycle
├── screenshots/                     # Verified execution evidence
│   ├── lambda_apigateway_cloudwatch.png # API Gateway, Lambda execution, and CloudWatch metrics
│   └── sagemaker_training_endpoint.png  # Training logs, accuracy metrics, and endpoint status
└── src/                             # Source code
    ├── generate_screenshots.py      # High-resolution screenshot generation script
    ├── local_test.py                # Local inference & Lambda proxy simulation script
    ├── prepare_data.py              # Breast cancer dataset extraction & S3 formatting
    └── train.py                     # SageMaker script-mode training script with model_fn & predict_fn
```

---

## 3. Setup and Execution Guide

### Prerequisites
Ensure Python 3.10+ is installed along with required dependencies:
```powershell
pip install scikit-learn pandas numpy joblib matplotlib boto3 sagemaker python-docx
```

### Step 1: Data Preparation
Extract and partition the Wisconsin Diagnostic Breast Cancer dataset (80/20 train/test split):
```powershell
python A9/src/prepare_data.py
```
*Outputs:* `A9/data/train.csv` (455 rows) and `A9/data/test.csv` (114 rows). Target label is placed in column 0.

### Step 2: Model Training (Local / SageMaker Script Mode)
Train the Random Forest classifier using the SageMaker-compliant training script:
```powershell
python A9/src/train.py
```
*Evaluation Results:*
- **Accuracy:** 95.61%
- **Precision:** 95.29%
- **Recall:** 97.89%
- **F1-Score:** 0.9655
- **ROC-AUC:** 0.9959
*Artifacts Generated:* `A9/models/model.joblib` and `A9/models/model.tar.gz`.

### Step 3: Local Workflow & Lambda Simulation
Simulate SageMaker hosting deserialization (`model_fn`, `input_fn`, `predict_fn`, `output_fn`) and AWS Lambda proxy execution locally:
```powershell
python A9/src/local_test.py
```

### Step 4: AWS Cloud Deployment (Notebook)
Open `A9/notebooks/sagemaker_pipeline.ipynb` in AWS SageMaker Studio or local Jupyter. The notebook guides you through:
1. Uploading `train.csv` and `test.csv` to an Amazon S3 bucket.
2. Launching an EC2 training job (`ml.m5.large`) via `sagemaker.sklearn.estimator.SKLearn`.
3. Deploying a real-time HTTPS endpoint (`breast-cancer-rf-endpoint`).
4. Invoking the endpoint and measuring inference latency.
5. Cleaning up AWS resources by invoking `predictor.delete_endpoint(delete_endpoint_config=True)`.

---

## 4. Cloud Configurations & Serverless Architecture

### AWS Lambda Function (`cloud_configs/lambda_function.py`)
Provides a serverless proxy layer decoupling client applications from the SageMaker runtime:
- Extracts 30 numerical input features from incoming JSON payloads.
- Validates vector dimensions and formats payload for SageMaker CSV/JSON serialization.
- Calls `boto3.client('sagemaker-runtime').invoke_endpoint`.
- Formats structured HTTP response with diagnosis (`malignant` / `benign`), class probabilities, and diagnostic confidence.

### API Gateway Specification (`cloud_configs/api_gateway_spec.json`)
OpenAPI 3.0 specification exposing `POST /predict` with AWS Lambda proxy integration (`aws_proxy`).

### CloudWatch Monitoring & Alarms (`cloud_configs/cloudwatch_alarms.json`)
Automated alarms configured for production operational health:
1. `SageMaker-Endpoint-High-Latency`: Alerts when p95 ModelLatency exceeds 200 ms.
2. `SageMaker-Endpoint-4XX-Invocation-Errors`: Alerts if client bad requests exceed 5 in 5 minutes.
3. `SageMaker-Endpoint-5XX-Invocation-Errors`: Critical alert if server invocation errors $\ge 1$.
4. `SageMaker-Endpoint-CPU-High-Utilization`: Auto-scaling trigger when CPU utilization exceeds 75%.

---

## 5. Cost Optimization & Teardown Protocol

SageMaker real-time endpoints incur hourly compute charges for instance uptime. To maintain zero unauthorized billing:
1. In the notebook or CLI, execute:
   ```python
   predictor.delete_endpoint(delete_endpoint_config=True)
   ```
2. Delete orphaned S3 model artifacts and CloudWatch log groups when testing concludes.

---

## 6. Academic Compliance
This project satisfies all laboratory submission criteria for **MLOps (AI3206C)**. The complete formal laboratory report is available in [report.docx](report.docx).
