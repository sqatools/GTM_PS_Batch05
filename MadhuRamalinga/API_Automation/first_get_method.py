import requests

def execute_get_method():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    print(response.status_code)

execute_get_method()    