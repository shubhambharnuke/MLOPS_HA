# MLOps Laboratory Final Submissions (AI3206C)

**Student Name:** Shubham Bharnuke  
**Roll No:** 36 | **PRN:** 12411834  
**Class / Division:** TY AI&DS, Division A | **Semester:** 5 (2026–27)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  
**Department:** Department of Artificial Intelligence & Data Science  
**Faculty In-Charge:** Prof. (Dr.) Premanand Ghadekar  

---

## Executive Summary

This repository contains the complete, production-grade implementations and formal laboratory reports for all **9 MLOps (Machine Learning Operations)** assignments. Each assignment represents an isolated, end-to-end engineered subsystem spanning modern data versioning, experiment tracking, pipeline orchestration, model containerization, CI/CD automation, operational telemetry, and cloud ML deployments.

All deliverables adhere strictly to industry best practices, include verified visual evidence, and contain fully populated academic laboratory reports formatted against the official institutional template (`REPORT_TEMPLATE.docx`) with **zero unfilled placeholders**.

---

## Project Submissions Overview (A1 – A9)

| Assignment | Domain & Tooling | Key Technical Deliverables | Commit Hash | Report Status |
|:---:|:---|:---|:---:|:---:|
| **[A1](A1/)** | **Dataset Versioning with DVC**<br>`DVC`, `Git` | Multi-version data tracking (v1 & v2), local remote storage, SHA-1 checksum tracking, tag-based rollback. | `e3ad109` | Verified |
| **[A2](A2/)** | **Experiment Tracking with MLflow**<br>`MLflow`, `SQLite`, `Scikit-Learn` | 6 logged runs across RF, LR, and Gradient Boosting; parameter/metric tracking; ROC/CM artifact logging; Model Registry registration (`BestClassificationModel` v1). | `e3f82c8` | Verified |
| **[A3](A3/)** | **Feature Engineering Pipeline**<br>`Scikit-Learn`, `Pandas`, `Titanic` | Production pipeline with custom transformers (`MissingValueImputer`, `FeatureEncoder`, `FeatureScaler`), pipeline serialization (`feature_pipeline.pkl`), and batch inference. | `9aef9da` | Verified |
| **[A4](A4/)** | **Workflow Automation with Apache Airflow**<br>`Apache Airflow`, `DAG`, `Python` | 5-stage automated DAG (`extract >> validate >> process >> report >> notify`), task isolation, validation summary generation, failure alerts. | `4831eaa` | Verified |
| **[A5](A5/)** | **Model Serving with FastAPI**<br>`FastAPI`, `Pydantic v2`, `Pytest` | Production REST API with `/health`, `/model-info`, `/predict`, `/predict-batch`; strict Pydantic validation; 100% test pass rate (7/7 pytest). | `d08c6ea` | Verified |
| **[A6](A6/)** | **Model Containerization with Docker**<br>`Docker`, `FastAPI`, `Scikit-Learn` | Multi-stage slim Docker image (`mlops-docker-model:v1`), port mapping (`8080:8080`), healthcheck validation, containerized inference. | `7531e69` | Verified |
| **[A7](A7/)** | **CI/CD Automation with GitHub Actions**<br>`GitHub Actions`, `Pytest`, `flake8` | 3-stage automated CI/CD pipeline (`lint >> test >> deploy`), model accuracy gating (threshold $\ge 0.90$), automated pass/fail build enforcement. | `f4bd909` | Verified |
| **[A8](A8/)** | **Model Monitoring with Prometheus & Grafana**<br>`Prometheus`, `Grafana`, `Docker Compose` | Real-time observability stack, custom Counter & Histogram metrics, 5s scrape target, P95 latency tracking, error spike detection. | `549b64d` | Verified |
| **[A9](A9/)** | **Cloud ML Pipeline with AWS SageMaker**<br>`AWS SageMaker`, `S3`, `Lambda`, `API Gateway` | Script Mode training on EC2 (`ml.m5.large`), `model.tar.gz` artifact, real-time HTTPS endpoint, AWS Lambda serverless proxy, CloudWatch alarms. | `94c7f29` | Verified |

---

## Repository Structure

