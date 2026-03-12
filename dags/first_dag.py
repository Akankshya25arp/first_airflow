from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import shutil
import pandas as pd

DATA_PATH = "/opt/airflow/data/employees.csv"
PROCESSED_PATH = "/opt/airflow/processed/employees.csv"

def check_file():
    if os.path.exists(DATA_PATH):
        print("File exists")
    else:
        raise FileNotFoundError("CSV file not found")

def load_csv():
    df = pd.read_csv(DATA_PATH)
    print("Data loaded:")
    print(df)

def move_file():
    shutil.move(DATA_PATH, PROCESSED_PATH)
    print("File moved to processed folder")

with DAG(
    dag_id="data_pipeline_local",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="check_file",
        python_callable=check_file
    )

    task2 = PythonOperator(
        task_id="load_csv",
        python_callable=load_csv
    )

    task3 = PythonOperator(
        task_id="move_file",
        python_callable=move_file
    )

    task1 >> task2 >> task3