import pandas as pd
import json

def get_csv_data(path, **kwargs):
    return pd.read_csv(path, **kwargs)

def get_excel_data(path, **kwargs):
    # pip install xlrd for xls files 
    return pd.read_excel(path, **kwargs)

# https://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en
def get_json_data(method, path, **kwargs):
    if method not in ("pandas","custom"):
        raise ValueError("method must be set to either 'pandas' or 'custom'")

    if method=='pandas':
        return pd.read_json(path, **kwargs)
    
    if method == 'custom':
        # Load the JSON file
        with open(path, 'r') as file:
            data = json.load(file)

        # Extract the list of "event" objects from the JSON
        events = data['result']['events']

        # Create a Pandas DataFrame
        df = pd.DataFrame(events)

        # Select specific columns
        df = df[['date', 'description', 'lang', 'category1', 'category2', 'granularity']]

        # Display the DataFrame
        return df