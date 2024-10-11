import requests
import json

def execute_post_method():

    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

execute_post_method()

#output - {"id":"ff808181923ed5e2019278f878f87709","name":"Apple MacBook Pro 16","createdAt":"2024-10-11T00:29:31.396+00:00","data":{"year":2019,"price":1849.99,"CPU model":"Intel Core i9","Hard disk size":"1 TB"}}
#200

#id: ff808181923ed5e2019278f878f87709