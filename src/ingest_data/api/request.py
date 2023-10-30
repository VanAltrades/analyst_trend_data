import requests

def get_request_data(base_url : str, params : dict):
    
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        return response.json()

    else:
        print("Failed to retrieve news data. Status code:", response.status_code)