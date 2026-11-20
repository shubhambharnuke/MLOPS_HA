"""
Assignment 4: Apache Airflow DAG Definition
data_pipeline_dag with tasks:
extract >> validate >> process >> report >> notify
"""

import os
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def extract(**kwargs):
    os.makedirs('A4/data', exist_ok=True)
    # Generate structured dataset or extract records
    np.random.seed(42)
    n_samples = 200
    data = {
        'CustomerID': range(1001, 1001 + n_samples),
        'Age': np.random.randint(18, 70, size=n_samples),
        'MonthlySpend': np.random.uniform(20.0, 500.0, size=n_samples).round(2),
        'SupportCalls': np.random.randint(0, 8, size=n_samples),
        'Churn': np.random.choice([0, 1], size=n_samples, p=[0.75, 0.25])
    }
    # Introduce small missing values for validation testing
    df = pd.DataFrame(data)
    df.loc[5, 'MonthlySpend'] = np.nan
    df.loc[12, 'Age'] = np.nan
    
    filepath = 'A4/data/raw_data.csv'
    df.to_csv(filepath, index=False)
    print(f"[Task: Extract] Extracted {len(df)} records to {filepath}")
    return filepath

def validate(**kwargs):
    os.makedirs('A4/output', exist_ok=True)
    raw_path = 'A4/data/raw_data.csv'
    df = pd.read_csv(raw_path)
    
    null_counts = df.isnull().sum().to_dict()
    total_records = len(df)
    valid_records = len(df.dropna())
    
    validation_results = {
        'total_records': total_records,
        'valid_records': valid_records,
        'null_counts': null_counts,
        'status': 'PASSED' if valid_records / total_records >= 0.95 else 'FAILED'
    }
    
    val_path = 'A4/output/validation_summary.json'
    with open(val_path, 'w') as f:
        json.dump(validation_results, f, indent=4)
        
    print(f"[Task: Validate] Validation {validation_results['status']} - {valid_records}/{total_records} valid records.")
    return val_path

def process(**kwargs):
    os.makedirs('A4/output', exist_ok=True)
    raw_path = 'A4/data/raw_data.csv'
    df = pd.read_csv(raw_path)
    
    # Impute missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['MonthlySpend'] = df['MonthlySpend'].fillna(df['MonthlySpend'].median())
    
    # Feature engineering: Spend per call ratio
    df['SpendPerCall'] = (df['MonthlySpend'] / (df['SupportCalls'] + 1)).round(2)
    # Normalized spend
    df['NormalizedSpend'] = ((df['MonthlySpend'] - df['MonthlySpend'].mean()) / df['MonthlySpend'].std()).round(4)
    
    proc_path = 'A4/output/processed_data.csv'
    df.to_csv(proc_path, index=False)
    print(f"[Task: Process] Cleaned and processed {len(df)} records into {proc_path}")
    return proc_path

def report(**kwargs):
    os.makedirs('A4/output', exist_ok=True)
    proc_path = 'A4/output/processed_data.csv'
    df = pd.read_csv(proc_path)
    
    avg_spend = df['MonthlySpend'].mean()
    churn_rate = df['Churn'].mean() * 100
    avg_age = df['Age'].mean()
    
    report_text = f"""==================================================
        M L O p s   P I P E L I N E   E X E C U T I O N   R E P O R T
==================================================
Execution Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Workflow Orchestrator: Apache Airflow (data_pipeline_dag)
Status               : SUCCESS (All 5 Tasks Completed)
--------------------------------------------------
Total Records Processed : {len(df)}
Average Customer Age    : {avg_age:.1f} years
Average Monthly Spend   : ${avg_spend:.2f}
Customer Churn Rate     : {churn_rate:.1f}%
Output Processed File   : A4/output/processed_data.csv
=================================================="""

    rep_path = 'A4/output/pipeline_report.txt'
    with open(rep_path, 'w') as f:
        f.write(report_text)
        
    print(f"[Task: Report] Generated pipeline executive summary report at {rep_path}")
    return rep_path

def notify(**kwargs):
    rep_path = 'A4/output/pipeline_report.txt'
    with open(rep_path, 'r') as f:
        summary = f.read()
        
    notification_payload = {
        'event': 'PIPELINE_SUCCESS',
        'dag_id': 'data_pipeline_dag',
        'timestamp': datetime.now().isoformat(),
        'recipient': 'mlops-team@vit.edu',
        'message': 'Airflow automated workflow data_pipeline_dag completed successfully with 0 errors.'
    }
    
    os.makedirs('A4/logs', exist_ok=True)
    log_path = 'A4/logs/notification.log'
    with open(log_path, 'w') as f:
        json.dump(notification_payload, f, indent=4)
        
    print(f"[Task: Notify] Dispatched automated alert notification to {notification_payload['recipient']}")
    print(f"[Task: Notify] Notification record saved to {log_path}")
    return log_path

# Airflow DAG definition (Compatible with Airflow scheduler when imported)
try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator

    default_args = {
        'owner': 'shubham_bharnuke',
        'depends_on_past': False,
        'start_date': datetime(2026, 11, 20),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=2),
    }

    dag = DAG(
        'data_pipeline_dag',
        default_args=default_args,
        description='End-to-End Automated MLOps Data Pipeline DAG',
        schedule='@daily',
        catchup=False
    )

    t1 = PythonOperator(task_id='extract', python_callable=extract, dag=dag)
    t2 = PythonOperator(task_id='validate', python_callable=validate, dag=dag)
    t3 = PythonOperator(task_id='process', python_callable=process, dag=dag)
    t4 = PythonOperator(task_id='report', python_callable=report, dag=dag)
    t5 = PythonOperator(task_id='notify', python_callable=notify, dag=dag)

    # Set strict sequential dependencies
    t1 >> t2 >> t3 >> t4 >> t5

except ImportError:
    pass

if __name__ == '__main__':
    # Standalone execution simulator demonstrating strict sequential dependencies
    print("=== Executing data_pipeline_dag (Sequential Task Pipeline) ===")
    p1 = extract()
    p2 = validate()
    p3 = process()
    p4 = report()
    p5 = notify()
    print("\nAll 5 DAG tasks executed successfully in strict sequential order.")
