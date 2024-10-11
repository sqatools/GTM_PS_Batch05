import requests
import json

def execute_put_method(id):

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 160",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "2 TB",
            "color": "silver"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

execute_put_method("ff808181923ed5e2019276fb37f27396")

#output - {"id":"ff808181923ed5e2019276fb37f27396","name":"Apple MacBook Pro 160","updatedAt":"2024-10-11T00:29:00.275+00:00","data":{"year":2019,"price":2049.99,"CPU model":"Intel Core i10","Hard disk size":"2 TB","color":"silver"}}
#200