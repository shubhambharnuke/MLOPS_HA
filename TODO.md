# Master Project Todo List — MLOps Final Assignments (A1–A9)

**Course:** MLOps (AI3206C) — Third Year B.Tech (Artificial Intelligence & Data Science)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  
**Student Details:** Shubham Bharnuke | PRN: 12411834 | Roll No: 36 | Division: A | Semester: 5 (2026–27)  
**Execution Standard:** Antigravity Autonomous Agent Workspace (`final_submissions/`)  
**Methodology:** Strict sequential execution (A1 $\rightarrow$ A9), atomic tasks, isolated dependencies, validation-first verification, standardized academic reporting (`REPORT_TEMPLATE.docx`), and dedicated Git commits per assignment.

---

## Progress Overview & Status Tracker

| Phase | Assignment ID & Topic | Requirements Analysis | Implementation | Validation & Testing | Academic Report | Git Commit | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Phase 1** | **A1: Dataset Versioning using DVC** | Done | Done | Done | Done | `e3ad109` | `COMPLETE` |
| **Phase 2** | **A2: Experiment Tracking using MLflow** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |
| **Phase 3** | **A3: Feature Engineering Pipeline** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |
| **Phase 4** | **A4: Workflow Automation using Apache Airflow** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |
| **Phase 5** | **A5: ML REST API using FastAPI** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |
| **Phase 6** | **A6: Model Containerization using Docker** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |
| **Phase 7** | **A7: MLOps CI/CD with GitHub Actions** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |
| **Phase 8** | **A8: Model Monitoring with Prometheus & Grafana** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |
| **Phase 9** | **A9: Cloud ML Pipeline with AWS SageMaker** | Pending | Pending | Pending | Pending | Pending | `NOT STARTED` |

---

## Phase 1: Assignment 1 — Implement Dataset Versioning using DVC

> **Objective:** Establish data versioning best practices using DVC integrated with Git. Create, version, modify, roll back, and store datasets in local remote storage, demonstrating reproducibility and disaster recovery.

- [x] **Task 1.1: Workspace Git Baseline Setup**
  - *Action:* Verify or initialize the Git repository rooted at `final_submissions/`. Create `.gitignore` to exclude `__pycache__/`, `.venv/`, `.dvc/cache/`, and local temporary files while tracking code and metadata.
  - *Verification:* `git status` executes cleanly at the workspace root without untracked clutter.

- [x] **Task 1.2: A1 Environment & Folder Structure Initialization**
  - *Action:* Create dedicated folders inside `A1/`: `data/`, `src/`, `screenshots/`, and `storage/`. Ensure `A1/INSTRUCTIONS.pdf` remains untouched.
  - *Verification:* Subdirectories exist within `A1/`.

- [x] **Task 1.3: DVC Repository Initialization**
  - *Action:* Run `dvc init --subdir` inside `A1/` (or configure DVC tracking for the repository). Verify generation of `.dvc/` internal files and `.dvcignore`.
  - *Verification:* `dvc version` runs successfully and `.dvc` configuration directory is created.

- [x] **Task 1.4: Initial Dataset Creation (Version 1)**
  - *Action:* Create `A1/data/student.csv` with initial student records (`RollNo,Name,Marks` with rows: `1,Amit,80`, `2,Rahul,72`, `3,Priya,91`, `4,Sneha,88`).
  - *Verification:* `A1/data/student.csv` contains exactly 4 student records.

- [x] **Task 1.5: DVC Dataset Tracking (Version 1)**
  - *Action:* Execute `dvc add data/student.csv` inside `A1/`. Verify that `A1/data/student.csv.dvc` is generated and `A1/data/.gitignore` ignores `student.csv`.
  - *Verification:* `student.csv.dvc` is created containing the MD5 content hash.

- [x] **Task 1.6: Git Commit for Dataset Version 1**
  - *Action:* Stage and commit `student.csv.dvc` and `.gitignore` using `git add` and `git commit -m "A1: Track dataset version 1 with DVC"`.
  - *Verification:* `git log -1` records the Version 1 metadata commit.

- [x] **Task 1.7: Dataset Modification (Version 2)**
  - *Action:* Append record `5,Neha,77` to `A1/data/student.csv`.
  - *Verification:* File has 5 records.

- [x] **Task 1.8: DVC Tracking & Git Commit for Dataset Version 2**
  - *Action:* Execute `dvc add data/student.csv` to capture updated hash in `student.csv.dvc`. Stage and commit with `git commit -m "A1: Track dataset version 2 with DVC"`.
  - *Verification:* `student.csv.dvc` hash updates; Git log records Version 2.

- [x] **Task 1.9: Version Rollback Verification**
  - *Action:* Checkout Version 1 commit in Git (`git checkout <v1-hash> A1/data/student.csv.dvc`), run `dvc checkout`, and verify `student.csv` rolls back to 4 records.
  - *Verification:* `A1/data/student.csv` contains 4 rows.

- [x] **Task 1.10: Version Re-advance Verification**
  - *Action:* Checkout latest commit (`git checkout HEAD A1/data/student.csv.dvc`), run `dvc checkout`, and confirm `student.csv` returns to 5 records.
  - *Verification:* `A1/data/student.csv` contains 5 rows.

- [x] **Task 1.11: Local Remote Storage Configuration**
  - *Action:* Create directory `A1/storage/dvc_remote` and configure DVC remote: `dvc remote add -d local_remote storage/dvc_remote`. Commit `.dvc/config`.
  - *Verification:* `dvc remote list` displays `local_remote`.

