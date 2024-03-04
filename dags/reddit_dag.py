import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

from pipelines.aws_s3_pipeline import upload_s3_pipeline