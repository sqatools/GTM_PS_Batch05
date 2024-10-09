import requests
import json

def execute_patch_method():
    url = "https://api.restful-api.dev/objects/7"

    payload = json.dumps({
        "name": "Apple MacBook Pro 16 (Updated Name)"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

execute_patch_method()