- [x] **Task 1.12: Remote Push & Disaster Recovery Test**
  - *Action:* Execute `dvc push` to sync data hashes to `local_remote`. Delete `A1/data/student.csv` manually. Run `dvc pull` and confirm restored dataset.
  - *Verification:* Deleted file is restored bit-for-bit from remote storage.

- [x] **Task 1.13: Evidence & Screenshot Capture**
  - *Action:* Collect and save clear terminal screenshots showing DVC init, `dvc add`, Git history, `dvc checkout` rollback, remote push, and `dvc pull` into `A1/screenshots/`.
  - *Verification:* High-resolution images saved with captions.

- [x] **Task 1.14: A1 Assignment Documentation**
  - *Action:* Create `A1/README.md` documenting prerequisites, folder architecture, exact commands to reproduce versioning, rollback, and remote sync.
  - *Verification:* `A1/README.md` is complete and clear.

- [x] **Task 1.15: Academic Report Generation (`A1/report.docx`)**
  - *Action:* Generate `A1/report.docx` adhering strictly to `REPORT_TEMPLATE.docx`. Populate cover table (Shubham Bharnuke, Roll 36, PRN 12411834, TY AI&DS), Aim, Problem Statement, Objectives, DVC Background Theory, Architecture Diagram, Step-by-Step Procedure with commands & screenshots, Results Table, Observations, Conclusion, and IEEE references.
  - *Verification:* Document generated with zero unfilled placeholders.

- [x] **Task 1.16: Final Validation & Dedicated Git Commit**
  - *Action:* Review `git status`, verify all deliverables inside `A1/`, and commit: `git commit -m "Complete A1 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Commit created; working directory clean for A1.

---

## Phase 2: Assignment 2 — Track Machine Learning Experiments Using MLflow

> **Objective:** Develop a machine learning application and implement MLflow experiment tracking. Log hyperparameters, metrics, evaluation curves, and artifacts across multiple models; compare runs and register the top-performing model.

- [x] **Task 2.1: A2 Environment & Folder Setup**
  - *Action:* Create `A2/src/`, `A2/artifacts/`, `A2/screenshots/`, and `A2/models/`. Keep `A2/INSTRUCTIONS.pdf` untouched.
  - *Verification:* Directory structure in place.

- [x] **Task 2.2: Dataset Selection & Preprocessing Module**
  - *Action:* Author `A2/src/dataset.py` using Breast Cancer Wisconsin / Wine dataset. Implement 80/20 stratified train-test split and standard scaling.
  - *Verification:* Script returns preprocessed `X_train`, `X_test`, `y_train`, `y_test` with shapes verified.

- [x] **Task 2.3: MLflow Experiment Tracking Setup**
  - *Action:* In `A2/src/train.py`, configure MLflow tracking URI (local `./mlruns`) and create/set experiment `MLOps_Experiment_Tracking`.
  - *Verification:* MLflow initializes experiment without errors.

- [x] **Task 2.4: Experiment Run 1 — Logistic Regression**
  - *Action:* Train Logistic Regression with params (`C=0.1, 1.0`, `solver='lbfgs'`). Log parameters, evaluation metrics (Accuracy, Precision, Recall, F1-score), confusion matrix plot, and model artifact via `mlflow.sklearn.log_model`.
  - *Verification:* Run 1 logged with artifacts in MLflow.

- [x] **Task 2.5: Experiment Run 2 — Decision Tree Classifier**
  - *Action:* Train Decision Tree with params (`max_depth=4`, `criterion='gini'`). Log metrics, parameters, tree plot artifact, and model.
  - *Verification:* Run 2 successfully recorded.

- [x] **Task 2.6: Experiment Run 3 — Random Forest Classifier**
  - *Action:* Train Random Forest with params (`n_estimators=100`, `max_depth=5`). Log metrics, feature importance plot, ROC curve, and model artifact.
  - *Verification:* Run 3 recorded with full metrics.

- [x] **Task 2.7: Multi-Run Hyperparameter Tuning**
  - *Action:* Implement nested runs / hyperparameter grid over Random Forest (`n_estimators` in `[50, 100, 200]`, `max_depth` in `[3, 5, 8]`) logging each run.
  - *Verification:* At least 5 distinct runs present in the MLflow tracking store.

- [x] **Task 2.8: MLflow UI Inspection & Run Comparison**
  - *Action:* Launch `mlflow ui` on port 5000. Capture screenshots of experiment runs table, parallel coordinates plot, metric comparison charts, and artifact viewer.
  - *Verification:* Metrics compared side-by-side; best model identified.

- [x] **Task 2.9: Best Model Registration into MLflow Model Registry**
  - *Action:* Programmatically or via UI register the best-performing model as `BestClassificationModel` and transition stage to `Staging`/`Production`.
  - *Verification:* Registered model appears in MLflow Model Registry.

- [x] **Task 2.10: Inference Script from Model Registry**
  - *Action:* Create `A2/src/predict.py` loading model using `mlflow.pyfunc.load_model(model_uri)` to predict sample input data and verify output format.
  - *Verification:* Script outputs valid predictions matching expected classes.

- [x] **Task 2.11: A2 README & Reproducibility Guide**
  - *Action:* Create `A2/README.md` with dataset description, training execution instructions, MLflow UI commands, and prediction steps.
  - *Verification:* `A2/README.md` verified.

- [x] **Task 2.12: Academic Report Generation (`A2/report.docx`)**
  - *Action:* Generate `A2/report.docx` based on `REPORT_TEMPLATE.docx`. Include student details (Shubham Bharnuke), Aim, Objectives, MLflow Theory (Tracking, Artifacts, Registry), Comparative Model Metrics Table, MLflow UI Figures, Observations, and References.
  - *Verification:* Clean document without placeholders.

- [x] **Task 2.13: Final Validation & Dedicated Git Commit**
  - *Action:* Verify deliverables inside `A2/`, stage changes, and commit: `git commit -m "Complete A2 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Git commit logged cleanly.

