from google.cloud import bigquery
import os

def upload_to_bigquery(df, table_id, key_path="key.json"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",
        schema=[
            bigquery.SchemaField("city", "STRING"),
            bigquery.SchemaField("country", "STRING"),
            bigquery.SchemaField("temperature", "FLOAT"),
            bigquery.SchemaField("humidity", "FLOAT"),
            bigquery.SchemaField("weather", "STRING"),
            bigquery.SchemaField("timestamp", "TIMESTAMP"),
        ]
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()

    print(f"✅ Đã upload {len(df)} dòng vào {table_id}")
