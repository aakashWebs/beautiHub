# app1/utils.py
import requests
def callRestApi(api_name,api_params = {}):
    # Your common function logic here
    api_url = 'http://127.0.0.1:8000/api/'+api_name
    response = requests.get(api_url, params=api_params)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    data_from_api = response.json()
    return data_from_api
