import requests
"""
pip install requests
"""


def execute_get_method():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)
    data = response.json()
    for val in data:
        print(val)

#execute_get_method()


def get_specific_ids():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10&id=6"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

# get_specific_ids()


def get_one_single_ids():
    url = "https://api.restful-api.dev/objects/7"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

#get_one_single_ids()

def create_new_entry():

    import json
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


create_new_entry()
