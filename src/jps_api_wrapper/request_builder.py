import re
from os.path import exists, expanduser, splitext
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

    def __enter__(self):  # pragma: no cover
        self.session.auth.refresh_auth_if_needed()
        return self

    def __exit__(self, exception_type, exception_value, traceback):  # pragma: no cover
        self.session.auth.invalidate()

    @classmethod
    def _raise_recognized_errors(self, r: requests.Response):
        if r.status_code == 400:
            raise ClientError(
                "The request was not successful due to a client error, check "
                "your data for malformed JSON, XML, or URL. Jamf's response "
                "code was 400.\n "
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
        self,
        endpoint: str,
        data_type: str = "json",
        params: dict = None,
        success_message: str = None,
        headers=None,
    ) -> Union[dict, str]:
        """
        Sends get requests given an endpoint and data type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param data_type:
            json or xml
        :param params:
            Optional params for the request
        :param headers:
            Optional headers for content that is not JSON or XML which are
            handled by the method

        :returns:
            - response.json - Returned if the data_type was json
            - response.text - Returned if the data_type was xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        full_url = self.base_url + quote(endpoint)
        if not headers:
            headers = {"Accept": f"application/{data_type}"}
        response = self.session.get(full_url, headers=headers, params=params)
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if success_message:
            return success_message
        elif data_type == "json":
            return response.json()
        elif data_type in ["xml", None]:
            return response.text
        else:
            raise InvalidDataType("data_type needs to be either json or xml")

    def _download(self, endpoint: str, params: dict = None):  # pragma: no cover
        """
        Sends get request with special cases that require file downloads

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param params:
            Optional params for the request
        """
        full_url = self.base_url + quote(endpoint)
        headers = {"Accept": "application/json"}
        response = self.session.get(full_url, headers=headers, params=params)
        self._raise_recognized_errors(response)
        response.raise_for_status()
        try:
            filename = re.findall(
                '(?<=filename=").*(?=")', response.headers.get("content-disposition")
            )[0]
        except TypeError:
            filename = "jamf-download"
            if "image" in response.headers.get("Content-type"):
                filename = (
                    filename + "." + response.headers.get("Content-type").split("/")[-1]
                )
        filepath = expanduser(f"~/Downloads/{filename}")
        if exists(filepath):
            original_filepath = filepath
            i = 1
            if "." in filename:
                name, ext = splitext(original_filepath)
                while exists(filepath):
                    filepath = name + f"({i})" + ext
                    i += 1
            else:
                while exists(filepath):
                    filepath = original_filepath + f"({i})"
                    i += 1
            filename = filepath.split("/")[-1]

        with open(filepath, "wb") as f:
            f.write(response.content)
        return (
            f"File {filename} successfully downloaded to current users "
            "Downloads folder."
        )

    def _post(
        self,
        endpoint: str,
        data: Union[dict, str] = None,
        file: dict = None,
        params: dict = None,
        headers: dict = None,
        success_message: str = None,
        data_type: str = "json",
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
        :param params:
            Optional params for the request
        :param headers:
            Optional headers for content that is not JSON or XML which are
            handled by the method
        :param success_message:
            Optional string to return instead of request data
        :param data_type:
            json or xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        full_url = self.base_url + quote(endpoint)
        if not file:
            if not headers:
                headers = {"Content-type": f"application/{data_type}"}
            if data_type == "xml":
                response = self.session.post(
                    full_url, headers=headers, data=data, params=params
                )
            else:
                response = self.session.post(
                    full_url, headers=headers, json=data, params=params
                )
        if file:
            response = self.session.post(full_url, data=data, params=params, files=file)
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if success_message:
            return success_message
        elif data_type == "json":
            return response.json()
        elif data_type in ["xml", None]:
            return response.text
        else:  # pragma: no cover
            raise InvalidDataType("data_type needs to be either json or xml")

    def _put(
        self,
        endpoint: str,
        data: Union[dict, str],
        params: dict = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Sends put requests given an endpoint, data, and data_type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param data:
            xml data or json dict used in the put request
        :param params:
            Optional params for the request
        :param data_type:
            json or xml

        :returns:
            - response.json - Returned if the data_type was json
            - response.text - Returned if the data_type was xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        full_url = self.base_url + quote(endpoint)
        headers = {"Content-type": f"application/{data_type}"}
        if data_type == "xml":
            response = self.session.put(
                full_url, headers=headers, data=data, params=params
            )
        else:
            response = self.session.put(
                full_url, headers=headers, json=data, params=params
            )
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:  # pragma: no cover
            raise InvalidDataType("data_type needs to be either json or xml")

    def _patch(
        self,
        endpoint: str,
        data: Union[dict, str],
        params: dict = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Sends patch requests given an endpoint, data, and data_type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param data:
            xml data or json dict used in the put request
        :param params:
            Optional params for the request
        :param data_type:
            json or xml

        :returns:
            - response.json - Returned if the data_type was json
            - response.text - Returned if the data_type was xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        full_url = self.base_url + quote(endpoint)
        headers = {"Content-type": f"application/{data_type}"}
        if data_type == "xml":
            response = self.session.patch(
                full_url, headers=headers, data=data, params=params
            )
        else:
            response = self.session.patch(
                full_url, headers=headers, json=data, params=params
            )
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if data_type == "json":
            return response.json()
        elif data_type == "xml":
            return response.text
        else:  # pragma: no cover
            raise InvalidDataType("data_type needs to be either json or xml")

    def _delete(
        self,
        endpoint: str,
        data: Union[dict, str] = None,
        params: dict = None,
        success_message: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Sends delete requests given an endpoint and data type

        :param endpoint:
            The url section of the api endpoint following the base_url
            e.g. /JSSResource/computers
        :param params:
            Optional params for the request
        :param success_message:
            Optional string to return instead of request data
        :param data_type:
            json or xml

        :returns:
            - response.json - Returned if the data_type was json
            - response.text - Returned if the data_type was xml

        :raises InvalidDataType:
            data_type is not json or xml
        """
        # + was added as a safe character to make
        # Classic.log_flush_interval work, need to find a better workaround
        full_url = self.base_url + quote(endpoint, safe="/+")
        headers = {"Content-type": f"application/{data_type}"}
        response = self.session.delete(
            full_url, headers=headers, data=data, params=params
        )
        self._raise_recognized_errors(response)
        response.raise_for_status()
        if success_message:
            return success_message
        elif data_type == "json":  # pragma: no cover
            return response.json()
        elif data_type == "xml":
            return response.text
        else:  # pragma: no cover
            raise InvalidDataType("data_type needs to be either json or xml")


class InvalidDataType(Exception):
    """Raised when the data_type parameter is not json or xml"""


class ClientError(Exception):
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