---

## Phase 3: Assignment 3 — Design and Implement a Feature Engineering Pipeline

> **Objective:** Design, implement, persist, and reuse an end-to-end scikit-learn feature engineering pipeline handling missing values, encoding, scaling, and feature selection on a raw tabular dataset.

- [x] **Task 3.1: A3 Directory Structure Setup**
  - *Action:* Create `A3/data/`, `A3/src/`, `A3/models/`, `A3/output/`, and `A3/screenshots/`.
  - *Verification:* Subdirectories ready; `A3/INSTRUCTIONS.pdf` preserved.

- [x] **Task 3.2: Raw Dataset Acquisition & Exploratory Analysis**
  - *Action:* Place Titanic dataset into `A3/data/dataset.csv`. Write `A3/src/inspect_data.py` to display original shape `(891, 12)`, column data types, missing value percentages, and duplicate counts.
  - *Verification:* Inspection output accurately identifies numerical (`Age`, `Fare`) and categorical (`Sex`, `Pclass`, `Embarked`) columns.

- [x] **Task 3.3: Data Cleaning & Preprocessing Module**
  - *Action:* Implement `A3/src/preprocessing.py` containing transformers for numerical missing-value imputation (median) and categorical imputation (most frequent).
  - *Verification:* Preprocessing module cleans null values cleanly without data leakage.

- [x] **Task 3.4: Categorical Encoding & Numerical Scaling**
  - *Action:* Implement standard scaling for numerical features and One-Hot / Ordinal encoding for categorical features within ColumnTransformer.
  - *Verification:* Intermediate transformation produces numeric array with proper dimensionality.

- [x] **Task 3.5: Feature Selection Module**
  - *Action:* Implement `A3/src/feature_selection.py` using `SelectKBest` with ANOVA F-value / mutual info (or correlation analysis) to isolate the most predictive feature subset.
  - *Verification:* Selected feature names and importance scores printed.

- [x] **Task 3.6: Unified Pipeline Construction**
  - *Action:* In `A3/src/pipeline.py`, construct unified pipeline using `sklearn.pipeline.Pipeline` combining preprocessing, scaling, and feature selection.
  - *Verification:* Pipeline object passes `fit` and `transform` tests on raw input data.

- [x] **Task 3.7: Dataset Transformation & Output Generation**
  - *Action:* Execute pipeline on `A3/data/dataset.csv`, transform data, and save transformed output into `A3/output/transformed_data.csv`. Display original shape vs transformed shape.
  - *Verification:* `transformed_data.csv` is populated with clean, encoded numerical values.

- [x] **Task 3.8: Pipeline Serialization**
  - *Action:* Export fitted pipeline to `A3/models/feature_pipeline.pkl` using `joblib`.
  - *Verification:* `A3/models/feature_pipeline.pkl` is verified on disk and loadable.

- [x] **Task 3.9: Pipeline Deserialization & Inference Verification**
  - *Action:* Author `A3/src/inference.py` to load `feature_pipeline.pkl`, ingest unseen raw passenger records with missing attributes, transform them, and verify consistent output shapes.
  - *Verification:* Deterministic feature matrix generated for unseen inputs.

- [x] **Task 3.10: Screenshots & Execution Evidence**
  - *Action:* Capture terminal outputs showing dataset summary, transformation shapes, saved model files, and inference test.
  - *Verification:* Saved into `A3/screenshots/`.

- [x] **Task 3.11: A3 README Documentation**
  - *Action:* Write `A3/README.md` covering pipeline architecture, module breakdown, execution commands, and pipeline reuse instructions.
  - *Verification:* `A3/README.md` verified.

- [x] **Task 3.12: Academic Report Generation (`A3/report.docx`)**
  - *Action:* Build `A3/report.docx` based on `REPORT_TEMPLATE.docx`. Include student details, Feature Engineering theory (imputation, encoding, scaling, selection), Architecture Diagram, Code listings, Before-and-After Data Shapes Table, Observations, and IEEE References.
  - *Verification:* Complete document without template placeholders.

