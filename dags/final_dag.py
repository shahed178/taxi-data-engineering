from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

def extract_data():
    df = pd.read_csv("/opt/airflow/data/taxi_data.csv")
    df.to_csv("/opt/airflow/data/extracted_taxi_data.csv", index=False)
    print("Extract completed")

def transform_data():
    df = pd.read_csv("/opt/airflow/data/extracted_taxi_data.csv")

    df = df.drop_duplicates()
    df = df.dropna()

    df = df[df["trip_distance"] > 0]
    df = df[df["fare_amount"] > 0]
    df = df[df["total_amount"] > 0]

    df.to_parquet("/opt/airflow/parquet/taxi_data.parquet", index=False)
    print("Transform completed")

def load_data():
    engine = create_engine("postgresql://postgres:password@postgres:5432/taxi_db")

    df = pd.read_parquet("/opt/airflow/parquet/taxi_data.parquet")

    df.to_sql(
        "trips",
        engine,
        if_exists="replace",
        index=False
    )

    print("Load completed")

with DAG(
    dag_id="final_taxi_etl_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract_csv_data",
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id="clean_and_transform_data",
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id="load_data_to_postgresql",
        python_callable=load_data
    )

    extract_task >> transform_task >> load_task
