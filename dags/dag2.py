from airflow import Dataset
from airflow.decorators import task, dag
from datetime import datetime

# Define dataset
file_dataset = Dataset('/opt/airflow/data/output1.txt')

@task
def read_and_process_file():
    file_path = file_dataset.uri
    with open(file_path, 'r') as f:
        content = f.read()

    # Process content (for example, reversing the content)
    processed_content = content[::-1]
    print(f"Processed content: {processed_content}")  # Example: Reverse content

    # Return the processed content or any other status
    return processed_content  # Return the processed content as a value

@dag(
    dag_id="second_dag",
    start_date=datetime(2023, 1, 1),
    catchup=False
)
def consumer_dag():
    read_and_process_file()

consumer_dag = consumer_dag()