- [x] **Task 3.13: Final Validation & Dedicated Git Commit**
  - *Action:* Verify deliverables inside `A3/`, stage changes, and commit: `git commit -m "Complete A3 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Commit created cleanly.

---

## Phase 4: Assignment 4 — Build Workflow Automation Using Apache Airflow

> **Objective:** Implement workflow orchestration using Apache Airflow by designing an automated Directed Acyclic Graph (`data_pipeline_dag`) with sequential tasks: extraction $\rightarrow$ validation $\rightarrow$ processing $\rightarrow$ report generation $\rightarrow$ notification.

- [x] **Task 4.1: A4 Environment Setup & Directory Structure**
  - *Action:* Create `A4/dags/`, `A4/data/`, `A4/output/`, `A4/logs/`, and `A4/screenshots/`. Keep `A4/INSTRUCTIONS.pdf` untouched.
  - *Verification:* Directories prepared.

- [x] **Task 4.2: Airflow Environment Configuration**
  - *Action:* Configure localized Airflow environment (setting `AIRFLOW_HOME` to isolated path `A4/airflow_home` or using virtualenv/Docker standalone). Initialize database (`airflow db init`).
  - *Verification:* SQLite/database initialized and verified.

- [x] **Task 4.3: Implement Task 1 — Data Extraction (`extract`)**
  - *Action:* Author Python function `extract_data` to load raw dataset or generate structured sales/telecom records, saving output to `A4/data/raw_data.csv`.
  - *Verification:* `raw_data.csv` successfully produced.

- [x] **Task 4.4: Implement Task 2 — Data Validation (`validate`)**
  - *Action:* Author Python function `validate_data` to check schema integrity, detect nulls/outliers, and write validation log to `A4/output/validation_summary.json`.
  - *Verification:* Validation summary records record counts and verification pass/fail status.

- [x] **Task 4.5: Implement Task 3 — Data Processing (`process`)**
  - *Action:* Author Python function `process_data` to perform feature transformations, aggregations, and compute business metrics, saving output to `A4/output/processed_data.csv`.
  - *Verification:* Processed data generated with transformed values.

- [x] **Task 4.6: Implement Task 4 — Report Generation (`report`)**
  - *Action:* Author Python function `generate_report` to generate summary report (`A4/output/pipeline_report.txt`) summarizing total records, metrics, and completion timestamp.
  - *Verification:* Summary report generated.

- [x] **Task 4.7: Implement Task 5 — Pipeline Notification (`notify`)**
  - *Action:* Author Python function `send_notification` simulating alert dispatch (logging notification payload with pipeline status and execution metadata).
  - *Verification:* Notification log emitted.

- [x] **Task 4.8: Assemble Complete DAG (`data_pipeline_dag.py`)**
  - *Action:* In `A4/dags/data_pipeline_dag.py`, define DAG with default arguments (owner, retries, retry_delay), schedule interval, and instantiate tasks with `PythonOperator`. Set strict sequential dependencies:
    `t1_extract >> t2_validate >> t3_process >> t4_report >> t5_notify`.
  - *Verification:* DAG syntax valid (`python A4/dags/data_pipeline_dag.py` exits 0).

- [x] **Task 4.9: Airflow DAG Execution & Task State Verification**
  - *Action:* Test DAG execution via Airflow CLI (`airflow tasks test data_pipeline_dag extract <date>` through `notify`) or trigger run in Airflow scheduler.
  - *Verification:* All 5 tasks succeed (`success` state) with zero task failures.

- [x] **Task 4.10: Capture UI & Execution Screenshots**
  - *Action:* Capture screenshots of DAG Graph View, Grid View, Task duration / Gantt chart, and task execution logs into `A4/screenshots/`.
  - *Verification:* Clear screenshots depicting green successful runs saved.

- [x] **Task 4.11: A4 README Documentation**
  - *Action:* Author `A4/README.md` detailing Airflow architecture, DAG design, operator details, and instructions for setting `AIRFLOW_HOME` and running the DAG.
  - *Verification:* `A4/README.md` verified.

- [x] **Task 4.12: Academic Report Generation (`A4/report.docx`)**
  - *Action:* Generate `A4/report.docx` based on `REPORT_TEMPLATE.docx`. Include cover details (Shubham Bharnuke), Airflow theory (DAGs, Operators, Schedulers, Executors), DAG architecture diagram, task implementations, screenshots, and references.
  - *Verification:* Clean document without template placeholders.

- [x] **Task 4.13: Final Validation & Dedicated Git Commit**
  - *Action:* Review `A4/` deliverables, stage files, and commit: `git commit -m "Complete A4 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Git commit logged cleanly.

---

## Phase 5: Assignment 5 — Create REST API Using FastAPI

> **Objective:** Train an ML classification model and serve it via a robust production-grade REST API using FastAPI. Implement Pydantic schema validation, health checks, model metadata endpoints, single/batch prediction endpoints, automated Swagger UI documentation, and unit tests with `pytest`.

- [x] **Task 5.1: A5 Environment Setup & Directory Structure**
  - *Action:* Create `A5/app/`, `A5/models/`, `A5/tests/`, and `A5/screenshots/`. Keep `A5/INSTRUCTIONS.pdf` untouched.
  - *Verification:* Directory structure ready.

- [x] **Task 5.2: Model Training & Serialization**
  - *Action:* Author `A5/train.py` to train an Iris classification model (Random Forest / Logistic Regression) using scikit-learn. Evaluate accuracy on test set and serialize model and target labels to `A5/models/iris_model.pkl`.
  - *Verification:* `iris_model.pkl` generated; accuracy $\ge 0.90$.

- [x] **Task 5.3: Define Pydantic Schemas**
  - *Action:* In `A5/app/schemas.py`, create `IrisFeatures` (with `Field(..., gt=0)` validations for sepal/petal dimensions), `PredictionResponse` (`prediction_class`, `confidence_score`, `model_version`), and `BatchPredictionRequest`.
  - *Verification:* Schema rejects invalid/negative values with validation errors.

- [x] **Task 5.4: FastAPI Application Core Implementation**
  - *Action:* In `A5/app/main.py`, initialize FastAPI application with title, version, and description. Implement startup/lifespan handler to load `iris_model.pkl` into app state.
  - *Verification:* App initializes and loads model cleanly on startup.

