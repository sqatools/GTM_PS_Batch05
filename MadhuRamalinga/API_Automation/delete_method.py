import requests
import json

def execute_delete_method(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

execute_delete_method("ff808181923ed5e2019278ff089c7715")

#output - {"message":"Object with id = ff808181923ed5e2019278ff089c7715 has been deleted."}
#200