```
FINAL_SUBMISSIONS/
├── README.md                            # Master project documentation & submission summary
├── TODO.md                              # Detailed atomic task execution tracker (Phases 1-9)
├── REPORT_TEMPLATE.docx                 # Institutional laboratory report template
├── A1/                                  # Assignment 1: DVC Dataset Versioning
│   ├── data/                            # student.csv (v1/v2), student.csv.dvc
│   ├── storage/dvc_remote/              # Content-addressable remote store
│   ├── screenshots/                     # 5 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
├── A2/                                  # Assignment 2: MLflow Experiment Tracking
│   ├── src/                             # dataset.py, train.py, predict.py
│   ├── artifacts/                       # Confusion matrices, ROC curves, summary JSON
│   ├── models/                          # Serialized best model artifact
│   ├── mlflow.db                        # SQLite backend tracking database
│   ├── screenshots/                     # 3 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
├── A3/                                  # Assignment 3: Feature Engineering Pipeline
│   ├── data/                            # Raw Titanic dataset (891 rows)
│   ├── src/                             # preprocessing.py, pipeline.py, inference.py
│   ├── models/                          # feature_pipeline.pkl
│   ├── output/                          # transformed_data.csv (891 x 11)
│   ├── screenshots/                     # 2 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
├── A4/                                  # Assignment 4: Apache Airflow Workflow DAG
│   ├── dags/                            # data_pipeline_dag.py (5-task pipeline)
│   ├── data/                            # raw_data.csv
│   ├── output/                          # validation_summary.json, processed_data.csv, report
│   ├── logs/                            # notification.log
│   ├── screenshots/                     # 2 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
├── A5/                                  # Assignment 5: FastAPI ML REST API
│   ├── app/                             # main.py, schemas.py
│   ├── models/                          # iris_model.pkl
│   ├── tests/                           # test_api.py (7 unit/integration tests)
│   ├── screenshots/                     # 2 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
├── A6/                                  # Assignment 6: Docker Model Containerization
│   ├── src/                             # train.py, app.py
│   ├── models/                          # model.joblib
│   ├── Dockerfile                       # Python 3.11-slim container configuration
│   ├── screenshots/                     # 2 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
├── A7/                                  # Assignment 7: GitHub Actions CI/CD Pipeline
│   ├── .github/workflows/               # mlops_ci_cd.yml
│   ├── src/                             # train.py, simulate_cicd.py
│   ├── tests/                           # test_model.py, test_code_quality.py
│   ├── screenshots/                     # 2 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
├── A8/                                  # Assignment 8: Prometheus & Grafana Monitoring
│   ├── src/                             # train.py, app.py, traffic_generator.py
│   ├── config/                          # prometheus.yml
│   ├── dashboards/                      # model_monitoring_dashboard.json
│   ├── docker-compose.yml               # Container orchestration file
│   ├── screenshots/                     # 2 verified execution screenshots
│   ├── README.md                        # Documentation & setup instructions
│   └── report.docx                      # Fully populated formal report
└── A9/                                  # Assignment 9: AWS SageMaker Cloud ML Pipeline
    ├── cloud_configs/                   # api_gateway_spec.json, cloudwatch_alarms.json, lambda_function.py
    ├── data/                            # train.csv, test.csv
    ├── models/                          # model.joblib, model.tar.gz
    ├── notebooks/                       # sagemaker_pipeline.ipynb
    ├── screenshots/                     # 2 verified execution screenshots
    ├── src/                             # prepare_data.py, train.py, local_test.py, build_report.py
    ├── README.md                        # Documentation & setup instructions
    └── report.docx                      # Fully populated formal report
```

---

## Verification and Quality Assurance Standards

Across all 9 assignments, the following rigorous quality checks were conducted and passed:
1. **Source Code Execution:** All data extraction, model training, API serving, tests, and simulations execute cleanly without runtime exceptions.
2. **Visual Evidence:** High-resolution screenshots documenting CLI runs, dashboards, container executions, and cloud metrics were captured into each assignment's `screenshots/` directory.
3. **Academic Integrity & Reports:** Every assignment contains a complete, customized `report.docx` derived from `REPORT_TEMPLATE.docx`. All bracketed placeholder tokens were replaced with genuine technical descriptions, code listings, execution procedures, mathematical insights, and IEEE citations.
4. **Git Commit Lineage:** Each assignment was committed to Git independently immediately upon completion with clean, descriptive commit messages.