- [x] **Task 5.5: Implement API Endpoints**
  - *Action:* Implement the following endpoints in `A5/app/main.py`:
    - `GET /` — Welcome message, API status, and documentation links.
    - `GET /health` — Health check endpoint reporting service availability and model load state.
    - `GET /model-info` — Metadata regarding model algorithm, features, and target classes.
    - `POST /predict` — Accepts `IrisFeatures`, runs inference, and returns predicted class and confidence score.
    - `POST /predict-batch` — Accepts list of samples and returns batch predictions.
  - *Verification:* All endpoints defined with proper status codes and error handlers (HTTP 400/422/500).

- [x] **Task 5.6: Implement Comprehensive Unit Test Suite**
  - *Action:* In `A5/tests/test_api.py`, author unit tests using `pytest` and `fastapi.testclient.TestClient`. Test `GET /`, `GET /health`, `GET /model-info`, valid `POST /predict`, invalid payload (422 Unprocessable Entity), and batch predictions.
  - *Verification:* `pytest A5/tests/ -v` executes with 100% test pass rate.

- [x] **Task 5.7: Run Server & Execute API Client Tests**
  - *Action:* Launch Uvicorn server (`uvicorn app.main:app --port 8000`). Execute sample curl/HTTP requests verifying JSON response formats.
  - *Verification:* Responses contain accurate species predictions and confidence scores.

- [x] **Task 5.8: Capture Swagger Documentation & Test Screenshots**
  - *Action:* Capture screenshots of interactive Swagger UI (`/docs`), ReDoc (`/redoc`), successful `/predict` execution, validation error responses, and pytest terminal results. Save to `A5/screenshots/`.
  - *Verification:* Clean screenshots organized with labels.

- [x] **Task 5.9: A5 README Documentation**
  - *Action:* Create `A5/README.md` covering prerequisites, setup, server launch instructions, API endpoint reference, example curl payloads, and testing procedures.
  - *Verification:* `A5/README.md` verified.

- [x] **Task 5.10: Academic Report Generation (`A5/report.docx`)**
  - *Action:* Generate `A5/report.docx` based on `REPORT_TEMPLATE.docx`. Include student cover details (Shubham Bharnuke), REST API & FastAPI Theory, Pydantic validation concepts, API Architecture Diagram, Endpoint Specifications Table, Test Cases & Pytest Output, Screenshots, and References.
  - *Verification:* Document generated with zero unfilled placeholders.

- [x] **Task 5.11: Final Validation & Dedicated Git Commit**
  - *Action:* Check deliverables inside `A5/`, stage changes, and commit: `git commit -m "Complete A5 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Git commit logged cleanly.

---

## Phase 6: Assignment 6 — Containerize an ML Model Using Docker

> **Objective:** Package a trained Machine Learning model and serving application into a lightweight, reproducible Docker container. Build the image, run the container in an isolated environment, and verify inference via port forwarding.

- [x] **Task 6.1: A6 Environment Setup & Directory Structure**
  - *Action:* Create `A6/src/`, `A6/models/`, and `A6/screenshots/`. Keep `A6/INSTRUCTIONS.pdf` untouched.
  - *Verification:* Directories prepared.

- [x] **Task 6.2: Train and Export ML Model**
  - *Action:* In `A6/src/train.py`, train a classification model (Random Forest / Logistic Regression) on Iris / Wine dataset and export to `A6/models/model.joblib`.
  - *Verification:* `model.joblib` created and verified.

- [x] **Task 6.3: Implement Serving Application**
  - *Action:* Author `A6/src/app.py` using Flask or FastAPI exposing `/health` and `/predict` endpoints that load `model.joblib` and return predictions.
  - *Verification:* App runs locally and returns valid predictions.

- [x] **Task 6.4: Dependency Manifest Creation**
  - *Action:* Create `A6/requirements.txt` with pinned, minimal dependencies (`scikit-learn`, `joblib`, `flask`/`fastapi`, `uvicorn`, `numpy`).
  - *Verification:* Requirements file created with no bloated packages.

- [x] **Task 6.5: Author Dockerfile & Dockerignore**
  - *Action:* Create `A6/Dockerfile` using multi-stage or lean base image `python:3.11-slim`. Set `WORKDIR /app`, copy `requirements.txt`, install dependencies with `--no-cache-dir`, copy application files, expose port 8080, and set `CMD ["python", "src/app.py"]`. Create `A6/.dockerignore` to exclude cache and git files.
  - *Verification:* Dockerfile follows containerization best practices.

- [x] **Task 6.6: Build Docker Container Image**
  - *Action:* Execute `docker build -t mlops-docker-model:v1 .` in `A6/`. Verify successful build and inspect image layers and size (`docker images mlops-docker-model:v1`).
  - *Verification:* Docker image built successfully.

- [x] **Task 6.7: Run Containerized Application**
  - *Action:* Start container in detached mode with port mapping: `docker run -d -p 8080:8080 --name mlops-prediction-service mlops-docker-model:v1`.
  - *Verification:* `docker ps` shows container in running state on port 8080.

- [x] **Task 6.8: Verify Containerized Inference**
  - *Action:* Send test HTTP prediction requests to `http://localhost:8080/predict` using curl or python script. Verify HTTP 200 response and correct prediction JSON.
  - *Verification:* Container returns accurate prediction outputs.

- [x] **Task 6.9: Inspect Container Logs & Teardown Verification**
  - *Action:* Check container logs via `docker logs mlops-prediction-service`. Stop and remove container cleanly (`docker stop`, `docker rm`).
  - *Verification:* Execution logs confirm received requests; teardown executes without errors.

