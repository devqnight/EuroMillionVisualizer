import requests
import json

def get_parsed_data_from_api(api):
    response_API = requests.get(api)
    data = response_API.text
    parsed_data = json.loads(data)  
    return parsed_data

def get_parsed_data_from_api_param_date(api, date):
    return get_parsed_data_from_api(api.strip()+'?dates='+date)