import requests
import logging

class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("GET", url, headers=header, data=payload)
        return response.json(), response.status_code

    def post_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("POST", url, headers=header, data=payload)
        return response.json(), response.status_code

    def put_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("PUT", url, headers=header, data=payload)
        self.log.info(f"response content : {response.text}")
        self.log.info(f"response status_code : {response.status_code}")
        return response.json(), response.status_code

    def get_patch(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("PATCH", url, headers=header, data=payload)
        return response.json(), response.status_code

    def delete_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("DELETE", url, headers=header, data=payload)
        return response.json(), response.status_code