- [x] **Task 6.10: Capture Container Execution Evidence**
  - *Action:* Capture screenshots of `docker build`, `docker images`, `docker ps`, curl inference request/response, and container logs into `A6/screenshots/`.
  - *Verification:* Evidence files saved.

- [x] **Task 6.11: A6 README Documentation**
  - *Action:* Author `A6/README.md` detailing container architecture, image build commands, run instructions, port mapping, and sample prediction requests.
  - *Verification:* `A6/README.md` verified.

- [x] **Task 6.12: Academic Report Generation (`A6/report.docx`)**
  - *Action:* Generate `A6/report.docx` based on `REPORT_TEMPLATE.docx`. Include cover details (Shubham Bharnuke), Containerization & Docker Theory (Images, Containers, Layers, Isolation), Dockerfile Architecture Diagram, Step-by-Step Procedure, Build & Run Screenshots, Observations, and References.
  - *Verification:* Clean document without template placeholders.

- [x] **Task 6.13: Final Validation & Dedicated Git Commit**
  - *Action:* Check deliverables inside `A6/`, stage files, and commit: `git commit -m "Complete A6 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Commit created cleanly.

---

## Phase 7: Assignment 7 — MLOps CI/CD Pipeline with GitHub Actions

> **Objective:** Study the existing project in `A7/INSTRUCTIONS/`, preserve its history and functionality, and implement an automated CI/CD pipeline using GitHub Actions (testing, linting, model accuracy validation threshold $\ge 0.80$, and simulated deployment).

- [x] **Task 7.1: Existing Project Discovery & Codebase Inspection**
  - *Action:* Inspect `A7/INSTRUCTIONS/` completely (`app.py`, `src/model.py`, `tests/test_model.py`, `requirements.txt`, `.github/workflows/ci-cd.yml`, `README.md`). Identify project dependencies (Python 3.11, scikit-learn, pytest) and validation threshold (accuracy $\ge 0.80$).
  - *Verification:* Existing project architecture and test rules documented.

- [x] **Task 7.2: Local Environment Setup & Baseline Execution**
  - *Action:* Install dependencies from `requirements.txt`. Execute `python src/model.py` and run `pytest -v` inside `A7/INSTRUCTIONS/`.
  - *Verification:* Baseline model trains, prints accuracy $\ge 0.80$, and unit test passes.

- [x] **Task 7.3: Test-Gating Failure Verification**
  - *Action:* Temporarily modify the accuracy threshold in `tests/test_model.py` to `0.99` and run `pytest -v`. Confirm test failure blocks execution, demonstrating pipeline gating logic. Restore threshold to `0.80`.
  - *Verification:* Test failure prevents downstream deployment as expected.

- [x] **Task 7.4: Review and Enhance GitHub Actions CI/CD Workflow**
  - *Action:* Review `.github/workflows/ci-cd.yml`. Ensure workflow features:
    - Triggers on `push` and `pull_request` to `main`.
    - **CI Test Job:** Python 3.11 setup, pip cache, dependency installation, code linting/syntax verification, and `pytest -v`.
    - **CD Deploy Job:** Explicit dependency `needs: test`, branch condition `if: github.ref == 'refs/heads/main'`, and deployment simulation.
  - *Verification:* YAML syntax validated against GitHub Actions schema.

- [x] **Task 7.5: Repository-Level Workflow Placement & Validation**
  - *Action:* Per PRD Section 6A, configure workflow visibility so GitHub Actions can detect it at repository level while preserving `A7/INSTRUCTIONS/` starter files intact.
  - *Verification:* Workflow paths mapped correctly without breaking overall repository structure.

- [x] **Task 7.6: Execute Local Pipeline Validation & Runner Check**
  - *Action:* Run automated test runner script or act/local CI simulation validating end-to-end execution of test and deploy steps.
  - *Verification:* Both CI test and CD deploy jobs pass cleanly in sequence.

- [x] **Task 7.7: Evidence & Test Execution Capture**
  - *Action:* Capture screenshots of passing pytest suite, failing test demonstration, workflow execution logs, and job status matrix into `A7/screenshots/`.
  - *Verification:* Evidence saved and captioned.

- [x] **Task 7.8: A7 Documentation Update**
  - *Action:* Create or update `A7/README.md` explaining the CI/CD pipeline, test rules, gating logic, and workflow execution steps.
  - *Verification:* `A7/README.md` verified.

- [x] **Task 7.9: Academic Report Generation (`A7/report.docx`)**
  - *Action:* Generate `A7/report.docx` based on `REPORT_TEMPLATE.docx`. Include cover details (Shubham Bharnuke), CI/CD Theory in MLOps, Pipeline Architecture Diagram (`Code Commit -> Build -> Test -> Deploy`), Step-by-Step Procedure, Pass vs Fail Test Scenarios Table, Screenshots, and IEEE References.
  - *Verification:* Clean document without template placeholders.

- [x] **Task 7.10: Final Validation & Dedicated Git Commit**
  - *Action:* Check deliverables inside `A7/`, stage changes, and commit: `git commit -m "Complete A7 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Git commit logged cleanly.

---

## Phase 8: Assignment 8 — Monitor a Machine Learning Model Using Prometheus and Grafana

> **Objective:** Build an end-to-end operational monitoring framework for a deployed ML model using Prometheus and Grafana. Instrument a FastAPI model service to expose latency, request volume, errors, and prediction distribution; visualize metrics in real-time Grafana dashboards.

