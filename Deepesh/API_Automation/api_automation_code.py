import requests
import json
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


# create_new_entry()

# ID = ff808181923ed5e2019276f9c7007394

def put_method_to_update_details(id):

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

#put_method_to_update_details("ff808181923ed5e2019276f9c7007394")


def patch_mobile_details(id):

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
       "name": "Apple MacBook Pro 170",
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("PATCH", url, headers=headers, data=payload)
    print(response.text)
    print(response.status_code)


#patch_mobile_details("ff808181923ed5e2019276f9c7007394")
#patch_mobile_details("ff808181923ed5e2019276f9c7007394")

#try to patch the details  after deleting the entry
# {"error":"The Object with id = ff808181923ed5e2019276f9c7007394 doesn't exist. Please provide an object id which exists or generate a new Object using POST request and capture the id of it to use it as part of PATCH request after that."}
# 404

patch_mobile_details("1")

def delete_mobile_details(id):

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)
    print(response.status_code)

# delete_mobile_details("ff808181923ed5e2019276f9c7007394")
# {"message":"Object with id = ff808181923ed5e2019276f9c7007394 has been deleted."}
