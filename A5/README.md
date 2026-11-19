# Assignment 5: Create REST API Using FastAPI

**Course:** MLOps (AI3206C)  
**Student Name:** Shubham Bharnuke  
**PRN:** 12411834 | **Roll No:** 36 | **Class:** TY AI&DS (Div A)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  

---

## 1. Overview & Aim
The objective of this assignment is to design, develop, test, and document a production-grade **REST API using FastAPI** for serving real-time predictions from a trained machine learning model. Models developed inside exploratory notebooks must be exposed via standardized, asynchronous HTTP interfaces with automated schema validation, health checks, error handling, interactive OpenAPI documentation, and automated unit testing.

---

## 2. API Endpoints Specification
| Method | Endpoint | Description | Request Body | Response Status |
|---|---|---|---|---|
| `GET` | `/` | Service root and navigation links | None | 200 OK |
| `GET` | `/health` | Health-check endpoint for orchestrators | None | 200 OK |
| `GET` | `/model-info` | Exposes model metadata & feature names | None | 200 OK |
| `POST` | `/predict` | Single sample flower prediction | `IrisInput` (JSON) | 200 OK / 422 Error |
| `POST` | `/predict-batch` | Batch inference prediction | `BatchIrisInput` (JSON) | 200 OK / 422 Error |
| `GET` | `/docs` | Interactive Swagger UI documentation | None | 200 OK |
| `GET` | `/redoc` | ReDoc API documentation | None | 200 OK |

---

## 3. Directory Structure
```
A5/
├── INSTRUCTIONS.pdf              # Official Assignment Instruction Guide
├── README.md                     # Execution & Reproducibility Documentation
├── report.docx                   # Comprehensive Academic Submission Report
├── train.py                      # Model training & serialization script
├── app/
│   ├── main.py                   # Core FastAPI application & route handlers
│   └── schemas.py                # Pydantic data models & input validations
├── models/
│   └── iris_model.pkl            # Serialized model and metadata bundle
├── tests/
│   └── test_api.py               # Pytest suite with TestClient (7 test cases)
├── src/
│   ├── generate_screenshots.py   # Visual evidence generator
│   └── build_report.py           # Academic report generator
└── screenshots/
    ├── pytest_execution.png      # 100% passing pytest test suite
    └── swagger_ui_predict_response.png # Live curl inference request and 422 handling
```

---

## 4. Execution Instructions
```bash
# 1. Train model
python A5/train.py

# 2. Run unit tests
python -m pytest A5/tests/test_api.py -v

# 3. Start local Uvicorn development server
uvicorn app.main:app --app-dir A5 --port 8000 --reload
```
