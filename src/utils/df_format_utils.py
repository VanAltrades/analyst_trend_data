import plotly.express as px
import re

def get_year_from_series(date):
    try:
        year = int(date)
        return year
    except ValueError:
        match = re.search(r'(-?\d+)', str(date))
        if match:
            year = int(match.group(0))
            return year
        return None

def transform_series_to_year(data, date_column : str):
    # Apply the custom function to the 'date' column
    data['year'] = data[date_column].apply(get_year_from_series)
    return data.dropna()

def group_trend(data, dimensions : list, agg_dict : dict):
    grouped = data.groupby(by=dimensions).agg(agg_dict)
    return grouped.reset_index(inplace=True)