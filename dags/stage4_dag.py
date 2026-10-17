from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
with DAG(
   dag_id="stage4_preprocessing_dag",
   start_date=datetime(2026, 5, 1),
   schedule=None,
   catchup=False
) as dag:
   run_preprocessing = BashOperator(
       task_id="run_preprocessing_script",
       bash_command="python /usr/local/airflow/dags/stage4_preprocessing/preprocessing.py"
   )
   check_output = BashOperator(
       task_id="check_cleaned_dataset",
       bash_command="ls /usr/local/airflow/dags/stage4_preprocessing/cleaned_taxi_data.csv"
   )
   run_preprocessing >> check_output
