import requests
import json

def execute_delete_method():
    url = "https://api.restful-api.dev/objects/6"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

execute_delete_method()