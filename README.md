This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.





** This is the workflow of the project **
![image](https://github.com/manhzeff/Reddit-DataEngineering/assets/104782892/b2057394-9d39-437b-a970-241a7ee8b564)

The pipeline is designed to:

Extract data from Reddit using its API.
Store the raw data into an S3 bucket from Airflow.
Transform the data using AWS Glue and Amazon Athena.
Load the transformed data into Amazon Redshift for analytics and querying.


