import requests
import json

def execute_patch_method(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 170"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

execute_patch_method("ff808181923ed5e2019278ff089c7715")

#output - {"id":"ff808181923ed5e2019278ff089c7715","name":"Apple MacBook Pro 170","updatedAt":"2024-10-11T00:35:53.890+00:00","data":{"year":2019,"price":1849.99,"CPU model":"Intel Core i9","Hard disk size":"1 TB"}}
#200