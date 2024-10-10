import requests


class APIBase:

    def get_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("GET", url, headers=header, data=payload)
        return response.json()

    def post_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("POST", url, headers=header, data=payload)
        return response.json()

    def put_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("PUT", url, headers=header, data=payload)
        return response.json()

    def get_patch(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("PATCH", url, headers=header, data=payload)
        return response.json()

    def delete_method(self, url, header=None, payload=None):
        header = header if header else {}
        payload = payload if payload else {}
        response = requests.request("DELETE", url, headers=header, data=payload)
        return response.json()
