# app1/utils.py
import requests
from decouple import config
base_url = config("BASE_URL")

def callRestApi(api_name,api_params = {}):
    # Your common function logic here
    api_url = base_url+api_name
    response = requests.get(api_url, params=api_params)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    data_from_api = response.json()
    return data_from_api
