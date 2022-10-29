import requests

from jamf_auth import JamfAuth

class RequestBuilder:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = JamfAuth(self.base_url, username, password)

    def get(self, endpoint: str, data_type: str = "json"):
        full_url = self.base_url + endpoint
        headers = {"Accept": f"application/{data_type}"}
        response = self.session.get(full_url, headers=headers)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:
            raise IncorrectDataType("data_type needs to be either json or xml")

    def post(self, endpoint: str, data, data_type: str = "json"):
        full_url = self.base_url + endpoint
        headers = {"Content-type": f"application/{data_type}"}
        response = self.session.post(full_url, headers=headers, data=data)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:
            raise IncorrectDataType("data_type needs to be either json or xml")

    def put(self, endpoint: str, data, data_type: str = "json"):
        full_url = self.base_url + endpoint
        headers = {"Content-type": f"application/{data_type}"}
        response = self.session.put(full_url, headers=headers, data=data)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:
            raise IncorrectDataType("data_type needs to be either json or xml")

    def delete(self, endpoint: str, data_type: str = "json"):
        full_url = self.base_url + endpoint
        headers = {"Content-type": f"application/{data_type}"}
        response = self.session.delete(full_url, headers=headers)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:
            raise IncorrectDataType("data_type needs to be either json or xml")


class IncorrectDataType(Exception):
    """Raised when the data_type parameter is not json or xml"""
