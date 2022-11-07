from typing import Union
from urllib.parse import quote

import requests

from jamf_auth import JamfAuth


class RequestBuilder:
    """
    Handles auth and requests for the Classic and Pro modules

    :param base_url:
        Base URL of the JPS server
        e.g. https://example.jamfcloud.com
    :param username:
        Username for the JPS instance
    :param password:
        Password for the JPS instance

    :raises InvalidDataType:
        data_type is not json or xml
    """

    def __init__(self, base_url: str, username: str, password: str):  # pragma: no cover
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = JamfAuth(self.base_url, username, password)

    @classmethod
    def _raise_recognized_errors(self, r: requests.Response):
        if r.status_code == 400:
            raise MalformedRequest(
                "The request was not successful due to a client error, check "
                "your data for malformed XML or JSON. Jamf's response code "
                "was 400.\n "
                f"Response:\n{r.text}"
            )
        if r.status_code == 404:
            raise NotFound(
                "The requested resource did not exist, Jamf's response code was 404.\n"
                f"Response:\n{r.text}"
            )
        if r.status_code == 409:
            raise RequestConflict(
                "The request could not be completed due to a conflict in the request, "
                "this is most commonly caused by incorrect XML. Jamf's response code "
                "was 409.\n"
                f"Response:\n{r.text}"
            )
        if r.status_code == 502:
            raise RequestTimedOut(
                "The request timed out, check if you can load the endpoint in the GUI. "
                "Jamf's response code was 502.\n"
                f"Response:\n{r.text}"
            )

    def _get(
        self, endpoint: str, data_type: str = "json", query_string: list = None
    ) -> Union[dict, str]:
        """
        Sends get requests given an endpoint and data type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param data_type:
            json or xml
        :param query_string:
            Optional query string for the request

        :returns:
            - response.json - Returned if the data_type was json
            - response.text - Returned if the data_type was xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        if query_string:
            full_url = self.base_url + quote(endpoint) + f"?{'&'.join(query_string)}"
        else:
            full_url = self.base_url + quote(endpoint)
        headers = {"Accept": f"application/{data_type}"}
        response = self.session.get(full_url, headers=headers)
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:
            raise InvalidDataType("data_type needs to be either json or xml")

    def _post(
        self,
        endpoint: str,
        data: Union[dict, str],
        file: dict = None,
        data_type: str = "json",
        query_string: list = None,
    ) -> Union[dict, str]:
        """
        Sends post requests given an endpoint, data, and data_type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param data:
            XML data or json dict used in the post request
        :param file:
            File to upload in format {"filename": file}
        :param data_type:
            json or xml
        :param query_string:
            Optional query string for the request

        :raises InvalidDataType:
            data_type is not json or xml
        :raises ContentTypeAndFile:
            Content-type and file were both sent to the post module
        """
        if query_string:
            full_url = self.base_url + quote(endpoint) + f"?{'&'.join(query_string)}"
        else:
            full_url = self.base_url + quote(endpoint)
        if file and data_type:
            raise ContentTypeAndFile(
                "The post request cannot use both file and content-type headers."
            )
        if data_type in ["json", "xml"] and not file:
            headers = {"Content-type": f"application/{data_type}"}
            response = self.session.post(
                full_url, headers=headers, data=data, files=file
            )
        if not data_type and file:
            response = self.session.post(full_url, data=data, files=file)
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type in ["xml"]:
            return response.text
        elif not data_type:
            return "File uploaded successfully."
        else:
            raise InvalidDataType("data_type needs to be either json or xml")

    def _put(
        self,
        endpoint: str,
        data: Union[dict, str],
        data_type: str = "json",
        query_string: list = None,
    ) -> Union[dict, str]:
        """
        Sends put requests given an endpoint, data, and data_type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param data:
            xml data or json dict used in the put request
        :param data_type:
            json or xml
        :param query_string:
            Optional query string for the request

        :returns:
            - response.json - Returned if the data_type was json
            - response.text - Returned if the data_type was xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        if query_string:
            full_url = self.base_url + quote(endpoint) + f"?{'&'.join(query_string)}"
        else:
            full_url = self.base_url + quote(endpoint)
        headers = {"Content-type": f"application/{data_type}"}
        response = self.session.put(full_url, headers=headers, data=data)
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:
            raise InvalidDataType("data_type needs to be either json or xml")

    def _delete(
        self,
        endpoint: str,
        data: Union[dict, str] = None,
        data_type: str = "json",
        query_string: list = None,
    ) -> Union[dict, str]:
        """
        Sends delete requests given an endpoint and data type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param data_type:
            json or xml
        :param query_string:
            Optional query string for the request

        :returns:
            - response.json - Returned if the data_type was json
            - response.text - Returned if the data_type was xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        if query_string:
            full_url = self.base_url + quote(endpoint) + f"?{'&'.join(query_string)}"
        else:
            full_url = self.base_url + quote(endpoint)
        headers = {"Content-type": f"application/{data_type}"}
        response = self.session.delete(full_url, headers=headers, data=data)
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:
            raise InvalidDataType("data_type needs to be either json or xml")


class InvalidDataType(Exception):
    """Raised when the data_type parameter is not json or xml"""


class MalformedRequest(Exception):
    """
    The request was not successful due to a client error, check your data
    for malformed xml or json. Jamf's response code was 400.
    """


class NotFound(Exception):
    """
    The requested record could not be found. Jamf's response code was 404.
    """


class RequestConflict(Exception):
    """
    The changes could not be made due to a conflict in the request, this is
    most commonly caused by incorrect XML. Jamf's response code was 409.
    """


class RequestTimedOut(Exception):
    """
    The request timed out, check if you can load the endpoint in the GUI.
    Jamf's response code was 502.
    """


class ContentTypeAndFile(Exception):
    """
    The post request cannot use both file and content-type headers.
    """
