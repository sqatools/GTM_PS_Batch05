import requests
import json

def execute_put_method():

    url = "https://api.restful-api.dev/objects/7"

    payload = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

execute_put_method()