- [x] **Task 8.1: A8 Environment Setup & Directory Structure**
  - *Action:* Create `A8/src/`, `A8/config/`, `A8/dashboards/`, and `A8/screenshots/`. Keep `A8/INSTRUCTIONS.pdf` untouched.
  - *Verification:* Directories prepared.

- [x] **Task 8.2: Train and Save Classification Model**
  - *Action:* In `A8/src/train.py`, train a classification model (Random Forest / Logistic Regression) on Iris or Breast Cancer dataset and save model to `A8/models/model.joblib`.
  - *Verification:* `model.joblib` created.

- [x] **Task 8.3: Instrument Model-Serving API with Prometheus Metrics**
  - *Action:* Author `A8/src/app.py` using FastAPI and `prometheus_client`. Instrument:
    - Counter `ml_prediction_requests_total` (`endpoint`, `status`).
    - Histogram `ml_prediction_latency_seconds` (`buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]`).
    - Counter `ml_prediction_errors_total` (`endpoint`, `error_type`).
    - Counter `ml_predictions_by_class_total` (`predicted_class`).
    - Expose Prometheus metrics endpoint `/metrics`.
  - *Verification:* `/metrics` endpoint exports custom Prometheus metrics on port 8000.

- [x] **Task 8.4: Create Prometheus Configuration**
  - *Action:* Author `A8/config/prometheus.yml` configuring scrape job `ml_api` with scrape interval `5s` pointing to application target `ml_api:8000`.
  - *Verification:* Prometheus configuration syntax validated.

- [x] **Task 8.5: Orchestrate Stack with Docker Compose**
  - *Action:* Create `A8/docker-compose.yml` linking 3 services:
    1. `ml_api` (FastAPI app on port 8000).
    2. `prometheus` (`prom/prometheus:latest` on port 9090).
    3. `grafana` (`grafana/grafana:latest` on port 3000).
  - *Verification:* `docker-compose config` validates without errors.

- [x] **Task 8.6: Implement Traffic Generation Script**
  - *Action:* Author `A8/src/traffic_generator.py` simulating client requests: 90% valid requests and 10% intentionally malformed requests (triggering HTTP 422/500 errors to test error rate tracking).
  - *Verification:* Script sends steady stream of requests and reports status codes.

- [x] **Task 8.7: Launch Monitoring Stack & Verify Targets**
  - *Action:* Launch stack (`docker-compose up -d`). Open Prometheus UI (`http://localhost:9090/targets`) and confirm `ml_api` target reports `UP`.
  - *Verification:* Target status `UP (1/1)` verified.

- [x] **Task 8.8: Execute and Validate PromQL Queries**
  - *Action:* Run required PromQL queries in Prometheus Expression Browser:
    - Request Rate: `sum(rate(ml_prediction_requests_total[5m]))`
    - Average Latency: `sum(rate(ml_prediction_latency_seconds_sum[5m])) / sum(rate(ml_prediction_latency_seconds_count[5m]))`
    - P95 Latency: `histogram_quantile(0.95, sum by (le) (rate(ml_prediction_latency_seconds_bucket[5m])))`
    - Error Rate: `sum(rate(ml_prediction_errors_total[5m])) / clamp_min(sum(rate(ml_prediction_requests_total[5m])), 1e-9)`
    - Scrape Health: `up{job="ml_api"}`.
  - *Verification:* All queries return valid metric vectors.

- [x] **Task 8.9: Build Grafana Dashboard & Export Configuration**
  - *Action:* Configure Prometheus data source in Grafana. Create interactive dashboard with 4 core panels (Request Volume, P95 Latency, Error Rate %, Service Health). Export dashboard JSON to `A8/dashboards/ml_monitoring_dashboard.json`.
  - *Verification:* Grafana dashboard reflects live metric variations during traffic generation.

- [x] **Task 8.10: Formulate Review Questions Analysis**
  - *Action:* Author detailed technical answers for the 7 review questions from the PDF (necessity of model monitoring, Prometheus vs Grafana, histogram benefits, P95 vs average latency, failure detection, accuracy/drift monitoring in production, operational metric limits).
  - *Verification:* Complete analysis prepared for report inclusion.

- [x] **Task 8.11: Capture Monitoring Screenshots**
  - *Action:* Capture screenshots of Prometheus Target status, PromQL execution graphs, Grafana dashboard panels under load, and error rate spikes into `A8/screenshots/`.
  - *Verification:* Screenshots verified.

- [x] **Task 8.12: A8 README & Stack Teardown**
  - *Action:* Author `A8/README.md` explaining architecture, compose commands, PromQL queries, and teardown instructions (`docker-compose down`).
  - *Verification:* `A8/README.md` verified.

- [x] **Task 8.13: Academic Report Generation (`A8/report.docx`)**
  - *Action:* Generate `A8/report.docx` based on `REPORT_TEMPLATE.docx`. Include cover details (Shubham Bharnuke), Monitoring Theory, System Architecture Diagram, PromQL Queries Table, Grafana Dashboard Screenshots, Answers to Review Questions, Observations, and IEEE References.
  - *Verification:* Clean document without template placeholders.

