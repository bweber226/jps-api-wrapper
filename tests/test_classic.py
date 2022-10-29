import pytest
import requests.exceptions
import requests
import responses
from requests.auth import AuthBase

from classic import Classic
from request_builder import IncorrectDataType

MOCK_AUTH_STRING = "This is a MockAuth"
EXPECTED_AUTH = {"Authorization": MOCK_AUTH_STRING}
EXAMPLE_JSS = "https://jss.example.com"
EXPECTED_JSON = {"test": "test_get_request"}
EXPECTED_XML = "<test />"

class ClassicTest(Classic):
    
    def __init__(self, base_url: str, auth: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth = auth


class MockAuth(AuthBase):
    def __call__(self, r):
        r.headers["Authorization"] = MOCK_AUTH_STRING
        return r


@pytest.fixture
def classic():
    return ClassicTest(EXAMPLE_JSS, MockAuth())


def jps_url(endpoint):
    return EXAMPLE_JSS + endpoint


def detail_builder(
    method: str, url: str, data_type: str = "json", status: int = 200
):
    """
    Builds the response detail for a test request.

    :param method:
    :param url:
    :param body:
    :param json:
    :param status:

    :return detail:
    """
    json = ""
    body = ""
    if data_type == "json":
        json = EXPECTED_JSON
    elif data_type == "xml":
        body = EXPECTED_XML
    else:
        raise IncorrectDataType("data_type must be either json or xml")

    detail = responses.Response(
        method=method,
        url=url,
        body=body,
        json=json,
        status=status
    )
    
    return detail

@responses.activate
def test_get_mobile_devices(classic):
    """
    Ensures get_mobile_devices returns content from the API and uses its
    authorization correctly.
    """
    responses.add(detail_builder("GET", jps_url("/JSSResource/mobiledevices")))
    assert classic.get_mobile_devices() == EXPECTED_JSON

@responses.activate
def test_get_mobile_devices_500(classic):
    """
    Ensures that get_mobile_devices error out correctly when a 500 error
    is receieved.
    """
    responses.add(detail_builder("GET", jps_url("/JSSResource/mobiledevices"), status=500))
    with pytest.raises(requests.exceptions.HTTPError):
        classic.get_mobile_devices()

@responses.activate
def test_get_mobile_device_500(classic):
    """
    test
    """
    responses.add(
        method="GET",
        url=jps_url("/JSSResource/mobiledevices/id/1001"),
        status=500
    )
    with pytest.raises(requests.exceptions.HTTPError):
        classic.get_mobile_device(1001)