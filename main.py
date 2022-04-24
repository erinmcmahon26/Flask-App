from flask import Flask
from flask_restful import Api
from google.cloud import bigquery

app = Flask(__name__)
api = Api(app)

# constructing a BQ client object
client = bigquery.Client()

query = """
    SELECT *
    FROM bigquery-public-data.noaa_tsunami.historical_source_event
    LIMIT 20
"""

query_job = client.query(query) # make an API request

df = query_job.to_dataframe()
json_object = df.to_json(orient='records')

@app.route('/')
def query():
    response = json_object
    return response

