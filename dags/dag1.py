# dag1.py
from airflow import Dataset
from airflow.decorators import task, dag
from airflow.operators.dagrun_operator import TriggerDagRunOperator  # Import the TriggerDagRunOperator
from datetime import datetime

# Define dataset
file_dataset = Dataset('/opt/airflow/data/output1.txt')

@task
def write_to_file():
    file_path = file_dataset.uri
    with open(file_path, 'w') as f:
        f.write("Hello from the first DAG!")  # Example content

@dag(
    dag_id="first_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    params={"example_param": "default_value"},
)
def producer_dag():
    write_to_file_task = write_to_file()

    # Trigger second DAG after write_to_file completes
    trigger_second_dag = TriggerDagRunOperator(
        task_id='trigger_second_dag',
        trigger_dag_id='second_dag',  # The second DAG ID to trigger
        conf={},  # Optional: pass additional parameters to second DAG if needed
    )

    write_to_file_task >> trigger_second_dag  # Ensure second DAG is triggered after the task completes

producer_dag = producer_dag()
