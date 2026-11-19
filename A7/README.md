# Assignment 7: MLOps CI/CD Pipeline with GitHub Actions

**Course:** MLOps (AI3206C)  
**Student Name:** Shubham Bharnuke  
**PRN:** 12411834 | **Roll No:** 36 | **Class:** TY AI&DS (Div A)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  

---

## 1. Overview & Objective
The objective of this assignment is to study the provided starter project in `A7/INSTRUCTIONS/` and implement an automated **Continuous Integration and Continuous Deployment (CI/CD)** pipeline using **GitHub Actions**. In production MLOps workflows, code changes and model training scripts must undergo automated regression tests, syntax validation, and accuracy threshold verification before being deployed to staging or production environments.

---

## 2. Pipeline Overview & Gating Architecture
```
Code Commit / PR -> Build & Dependencies -> Unit & Accuracy Test -> Conditional Deploy
```
- **Trigger Conditions:** `push` or `pull_request` to the `main` branch.
- **CI Test Job (`test`):**
  - Runs on `ubuntu-latest`
  - Sets up Python 3.11
  - Installs requirements (`scikit-learn`, `pytest`)
  - Executes unit tests with `pytest -v` asserting model accuracy $\ge 0.80$
- **CD Deploy Job (`deploy`):**
  - Dependent on upstream test pass (`needs: test`)
  - Conditional branch protection (`if: github.ref == 'refs/heads/main'`)
  - Executes deployment simulation

### Gating Matrix
| Scenario | Test Job | Deploy Job |
|---|---|---|
| Tests pass on `main` | **Passed** | **Runs & Deploys** |
| Model Accuracy fails (<0.80) | **Failed** | **Skipped (Blocked)** |
| Pull Request to `main` | **Runs** | **Skipped (Protected)** |

---

## 3. Directory Structure
```
A7/
├── README.md                     # Execution & Architecture Documentation
├── report.docx                   # Comprehensive Academic Submission Report
├── INSTRUCTIONS/                 # Original starter project directory
│   ├── .github/workflows/
│   │   └── ci-cd.yml             # GitHub Actions declarative workflow
│   ├── src/
│   │   └── model.py              # Iris Logistic Regression model
│   ├── tests/
│   │   └── test_model.py         # Unit test asserting accuracy >= 0.80
│   ├── app.py                    # Inference application
│   ├── requirements.txt          # Pinned dependencies
│   └── README.md                 # Starter documentation
├── src/
│   ├── simulate_cicd.py          # Local CI/CD pipeline simulation runner
│   ├── generate_screenshots.py   # Visual evidence generator
│   └── build_report.py           # Academic report generator
└── screenshots/
    ├── github_actions_workflow_passing.png # Successful run trace
    └── github_actions_test_failure_gating.png # Blocked deployment demonstration
```

---

## 4. Execution Commands
```bash
# 1. Run model training locally
python A7/INSTRUCTIONS/src/model.py

# 2. Run unit tests
cd A7/INSTRUCTIONS
python -m pytest tests/test_model.py -v

# 3. Run complete CI/CD pipeline simulation
python A7/src/simulate_cicd.py
```
