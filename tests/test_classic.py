from importlib.util import resolve_name
import pytest
from requests.exceptions import HTTPError
import requests
import responses
from requests.auth import AuthBase

from classic import Classic
from request_builder import (
    IncorrectDataType,
    MalformedRequest,
    NotFound,
    RequestTimedOut,
)
from utils import NoIdentification, MultipleIdentifications, InvalidSubset

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


def response_builder(method: str, url: str, data_type: str = "json", status: int = 200):
    """
    Builds the response detail for a test request.

    :param method:
    :param url:
    :param body:
    :param json:
    :param status:

    :returns detail:
    """
    json = None
    body = None
    if data_type == "json":
        json = EXPECTED_JSON
    elif data_type == "xml":
        body = EXPECTED_XML
    else:
        raise IncorrectDataType("data_type must be either json or xml")

    response = responses.Response(
        method=method, url=url, body=body, json=json, status=status
    )

    return response


"""
/mobiledevices
"""


@responses.activate
def test_get_mobile_devices(classic):
    """
    Ensures get_mobile_devices returns content from the API and uses its
    authorization correctly.
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/mobiledevices")))
    assert classic.get_mobile_devices() == EXPECTED_JSON


@responses.activate
def test_get_mobile_devices_match(classic):
    """
    Ensures get_mobile_devices returns content from the API and uses its
    authorization correctly.
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/mobiledevices/match/iPad%2A")))
    assert classic.get_mobile_devices(match="iPad*") == EXPECTED_JSON


@responses.activate
def test_get_mobile_devices_500(classic):
    """
    Ensures that get_mobile_devices error out correctly when a 500 error
    is receieved.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledevices"), status=500)
    )
    with pytest.raises(HTTPError):
        classic.get_mobile_devices()


@responses.activate
def test_get_mobile_device_id_json(classic):
    """
    Ensures that get_mobile_device returns content from the API when using id
    as an identifier.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledevices/id/1001"))
    )
    assert classic.get_mobile_device(id="1001") == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_id_subset_json(classic):
    """
    Ensures that get_mobile_device returns content from the API when using id
    as an identifier.
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledevices/id/1001" "/subset/General%26Network"),
        )
    )
    assert (
        classic.get_mobile_device(id="1001", subsets=["General", "Network"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_id_subset_invalid_subset(classic):
    """
    Ensures that get_mobile_device raises InvalidSubset when passed an invalid
    subset for the endpoint.
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledevices/id/1001/subset/General&Network")
        )
    )
    with pytest.raises(InvalidSubset):
        classic.get_mobile_device(id=1001, subsets=["General", "Hardware"])


@responses.activate
def test_get_mobile_device_no_identification(classic):
    """
    Ensures that get_mobile_device raises NoIdentification when no form of
    identification is passed.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledevices/id/1001"))
    )
    with pytest.raises(NoIdentification):
        classic.get_mobile_device()


@responses.activate
def test_get_mobile_device_multiple_identification(classic):
    """
    Ensures that get_mobile_device raises MultipleIdentifications when more
    than one form of identification is passed to an endpoint.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledevices/id/1001"))
    )
    with pytest.raises(MultipleIdentifications):
        classic.get_mobile_device(id=1001, name="name")


@responses.activate
def test_get_mobile_device_id_xml(classic):
    """
    Ensures that get_mobile_device returns content from the API when using id
    as an identifier.
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledevices/id/1001"), data_type="xml"
        )
    )
    assert classic.get_mobile_device(id="1001", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_mobile_device_500(classic):
    """
    Ensures that get_mobile_device correctly raises a HTTPError when the request
    returns a 500 error.
    """
    responses.add(
        method="GET", url=jps_url("/JSSResource/mobiledevices/id/1001"), status=500
    )
    with pytest.raises(HTTPError):
        classic.get_mobile_device(id="1001")


@responses.activate
def test_update_mobile_device_id(classic):
    """
    Ensures that update_mobile_device returns content when updating a device
    using id as an identifier.
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/mobiledevices/id/1001"), data_type="xml"
        )
    )
    assert classic.update_mobile_device(EXPECTED_XML, id="1001") == EXPECTED_XML


@responses.activate
def test_update_mobile_device_id_400(classic):
    """
    Ensures that update_mobile_device raises MalformedRequest when the request
    returns a 400 status code.
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/mobiledevices/id/1001"), status=400
        )
    )
    with pytest.raises(MalformedRequest):
        classic.update_mobile_device(EXPECTED_XML, id="1001")


@responses.activate
def test_update_mobile_device_id_404(classic):
    """
    Ensures that update_mobile_device raises NotFound when the request
    returns a 404 status code.
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/mobiledevices/id/1001"), status=404
        )
    )
    with pytest.raises(NotFound):
        classic.update_mobile_device(EXPECTED_XML, id="1001")


@responses.activate
def test_update_mobile_device_id_502(classic):
    """
    Ensures that update_mobile_device raises RequestTimedOut when the request
    returns a 502 status code.
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/mobiledevices/id/1001"), status=502
        )
    )
    with pytest.raises(RequestTimedOut):
        classic.update_mobile_device(EXPECTED_XML, id="1001")


@responses.activate
def test_update_mobile_device_id_500(classic):
    """
    Ensures that update_mobile_device raises a HTTPError when the request
    returns an unrecognized HTTP error.
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/mobiledevices/id/1001"), status=500
        )
    )
    with pytest.raises(HTTPError):
        classic.update_mobile_device(EXPECTED_XML, id="1001")


@responses.activate
def test_create_mobile_device_id(classic):
    """
    Ensures that create_mobile_device returns content when creating/updating
    a mobile device.
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/mobiledevices/id/0"), data_type="xml"
        )
    )
    assert classic.create_mobile_device(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_create_mobile_device_id_HTTPError(classic):
    """
    Ensures that update_mobile_device raises a HTTPError when the request
    returns an unrecognized HTTP error.
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/mobiledevices/id/0"), status=500)
    )
    with pytest.raises(HTTPError):
        classic.create_mobile_device(EXPECTED_XML)

@responses.activate
def test_delete_mobile_device_id(classic):
    """
    Ensures that delete_mobile_device processes correctly when using id as
    identification
    """
    responses.add(response_builder("DELETE", jps_url(
        "/JSSResource/mobiledevices/id/1001"
    ), data_type="xml"))
    assert classic.delete_mobile_device(id=1001) == EXPECTED_XML

@responses.activate
def test_delete_mobile_device_id_500(classic):
    """
    Ensures that delete_mobile_device raises a HTTPError when processing an
    unrecognized HTTP error
    """
    responses.add(response_builder("DELETE", jps_url(
        "/JSSResource/mobiledevices/id/1001"
    ), status=500))
    with pytest.raises(HTTPError):
        classic.delete_mobile_device(id=1001)