- [x] **Task 8.14: Final Validation & Dedicated Git Commit**
  - *Action:* Check deliverables inside `A8/`, stage files, and commit: `git commit -m "Complete A8 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Git commit logged cleanly.

---

## Phase 9: Assignment 9 — Train and Deploy a Machine Learning Model using AWS SageMaker

> **Objective:** Build an end-to-end cloud ML pipeline on AWS SageMaker. Manage training data in S3, write SageMaker script-mode training (`train.py`), train a Random Forest model, deploy real-time inference endpoint, expose via AWS Lambda and API Gateway, monitor with CloudWatch, and implement cost control teardown.

- [x] **Task 9.1: A9 Environment Setup & Directory Structure**
  - *Action:* Create `A9/src/`, `A9/cloud_configs/`, `A9/notebooks/`, and `A9/screenshots/`. Keep `A9/INSTRUCTIONS.pdf` untouched.
  - *Verification:* Directories prepared.

- [x] **Task 9.2: Data Preparation & S3 Asset Generation**
  - *Action:* Author `A9/src/prepare_data.py` using Breast Cancer Wisconsin dataset (569 samples, 30 numeric features, binary target). Perform 80/20 stratified split, save `A9/data/train.csv` and `A9/data/test.csv`, and prepare S3 upload commands.
  - *Verification:* Training and testing CSVs generated with correct shapes.

- [x] **Task 9.3: SageMaker Script-Mode Training Script (`train.py`)**
  - *Action:* Author `A9/src/train.py` parsing CLI hyperparameters (`--n-estimators`, `--max-depth`), loading data from SageMaker environment channels (`SM_CHANNEL_TRAIN`, `SM_CHANNEL_TEST`), training Random Forest, computing metrics (Accuracy, Precision, Recall, F1, ROC-AUC), and saving model artifact to `model.tar.gz`.
  - *Verification:* `train.py` satisfies SageMaker container entrypoint specifications.

- [x] **Task 9.4: Local Execution & Inference Simulation**
  - *Action:* Implement `A9/src/local_test.py` to run `train.py` locally and verify model serialization, scoring, and input handler (`model_fn`, `predict_fn`, `input_fn`).
  - *Verification:* Script executes and confirms model generates accurate predictions.

- [x] **Task 9.5: SageMaker Pipeline Orchestration Notebook**
  - *Action:* Create `A9/notebooks/sagemaker_pipeline.ipynb` utilizing SageMaker Python SDK (`sagemaker.sklearn.estimator.SKLearn`). Document IAM execution role setup, S3 bucket storage, estimator configuration, `estimator.fit()`, and `estimator.deploy()`.
  - *Verification:* Notebook contains complete end-to-end execution code and outputs.

- [x] **Task 9.6: AWS Lambda Function Integration Handler**
  - *Action:* Author `A9/cloud_configs/lambda_function.py` for AWS Lambda. Parse incoming JSON request from API Gateway, validate 30 features, call `boto3.client('sagemaker-runtime').invoke_endpoint`, and format HTTP response.
  - *Verification:* Lambda handler handles valid payloads and invalid inputs gracefully.

- [x] **Task 9.7: Amazon API Gateway REST Specification**
  - *Action:* Create `A9/cloud_configs/api_gateway_spec.json` (OpenAPI specification) defining `POST /predict` endpoint, request throttling, CORS headers, and Lambda proxy integration.
  - *Verification:* API Gateway specification validated.

- [x] **Task 9.8: CloudWatch Monitoring & Cost-Control Teardown Plan**
  - *Action:* Author `A9/cloud_configs/cloudwatch_alarms.json` configuring alarms for endpoint invocation latency, error counts, and instance CPU utilization. Document teardown commands (`endpoint.delete_endpoint()`) to prevent unwanted cloud billing.
  - *Verification:* Monitoring and cost control policies documented.

- [x] **Task 9.9: Evidence & Architecture Diagrams**
  - *Action:* Generate detailed cloud architecture diagram and capture screenshots of training metrics, endpoint configuration, S3 bucket structure, and Lambda integration into `A9/screenshots/`.
  - *Verification:* Evidence files saved.

- [x] **Task 9.10: A9 README Documentation**
  - *Action:* Author `A9/README.md` covering cloud architecture, IAM roles, S3 configuration, script-mode training, deployment, API Gateway invocation, and teardown.
  - *Verification:* `A9/README.md` verified.

- [x] **Task 9.11: Academic Report Generation (`A9/report.docx`)**
  - *Action:* Generate `A9/report.docx` based on `REPORT_TEMPLATE.docx`. Include cover details (Shubham Bharnuke), AWS SageMaker & Cloud ML Theory, Cloud Architecture Diagram, Step-by-Step Procedure, Evaluation Metrics Table, Lambda/API Gateway Integration, CloudWatch Monitoring, and IEEE References.
  - *Verification:* Clean document without template placeholders.

- [x] **Task 9.12: Final Validation & Dedicated Git Commit for A9**
  - *Action:* Check deliverables inside `A9/`, stage files, and commit: `git commit -m "Complete A9 assignment and report"`. Record commit hash in root tracker.
  - *Verification:* Git commit logged cleanly.

- [x] **Task 9.13: Root Progress Tracker & README Update**
  - *Action:* Update root `README.md` with final completion table across all 9 assignments, listing assignment titles, deliverables, report paths, validation status, and commit hashes.
  - *Verification:* Root `README.md` accurately reflects project status.

- [x] **Task 9.14: Final Multi-Assignment Audit & Completion Report**
  - *Action:* Perform complete audit against PRD Section 10 checklist:
    - [x] All 9 assignment folders contain complete implementations.
    - [x] All 8 instruction PDFs and A7 starter project are intact.
    - [x] All 9 formal `.docx` reports adhere to `REPORT_TEMPLATE.docx`.
    - [x] Git history reflects 9 dedicated assignment commits.
    - [x] Working tree is clean.
  - *Verification:* Handoff report prepared for the user.
