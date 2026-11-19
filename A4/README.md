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
```bash
# Execute standalone DAG verification runner
python A4/dags/data_pipeline_dag.py
```
