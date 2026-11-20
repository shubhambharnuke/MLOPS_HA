# Assignment 4: Build Workflow Automation Using Apache Airflow

**Course:** MLOps (AI3206C)  
**Student Name:** Shubham Bharnuke  
**PRN:** 12411834 | **Roll No:** 36 | **Class:** TY AI&DS (Div A)  
**Institution:** Bansilal Ramnath Agarwal Charitable Trust's Vishwakarma Institute of Technology, Pune  

---

## 1. Overview & Objective
The objective of this assignment is to understand workflow orchestration concepts and implement automated task scheduling and dependency management using **Apache Airflow**. In production MLOps systems, monolithic scripts fail silently when upstream dependencies crash. Directed Acyclic Graphs (DAGs) decompose complex workflows into discrete, modular, observable, and retryable units of execution.

---

## 2. DAG Design & Task Dependencies
The DAG named `data_pipeline_dag` implements 5 sequential tasks:
```
extract >> validate >> process >> report >> notify
```
1. **extract:** Generates or extracts structured customer records (`A4/data/raw_data.csv`).
2. **validate:** Checks schema validity and missing value thresholds, saving results to `A4/output/validation_summary.json`.
3. **process:** Imputes missing values, scales features, and creates engineered ratio features in `A4/output/processed_data.csv`.
4. **report:** Aggregates business performance and customer churn metrics into `A4/output/pipeline_report.txt`.
5. **notify:** Emits automated alert payloads and records execution logs in `A4/logs/notification.log`.

---

## 3. Directory Structure
```
A4/
├── INSTRUCTIONS.pdf              # Official Assignment Instruction Guide
├── README.md                     # Execution & Reproducibility Documentation
├── report.docx                   # Comprehensive Academic Submission Report
├── dags/
│   └── data_pipeline_dag.py      # Core Airflow DAG definition script
├── data/
│   └── raw_data.csv              # Extracted raw data
├── output/
│   ├── validation_summary.json   # Validation results log
│   ├── processed_data.csv        # Processed clean dataset
│   └── pipeline_report.txt       # Executive summary report
├── logs/
│   └── notification.log          # Automated alert audit trail
├── src/
│   ├── generate_screenshots.py   # Visual evidence generator
│   └── build_report.py           # Academic report generator
└── screenshots/
    ├── airflow_dag_graph_view.png # DAG Graph View (Green / Success states)
    └── dag_execution_logs.png     # Task log execution output
```

---

## 4. Execution Instructions

### A. Standalone DAG Verification Runner (Local PowerShell)
Run the pipeline directly through Python to execute all 5 tasks sequentially and generate outputs:
```bash
python A4/dags/data_pipeline_dag.py
```

### B. Launching & Viewing the Apache Airflow Web Dashboard (WSL2)
Because Apache Airflow requires a POSIX environment, it runs in WSL2 (Ubuntu). Note: Port 8088 is configured to avoid conflicts with other Docker services on port 8080.

1. **Verify or Start Airflow Standalone:**
   ```bash
   wsl -d Ubuntu
   export PATH="/home/arp10/airflow_env/bin:$PATH"
   export AIRFLOW_HOME="/home/arp10/airflow"
   export AIRFLOW__API_SERVER__PORT="8088"
   export AIRFLOW__WEBSERVER__WEB_SERVER_PORT="8088"
   airflow standalone
   ```

2. **Access the Dashboard:**
   - **URL:** [http://localhost:8088](http://localhost:8088)
   - **Username:** `admin`
   - **Password:** `mp66gqwWw3G5vrb2` (stored in `/home/arp10/airflow/simple_auth_manager_passwords.json.generated`)

3. **In the Web UI:**
   - Locate **`data_pipeline_dag`** in the DAGs list.
   - Click the DAG to open the **Graph View** or **Grid View** to observe the sequential task dependency execution: `extract >> validate >> process >> report >> notify`.
