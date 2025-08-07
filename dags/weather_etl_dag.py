from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/airflow')

from etl.extract import fetch_weather_data
from etl.transform import clean_weather_data
from etl.load import upload_to_bigquery

# thông số DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def run_etl():
    api_key = "e80e73135ab81e6a14600ea4474772c4"
    table_id = "weather-468210.weather_dataset.weather_data" 

    df = fetch_weather_data(api_key)
    df_clean = clean_weather_data(df)
    upload_to_bigquery(df_clean, table_id)

with DAG(
    dag_id='weather_etl_dag',
    default_args=default_args,
    start_date=datetime(2025, 8, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_weather_etl',
        python_callable=run_etl
    )

    etl_task
