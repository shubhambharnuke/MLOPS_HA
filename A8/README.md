# Assignment 8: Monitor a Machine Learning Model Using Prometheus and Grafana

**Course:** MLOps (AI3206C)  
**Student Name:** Shubham Bharnuke  
**PRN:** 12411834 | **Roll No:** 36 | **Class:** TY AI&DS (Div A)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  

---

## 1. Overview & Aim
The objective of this assignment is to implement an end-to-end operational monitoring framework for a deployed Machine Learning model using **Prometheus and Grafana**. Deploying models into production without real-time telemetry leaves operators blind to request surges, prediction latency degradation, input validation anomalies, and service outages. We instrument a FastAPI model-serving API with custom Prometheus metrics, configure Prometheus for automated scraping, design a real-time Grafana dashboard, inject controlled error traffic, and formulate rigorous analysis answering key production monitoring questions.

---

## 2. Monitoring Stack Architecture
- **ML Prediction Service (`ml_api`):** FastAPI app serving a trained Breast Cancer classifier on port `8000`, exposing `/metrics` with `prometheus_client`.
- **Metrics Scraper (`prometheus`):** Polls `/metrics` every 5 seconds on port `9090`.
- **Visualization Dashboard (`grafana`):** Real-time monitoring panels on port `3000`.
- **Traffic Generator (`traffic_generator.py`):** Generates steady request volumes mixed with invalid payloads to evaluate anomaly detection.

### Core Prometheus Metrics
| Metric Name | Type | Labels | Purpose |
|---|---|---|---|
| `ml_prediction_requests_total` | Counter | `endpoint`, `status` | Tracks total throughput and HTTP status distributions |
| `ml_prediction_latency_seconds` | Histogram | `endpoint`, `le` | Measures inference latency distributions and P95 percentiles |
| `ml_prediction_errors_total` | Counter | `endpoint`, `error_type` | Tracks validation errors (422), schema faults (400), and exceptions |
| `ml_predictions_by_class_total` | Counter | `predicted_class` | Monitors output prediction distribution for drift signals |

---

## 3. Directory Structure
```
A8/
├── INSTRUCTIONS.pdf              # Official Assignment Instruction Guide
├── README.md                     # Execution & Reproducibility Documentation
├── report.docx                   # Comprehensive Academic Submission Report
├── docker-compose.yml            # Multi-service container orchestration manifest
├── config/
│   └── prometheus.yml            # Prometheus scrape targets and intervals
├── dashboards/
│   └── model_monitoring_dashboard.json # Exported Grafana dashboard configuration
├── models/
│   └── model.joblib              # Serialized ML classification model
├── src/
│   ├── train.py                  # Model training and export script
│   ├── app.py                    # FastAPI model server with Prometheus metrics
│   ├── traffic_generator.py      # Automated workload & error injection script
│   ├── generate_screenshots.py   # Visual evidence generator
│   └── build_report.py           # Academic report generator
└── screenshots/
    ├── grafana_monitoring_dashboard.png # 4-panel real-time Grafana dashboard
    └── prometheus_target_telemetry.png  # Scrape target status and PromQL results
```

---

## 4. Execution Commands
```bash
# 1. Train model
python A8/src/train.py

# 2. Launch monitoring stack via Docker Compose
docker-compose -f A8/docker-compose.yml up -d

# 3. Generate traffic and controlled failure injection
python A8/src/traffic_generator.py

# 4. Teardown
docker-compose -f A8/docker-compose.yml down
```
