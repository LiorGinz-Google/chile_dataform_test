from google.cloud import bigquery

client = bigquery.Client()

#gcs_uri = 'gs://cloud-samples-data/bigquery/us-states/us-states.json'

dataset = client.create_dataset('dataproc_test')
table_id = dataset.table('ginzberg_family')
schema = [
          bigquery.SchemaField("first_name", "STRING", mode="REQUIRED"),
          bigquery.SchemaField("last_name", "INTEGER", mode="REQUIRED"),
          bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
         ]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)
