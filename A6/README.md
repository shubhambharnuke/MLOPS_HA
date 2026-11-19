# Assignment 6: Containerize an ML Model Using Docker

**Course:** MLOps (AI3206C)  
**Student Name:** Shubham Bharnuke  
**PRN:** 12411834 | **Roll No:** 36 | **Class:** TY AI&DS (Div A)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  

---

## 1. Overview & Aim
The objective of this assignment is to containerize a trained Machine Learning model using **Docker** and execute the model in an isolated, reproducible environment. Machine learning models depend on precise versions of runtimes, C++ system libraries (BLAS/LAPACK), and language dependencies. Containerizing the model encapsulates the code, weights, dependencies, and web serving interface into an immutable image that runs identically on developer workstations, test clusters, or Kubernetes nodes.

---

## 2. Docker Packaging Architecture
- **Base Image:** `python:3.11-slim` (minimal attack surface, lean footprint)
- **Application:** Flask REST API (`A6/src/app.py`)
- **Serialized Model:** Scikit-learn Random Forest classifier (`A6/models/model.joblib`)
- **Port Mapping:** Host `8080` mapped to Container `8080`
- **Healthcheck:** Automated `curl -f http://localhost:8080/health` interval polling

---

## 3. Directory Structure
```
A6/
├── INSTRUCTIONS.pdf              # Official Assignment Instruction Guide
├── README.md                     # Execution & Reproducibility Documentation
├── report.docx                   # Comprehensive Academic Submission Report
├── Dockerfile                    # Container definition manifest
├── .dockerignore                 # Excludes caches and temporary files
├── requirements.txt              # Pinned Python package dependencies
├── src/
│   ├── train.py                  # Model training and export script
│   ├── app.py                    # Container entrypoint REST serving API
│   ├── generate_screenshots.py   # Visual evidence generator
│   └── build_report.py           # Academic report generator
├── models/
│   └── model.joblib              # Exported model weights and labels
└── screenshots/
    ├── docker_build_run.png      # Docker build, image verification & docker ps
    └── docker_inference_logs.png # HTTP inference requests and container logs
```

---

## 4. Execution Commands
```bash
# 1. Train and export model
python A6/src/train.py

# 2. Build Docker container image
cd A6
docker build -t mlops-docker-model:v1 .

# 3. Run container in detached mode
docker run -d -p 8080:8080 --name mlops-prediction-service mlops-docker-model:v1

# 4. Test prediction endpoint
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'

# 5. Teardown
docker stop mlops-prediction-service
docker rm mlops-prediction-service
```
