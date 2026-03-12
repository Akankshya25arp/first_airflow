Project Title
Apache Airflow CSV ETL Pipeline

Description
This project demonstrates a simple ETL pipeline built using Apache Airflow 
running locally with Docker.

The pipeline processes a CSV file by performing the following steps:
1. Check if the input CSV file exists
2. Load and read the CSV data using Pandas
3. Move the processed file to a processed folder

This project demonstrates workflow orchestration, task dependencies,
and file-based data pipelines using Apache Airflow.
Pipeline Architecture
check_file → load_csv → move_file
Technologies Used

Apache Airflow

Docker

Python

Pandas

How to Run
docker compose up

Open Airflow UI:

http://localhost:8080
