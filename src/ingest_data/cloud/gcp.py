def get_bigquery_data(query : str, client):

    query_job=client.query(query) 
    results = query_job.result()
    df = results.to_dataframe()
    return df