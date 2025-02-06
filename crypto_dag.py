from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from fetch_crypto_data import store_data

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 2, 6),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("crypto_pipeline", default_args=default_args, schedule_interval="*/5 * * * *")

task = PythonOperator(
    task_id="fetch_crypto_data",
    python_callable=store_data,
    dag=dag,
)