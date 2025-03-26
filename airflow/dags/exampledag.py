from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Definição da DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "Daily Data Gerenation.",
    default_args=default_args,
    description="Generate the data and execute the ELT.",
    schedule_interval="@daily",  # Executa diariamente
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id="extract_data",
        bash_command="python /src/python/main.py",
        dag=dag,
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    # Definição da ordem das tarefas
    extract_task >> transform_task >> load_task
