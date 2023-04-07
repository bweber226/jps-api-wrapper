from unittest import mock

import pytest
import requests
import responses
from requests.auth import AuthBase
from requests.exceptions import HTTPError

from jps_api_wrapper.classic import Classic
from jps_api_wrapper.request_builder import (
    InvalidDataType,
    ClientError,
    NotFound,
    RequestConflict,
    RequestTimedOut,
)
from jps_api_wrapper.utils import (
    ConflictingParameters,
    InvalidParameterOptions,
    InvalidSubset,
    MissingParameters,
    MultipleIdentifications,
    NoIdentification,
    NoParametersOrData,
    ParametersAndData,
)

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
        raise InvalidDataType("data_type must be either json or xml")

    response = responses.Response(
        method=method, url=url, body=body, json=json, status=status
    )

    return response


"""
/accounts
"""


@responses.activate
def test_get_accounts_json(classic):
    """
    Ensures data is returned when accessing get_accounts with json
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/accounts")))
    assert classic.get_accounts() == EXPECTED_JSON


@responses.activate
def test_get_accounts_json_500(classic):
    """
    Ensures get_accounts raises HTTPError when an unrecognized HTTP error
    is raised
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/accounts"), status=500))
    with pytest.raises(HTTPError):
        classic.get_accounts()


@responses.activate
def test_get_accounts_json_invalid_data_type(classic):
    """
    Ensures get_accounts raises InvalidDataType when used with data_type is not
    json or xml
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/accounts")))
    with pytest.raises(InvalidDataType):
        classic.get_accounts(data_type="test")


@responses.activate
def test_get_account_group_id_json(classic):
    """
    Ensures data is returned when get_account_group is used with an id
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/accounts/groupid/1001"))
    )
    assert classic.get_account_group(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_account_group_name_json(classic):
    """
    Ensures data is returned when get_account_group us used with a name
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/accounts/groupname/name"))
    )
    assert classic.get_account_group(name="name") == EXPECTED_JSON


@responses.activate
def test_get_account_group_id_500(classic):
    """
    Ensures that get_account_group raises HTTPError when the request returns
    an unrecognized HTTP error
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/accounts/groupid/1001"), status=500
        )
    )
    with pytest.raises(HTTPError):
        classic.get_account_group(id=1001)


@responses.activate
def test_create_account_group(classic):
    """
    Ensures that create_account_group returns data when creating an account
    group.
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/accounts/groupid/0"), data_type="xml"
        )
    )
    assert classic.create_account_group(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_create_account_group_500(classic):
    """
    Ensures that create_account_group raises HTTPError when receiving an
    unrecognized HTTP error from a request.
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/accounts/groupid/0"),
            data_type="xml",
            status=500,
        )
    )
    with pytest.raises(HTTPError):
        classic.create_account_group(EXPECTED_XML)


@responses.activate
def test_update_account_group_name(classic):
    """
    Ensures that update_account_group returns data when updating an account
    group by name
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/accounts/groupname/testgroup"), data_type="xml"
        )
    )
    assert classic.update_account_group(EXPECTED_XML, name="testgroup") == EXPECTED_XML


@responses.activate
def test_update_account_group_id(classic):
    """
    Ensures that update_account_group returns data when updating an account
    group by id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/accounts/groupid/1001"), data_type="xml"
        )
    )
    assert classic.update_account_group(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_delete_account_group_name(classic):
    """
    Ensures that delete_account_group returns data when updating an account
    group by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/accounts/groupname/testgroup"),
            data_type="xml",
        )
    )
    assert classic.delete_account_group(name="testgroup") == EXPECTED_XML


@responses.activate
def test_delete_account_group_id(classic):
    """
    Ensures that delete_account_group returns data when deleting an account
    group by id
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/accounts/groupid/1001"), data_type="xml"
        )
    )
    assert classic.delete_account_group(id=1001) == EXPECTED_XML


@responses.activate
def test_get_account_id_json(classic):
    """
    Ensures data is returned when get_account is used with an id
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/accounts/userid/1001")))
    assert classic.get_account(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_account_name_json(classic):
    """
    Ensures data is returned when get_account is used with a name
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/accounts/username/name"))
    )
    assert classic.get_account(name="name") == EXPECTED_JSON


@responses.activate
def test_get_account_id_500(classic):
    """
    Ensures that get_account raises HTTPError when the request returns
    an unrecognized HTTP error
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/accounts/userid/1001"), status=500
        )
    )
    with pytest.raises(HTTPError):
        classic.get_account(id=1001)


@responses.activate
def test_create_account(classic):
    """
    Ensures that create_account returns data when creating an account.
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/accounts/userid/0"), data_type="xml"
        )
    )
    assert classic.create_account(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_create_account_500(classic):
    """
    Ensures that create_account raises HTTPError when receiving an
    unrecognized HTTP error from a request.
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/accounts/userid/0"),
            data_type="xml",
            status=500,
        )
    )
    with pytest.raises(HTTPError):
        classic.create_account(EXPECTED_XML)


@responses.activate
def test_update_account_name(classic):
    """
    Ensures that update_account returns data when updating an account by name
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/accounts/username/testuser"), data_type="xml"
        )
    )
    assert classic.update_account(EXPECTED_XML, name="testuser") == EXPECTED_XML


@responses.activate
def test_update_account_id(classic):
    """
    Ensures that update_account returns data when updating an account by id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/accounts/userid/1001"), data_type="xml"
        )
    )
    assert classic.update_account(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_delete_account_name(classic):
    """
    Ensures that delete_account returns data when deleting an account by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/accounts/username/testuser"),
            data_type="xml",
        )
    )
    assert classic.delete_account(name="testuser") == EXPECTED_XML


@responses.activate
def test_delete_account_id(classic):
    """
    Ensures that delete_account returns data when deleting an account by id
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/accounts/userid/1001"), data_type="xml"
        )
    )
    assert classic.delete_account(id=1001) == EXPECTED_XML


"""
/activationcode
"""


@responses.activate
def test_get_activation_code_json(classic):
    """
    Ensures that get_activation_code returns a json dict when passing "json" to
    the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/activationcode")))
    assert classic.get_activation_code() == EXPECTED_JSON


@responses.activate
def test_get_activation_code_xml(classic):
    """
    Ensures that get_activation_code returns an XML str when passing "xml" to
    the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/activationcode"), data_type="xml")
    )
    assert classic.get_activation_code(data_type="xml") == EXPECTED_XML


@responses.activate
def test_update_activation_code(classic):
    """
    Ensures that update_activation_code returns data when updating the
    activation code.
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/activationcode"), data_type="xml")
    )
    assert classic.update_activation_code(EXPECTED_XML) == EXPECTED_XML


"""
/advancedcomputersearches
"""


@responses.activate
def test_get_advanced_computer_searches_json(classic):
    """
    Ensures that get_advanced_computer_searches returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/advancedcomputersearches"))
    )
    assert classic.get_advanced_computer_searches() == EXPECTED_JSON


@responses.activate
def test_get_advanced_computer_searches_xml(classic):
    """
    Ensures that get_advanced_computer_searches returns an XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/advancedcomputersearches"), data_type="xml"
        )
    )
    assert classic.get_advanced_computer_searches(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_advanced_computer_search_id_json(classic):
    """
    Ensures that get_advanced_computer_search returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/advancedcomputersearches/id/1001")
        )
    )
    assert classic.get_advanced_computer_search(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_advanced_computer_search_name_xml(classic):
    """
    Ensures that get_advanced_computer_search returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/advancedcomputersearches/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_advanced_computer_search(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_advanced_computer_search_id(classic):
    """
    Ensures that create_advanced_computer_search returns data when creating
    an advanced computer search with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/advancedcomputersearches/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_advanced_computer_search(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_advanced_computer_search_id(classic):
    """
    Ensures that update_advanced_computer_search returns data when updating
    an advanced computer search with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/advancedcomputersearches/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_advanced_computer_search(EXPECTED_XML, id=1001) == EXPECTED_XML
    )


@responses.activate
def test_update_advanced_computer_search_name(classic):
    """
    Ensures that update_advanced_computer_search returns data when updating
    an advanced computer search with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/advancedcomputersearches/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_advanced_computer_search(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_advanced_computer_search_id(classic):
    """
    Ensures that delete_advanced_computer_search returns data when deleting an
    advanced computer search by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/advancedcomputersearches/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_advanced_computer_search(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_advanced_computer_search_name(classic):
    """
    Ensures that delete_advanced_computer_search returns data when deleting an
    advanced computer search by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/advancedcomputersearches/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_advanced_computer_search(name="testname") == EXPECTED_XML


"""
/advancedmobiledevicesearches
"""


@responses.activate
def test_get_advanced_mobile_device_searches_json(classic):
    """
    Ensures that get_advanced_mobile_device_searches returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/advancedmobiledevicesearches"))
    )
    assert classic.get_advanced_mobile_device_searches() == EXPECTED_JSON


@responses.activate
def test_get_advanced_mobile_device_searches_xml(classic):
    """
    Ensures that get_advanced_mobile_device_searches returns an XML str when
    passing "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/advancedmobiledevicesearches"), data_type="xml"
        )
    )
    assert classic.get_advanced_mobile_device_searches(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_advanced_mobile_device_search_id_json(classic):
    """
    Ensures that get_advanced_mobile_device_search returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/advancedmobiledevicesearches/id/1001")
        )
    )
    assert classic.get_advanced_mobile_device_search(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_advanced_mobile_device_search_name_xml(classic):
    """
    Ensures that get_advanced_mobile_device_search returns XML when passing
    "xml" as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/advancedmobiledevicesearches/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_advanced_mobile_device_search(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_advanced_mobile_device_search_id(classic):
    """
    Ensures that create_advanced_mobile_device_search returns data when
    updating an advanced mobile device search with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/advancedmobiledevicesearches/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_advanced_mobile_device_search(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_advanced_mobile_device_search_id(classic):
    """
    Ensures that update_advanced_mobile_device_search returns data when
    updating an advanced mobile device search with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/advancedmobiledevicesearches/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_advanced_mobile_device_search(EXPECTED_XML, id=1001)
        == EXPECTED_XML
    )


@responses.activate
def test_update_advanced_mobile_device_search_name(classic):
    """
    Ensures that update_advanced_mobile_device_search returns data when
    updating an advanced mobile device search with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/advancedmobiledevicesearches/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_advanced_mobile_device_search(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_advanced_mobile_device_search_id(classic):
    """
    Ensures that delete_advanced_mobile_device_search returns data when
    deleting an advanced mobile device search by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/advancedmobiledevicesearches/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_advanced_mobile_device_search(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_advanced_mobile_device_search_name(classic):
    """
    Ensures that delete_advanced_mobile_device_search returns data when
    deleting an advanced mobile search by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/advancedmobiledevicesearches/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_advanced_mobile_device_search(name="testname") == EXPECTED_XML


"""
/advancedusersearches
"""


@responses.activate
def test_get_advanced_user_searches_json(classic):
    """
    Ensures that get_advanced_user_searches returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/advancedusersearches")))
    assert classic.get_advanced_user_searches() == EXPECTED_JSON


@responses.activate
def test_get_advanced_user_searches_xml(classic):
    """
    Ensures that get_advanced_user_searches returns an XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/advancedusersearches"), data_type="xml"
        )
    )
    assert classic.get_advanced_user_searches(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_advanced_user_search_id_json(classic):
    """
    Ensures that get_advanced_user_search returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/advancedusersearches/id/1001"))
    )
    assert classic.get_advanced_user_search(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_advanced_user_search_name_xml(classic):
    """
    Ensures that get_advanced_user_search returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/advancedusersearches/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_advanced_user_search(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_advanced_user_search_id(classic):
    """
    Ensures that create_advanced_user_search returns data when creating
    an advanced user search with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/advancedusersearches/id/0"), data_type="xml"
        )
    )
    assert classic.create_advanced_user_search(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_advanced_user_search_id(classic):
    """
    Ensures that update_advanced_user_search returns data when updating
    an advanced user search with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/advancedusersearches/id/1001"), data_type="xml"
        )
    )
    assert classic.update_advanced_user_search(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_advanced_user_search_name(classic):
    """
    Ensures that update_advanced_user_search returns data when updating
    an advanced user search with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/advancedusersearches/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_advanced_user_search(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_advanced_user_search_id(classic):
    """
    Ensures that delete_advanced_user_search returns data when deleting an
    advanced user search by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/advancedusersearches/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_advanced_user_search(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_advanced_user_search_name(classic):
    """
    Ensures that delete_advanced_user_search returns data when deleting an
    advanced user search by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/advancedusersearches/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_advanced_user_search(name="testname") == EXPECTED_XML


"""
/allowedfileextensions
"""


@responses.activate
def test_get_allowed_file_extensions_json(classic):
    """
    Ensures get_allowed_file_extensions returns json when "json" is passed
    as the data_type param.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/allowedfileextensions"))
    )
    assert classic.get_allowed_file_extensions() == EXPECTED_JSON


@responses.activate
def test_get_allowed_file_extensions_xml(classic):
    """
    Ensures get_allowed_file_extensions returns xml when "xml" is passed as the
    data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/allowedfileextensions"), data_type="xml"
        )
    )
    assert classic.get_allowed_file_extensions(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_allowed_file_extension_id_json(classic):
    """
    Ensures get_allowed_file_extension returns json when "json" is passed as
    the data_type param and the id identifier is used
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/allowedfileextensions/id/1001"))
    )
    assert classic.get_allowed_file_extension(1001) == EXPECTED_JSON


@responses.activate
def test_get_allowed_file_extension_name_xml(classic):
    """
    Ensures get_allowed_file_extension returns XML when "xml" is passed as the
    data_type param and the name identifier is used
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/allowedfileextensions/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_allowed_file_extension(name="testname", data_type="xml")


@responses.activate
def test_create_allowed_file_extension(classic):
    """
    Ensures create_allowed_file_extension returns content when creating an
    allowed file extension
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/allowedfileextensions/id/0"), data_type="xml"
        )
    )
    assert classic.create_allowed_file_extension(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_delete_allowed_file_extension(classic):
    """
    Ensures delete_allowed_file_extension returns content when deleting an
    allowed file extension
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/allowedfileextensions/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_allowed_file_extension(1001) == EXPECTED_XML


"""
/buildings
"""


@responses.activate
def test_get_buildings_json(classic):
    """
    Ensures that get_buildings returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/buildings")))
    assert classic.get_buildings() == EXPECTED_JSON


@responses.activate
def test_get_buildings_xml(classic):
    """
    Ensures that get_buildings returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/buildings"), data_type="xml")
    )
    assert classic.get_buildings(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_building_id_json(classic):
    """
    Ensures that get_building returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/buildings/id/1001")))
    assert classic.get_building(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_building_name_xml(classic):
    """
    Ensures that get_building returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/buildings/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_building(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_building_id(classic):
    """
    Ensures that create_building returns data when creating
    a building with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/buildings/id/0"), data_type="xml"
        )
    )
    assert classic.create_building(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_building_id(classic):
    """
    Ensures that update_building returns data when updating
    a building with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/buildings/id/1001"), data_type="xml"
        )
    )
    assert classic.update_building(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_building_name(classic):
    """
    Ensures that update_building returns data when updating
    a building with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/buildings/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_building(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_building_id(classic):
    """
    Ensures that delete_building returns data when deleting a
    building by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/buildings/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_building(id=1001) == EXPECTED_XML


"""
/byoprofiles
"""


@responses.activate
def test_get_byo_profiles_json(classic):
    """
    Ensures that get_byo_profiles returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/byoprofiles")))
    assert classic.get_byo_profiles() == EXPECTED_JSON


@responses.activate
def test_get_byo_profiles_xml(classic):
    """
    Ensures that get_byo_profiles returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/byoprofiles"), data_type="xml")
    )
    assert classic.get_byo_profiles(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_byo_profile_id_json(classic):
    """
    Ensures that get_byo_profile returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/byoprofiles/id/1001")))
    assert classic.get_byo_profile(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_byo_profile_name_xml(classic):
    """
    Ensures that get_byo_profile returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/byoprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_byo_profile(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_byo_profile_id(classic):
    """
    Ensures that create_byo_profile returns data when creating
    a byo profile with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/byoprofiles/id/0"), data_type="xml"
        )
    )
    assert classic.create_byo_profile(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_byo_profile_id(classic):
    """
    Ensures that update_byo_profile returns data when updating
    a byo profile with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/byoprofiles/id/1001"), data_type="xml"
        )
    )
    assert classic.update_byo_profile(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_byo_profile_name(classic):
    """
    Ensures that update_byo_profile returns data when updating
    a byo profile with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/byoprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_byo_profile(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_byo_profile_id(classic):
    """
    Ensures that delete_byo_profile returns data when deleting an
    byo profile by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/byoprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_byo_profile(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_byo_profile_name(classic):
    """
    Ensures that delete_byo_profile returns data when deleting an
    byo profile by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/byoprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_byo_profile(name="testname") == EXPECTED_XML


"""
/categories
"""


@responses.activate
def test_get_categories_json(classic):
    """
    Ensures that get_categories returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/categories")))
    assert classic.get_categories() == EXPECTED_JSON


@responses.activate
def test_get_categories_xml(classic):
    """
    Ensures that get_categories returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/categories"), data_type="xml")
    )
    assert classic.get_categories(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_category_id_json(classic):
    """
    Ensures that get_category returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/categories/id/1001")))
    assert classic.get_category(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_category_name_xml(classic):
    """
    Ensures that get_category returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/categories/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_category(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_category_id(classic):
    """
    Ensures that create_category returns data when creating
    a category with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/categories/id/0"), data_type="xml"
        )
    )
    assert classic.create_category(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_category_id(classic):
    """
    Ensures that update_category returns data when updating
    a category with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/categories/id/1001"), data_type="xml"
        )
    )
    assert classic.update_category(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_category_name(classic):
    """
    Ensures that update_category returns data when updating
    a category with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/categories/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_category(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_category_id(classic):
    """
    Ensures that delete_category returns data when deleting an
    category by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/categories/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_category(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_category_name(classic):
    """
    Ensures that delete_category returns data when deleting an
    category by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/categories/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_category(name="testname") == EXPECTED_XML


"""
/classes
"""


@responses.activate
def test_get_classes_json(classic):
    """
    Ensures that get_classes returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/classes")))
    assert classic.get_classes() == EXPECTED_JSON


@responses.activate
def test_get_classes_xml(classic):
    """
    Ensures that get_classes returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/classes"), data_type="xml")
    )
    assert classic.get_classes(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_class_id_json(classic):
    """
    Ensures that get_class returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/classes/id/1001")))
    assert classic.get_class(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_class_name_xml(classic):
    """
    Ensures that get_class returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/classes/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_class(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_class_id(classic):
    """
    Ensures that create_class returns data when creating
    a class with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/classes/id/0"), data_type="xml")
    )
    assert classic.create_class(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_class_id(classic):
    """
    Ensures that update_class returns data when updating
    a class with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/classes/id/1001"), data_type="xml"
        )
    )
    assert classic.update_class(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_class_name(classic):
    """
    Ensures that update_class returns data when updating
    a class with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/classes/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_class(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_class_id(classic):
    """
    Ensures that delete_class returns data when deleting an
    class by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/classes/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_class(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_class_name(classic):
    """
    Ensures that delete_class returns data when deleting an
    class by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/classes/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_class(name="testname") == EXPECTED_XML


"""
/commandflush
"""


@responses.activate
def test_create_command_flush_params(classic):
    """
    Ensures that command flush completes successfully when used with parameters
    and not data.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/commandflush/computers/id/1001/status/Pending"),
            data_type="xml",
        )
    )
    assert classic.create_command_flush("computers", 1001, "Pending") == EXPECTED_XML


@responses.activate
def test_create_command_flush_data(classic):
    """
    Ensures that command flush completes successfully when used with data and
    not parameters.
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/commandflush"), data_type="xml"
        )
    )
    assert classic.create_command_flush(data=EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_create_command_flush_no_parameters_or_data(classic):
    """
    Ensures that command_flush raises NoParametersOrData when neither
    parameter or data options are passed.
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/commandflush"), data_type="xml"
        )
    )
    with pytest.raises(NoParametersOrData):
        classic.create_command_flush()


@responses.activate
def test_create_command_flush_parameters_and_data(classic):
    """
    Ensures that command_flush raises ParametersAndData when both parameter
    and data options are passed.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/commandflush/computers/id/1001/status/Pending"),
            data_type="xml",
        )
    )
    with pytest.raises(ParametersAndData):
        classic.create_command_flush("computers", 1001, "Pending", EXPECTED_XML)


@responses.activate
def test_create_command_flush_missing_parameters(classic):
    """
    Ensures that command_flush raises MissingParameters when parameters are
    used but not all necessary ones are supplied.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/commandflush/computers/id/1001/status/Pending"),
            data_type="xml",
        )
    )
    with pytest.raises(MissingParameters):
        classic.create_command_flush(idtype="computers", status="Pending")


@responses.activate
def test_create_command_flush_invalid_parameter_options(classic):
    """
    Ensures that command_flush raises InvalidParameterOptions when using an
    invalid option for a parameter value.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/commandflush/computers/id/1001/status/Pending"),
            data_type="xml",
        )
    )
    with pytest.raises(InvalidParameterOptions):
        classic.create_command_flush("commuters", 1001, "Pending")


"""
/computerapplications
"""


@responses.activate
def test_get_computer_application_json(classic):
    """
    Ensures get_computer_application returns data when given only the
    application parameter.
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computerapplications/application/Safari.app")
        )
    )
    assert classic.get_computer_application("Safari.app") == EXPECTED_JSON


@responses.activate
def test_get_computer_application_version_xml(classic):
    """
    Ensures that get_computer_application returns data when given the
    application and version parameters along with xml as the data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerapplications/application/Safari.app"
                "/version/15.4"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.get_computer_application("Safari.app", 15.4, data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_computer_application_inventory(classic):
    """
    Ensures that get_computer_application returns data when given the
    application and inventory parameters
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerapplications/application/Safari.app"
                "/inventory/Platform"
            ),
        )
    )
    assert (
        classic.get_computer_application("Safari.app", inventory="Platform")
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_application_version_and_inventory(classic):
    """
    Ensures that get_computer_application returns data when given the
    application, version, and inventory parameters
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerapplications/application/Safari.app"
                "/version/15.4/inventory/Platform"
            ),
        )
    )
    assert (
        classic.get_computer_application("Safari.app", 15.4, "Platform")
        == EXPECTED_JSON
    )


"""
/computerapplicationusage
"""


@responses.activate
def test_get_computer_application_usage_id(classic):
    """
    Ensures that get_computer_application_usage returns json data when used
    with the right date format and ID
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerapplicationusage/id/1001/2022-01-01_2022-01-02"
            ),
        )
    )
    assert (
        classic.get_computer_application_usage("2022-01-01", "2022-01-02", id=1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_application_usage(classic):
    """
    Ensures that get_computer_application_usage returns XML data when used with
    the right date format and UDID with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerapplicationusage/udid/1001/2022-01-01_2022-01-02"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.get_computer_application_usage(
            "2022-01-01", "2022-01-02", udid=1001, data_type="xml"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_get_computer_application_usage_invalid_date_format(classic):
    """
    Ensures that valid_date raises ValueError when
    get_computer_application_usage is given an incorrect date format
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerapplicationusage/id/1001/2022-01-01_2022-01-02"
            ),
        )
    )
    with pytest.raises(ValueError):
        classic.get_computer_application_usage("1-1-2022", "1-2-2022", id=1001)


"""
/computercheckin
"""


@responses.activate
def test_get_computer_check_in_json(classic):
    """
    Ensures that get_computer_check_in returns a JSON dict when used without
    any specific parameters
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/computercheckin")))
    assert classic.get_computer_check_in() == EXPECTED_JSON


@responses.activate
def test_get_computer_check_in_xml(classic):
    """
    Ensures that get_computer_check_in returns an XML str when used with
    data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computercheckin"), data_type="xml"
        )
    )
    assert classic.get_computer_check_in(data_type="xml") == EXPECTED_XML


@responses.activate
def test_update_computer_check_in(classic):
    """
    Ensures that update_computer_check_in returns data when updating computer
    check in information
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/computercheckin"), data_type="xml"
        )
    )
    assert classic.update_computer_check_in(EXPECTED_XML) == EXPECTED_XML


"""
/computercommands
"""


@responses.activate
def test_get_computer_commands_json(classic):
    """
    Ensures that get_computer_commands returns JSON data when used without
    any optional parameters
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/computercommands")))
    assert classic.get_computer_commands() == EXPECTED_JSON


@responses.activate
def test_get_computer_commands_name_xml(classic):
    """
    Ensures that get_computer_commands returns XML when using name filtering
    and "xml" is set as data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computercommands/name/CommandName"),
            data_type="xml",
        )
    )
    assert classic.get_computer_commands("CommandName", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_command(classic):
    """
    Ensures that get_computer_command returns JSON data when used without extra
    optional parameters
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computercommands/uuid/123a"))
    )
    assert classic.get_computer_command("123a") == EXPECTED_JSON


@responses.activate
def test_get_computer_command_status(classic):
    """
    Ensures that get_computer_command_status returns JSON data when used
    without extra optional parameters
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computercommands/status/123a"))
    )
    assert classic.get_computer_command_status("123a") == EXPECTED_JSON


@responses.activate
def test_create_computer_command_scheduleosupdate_data(classic):
    """
    Ensures that create_computer_command completes successfully when used with
    the ScheduleOSUpdate command.
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/computercommands/command/ScheduleOSUpdate"),
            data_type="xml",
        )
    )
    assert (
        classic.create_computer_command("ScheduleOSUpdate", data=EXPECTED_XML)
        == EXPECTED_XML
    )


@responses.activate
def test_create_computer_command_enableremotedesktop_ids(classic):
    """
    Ensures that create_computer_command completes successfully when used with
    the EnableRemoteDesktop command and ids
    """
    responses.add(
        response_builder(
            "POST",
            jps_url(
                "/JSSResource/computercommands/command/EnableRemoteDesktop/id/1001"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.create_computer_command("EnableRemoteDesktop", ["1001"]) == EXPECTED_XML
    )


@responses.activate
def test_create_computer_command_scheduleosupdate_action_multiple_ids(classic):
    """
    Ensures that create_computer_command completes successfully when used with
    the ScheduleOSUpdate command and action install
    """
    responses.add(
        response_builder(
            "POST",
            jps_url(
                "/JSSResource/computercommands/command/ScheduleOSUpdate/action/install"
                "/id/1001%2C1002"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.create_computer_command(
            "ScheduleOSUpdate", ids=["1001", "1002"], action="install"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_create_computer_command_invalid_command(classic):
    """
    Ensures that create_computer_command raises InvalidParameterOptions when
    given an invalid command
    """
    with pytest.raises(InvalidParameterOptions):
        classic.create_computer_command("InventoryUpdate", [1001])


@responses.activate
def test_create_computer_command_scheduleosupdate_invalid_action(classic):
    """
    Ensures that create_computer_command raises InvalidParameterOptions when
    given an incorrect value for the action param
    """
    with pytest.raises(InvalidParameterOptions):
        classic.create_computer_command("ScheduleOSUpdate", ["1001"], "wrong")


@responses.activate
def test_create_computer_command_action_and_passcode(classic):
    """
    Ensures that create_computer_command raises ConflictingParameters when both
    action and passcode are given values
    """
    with pytest.raises(ConflictingParameters):
        classic.create_computer_command("EraseDevice", ["1001"], "install", "123456")


@responses.activate
def test_create_computer_command_erasedevice_ids(classic):
    """
    Ensures that create_computer_command completes successfully when used with
    the EraseDevice command and passcode 123456
    """
    responses.add(
        response_builder(
            "POST",
            jps_url(
                "/JSSResource/computercommands/command/EraseDevice/passcode/123456"
                "/id/1001"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.create_computer_command("EraseDevice", passcode="123456", ids=[1001])
        == EXPECTED_XML
    )


@responses.activate
def test_create_computer_command_erasedevice_no_passcode(classic):
    """
    Ensures that create_computer_command raises ValueError when the EraseDevice
    command is used without a passcode set
    """
    with pytest.raises(ValueError):
        classic.create_computer_command("EraseDevice", [1001])


"""
/computerextensionattributes
"""


@responses.activate
def test_get_computer_extension_attributes_json(classic):
    """
    Ensures that get_computer_extension_attributes returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computerextensionattributes"))
    )
    assert classic.get_computer_extension_attributes() == EXPECTED_JSON


@responses.activate
def test_get_computer_extension_attributes_xml(classic):
    """
    Ensures that get_computer_extension_attributes returns a XML str when
    passing "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computerextensionattributes"), data_type="xml"
        )
    )
    assert classic.get_computer_extension_attributes(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_extension_attribute_id_json(classic):
    """
    Ensures that get_computer_extension_attribute returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computerextensionattributes/id/1001")
        )
    )
    assert classic.get_computer_extension_attribute(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_extension_attribute_name_xml(classic):
    """
    Ensures that get_computer_extension_attribute returns XML when passing
    "xml" as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computerextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_computer_extension_attribute(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_computer_extension_attribute_id(classic):
    """
    Ensures that create_computer_extension_attribute returns data when creating
    a computer extension attribute with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/computerextensionattributes/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_computer_extension_attribute(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_computer_extension_attribute_id(classic):
    """
    Ensures that update_computer_extension_attribute returns data when updating
    a computer extension attribute with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/computerextensionattributes/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_computer_extension_attribute(EXPECTED_XML, id=1001)
        == EXPECTED_XML
    )


@responses.activate
def test_update_computer_extension_attribute_name(classic):
    """
    Ensures that update_computer_extension_attribute returns data when updating
    a computer extension attribute with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/computerextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_computer_extension_attribute(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_computer_extension_attribute_id(classic):
    """
    Ensures that delete_computer_extension_attribute returns data when deleting
    a computer extension attribute by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/computerextensionattributes/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_computer_extension_attribute(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_computer_extension_attribute_name(classic):
    """
    Ensures that delete_computer_extension_attribute returns data when deleting
    a computer extension attribute by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/computerextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_computer_extension_attribute(name="testname") == EXPECTED_XML


"""
/computergroups
"""


@responses.activate
def test_get_computer_groups_json(classic):
    """
    Ensures that get_computer_groups returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/computergroups")))
    assert classic.get_computer_groups() == EXPECTED_JSON


@responses.activate
def test_get_computer_groups_xml(classic):
    """
    Ensures that get_computer_groups returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computergroups"), data_type="xml")
    )
    assert classic.get_computer_groups(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_group_id_json(classic):
    """
    Ensures that get_computer_group returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computergroups/id/1001"))
    )
    assert classic.get_computer_group(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_group_name_xml(classic):
    """
    Ensures that get_computer_group returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computergroups/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_computer_group(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_computer_group_id(classic):
    """
    Ensures that create_computer_group returns data when creating
    a computer group with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/computergroups/id/0"), data_type="xml"
        )
    )
    assert classic.create_computer_group(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_computer_group_id(classic):
    """
    Ensures that update_computer_group returns data when updating
    a computer group with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/computergroups/id/1001"), data_type="xml"
        )
    )
    assert classic.update_computer_group(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_computer_group_name(classic):
    """
    Ensures that update_computer_group returns data when updating
    a computer group with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/computergroups/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_computer_group(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_computer_group_id(classic):
    """
    Ensures that delete_computer_group returns data when deleting a
    computer group by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/computergroups/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_computer_group(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_computer_group_name(classic):
    """
    Ensures that delete_computer_group returns data when deleting a
    computer group by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/computergroups/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_computer_group(name="testname") == EXPECTED_XML


"""
/computerhardwaresoftwarereports
"""


@responses.activate
def test_get_computer_hardware_software_reports_id(classic):
    """
    Ensures that get_computer_hardware_software_reports returns json data when
    used with the right date format and ID
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerhardwaresoftwarereports/id/1001"
                "/2022-01-01_2022-01-02"
            ),
        )
    )
    assert (
        classic.get_computer_hardware_software_reports(
            "2022-01-01", "2022-01-02", id=1001
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_hardware_software_reports_udid_xml(classic):
    """
    Ensures that get_computer_hardware_software_reports returns XML data when
    used with the right date format and UDID with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerhardwaresoftwarereports/udid/1001"
                "/2022-01-01_2022-01-02"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.get_computer_hardware_software_reports(
            "2022-01-01", "2022-01-02", udid=1001, data_type="xml"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_get_computer_hardware_software_reports_invalid_date_format(classic):
    """
    Ensures that valid_date raises ValueError when
    get_computer_hardware_software_reports is given an incorrect date format
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerhardwaresoftwarereports/id/1001"
                "/2022-01-01_2022-01-02"
            ),
        )
    )
    with pytest.raises(ValueError):
        classic.get_computer_hardware_software_reports("1-1-2022", "1-2-2022", id=1001)


@responses.activate
def test_get_computer_hardware_software_reports_macaddress_subset(classic):
    """
    Ensures that get_computer_hardware_software_reports returns data when used
    with macaddress identifier and one subset
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerhardwaresoftwarereports/macaddress/"
                "12%3A34%3A56%3A78%3A90%3A12/2022-01-01_2022-01-02/subset/Hardware"
            ),
        )
    )
    assert (
        classic.get_computer_hardware_software_reports(
            "2022-01-01",
            "2022-01-02",
            macaddress="12:34:56:78:90:12",
            subsets=["Hardware"],
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_hardware_software_reports_serialnumber_subsets(classic):
    """
    Ensures that get_computer_hardware_software_reports returns data when used
    with serialnumber identifier and multiple subsets
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerhardwaresoftwarereports/serialnumber/1a2b3c4d5e"
                "/2022-01-01_2022-01-02/subset/Hardware%26Software"
            ),
        )
    )
    assert (
        classic.get_computer_hardware_software_reports(
            "2022-01-01",
            "2022-01-02",
            serialnumber="1a2b3c4d5e",
            subsets=["Hardware", "Software"],
        )
        == EXPECTED_JSON
    )


"""
/computerhistory
"""


@responses.activate
def test_get_computer_history_id(classic):
    """
    Ensures that get_computer_history returns json data when
    used with and ID
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computerhistory/id/1001"),
        )
    )
    assert classic.get_computer_history(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_history_udid_xml(classic):
    """
    Ensures that get_computer_history returns XML data when
    used with UDID with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computerhistory/udid/1001"),
            data_type="xml",
        )
    )
    assert classic.get_computer_history(udid=1001, data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_history_macaddress_subset(classic):
    """
    Ensures that get_computer_history returns data when used
    with macaddress identifier and one subset
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerhistory/macaddress/"
                "12%3A34%3A56%3A78%3A90%3A12/subset/General"
            ),
        )
    )
    assert (
        classic.get_computer_history(
            macaddress="12:34:56:78:90:12",
            subsets=["General"],
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_history_serialnumber_subsets(classic):
    """
    Ensures that get_computer_history returns data when used
    with serialnumber identifier and multiple subsets
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computerhistory/serialnumber/1a2b3c4d5e"
                "/subset/General%26ScreenSharingLogs"
            ),
        )
    )
    assert (
        classic.get_computer_history(
            serialnumber="1a2b3c4d5e",
            subsets=["General", "ScreenSharingLogs"],
        )
        == EXPECTED_JSON
    )


"""
/computerinventorycollection
"""


@responses.activate
def test_get_computer_inventory_collection_json(classic):
    """
    Ensures that get_computer_inventory_collection returns data when used
    without optional parameters.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computerinventorycollection"))
    )
    assert classic.get_computer_inventory_collection() == EXPECTED_JSON


@responses.activate
def test_get_computer_inventory_collection_xml(classic):
    """
    Ensures that get_computer_inventory_collection returns data when used
    with data_type set to "xml".
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computerinventorycollection"), data_type="xml"
        )
    )
    assert classic.get_computer_inventory_collection(data_type="xml") == EXPECTED_XML


@responses.activate
def test_update_computer_inventory_collection(classic):
    """
    Ensures that update_computer_inventory_collection runs successfully when
    given XML data
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/computerinventorycollection"), data_type="xml"
        )
    )
    assert classic.update_computer_inventory_collection(EXPECTED_XML) == EXPECTED_XML


"""
/computerinvitations
"""


@responses.activate
def test_get_computer_invitations_json(classic):
    """
    Ensures that get_computer_invitations returns data when used
    without optional parameters.
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/computerinvitations")))
    assert classic.get_computer_invitations() == EXPECTED_JSON


@responses.activate
def test_get_computer_invitations_xml(classic):
    """
    Ensures that get_computer_invitations returns data when used
    with data_type set to "xml".
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computerinvitations"), data_type="xml"
        )
    )
    assert classic.get_computer_invitations(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_invitation_id_json(classic):
    """
    Ensures that get_computer_invitation returns json data when used with
    id as the identifier and no additional params.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computerinvitations/id/1001"))
    )
    assert classic.get_computer_invitation(1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_invitation_invitation_xml(classic):
    """
    Ensures that get_computer)invitation returns xml data when used with
    invitation as the identifier and "xml" set as data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computerinvitations/invitation/123456789"),
            data_type="xml",
        )
    )
    assert (
        classic.get_computer_invitation(invitation=123456789, data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_computer_invitation_id_0(classic):
    """
    Ensures that create_computer_invitation successfully runs when used with ID
    set to 0 to use the next available ID
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/computerinvitations/id/0"), data_type="xml"
        )
    )
    assert classic.create_computer_invitation(EXPECTED_XML, id=0) == EXPECTED_XML


@responses.activate
def test_create_computer_invitation_invitation_0(classic):
    """
    Ensures that create_computer_invitation successfully runs when used with
    the invitation identifier set to 0 to use a random available invitation
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/computerinvitations/invitation/0"),
            data_type="xml",
        )
    )
    assert (
        classic.create_computer_invitation(EXPECTED_XML, invitation=0) == EXPECTED_XML
    )


@responses.activate
def test_delete_computer_invitation_id_json(classic):
    """
    Ensures that delete_computer_invitation completes successfully when used
    with id as the identifier.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/computerinvitations/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_computer_invitation(1001) == EXPECTED_XML


@responses.activate
def test_delete_computer_invitation_invitation_xml(classic):
    """
    Ensures that delete_computer_invitation completes successfully when used
    with invitation as the identifier.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/computerinvitations/invitation/123456789"),
            data_type="xml",
        )
    )
    assert classic.delete_computer_invitation(invitation=123456789) == EXPECTED_XML


"""
/computermanagement
"""


@responses.activate
def test_get_computer_management_id(classic):
    """
    Ensures that get_computer_management returns json data when
    used with the right date format and ID
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computermanagement/id/1001"),
        )
    )
    assert classic.get_computer_management(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_management_udid_xml(classic):
    """
    Ensures that get_computer_management returns XML data when
    used with the right date format and UDID with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computermanagement/udid/1001"),
            data_type="xml",
        )
    )
    assert classic.get_computer_management(udid=1001, data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_management_macaddress_subset(classic):
    """
    Ensures that get_computer_management returns data when used
    with macaddress identifier and one subset
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computermanagement/macaddress/"
                "12%3A34%3A56%3A78%3A90%3A12/subset/General"
            ),
        )
    )
    assert (
        classic.get_computer_management(
            macaddress="12:34:56:78:90:12",
            subsets=["General"],
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_management_serialnumber_subsets(classic):
    """
    Ensures that get_computer_management returns data when used
    with serialnumber identifier and multiple subsets
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computermanagement/serialnumber/1a2b3c4d5e"
                "/subset/General%26Ebooks"
            ),
        )
    )
    assert (
        classic.get_computer_management(
            serialnumber="1a2b3c4d5e",
            subsets=["General", "Ebooks"],
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_management_id_username(classic):
    """
    Ensures that get_computer_management returns data when used with ID and
    a username.
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computermanagement/id/1001/username/testuser")
        )
    )
    assert classic.get_computer_management(1001, username="testuser") == EXPECTED_JSON


@responses.activate
def test_get_computer_management_id_username_subsets(classic):
    """
    Ensures that get_computer_management returns data when used with ID and
    a username.
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/computermanagement/id/1001/username/testuser"
                "/subset/General%26MacAppStoreApps"
            ),
        )
    )
    assert (
        classic.get_computer_management(
            1001, username="testuser", subsets=["General", "MacAppStoreApps"]
        )
        == EXPECTED_JSON
    )


"""
/computerreports
"""


@responses.activate
def test_get_computer_reports_json(classic):
    """
    Ensures that get_computer_reports returns data when used
    without optional parameters.
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/computerreports")))
    assert classic.get_computer_reports() == EXPECTED_JSON


@responses.activate
def test_get_computer_reports_xml(classic):
    """
    Ensures that get_computer_reports returns data when used
    with data_type set to "xml".
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computerreports"), data_type="xml"
        )
    )
    assert classic.get_computer_reports(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_report_id_json(classic):
    """
    Ensures that get_computer_report returns json when used with id and no
    additional optional parameters
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computerreports/id/1001"))
    )
    assert classic.get_computer_report(1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_report_name_xml(classic):
    """
    Ensures that get_computer_report returns xml when used with name and "xml"
    set as data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computerreports/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_computer_report(name="testname", data_type="xml") == EXPECTED_XML


"""
/computers
"""


@responses.activate
def test_get_computers_json(classic):
    """
    Ensures that get_computer returns JSON when used without any optional
    parameters
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/computers")))
    assert classic.get_computers() == EXPECTED_JSON


@responses.activate
def test_get_computers_match_xml(classic):
    """
    Ensures that get_computer returns XML when used match filter and data_type
    set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computers/match/MAC%2A"), data_type="xml"
        )
    )
    assert classic.get_computers(match="MAC*", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_basic(classic):
    """
    Ensures that get_computer returns JSON when used with basic set to True
    and no additional optional params
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/computers/subset/basic"))
    )
    assert classic.get_computers(basic=True) == EXPECTED_JSON


@responses.activate
def test_get_computer_id_json(classic):
    """
    Ensures that get_computer returns content from the API when using id
    as an identifier.
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/computers/id/1001")))
    assert classic.get_computer(id="1001") == EXPECTED_JSON


@responses.activate
def test_get_computer_id_subset_json(classic):
    """
    Ensures that get_computer returns content from the API when using id
    as an identifier.
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/computers/id/1001/subset/General%26Location"),
        )
    )
    assert (
        classic.get_computer(id="1001", subsets=["General", "Location"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_id_subset_invalid_subset(classic):
    """
    Ensures that get_computer raises InvalidSubset when passed an invalid
    subset for the endpoint.
    """
    with pytest.raises(InvalidSubset):
        classic.get_computer(id=1001, subsets=["General", "InvalidSubset"])


@responses.activate
def test_get_computer_no_identification(classic):
    """
    Ensures that get_computer raises NoIdentification when no form of
    identification is passed.
    """
    with pytest.raises(NoIdentification):
        classic.get_computer()


@responses.activate
def test_get_computer_multiple_identification(classic):
    """
    Ensures that get_computer raises MultipleIdentifications when more
    than one form of identification is passed to an endpoint.
    """
    with pytest.raises(MultipleIdentifications):
        classic.get_computer(id=1001, name="name")


@responses.activate
def test_get_computer_id_xml(classic):
    """
    Ensures that get_computer returns content from the API when using id
    as an identifier.
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/computers/id/1001"), data_type="xml"
        )
    )
    assert classic.get_computer(id="1001", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_computer_500(classic):
    """
    Ensures that get_computer correctly raises a HTTPError when the
    request returns a 500 error.
    """
    responses.add(
        method="GET", url=jps_url("/JSSResource/computers/id/1001"), status=500
    )
    with pytest.raises(HTTPError):
        classic.get_computer(id="1001")


@responses.activate
def test_update_computer_id(classic):
    """
    Ensures that update_computer returns content when updating a device
    using id as an identifier.
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/computers/id/1001"), data_type="xml"
        )
    )
    assert classic.update_computer(EXPECTED_XML, id="1001") == EXPECTED_XML


@responses.activate
def test_update_computer_id_400(classic):
    """
    Ensures that update_computer raises ClientError when the request
    returns a 400 status code.
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/computers/id/1001"), status=400)
    )
    with pytest.raises(ClientError):
        classic.update_computer(EXPECTED_XML, id="1001")


@responses.activate
def test_update_computer_id_404(classic):
    """
    Ensures that update_computer raises NotFound when the request
    returns a 404 status code.
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/computers/id/1001"), status=404)
    )
    with pytest.raises(NotFound):
        classic.update_computer(EXPECTED_XML, id="1001")


@responses.activate
def test_update_computer_id_502(classic):
    """
    Ensures that update_computer raises RequestTimedOut when the request
    returns a 502 status code.
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/computers/id/1001"), status=502)
    )
    with pytest.raises(RequestTimedOut):
        classic.update_computer(EXPECTED_XML, id="1001")


@responses.activate
def test_update_computer_id_500(classic):
    """
    Ensures that update_computer raises a HTTPError when the request
    returns an unrecognized HTTP error.
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/computers/id/1001"), status=500)
    )
    with pytest.raises(HTTPError):
        classic.update_computer(EXPECTED_XML, id="1001")


@responses.activate
def test_create_computer_id(classic):
    """
    Ensures that create_computer returns content when creating/updating
    a computer.
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/computers/id/0"), data_type="xml"
        )
    )
    assert classic.create_computer(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_create_computer_id_HTTPError(classic):
    """
    Ensures that update_computer raises a HTTPError when the request
    returns an unrecognized HTTP error.
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/computers/id/0"), status=500)
    )
    with pytest.raises(HTTPError):
        classic.create_computer(EXPECTED_XML)


@responses.activate
def test_delete_computer_id(classic):
    """
    Ensures that delete_computer processes correctly when using id as
    identification
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/computers/id/1001"), data_type="xml"
        )
    )
    assert classic.delete_computer(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_computer_id_500(classic):
    """
    Ensures that delete_computer raises a HTTPError when processing an
    unrecognized HTTP error
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/computers/id/1001"), status=500
        )
    )
    with pytest.raises(HTTPError):
        classic.delete_computer(id=1001)


@responses.activate
def test_delete_computers_extension_attribute_data(classic):
    """
    Ensures that delete_computers_extension_attribute_data successfully runs
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/computers/extensionattributedataflush/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_computers_extension_attribute_data(1001) == EXPECTED_XML


"""
/departments
"""


@responses.activate
def test_get_departments_json(classic):
    """
    Ensures that get_departments returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/departments")))
    assert classic.get_departments() == EXPECTED_JSON


@responses.activate
def test_get_departments_xml(classic):
    """
    Ensures that get_departments returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/departments"), data_type="xml")
    )
    assert classic.get_departments(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_department_id_json(classic):
    """
    Ensures that get_department returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/departments/id/1001")))
    assert classic.get_department(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_department_name_xml(classic):
    """
    Ensures that get_department returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/departments/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_department(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_department_id(classic):
    """
    Ensures that create_department returns data when creating
    a department with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/departments/id/0"), data_type="xml"
        )
    )
    assert classic.create_department(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_department_id(classic):
    """
    Ensures that update_department returns data when updating
    a department with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/departments/id/1001"), data_type="xml"
        )
    )
    assert classic.update_department(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_department_name(classic):
    """
    Ensures that update_department returns data when updating
    a department with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/departments/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_department(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_department_id(classic):
    """
    Ensures that delete_department returns data when deleting a
    department by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/departments/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_department(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_department_name(classic):
    """
    Ensures that delete_department returns data when deleting a
    department by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/departments/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_department(name="testname") == EXPECTED_XML


"""
/directorybindings
"""


@responses.activate
def test_get_directory_bindings_json(classic):
    """
    Ensures that get_directory_bindings returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/directorybindings")))
    assert classic.get_directory_bindings() == EXPECTED_JSON


@responses.activate
def test_get_directory_bindings_xml(classic):
    """
    Ensures that get_directory_bindings returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/directorybindings"), data_type="xml"
        )
    )
    assert classic.get_directory_bindings(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_directory_binding_id_json(classic):
    """
    Ensures that get_directory_binding returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/directorybindings/id/1001"))
    )
    assert classic.get_directory_binding(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_directory_binding_name_xml(classic):
    """
    Ensures that get_directory_binding returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/directorybindings/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_directory_binding(name="testname", data_type="xml") == EXPECTED_XML
    )


@responses.activate
def test_create_directory_binding_id(classic):
    """
    Ensures that create_directory_binding returns data when creating
    a directory binding with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/directorybindings/id/0"), data_type="xml"
        )
    )
    assert classic.create_directory_binding(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_directory_binding_id(classic):
    """
    Ensures that update_directory_binding returns data when updating
    a directory binding with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/directorybindings/id/1001"), data_type="xml"
        )
    )
    assert classic.update_directory_binding(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_directory_binding_name(classic):
    """
    Ensures that update_directory_binding returns data when updating
    a directory binding with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/directorybindings/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_directory_binding(EXPECTED_XML, name="testname") == EXPECTED_XML
    )


@responses.activate
def test_delete_directory_binding_id(classic):
    """
    Ensures that delete_directory_binding returns data when deleting a
    directory binding by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/directorybindings/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_directory_binding(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_directory_binding_name(classic):
    """
    Ensures that delete_directory_binding returns data when deleting a
    directory binding by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/directorybindings/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_directory_binding(name="testname") == EXPECTED_XML


"""
/diskencryptionconfigurations
"""


@responses.activate
def test_get_disk_encryption_configurations_json(classic):
    """
    Ensures that get_disk_encryption_configurations returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/diskencryptionconfigurations"))
    )
    assert classic.get_disk_encryption_configurations() == EXPECTED_JSON


@responses.activate
def test_get_disk_encryption_configurations_xml(classic):
    """
    Ensures that get_disk_encryption_configurations returns a XML str when
    passing "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/diskencryptionconfigurations"), data_type="xml"
        )
    )
    assert classic.get_disk_encryption_configurations(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_disk_encryption_configuration_id_json(classic):
    """
    Ensures that get_disk_encryption_configuration returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/diskencryptionconfigurations/id/1001")
        )
    )
    assert classic.get_disk_encryption_configuration(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_disk_encryption_configuration_name_xml(classic):
    """
    Ensures that get_disk_encryption_configuration returns XML when passing
    "xml" as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/diskencryptionconfigurations/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_disk_encryption_configuration(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_disk_encryption_configuration_id(classic):
    """
    Ensures that create_disk_encryption_configuration returns data when
    updating a disk encryption configuration with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/diskencryptionconfigurations/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_disk_encryption_configuration(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_disk_encryption_configuration_id(classic):
    """
    Ensures that update_disk_encryption_configuration returns data when
    updating a disk encryption configuration with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/diskencryptionconfigurations/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_disk_encryption_configuration(EXPECTED_XML, id=1001)
        == EXPECTED_XML
    )


@responses.activate
def test_update_disk_encryption_configuration_name(classic):
    """
    Ensures that update_disk_encryption_configuration returns data when
    updating a disk encryption configuration with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/diskencryptionconfigurations/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_disk_encryption_configuration(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_disk_encryption_configuration_id(classic):
    """
    Ensures that delete_disk_encryption_configuration returns data when
    deleting a disk encryption configuration by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/diskencryptionconfigurations/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_disk_encryption_configuration(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_disk_encryption_configuration_name(classic):
    """
    Ensures that delete_disk_encryption_configuration returns data when
    deleting a disk encryption configuration by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/diskencryptionconfigurations/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_disk_encryption_configuration(name="testname") == EXPECTED_XML


"""
/distributionpoints
"""


@responses.activate
def test_get_distribution_points_json(classic):
    """
    Ensures that get_distribution_points returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/distributionpoints")))
    assert classic.get_distribution_points() == EXPECTED_JSON


@responses.activate
def test_get_distribution_points_xml(classic):
    """
    Ensures that get_distribution_points returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/distributionpoints"), data_type="xml"
        )
    )
    assert classic.get_distribution_points(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_distribution_point_id_json(classic):
    """
    Ensures that get_distribution_point returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/distributionpoints/id/1001"))
    )
    assert classic.get_distribution_point(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_distribution_point_name_xml(classic):
    """
    Ensures that get_distribution_point returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/distributionpoints/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_distribution_point(name="testname", data_type="xml") == EXPECTED_XML
    )


@responses.activate
def test_create_distribution_point_id(classic):
    """
    Ensures that create_distribution_point returns data when creating
    a distribution point with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/distributionpoints/id/0"), data_type="xml"
        )
    )
    assert classic.create_distribution_point(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_distribution_point_id(classic):
    """
    Ensures that update_distribution_point returns data when updating
    a distribution point with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/distributionpoints/id/1001"), data_type="xml"
        )
    )
    assert classic.update_distribution_point(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_distribution_point_name(classic):
    """
    Ensures that update_distribution_point returns data when updating
    a distribution point with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/distributionpoints/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_distribution_point(EXPECTED_XML, name="testname") == EXPECTED_XML
    )


@responses.activate
def test_delete_distribution_point_id(classic):
    """
    Ensures that delete_distribution_point returns data when deleting a
    distribution point by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/distributionpoints/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_distribution_point(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_distribution_point_name(classic):
    """
    Ensures that delete_distribution_point returns data when deleting a
    distribution point by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/distributionpoints/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_distribution_point(name="testname") == EXPECTED_XML


"""
/dockitems
"""


@responses.activate
def test_get_dock_items_json(classic):
    """
    Ensures that get_dock_items returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/dockitems")))
    assert classic.get_dock_items() == EXPECTED_JSON


@responses.activate
def test_get_dock_items_xml(classic):
    """
    Ensures that get_dock_items returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/dockitems"), data_type="xml")
    )
    assert classic.get_dock_items(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_dock_item_id_json(classic):
    """
    Ensures that get_dock_item returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/dockitems/id/1001")))
    assert classic.get_dock_item(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_dock_item_name_xml(classic):
    """
    Ensures that get_dock_item returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/dockitems/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_dock_item(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_dock_item_id(classic):
    """
    Ensures that create_dock_item returns data when creating
    a dock item with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/dockitems/id/0"), data_type="xml"
        )
    )
    assert classic.create_dock_item(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_dock_item_id(classic):
    """
    Ensures that update_dock_item returns data when updating
    a dock item with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/dockitems/id/1001"), data_type="xml"
        )
    )
    assert classic.update_dock_item(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_dock_item_name(classic):
    """
    Ensures that update_dock_item returns data when updating
    a dock item with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/dockitems/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_dock_item(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_dock_item_id(classic):
    """
    Ensures that delete_dock_item returns data when deleting a
    dock item by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/dockitems/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_dock_item(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_dock_item_name(classic):
    """
    Ensures that delete_dock_item returns data when deleting a
    dock item by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/dockitems/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_dock_item(name="testname") == EXPECTED_XML


"""
/ebooks
"""


@responses.activate
def test_get_ebooks_json(classic):
    """
    Ensures that get_ebooks returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/ebooks")))
    assert classic.get_ebooks() == EXPECTED_JSON


@responses.activate
def test_get_ebooks_xml(classic):
    """
    Ensures that get_ebooks returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/ebooks"), data_type="xml")
    )
    assert classic.get_ebooks(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_ebook_id_json(classic):
    """
    Ensures that get_ebook returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/ebooks/id/1001")))
    assert classic.get_ebook(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_ebook_name_xml(classic):
    """
    Ensures that get_ebook returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/ebooks/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_ebook(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_ebook_id_subset(classic):
    """
    Ensures that get_ebook returns data when used with id as an identifier
    and one subset options
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/ebooks/id/1001/subset/General"))
    )
    assert classic.get_ebook(1001, subsets=["General"]) == EXPECTED_JSON


@responses.activate
def test_get_ebook_id_subsets(classic):
    """
    Ensures that get_ebook returns data when used with id as an identifier
    and multiple subset options
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/ebooks/id/1001/subset/General%26SelfService")
        )
    )
    assert classic.get_ebook(1001, subsets=["General", "SelfService"]) == EXPECTED_JSON


@responses.activate
def test_create_ebook_id(classic):
    """
    Ensures that create_ebook returns data when creating
    a ebook with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/ebooks/id/0"), data_type="xml")
    )
    assert classic.create_ebook(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_ebook_id(classic):
    """
    Ensures that update_ebook returns data when updating
    a ebook with id
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/ebooks/id/1001"), data_type="xml")
    )
    assert classic.update_ebook(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_ebook_name(classic):
    """
    Ensures that update_ebook returns data when updating
    a ebook with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/ebooks/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_ebook(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_ebook_id(classic):
    """
    Ensures that delete_ebook returns data when deleting a
    ebook by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/ebooks/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_ebook(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_ebook_name(classic):
    """
    Ensures that delete_ebook returns data when deleting a
    ebook by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/ebooks/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_ebook(name="testname") == EXPECTED_XML


"""
/fileuploads
"""


@responses.activate
def test_create_file_upload_computers_txt(classic):
    """
    Ensures that create_file_upload runs successfully when uploading a txt file
    as a computer attachment
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add("POST", jps_url("/JSSResource/fileuploads/computers/id/1001"))
        assert (
            classic.create_file_upload("computers", filepath="/file.txt", id=1001)
            == "File uploaded successfully."
        )


def test_create_file_upload_file_not_found(classic):
    """
    Ensures that create_file_upload raises FileNotFoundError when trying to
    open a file that does not exist or you don't have permissions for.
    """
    with pytest.raises(FileNotFoundError):
        classic.create_file_upload(
            "computers", filepath="/This/does/not/exist", id=1001
        )


@responses.activate
def test_create_file_upload_mobiledeviceapplicationsipa_force_ipa_wrong_file_type(
    classic,
):
    """
    Ensures that create_file_upload param force_ipa_upload enforces ipa file
    type when used with the mobiledeviceapplicationsipa resource
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            "POST",
            jps_url(
                "/JSSResource/fileuploads/mobiledeviceapplicationsipa/id"
                "/1001?FORCE_IPA_UPLOAD=true"
            ),
            status=409,
        )
        with pytest.raises(RequestConflict):
            classic.create_file_upload(
                "mobiledeviceapplicationsipa",
                filepath="/test.txt",
                id=1001,
                force_ipa_upload=True,
            )


def test_create_file_upload_peripherals_name(classic):
    """
    Ensures that create_file_upload raises ValueError when trying to use the
    name identifier and peripherals resource
    """
    with pytest.raises(ValueError):
        classic.create_file_upload("peripherals", filepath="/test.txt", name="testname")


@responses.activate
def test_create_file_upload_name_mobiledeviceapplicationsipa_force_ipa_upload(classic):
    """
    Ensures that create_force_ipa_upload enforces ipa file type when used with
    the mobiledeviceapplicationsipa resource
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            "POST",
            jps_url(
                "/JSSResource/fileuploads/mobiledeviceapplicationsipa/name"
                "/%3Ftest%3Fname?FORCE_IPA_UPLOAD=true"
            ),
        )
        assert (
            classic.create_file_upload(
                "mobiledeviceapplicationsipa",
                filepath="/test.ipa",
                name="?test?name",
                force_ipa_upload=True,
            )
            == "File uploaded successfully."
        )


def test_create_file_upload_computers_force_ipa_upload(classic):
    """
    Ensures that create_file_upload raises ValueError when using
    force_ipa_upload and a resource that is not mobiledeviceapplicationsipa
    """
    with pytest.raises(ValueError):
        classic.create_file_upload(
            "computers", filepath="/test.txt", id=1001, force_ipa_upload=True
        )


def test_create_file_upload_unrecognized_mime_type(classic):
    """
    Ensures that create_file_upload raises ValueError when guess_type is not
    able to get the MIME type of the file.
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        with pytest.raises(ValueError):
            classic.create_file_upload("computers", filepath="/file", id=1001)


def test_create_file_upload_ebooks_invalid_file_type(classic):
    """
    Ensures that create_file_upload raises ValueError when the ebooks resource
    and a non image file or unrecognized image file is used.
    """
    with pytest.raises(ValueError):
        classic.create_file_upload("ebooks", "/file.text", id=1001)


def test_create_file_upload_diskencryptionconfigurations_invalid_file_type(classic):
    """
    Ensures that create_file_upload raises ValueError when the
    diskencryptionconfigurations resource is used with an unrecognized file
    type
    """
    with pytest.raises(ValueError):
        classic.create_file_upload("diskencryptionconfigurations", "/file.txt", id=1001)


@responses.activate
def test_create_file_upload_diskencryptionconfigurations_pem(classic):
    """
    Ensures that create_file_upload completes successfully when used with the
    diskencryptionconfigurations resource and filepath as a pem file
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            response_builder(
                "POST",
                jps_url(
                    "/JSSResource/fileuploads/diskencryptionconfigurations/id/1001"
                ),
            )
        )
        assert (
            classic.create_file_upload(
                "diskencryptionconfigurations", "file.pem", id=1001
            )
            == "File uploaded successfully."
        )


"""
/gsxconnection
"""


@responses.activate
def test_get_gsx_connection_json(classic):
    """
    Ensures that get_gsx_connection completes successfully when used with
    data_type set to json
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/gsxconnection")))
    assert classic.get_gsx_connection() == EXPECTED_JSON


@responses.activate
def test_get_gsx_connection_xml(classic):
    """
    Ensures that get_gsx_connection completes successfully when used with
    data_type set to xml
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/gsxconnection"), data_type="xml")
    )
    assert classic.get_gsx_connection("xml") == EXPECTED_XML


@responses.activate
def test_update_gsx_connection(classic):
    """
    Ensures that update_gsx_connection completes successfully
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/gsxconnection"), data_type="xml")
    )
    assert classic.update_gsx_connection(EXPECTED_XML) == EXPECTED_XML


"""
/healthcarelistener
"""


@responses.activate
def test_get_healthcare_listeners_json(classic):
    """
    Ensures that get_healthcare_listeners completes successfully when used with
    data_type set to json
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/healthcarelistener")))
    assert classic.get_healthcare_listeners() == EXPECTED_JSON


@responses.activate
def test_get_healthcare_listeners_xml(classic):
    """
    Ensures that get_healthcare_listeners completes successfully when used with
    data_type set to xml
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/healthcarelistener"), data_type="xml"
        )
    )
    assert classic.get_healthcare_listeners("xml") == EXPECTED_XML


@responses.activate
def test_get_healthcare_listener_json(classic):
    """
    Ensures that get_healthcare_listener completes successfully when used with
    required params and data_type set to json
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/healthcarelistener/id/1001"))
    )
    assert classic.get_healthcare_listener(1001) == EXPECTED_JSON


@responses.activate
def test_get_healthcare_listener_xml(classic):
    """
    Ensures that get_healthcare_listener completes successfully when used with
    required params and data_type set to xml
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/healthcarelistener/id/1001"), data_type="xml"
        )
    )
    assert classic.get_healthcare_listener(1001, "xml") == EXPECTED_XML


@responses.activate
def test_update_healthcare_listener(classic):
    """
    Ensures that update_healthcare_listener completes successfully when used
    with required params
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/healthcarelistener/id/1001"), data_type="xml"
        )
    )
    assert classic.update_healthcare_listener(EXPECTED_XML, 1001) == EXPECTED_XML


"""
/healthcarelistenerrule
"""


@responses.activate
def test_get_healthcare_listener_rules_json(classic):
    """
    Ensures that get_healthcare_listener_rules completes successfully when
    used with data_type set to json
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/healthcarelistenerrule"))
    )
    assert classic.get_healthcare_listener_rules() == EXPECTED_JSON


@responses.activate
def test_get_healthcare_listener_rules_xml(classic):
    """
    Ensures that get_healthcare_listener_rule_rules completes successfully
    when used with data_type set to xml
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/healthcarelistenerrule"), data_type="xml"
        )
    )
    assert classic.get_healthcare_listener_rules("xml") == EXPECTED_XML


@responses.activate
def test_get_healthcare_listener_rule_json(classic):
    """
    Ensures that get_healthcare_listener_rule completes successfully when used
    with required params and data_type set to json
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/healthcarelistenerrule/id/1001"))
    )
    assert classic.get_healthcare_listener_rule(1001) == EXPECTED_JSON


@responses.activate
def test_get_healthcare_listener_rule_xml(classic):
    """
    Ensures that get_healthcare_listener_rule completes successfully when used
    with required params and data_type set to xml
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/healthcarelistenerrule/id/1001"),
            data_type="xml",
        )
    )
    assert classic.get_healthcare_listener_rule(1001, "xml") == EXPECTED_XML


@responses.activate
def test_create_healthcare_listener_rule(classic):
    """
    Ensures that create_healthcare_listener_rule completes successfully when
    used with required params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/healthcarelistenerrule/id/0"), data_type="xml"
        )
    )
    assert classic.create_healthcare_listener_rule(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_healthcare_listener_rule(classic):
    """
    Ensures that update_healthcare_listener_rule completes successfully when
    used with required params
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/healthcarelistenerrule/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_healthcare_listener_rule(EXPECTED_XML, 1001) == EXPECTED_XML


"""
/ibeacons
"""


@responses.activate
def test_get_ibeacon_regions_json(classic):
    """
    Ensures that get_ibeacon_regions returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/ibeacons")))
    assert classic.get_ibeacon_regions() == EXPECTED_JSON


@responses.activate
def test_get_ibeacon_regions_xml(classic):
    """
    Ensures that get_ibeacon_regions returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/ibeacons"), data_type="xml")
    )
    assert classic.get_ibeacon_regions(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_ibeacon_region_id_json(classic):
    """
    Ensures that get_ibeacon_region returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/ibeacons/id/1001")))
    assert classic.get_ibeacon_region(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_ibeacon_region_name_xml(classic):
    """
    Ensures that get_ibeacon_region returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/ibeacons/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_ibeacon_region(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_ibeacon_region_id(classic):
    """
    Ensures that create_ibeacon_region returns data when creating
    a iBeacon region with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/ibeacons/id/0"), data_type="xml")
    )
    assert classic.create_ibeacon_region(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_ibeacon_region_id(classic):
    """
    Ensures that update_ibeacon_region returns data when updating
    a iBeacon region with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/ibeacons/id/1001"), data_type="xml"
        )
    )
    assert classic.update_ibeacon_region(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_ibeacon_region_name(classic):
    """
    Ensures that update_ibeacon_region returns data when updating
    a iBeacon region with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/ibeacons/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_ibeacon_region(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_ibeacon_region_id(classic):
    """
    Ensures that delete_ibeacon_region returns data when deleting a
    iBeacon region by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/ibeacons/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_ibeacon_region(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_ibeacon_region_name(classic):
    """
    Ensures that delete_ibeacon_region returns data when deleting a
    iBeacon region by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/ibeacons/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_ibeacon_region(name="testname") == EXPECTED_XML


"""
/infrastructuremanager
"""


@responses.activate
def test_get_infrastructure_managers_json(classic):
    """
    Ensures that get_infrastructure_managers completes successfully when used
    with data_type set to json
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/infrastructuremanager"))
    )
    assert classic.get_infrastructure_managers() == EXPECTED_JSON


@responses.activate
def test_get_infrastructure_managers_xml(classic):
    """
    Ensures that get_infrastructure_managers completes successfully when used
    with data_type set to xml
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/infrastructuremanager"), data_type="xml"
        )
    )
    assert classic.get_infrastructure_managers("xml") == EXPECTED_XML


@responses.activate
def test_get_infrastructure_manager_json(classic):
    """
    Ensures that get_infrastructure_manager completes successfully when used
    with required params and data_type set to json
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/infrastructuremanager/id/1001"))
    )
    assert classic.get_infrastructure_manager(1001) == EXPECTED_JSON


@responses.activate
def test_get_infrastructure_manager_xml(classic):
    """
    Ensures that get_infrastructure_manager completes successfully when used
    with required params and data_type set to xml
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/infrastructuremanager/id/1001"),
            data_type="xml",
        )
    )
    assert classic.get_infrastructure_manager(1001, "xml") == EXPECTED_XML


@responses.activate
def test_update_infrastructure_manager(classic):
    """
    Ensures that update_infrastructure_manager completes successfully when used
    with required params
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/infrastructuremanager/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_infrastructure_manager(EXPECTED_XML, 1001) == EXPECTED_XML


"""
/jssuser
"""

# This endpoint no longer works

"""
/jsonwebtokenconfigurations
"""


@responses.activate
def test_get_json_web_token_configurations_json(classic):
    """
    Ensures that get_json_web_token_configurations completes successfully when
    used with data_type set to json
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/jsonwebtokenconfigurations"))
    )
    assert classic.get_json_web_token_configurations() == EXPECTED_JSON


@responses.activate
def test_get_json_web_token_configurations_xml(classic):
    """
    Ensures that get_json_web_token_configuration completes successfully
    when used with data_type set to xml
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/jsonwebtokenconfigurations"), data_type="xml"
        )
    )
    assert classic.get_json_web_token_configurations("xml") == EXPECTED_XML


@responses.activate
def test_get_json_web_token_configuration_json(classic):
    """
    Ensures that get_json_web_token_configuration completes successfully when
    used with required params and data_type set to json
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/jsonwebtokenconfigurations/id/1001")
        )
    )
    assert classic.get_json_web_token_configuration(1001) == EXPECTED_JSON


@responses.activate
def test_get_json_web_token_configuration_xml(classic):
    """
    Ensures that get_json_web_token_configuration completes successfully when
    used with required params and data_type set to xml
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/jsonwebtokenconfigurations/id/1001"),
            data_type="xml",
        )
    )
    assert classic.get_json_web_token_configuration(1001, "xml") == EXPECTED_XML


@responses.activate
def test_create_json_web_token_configuration(classic):
    """
    Ensures that create_json_web_token_configuration completes successfully
    when used with required params
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/jsonwebtokenconfigurations/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_json_web_token_configuration(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_json_web_token_configuration(classic):
    """
    Ensures that update_json_web_token_configuration completes successfully
    when used with required params
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/jsonwebtokenconfigurations/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_json_web_token_configuration(EXPECTED_XML, 1001) == EXPECTED_XML
    )


@responses.activate
def test_delete_json_web_token_configuration(classic):
    """
    Ensures that delete_json_web_token_configuration completes successfully
    when used with required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/jsonwebtokenconfigurations/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_json_web_token_configuration(1001) == EXPECTED_XML


"""
/ldapservers
"""


@responses.activate
def test_get_ldap_servers(classic):
    """
    Ensures that get_ldap_servers returns JSON data when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/ldapservers")))
    assert classic.get_ldap_servers() == EXPECTED_JSON


@responses.activate
def test_get_ldap_servers_xml(classic):
    """
    Ensures that get_ldap_servers returns XML data when used data_type is set
    to "xml"
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/ldapservers"), data_type="xml")
    )
    assert classic.get_ldap_servers("xml") == EXPECTED_XML


@responses.activate
def test_get_ldap_server_id_json(classic):
    """
    Ensures that get_ldap_server returns JSON data when used with ID and no
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/ldapservers/id/1001")))
    assert classic.get_ldap_server(1001) == EXPECTED_JSON


@responses.activate
def test_get_ldap_server_name_xml(classic):
    """
    Ensures that get_ldap_server returns XML data when used with name and
    data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/ldapservers/name/testname"), data_type="xml"
        )
    )
    assert classic.get_ldap_server(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_ldap_server_user_id_json(classic):
    """
    Ensures that get_ldap_server_user returns JSON data when used with ID and
    no optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/ldapservers/id/1001/user/testuser")
        )
    )
    assert classic.get_ldap_server_user("testuser", 1001) == EXPECTED_JSON


@responses.activate
def test_get_ldap_server_user_name_xml(classic):
    """
    Ensures that get_ldap_server_user returns XML data when used with name and
    data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/ldapservers/name/testname/user/testuser"),
            data_type="xml",
        )
    )
    assert (
        classic.get_ldap_server_user("testuser", name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_ldap_server_group_id_json(classic):
    """
    Ensures that get_ldap_server_group returns JSON data when used with ID and
    no optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/ldapservers/id/1001/group/testgroup")
        )
    )
    assert classic.get_ldap_server_group("testgroup", 1001) == EXPECTED_JSON


@responses.activate
def test_get_ldap_server_group_name_xml(classic):
    """
    Ensures that get_ldap_server_group returns XML data when used with name and
    data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/ldapservers/name/testname/group/testgroup"),
            data_type="xml",
        )
    )
    assert (
        classic.get_ldap_server_group("testgroup", name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_ldap_server_group_user_id_json(classic):
    """
    Ensures that get_ldap_server_group_user returns JSON data when used with id
    and one user
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/ldapservers/id/1001/group/groupname/user/userone"),
        )
    )
    assert (
        classic.get_ldap_server_group_user("groupname", ["userone"], 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_get_ldap_server_group_users_name_xml(classic):
    """
    Ensures that get_ldap_server_group_user returns XML data when used with
    name and multiple users with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/ldapservers/name/ldapname/group/groupname/user"
                "/userone%2Cusertwo"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.get_ldap_server_group_user(
            "groupname", ["userone", "usertwo"], name="ldapname", data_type="xml"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_create_ldap_server_id(classic):
    """
    Ensures that create_ldap_server runs successfully when using ID 0
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/ldapservers/id/0"), data_type="xml"
        )
    )
    assert classic.create_ldap_server(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_ldap_server_id(classic):
    """
    Ensures that update_ldap_server runs successfully when using ID as the
    identifier
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/ldapservers/id/1001"), data_type="xml"
        )
    )
    assert classic.update_ldap_server(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_update_ldap_server_name(classic):
    """
    Ensures that update_ldap_server runs successfully when using name as the
    identifier
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/ldapservers/name/testname"), data_type="xml"
        )
    )
    assert classic.update_ldap_server(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_ldap_server_id(classic):
    """
    Ensures that delete_ldap_server runs successfully when using ID as the
    identifier
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/ldapservers/id/1001"), data_type="xml"
        )
    )
    assert classic.delete_ldap_server(1001) == EXPECTED_XML


@responses.activate
def test_delete_ldap_server_name(classic):
    """
    Ensures that delete_ldap_server runs successfully when using name as the
    identifier
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/ldapservers/name/testname"), data_type="xml"
        )
    )
    assert classic.delete_ldap_server(name="testname") == EXPECTED_XML


"""
/licensedsoftware
"""


@responses.activate
def test_get_licensed_software_all_json(classic):
    """
    Ensures that get_licensed_software_all returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/licensedsoftware")))
    assert classic.get_licensed_software_all() == EXPECTED_JSON


@responses.activate
def test_get_licensed_software_all_xml(classic):
    """
    Ensures that get_licensed_software_all returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/licensedsoftware"), data_type="xml"
        )
    )
    assert classic.get_licensed_software_all(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_licensed_software_id_json(classic):
    """
    Ensures that get_licensed_software returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/licensedsoftware/id/1001"))
    )
    assert classic.get_licensed_software(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_licensed_software_name_xml(classic):
    """
    Ensures that get_licensed_software returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/licensedsoftware/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_licensed_software(name="testname", data_type="xml") == EXPECTED_XML
    )


@responses.activate
def test_create_licensed_software_id(classic):
    """
    Ensures that create_licensed_software returns data when creating
    a licensed software with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/licensedsoftware/id/0"), data_type="xml"
        )
    )
    assert classic.create_licensed_software(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_licensed_software_id(classic):
    """
    Ensures that update_licensed_software returns data when updating
    a licensed software with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/licensedsoftware/id/1001"), data_type="xml"
        )
    )
    assert classic.update_licensed_software(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_licensed_software_name(classic):
    """
    Ensures that update_licensed_software returns data when updating
    a licensed software with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/licensedsoftware/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_licensed_software(EXPECTED_XML, name="testname") == EXPECTED_XML
    )


@responses.activate
def test_delete_licensed_software_id(classic):
    """
    Ensures that delete_licensed_software returns data when deleting a
    licensed software by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/licensedsoftware/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_licensed_software(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_licensed_software_name(classic):
    """
    Ensures that delete_licensed_software returns data when deleting a
    licensed software by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/licensedsoftware/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_licensed_software(name="testname") == EXPECTED_XML


"""
/logflush
"""


@responses.activate
def test_create_log_flush(classic):
    """
    Ensures that create_log_flush completes successfully when run with required
    params
    """
    responses.add(
        response_builder("DELETE", jps_url("/JSSResource/logflush"), data_type="xml")
    )
    assert classic.create_log_flush(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_log_flush_interval(classic):
    """
    Ensures that create_log_flush_interval completes successfully when run
    without using ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/logflush/policy/interval/One+Weeks"),
            data_type="xml",
        )
    )
    assert classic.create_log_flush_interval("One+Weeks") == EXPECTED_XML


@responses.activate
def test_create_log_flush_interval_id(classic):
    """
    Ensures that create_log_flush_interval completes successfully when run with
    ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/logflush/policy/id/1001/interval/Six+Months"),
            data_type="xml",
        )
    )
    assert classic.create_log_flush_interval("Six+Months", 1001) == EXPECTED_XML


def test_create_log_flush_interval_value_error(classic):
    """
    Ensures that create_log_flush raises ValueError when an interval is passed
    without a "+" in the string
    """
    with pytest.raises(ValueError):
        classic.create_log_flush_interval("One Week", id=1001)


"""
/macapplications
"""


@responses.activate
def test_get_mac_applications_json(classic):
    """
    Ensures that get_mac_applications returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/macapplications")))
    assert classic.get_mac_applications() == EXPECTED_JSON


@responses.activate
def test_get_mac_applications_xml(classic):
    """
    Ensures that get_mac_applications returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/macapplications"), data_type="xml"
        )
    )
    assert classic.get_mac_applications(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_mac_application_id_json(classic):
    """
    Ensures that get_mac_application returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/macapplications/id/1001"))
    )
    assert classic.get_mac_application(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_mac_application_name_xml(classic):
    """
    Ensures that get_mac_application returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/macapplications/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_mac_application(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_mac_application_id_subset(classic):
    """
    Ensures that get_mac_application returns data when used with id as an
    identifier and one subset options
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/macapplications/id/1001/subset/General")
        )
    )
    assert classic.get_mac_application(1001, subsets=["General"]) == EXPECTED_JSON


@responses.activate
def test_get_mac_application_id_subsets(classic):
    """
    Ensures that get_mac_application returns data when used with id as an
    identifier and multiple subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/macapplications/id/1001/subset/General%26SelfService"
            ),
        )
    )
    assert (
        classic.get_mac_application(1001, subsets=["General", "SelfService"])
        == EXPECTED_JSON
    )


@responses.activate
def test_create_mac_application_id(classic):
    """
    Ensures that create_mac_application returns data when creating
    a Mac application with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/macapplications/id/0"), data_type="xml"
        )
    )
    assert classic.create_mac_application(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_mac_application_id(classic):
    """
    Ensures that update_mac_application returns data when updating
    a Mac application with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/macapplications/id/1001"), data_type="xml"
        )
    )
    assert classic.update_mac_application(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_mac_application_name(classic):
    """
    Ensures that update_mac_application returns data when updating
    a Mac application with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/macapplications/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_mac_application(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_mac_application_id(classic):
    """
    Ensures that delete_mac_application returns data when deleting a
    Mac application by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/macapplications/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_mac_application(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_mac_application_name(classic):
    """
    Ensures that delete_mac_application returns data when deleting a
    Mac application by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/macapplications/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_mac_application(name="testname") == EXPECTED_XML


"""
/managedpreferenceprofiles
"""


@responses.activate
def test_get_managed_preference_profiles_json(classic):
    """
    Ensures that get_managed_preference_profiles returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/managedpreferenceprofiles"))
    )
    assert classic.get_managed_preference_profiles() == EXPECTED_JSON


@responses.activate
def test_get_managed_preference_profiles_xml(classic):
    """
    Ensures that get_managed_preference_profiles returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/managedpreferenceprofiles"), data_type="xml"
        )
    )
    assert classic.get_managed_preference_profiles(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_managed_preference_profile_id_json(classic):
    """
    Ensures that get_managed_preference_profile returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/managedpreferenceprofiles/id/1001")
        )
    )
    assert classic.get_managed_preference_profile(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_managed_preference_profile_name_xml(classic):
    """
    Ensures that get_managed_preference_profile returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/managedpreferenceprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_managed_preference_profile(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_managed_preference_profile_id_subset(classic):
    """
    Ensures that get_managed_preference_profile returns data when used with id
    as an identifier and one subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/managedpreferenceprofiles/id/1001/subset/General"),
        )
    )
    assert (
        classic.get_managed_preference_profile(1001, subsets=["General"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_managed_preference_profile_id_subsets(classic):
    """
    Ensures that get_managed_preference_profile returns data when used with id
    as an identifier and multiple subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/managedpreferenceprofiles/id/1001/subset/General%26Scope"
            ),
        )
    )
    assert (
        classic.get_managed_preference_profile(1001, subsets=["General", "Scope"])
        == EXPECTED_JSON
    )


@responses.activate
def test_update_managed_preference_profile_id(classic):
    """
    Ensures that update_managed_preference_profile returns data when updating
    a managed preference profile with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/managedpreferenceprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_managed_preference_profile(EXPECTED_XML, id=1001) == EXPECTED_XML
    )


@responses.activate
def test_update_managed_preference_profile_name(classic):
    """
    Ensures that update_managed_preference_profile returns data when updating
    a managed preference profile with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/managedpreferenceprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_managed_preference_profile(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_managed_preference_profile_id(classic):
    """
    Ensures that delete_managed_preference_profile returns data when deleting a
    managed preference profile by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/managedpreferenceprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_managed_preference_profile(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_managed_preference_profile_name(classic):
    """
    Ensures that delete_managed_preference_profile returns data when deleting a
    managed preference profile by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/managedpreferenceprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_managed_preference_profile(name="testname") == EXPECTED_XML


"""
/mobiledeviceapplications
"""


@responses.activate
def test_get_mobile_device_applications_json(classic):
    """
    Ensures that get_mobile_device_applications returns JSON when run without
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledeviceapplications"))
    )
    assert classic.get_mobile_device_applications() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_applications_xml(classic):
    """
    Ensures that get_mobile_device_applications returns XML when run with
    data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceapplications"), data_type="xml"
        )
    )
    assert classic.get_mobile_device_applications("xml") == EXPECTED_XML


@responses.activate
def test_get_mobile_device_application_id_json(classic):
    """
    Ensures that get_mobile_device_application returns JSON when run with ID as
    the identifier
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceapplications/id/1001")
        )
    )
    assert classic.get_mobile_device_application(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_application_name_xml(classic):
    """
    Ensures that get_mobile_device_application returns XML when run with name
    as the identifier and data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceapplications/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_application(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_mobile_device_application_id_subsets(classic):
    """
    Ensures that get_mobile_device_application returns JSON when run with ID
    as the identifier and subsets
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledeviceapplications/id/1001/subset/General%26Scope"
            ),
        )
    )
    assert (
        classic.get_mobile_device_application(id=1001, subsets=["General", "Scope"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_application_bundleid(classic):
    """
    Ensures that get_mobile_device_application returns JSON when run with
    bundleid as the identifier and no additional optional params
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceapplications/bundleid/com.testname"),
        )
    )
    assert (
        classic.get_mobile_device_application(bundleid="com.testname") == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_application_bundleid_version(classic):
    """
    Ensures that get_mobile_device_application returns JSON when run with
    bundleid and version set and no additional optional params
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledeviceapplications/bundleid/com.testname"
                "/version/0.1.0"
            ),
        )
    )
    assert (
        classic.get_mobile_device_application(bundleid="com.testname", version="0.1.0")
        == EXPECTED_JSON
    )


def test_get_mobile_device_application_id_version(classic):
    """
    Ensures that get_mobile_device_application raises ValueError when ID is
    used with version
    """
    with pytest.raises(ValueError):
        classic.get_mobile_device_application(1001, version="0.1.0")


def test_get_mobile_device_application_bundleid_subsets(classic):
    """
    Ensures that get_mobile_device_application raises ValueError when bundleid
    is used with subsets
    """
    with pytest.raises(ValueError):
        classic.get_mobile_device_application(
            bundleid="com.testname", subsets=["General"]
        )


@responses.activate
def test_create_mobile_device_application(classic):
    """
    Ensures that create_mobile_device_application completes successfully when
    run with no optional params
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceapplications/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_mobile_device_application(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_mobile_device_application_id(classic):
    """
    Ensures that update_mobile_device_application completes successfully when
    run with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceapplications/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_mobile_device_application(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_update_mobile_device_application_name(classic):
    """
    Ensures that update_mobile_device_application completes successfully when
    run with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceapplications/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_application(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_application_bundleid(classic):
    """
    Ensures that update_mobile_device_application completes successfully when
    run with bundleid
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceapplications/bundleid/com.testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_application(EXPECTED_XML, bundleid="com.testname")
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_application_bundleid_version(classic):
    """
    Ensures that update_mobile_device_application completes successfully when
    run with bundleid and version
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url(
                "/JSSResource/mobiledeviceapplications/bundleid/com.testname"
                "/version/0.1.0"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_application(
            EXPECTED_XML, bundleid="com.testname", version="0.1.0"
        )
        == EXPECTED_XML
    )


def test_update_mobile_device_application_id_version(classic):
    """
    Ensures that update_mobile_device_application raises ValueError when run
    with id and version
    """
    with pytest.raises(ValueError):
        classic.update_mobile_device_application(EXPECTED_XML, 1001, version="0.1.0")


@responses.activate
def test_delete_mobile_device_application_id(classic):
    """
    Ensures that delete_mobile_device_application completes successfully when
    run with id
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceapplications/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_application(1001) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_application_name(classic):
    """
    Ensures that delete_mobile_device_application completes successfully when
    run with name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceapplications/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_application(name="testname") == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_application_bundleid(classic):
    """
    Ensures that delete_mobile_device_application completes successfully when
    run with bundleid
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceapplications/bundleid/com.testname"),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_application(bundleid="com.testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_application_bundleid_version(classic):
    """
    Ensures that delete_mobile_device_application completes successfully when
    run with bundleid and version
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url(
                "/JSSResource/mobiledeviceapplications/bundleid/com.testname"
                "/version/0.1.0"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_application(
            bundleid="com.testname", version="0.1.0"
        )
        == EXPECTED_XML
    )


def test_delete_mobile_device_application_id_version(classic):
    """
    Ensures that delete_mobile_device_application raises ValueError when run
    with id and version
    """
    with pytest.raises(ValueError):
        classic.delete_mobile_device_application(1001, version="0.1.0")


"""
/mobiledevicecommands
"""


@responses.activate
def test_get_mobile_device_commands_json(classic):
    """
    Ensures that get_mobile_device_commands returns JSON when run without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/mobiledevicecommands")))
    assert classic.get_mobile_device_commands() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_commands_name_xml(classic):
    """
    Ensures that get_mobile_device_commands returns XML data when run
    with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledevicecommands/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_mobile_device_commands("testname", "xml") == EXPECTED_XML


@responses.activate
def test_get_mobile_device_command_json(classic):
    """
    Ensures that get_mobile_device_command returns JSON when used without
    optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledevicecommands/uuid/1a2b3c-4d")
        )
    )
    assert classic.get_mobile_device_command("1a2b3c-4d") == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_command_xml(classic):
    """
    Ensures that get_mobile_device_command returns XML when used with
    data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledevicecommands/uuid/1a2b3c-4d"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_command(uuid="1a2b3c-4d", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_mobile_device_command_data(classic):
    """
    Ensures that create_mobile_device_command completes successfully when run
    with data
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledevicecommands/command"),
            data_type="xml",
        )
    )
    assert classic.create_mobile_device_command(data=EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_create_mobile_device_command_generic_commands(classic):
    """
    Ensures that create_mobile_device_command completes successfully when run
    with commands that don't need additional params
    """
    generic_commands = [
        "BlankPush",
        "ClearPasscode",
        "ClearRestrictionsPassword",
        "DeviceLocation",
        "DisableLostMode",
        "PlayLostModeSound",
        "RestartDevice",
        "Settings",
        "SettingsDisableAppAnalytics",
        "SettingsDisableBluetooth",
        "SettingsEnablePersonalHotspot",
        "SettingsDisablePersonalHotspot",
        "SettingsDisableDataRoaming",
        "SettingsDisableDiagnosticSubmission",
        "SettingsDisableVoiceRoaming",
        "SettingsEnableAppAnalytics",
        "SettingsEnableBluetooth",
        "SettingsEnableDataRoaming",
        "SettingsEnableDiagnosticSubmission",
        "SettingsEnableVoiceRoaming",
        "ShutDownDevice",
        "UnmanageDevice",
        "UpdateInventory",
    ]
    for command in generic_commands:
        responses.add(
            response_builder(
                "POST",
                jps_url(
                    f"/JSSResource/mobiledevicecommands/command/{command}"
                    "/id/1001%2C1002"
                ),
                data_type="xml",
            )
        )
        assert (
            classic.create_mobile_device_command(command, [1001, "1002"])
            == EXPECTED_XML
        )


@responses.activate
def test_create_mobile_device_command_devicename(classic):
    """
    Ensures that create_mobile_device_command completes successfully with
    command set to DeviceName and device_name set
    """
    responses.add(
        response_builder(
            "POST",
            jps_url(
                "/JSSResource/mobiledevicecommands/command/DeviceName/testname/id/1001"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.create_mobile_device_command(
            "DeviceName", [1001], device_name="testname"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_create_mobile_device_command_devicelock(classic):
    """
    Ensures that create_mobile_device_command completes successfully with
    command set to DeviceLock and lock_message set
    """
    responses.add(
        response_builder(
            "POST",
            jps_url(
                "/JSSResource/mobiledevicecommands/command/DeviceLock"
                "/Test%20Lock%20Message/id/1001"
            ),
            data_type="xml",
        )
    )
    assert classic.create_mobile_device_command(
        "DeviceLock", [1001], lock_message="Test Lock Message"
    )


@responses.activate
def test_create_mobile_device_command_scheduleosupdate(classic):
    """
    Ensures that create_mobile_device_command completes successfully with
    command set to ScheduleOSUpdate and install_action set
    """
    install_actions = [1, 2]
    for install_action in install_actions:
        responses.add(
            response_builder(
                "POST",
                jps_url(
                    "/JSSResource/mobiledevicecommands/command/ScheduleOSUpdate"
                    f"/{install_action}/id/1001"
                ),
                data_type="xml",
            )
        )
        assert classic.create_mobile_device_command(
            "ScheduleOSUpdate", [1001], install_action=install_action
        )


@responses.activate
def test_create_mobile_device_command_scheduleosupdate_product_version(classic):
    """
    Ensures that create_mobile_device_command completes successfully with
    command set to ScheduleOsUpdate and product_version set
    """
    install_actions = [1, 2]
    for install_action in install_actions:
        responses.add(
            response_builder(
                "POST",
                jps_url(
                    "/JSSResource/mobiledevicecommands/command/ScheduleOSUpdate"
                    f"/{install_action}/16.1.1/id/1001"
                ),
                data_type="xml",
            )
        )
        assert classic.create_mobile_device_command(
            "ScheduleOSUpdate",
            [1001],
            install_action=install_action,
            product_version="16.1.1",
        )


def test_create_mobile_device_command_unsupported_command_parameter(classic):
    """
    Ensures that create_mobile_device_command raises InvalidParameterOptions
    when command is set to EnableLostMode, EraseDevice, or
    PasscodeLockGracePeriod
    """
    unsupported_command_params = [
        "EnableLostMode",
        "EraseDevice",
        "PasscodeLockGracePeriod",
    ]
    for unsupported_command_param in unsupported_command_params:
        with pytest.raises(InvalidParameterOptions):
            classic.create_mobile_device_command(unsupported_command_param, [1001])


def test_create_mobile_device_command_unrecognized_command(classic):
    """
    Ensures that create_mobile_device_command raises InvalidParameterOptions
    when command is set to something that is not in command_options
    """
    with pytest.raises(InvalidParameterOptions):
        classic.create_mobile_device_command("NotACommand", [1001])


def test_create_mobile_device_command_no_params_or_data(classic):
    """
    Ensures that create_mobile_device_command raises NoParametersOrData when
    used without params and data set
    """
    with pytest.raises(NoParametersOrData):
        classic.create_mobile_device_command()


def test_create_mobile_device_command_params_and_data(classic):
    """
    Ensures that create_mobile_device_command raises ParametersAndData when
    used with params and data set
    """
    with pytest.raises(ParametersAndData):
        classic.create_mobile_device_command("DeviceName", [1001], data=EXPECTED_XML)


def test_create_mobile_device_command_params_missing(classic):
    """
    Ensures that create_mobile_device_command raises MissingParameters when
    ran with only command or ids
    """
    with pytest.raises(MissingParameters):
        classic.create_mobile_device_command("DeviceName")


def test_create_mobile_device_command_scheduleosupdate_invalid_install_action(classic):
    """
    Ensures that create_mobile_device_command raises InvalidParameterOptions
    when ran with install_action set to a value other than 1 or 2
    """
    with pytest.raises(InvalidParameterOptions):
        classic.create_mobile_device_command(
            "ScheduleOSUpdate", [1001], install_action=3
        )


"""
/mobiledeviceconfigurationprofiles
"""


@responses.activate
def test_get_mobile_device_configuration_profiles_json(classic):
    """
    Ensures that get_mobile_device_configuration_profiles returns a JSON dict
    when passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceconfigurationprofiles")
        )
    )
    assert classic.get_mobile_device_configuration_profiles() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_configuration_profiles_xml(classic):
    """
    Ensures that get_mobile_device_configuration_profiles returns a XML str
    when passing "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceconfigurationprofiles"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_configuration_profiles(data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_mobile_device_configuration_profile_id_json(classic):
    """
    Ensures that get_mobile_device_configuration_profile returns a JSON dict
    when passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceconfigurationprofiles/id/1001")
        )
    )
    assert classic.get_mobile_device_configuration_profile(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_configuration_profile_name_xml(classic):
    """
    Ensures that get_mobile_device_configuration_profile returns XML when
    passing "xml" as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceconfigurationprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_configuration_profile(
            name="testname", data_type="xml"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_get_mobile_device_configuration_profile_id_subset(classic):
    """
    Ensures that get_mobile_device_configuration_profile returns data when
    used with id as an identifier and one subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledeviceconfigurationprofiles/id/1001"
                "/subset/General"
            ),
        )
    )
    assert (
        classic.get_mobile_device_configuration_profile(1001, subsets=["General"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_configuration_profile_id_subsets(classic):
    """
    Ensures that get_mobile_device_configuration_profile returns data when
    used with id as an identifier and multiple subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledeviceconfigurationprofiles/id/1001/subset"
                "/General%26SelfService"
            ),
        )
    )
    assert (
        classic.get_mobile_device_configuration_profile(
            1001, subsets=["General", "SelfService"]
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_mobile_device_configuration_profile_id(classic):
    """
    Ensures that create_mobile_device_configuration_profile returns data when
    updating a mobile device configuration profile with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceconfigurationprofiles/id/0"),
            data_type="xml",
        )
    )
    assert (
        classic.create_mobile_device_configuration_profile(EXPECTED_XML) == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_configuration_profile_id(classic):
    """
    Ensures that update_mobile_device_configuration_profile returns data when
    updating a mobile device configuration profile with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceconfigurationprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_configuration_profile(EXPECTED_XML, id=1001)
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_configuration_profile_name(classic):
    """
    Ensures that update_mobile_device_configuration_profile returns data when
    updating a mobile device configuration profile with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceconfigurationprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_configuration_profile(
            EXPECTED_XML, name="testname"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_configuration_profile_id(classic):
    """
    Ensures that delete_mobile_device_configuration_profile returns data when
    deleting a mobile device configuration profile by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceconfigurationprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_configuration_profile(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_configuration_profile_name(classic):
    """
    Ensures that delete_mobile_device_configuration_profile returns data when
    deleting a mobile device configuration profile by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceconfigurationprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_configuration_profile(name="testname")
        == EXPECTED_XML
    )


"""
/mobiledeviceenrollmentprofiles
"""


@responses.activate
def test_get_mobile_device_enrollment_profiles_json(classic):
    """
    Ensures that get_mobile_device_enrollment_profiles returns a JSON dict
    when passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledeviceenrollmentprofiles"))
    )
    assert classic.get_mobile_device_enrollment_profiles() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_enrollment_profiles_xml(classic):
    """
    Ensures that get_mobile_device_enrollment_profiles returns a XML str when
    passing "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceenrollmentprofiles"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_enrollment_profiles(data_type="xml") == EXPECTED_XML
    )


@responses.activate
def test_get_mobile_device_enrollment_profile_id_json(classic):
    """
    Ensures that get_mobile_device_enrollment_profile returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceenrollmentprofiles/id/1001")
        )
    )
    assert classic.get_mobile_device_enrollment_profile(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_enrollment_profile_name_xml(classic):
    """
    Ensures that get_mobile_device_enrollment_profile returns XML when passing
    "xml" as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceenrollmentprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_enrollment_profile(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_mobile_device_enrollment_profile_id_subset(classic):
    """
    Ensures that get_mobile_device_enrollment_profile returns data when used
    with id as an identifier and one subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledeviceenrollmentprofiles/id/1001/subset/General"
            ),
        )
    )
    assert (
        classic.get_mobile_device_enrollment_profile(1001, subsets=["General"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_enrollment_profile_id_subsets(classic):
    """
    Ensures that get_mobile_device_enrollment_profile returns data when used
    with id as an identifier and multiple subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledeviceenrollmentprofiles/id/1001"
                "/subset/General%26Location"
            ),
        )
    )
    assert (
        classic.get_mobile_device_enrollment_profile(
            1001, subsets=["General", "Location"]
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_enrollment_profile_invitation_subsets(classic):
    """
    Ensures that get_mobile_device_enrollment_profile returns data when used
    with invitation as an identifier and multiple subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledeviceenrollmentprofiles/invitation"
                "/testinvite/subset/General%26Location"
            ),
        )
    )
    assert classic.get_mobile_device_enrollment_profile(
        invitation="testinvite", subsets=["General", "Location"]
    )


@responses.activate
def test_create_mobile_device_enrollment_profile_id(classic):
    """
    Ensures that create_mobile_device_enrollment_profile returns data when
    updating a mobile device enrollment profile with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceenrollmentprofiles/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_mobile_device_enrollment_profile(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_mobile_device_enrollment_profile_id(classic):
    """
    Ensures that update_mobile_device_enrollment_profile returns data when
    updating a mobile device enrollment profile with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceenrollmentprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_enrollment_profile(EXPECTED_XML, id=1001)
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_enrollment_profile_name(classic):
    """
    Ensures that update_mobile_device_enrollment_profile returns data when
    updating a mobile device enrollment profile with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceenrollmentprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_enrollment_profile(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_enrollment_profile_invitation(classic):
    """
    Ensures that update_mobile_device_enrollment_profile returns data when
    updating a mobile device enrollment profile with invitation
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url(
                "/JSSResource/mobiledeviceenrollmentprofiles/invitation"
                "/testinvitation"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_enrollment_profile(
            EXPECTED_XML, invitation="testinvitation"
        )
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_enrollment_profile_id(classic):
    """
    Ensures that delete_mobile_device_enrollment_profile returns data when
    deleting a mobile device enrollment profile by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceenrollmentprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_enrollment_profile(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_enrollment_profile_name(classic):
    """
    Ensures that delete_mobile_device_enrollment_profile returns data when
    deleting a mobile device enrollment profile by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceenrollmentprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_enrollment_profile(name="testname") == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_enrollment_profile_invitation(classic):
    """
    Ensures that delete_mobile_device_enrollment_profile returns data when
    deleting a mobile device enrollment profile by invitation
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url(
                "/JSSResource/mobiledeviceenrollmentprofiles"
                "/invitation/testinvitation"
            ),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_enrollment_profile(invitation="testinvitation")
        == EXPECTED_XML
    )


"""
/mobiledeviceextensionattributes
"""


@responses.activate
def test_get_mobile_device_extension_attributes_json(classic):
    """
    Ensures that mobile_device_extension_attributes returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledeviceextensionattributes"))
    )
    assert classic.get_mobile_device_extension_attributes() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_extension_attributes_xml(classic):
    """
    Ensures that mobile_device_extension_attributes returns a XML str when
    passing "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceextensionattributes"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_extension_attributes(data_type="xml") == EXPECTED_XML
    )


@responses.activate
def test_get_mobile_device_extension_attribute_id_json(classic):
    """
    Ensures that get_mobile_device_extension_attribute returns a JSON dict
    when passing "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceextensionattributes/id/1001")
        )
    )
    assert classic.get_mobile_device_extension_attribute(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_extension_attribute_name_xml(classic):
    """
    Ensures that get_mobile_device_extension_attribute returns XML when
    passing "xml" as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_extension_attribute(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_mobile_device_extension_attribute_id(classic):
    """
    Ensures that create_mobile_device_extension_attribute returns data when
    updating a mobile device extension attribute with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceextensionattributes/id/0"),
            data_type="xml",
        )
    )
    assert (
        classic.create_mobile_device_extension_attribute(EXPECTED_XML) == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_extension_attribute_id(classic):
    """
    Ensures that update_mobile_device_extension_attribute returns data when
    updating a mobile device extension attribute with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceextensionattributes/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_extension_attribute(EXPECTED_XML, id=1001)
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_extension_attribute_name(classic):
    """
    Ensures that update_mobile_device_extension_attribute returns data when
    updating a mobile device extension attribute with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_extension_attribute(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_extension_attribute_id(classic):
    """
    Ensures that delete_mobile_device_extension_attribute returns data when
    deleting a mobile device extension attribute by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceextensionattributes/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_extension_attribute(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_extension_attribute_name(classic):
    """
    Ensures that delete_mobile_device_extension_attribute returns data when
    deleting a mobile device extension attribute by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_extension_attribute(name="testname")
        == EXPECTED_XML
    )


"""
/mobiledevicegroups
"""


@responses.activate
def test_get_mobile_device_groups_json(classic):
    """
    Ensures that mobile_device_groups returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/mobiledevicegroups")))
    assert classic.get_mobile_device_groups() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_groups_xml(classic):
    """
    Ensures that mobile_device_groups returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledevicegroups"), data_type="xml"
        )
    )
    assert classic.get_mobile_device_groups(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_mobile_device_group_id_json(classic):
    """
    Ensures that get_mobile_device_group returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledevicegroups/id/1001"))
    )
    assert classic.get_mobile_device_group(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_group_name_xml(classic):
    """
    Ensures that get_mobile_device_group returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledevicegroups/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_group(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_mobile_device_group_id(classic):
    """
    Ensures that create_mobile_device_group returns data when creating
    a mobile device group with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/mobiledevicegroups/id/0"), data_type="xml"
        )
    )
    assert classic.create_mobile_device_group(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_mobile_device_group_id(classic):
    """
    Ensures that update_mobile_device_group returns data when updating
    a mobile device group with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/mobiledevicegroups/id/1001"), data_type="xml"
        )
    )
    assert classic.update_mobile_device_group(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_mobile_device_group_name(classic):
    """
    Ensures that update_mobile_device_group returns data when updating
    a mobile device group with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledevicegroups/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_group(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_group_id(classic):
    """
    Ensures that delete_mobile_device_group returns data when deleting a
    mobile device group by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledevicegroups/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_group(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_group_name(classic):
    """
    Ensures that delete_mobile_device_group returns data when deleting a
    mobile device group by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledevicegroups/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_group(name="testname") == EXPECTED_XML


"""
/mobiledevicehistory
"""


@responses.activate
def test_get_mobile_device_history_id(classic):
    """
    Ensures that get_mobile_device_history returns json data when
    used with ID
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledevicehistory/id/1001"),
        )
    )
    assert classic.get_mobile_device_history(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_history_name(classic):
    """
    Ensures that get_mobile_device_history returns json data when
    used with name
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledevicehistory/name/testname"),
        )
    )
    assert classic.get_mobile_device_history(name="testname") == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_history_udid_xml(classic):
    """
    Ensures that get_mobile_device_history returns XML data when
    used with UDID with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledevicehistory/udid/1001"),
            data_type="xml",
        )
    )
    assert classic.get_mobile_device_history(udid=1001, data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_mobile_device_history_macaddress_subset(classic):
    """
    Ensures that get_mobile_device_history returns data when used
    with macaddress identifier and one subset
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledevicehistory/macaddress/"
                "12%3A34%3A56%3A78%3A90%3A12/subset/General"
            ),
        )
    )
    assert (
        classic.get_mobile_device_history(
            macaddress="12:34:56:78:90:12",
            subsets=["General"],
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_history_serialnumber_subsets(classic):
    """
    Ensures that get_mobile_device_history returns data when used
    with serialnumber identifier and multiple subsets
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/mobiledevicehistory/serialnumber/1a2b3c4d5e"
                "/subset/General%26Audits"
            ),
        )
    )
    assert (
        classic.get_mobile_device_history(
            serialnumber="1a2b3c4d5e",
            subsets=["General", "Audits"],
        )
        == EXPECTED_JSON
    )


"""
/mobiledeviceinvitations
"""


@responses.activate
def test_get_mobile_device_invitations_json(classic):
    """
    Ensures that get_mobile_device_invitations returns data when used
    without optional parameters.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledeviceinvitations"))
    )
    assert classic.get_mobile_device_invitations() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_invitations_xml(classic):
    """
    Ensures that get_mobile_device_invitations returns data when used
    with data_type set to "xml".
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceinvitations"), data_type="xml"
        )
    )
    assert classic.get_mobile_device_invitations(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_mobile_device_invitation_id_json(classic):
    """
    Ensures that get_mobile_device_invitation returns json data when used with
    id as the identifier and no additional params.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledeviceinvitations/id/1001"))
    )
    assert classic.get_mobile_device_invitation(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_invitation_invitation_xml(classic):
    """
    Ensures that get_mobile_device)invitation returns xml data when used with
    invitation as the identifier and "xml" set as data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceinvitations/invitation/123456789"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_invitation(invitation=123456789, data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_mobile_device_invitation_id_0(classic):
    """
    Ensures that create_mobile_device_invitation successfully runs when used
    with ID set to 0 to use the next available ID
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceinvitations/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_mobile_device_invitation(EXPECTED_XML, id=0) == EXPECTED_XML


@responses.activate
def test_create_mobile_device_invitation_invitation_0(classic):
    """
    Ensures that create_mobile_device_invitation successfully runs when used
    with the invitation identifier set to 0 to use a random available
    invitation
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceinvitations/invitation/0"),
            data_type="xml",
        )
    )
    assert (
        classic.create_mobile_device_invitation(EXPECTED_XML, invitation=0)
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_invitation_id_json(classic):
    """
    Ensures that delete_mobile_device_invitation completes successfully when
    used with id as the identifier.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceinvitations/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_invitation(1001) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_invitation_invitation_xml(classic):
    """
    Ensures that delete_mobile_device_invitation completes successfully when
    used with invitation as the identifier.
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceinvitations/invitation/123456789"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_invitation(invitation=123456789) == EXPECTED_XML


"""
/mobiledeviceprovisioningprofiles
"""


@responses.activate
def test_get_mobile_device_provisioning_profiles_json(classic):
    """
    Ensures that get_mobile_device_provisioning_profiles returns JSON when
    ran without optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceprovisioningprofiles")
        )
    )
    assert classic.get_mobile_device_provisioning_profiles() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_provisioning_profiles_xml(classic):
    """
    Ensures that get_mobile_device_provisioning_profiles returns XML when
    ran with "xml" set for data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles"),
            data_type="xml",
        )
    )
    assert classic.get_mobile_device_provisioning_profiles("xml") == EXPECTED_XML


@responses.activate
def test_get_mobile_device_provisioning_profile_id(classic):
    """
    Ensures that get_mobile_device_provisioning_profile returns JSON when id
    is used as the identification
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceprovisioningprofiles/id/1001")
        )
    )
    assert classic.get_mobile_device_provisioning_profile(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_provisioning_profile_name_xml(classic):
    """
    Ensures that get_mobile_device_provisioning_profile returns XML when name
    is used as the identifier and xml set as data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_mobile_device_provisioning_profile(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_mobile_device_provisioning_profile_uuid(classic):
    """
    Ensures that get_mobile_device_provisioning_profile returns JSON when uuid
    is used as the identifier
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/mobiledeviceprovisioningprofiles/uuid/1ab2")
        )
    )
    assert classic.get_mobile_device_provisioning_profile(uuid="1ab2") == EXPECTED_JSON


@responses.activate
def test_create_mobile_device_provisioning_profile_id(classic):
    """
    Ensures that create_mobile_device_provisioning_profile completes
    successfully when used with id as the identifier
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/id/0"),
            data_type="xml",
        )
    )
    assert (
        classic.create_mobile_device_provisioning_profile(EXPECTED_XML, id=0)
        == EXPECTED_XML
    )


@responses.activate
def test_create_mobile_device_provisioning_profile_name(classic):
    """
    Ensures that create_mobile_device_provisioning_profile completes
    successfully when used with name as the identifier
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.create_mobile_device_provisioning_profile(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_create_mobile_device_provisioning_profile_uuid(classic):
    """
    Ensures that create_mobile_device_provisioning_profile completes
    successfully when used with name as the identifier
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/uuid/1ab2"),
            data_type="xml",
        )
    )
    assert (
        classic.create_mobile_device_provisioning_profile(EXPECTED_XML, uuid="1ab2")
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_provisioning_profile_id(classic):
    """
    Ensures that update_mobile_device_provisioning_profile completes
    successfully when used with id as the identifier
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/id/0"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_provisioning_profile(EXPECTED_XML, id=0)
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_provisioning_profile_name(classic):
    """
    Ensures that update_mobile_device_provisioning_profile completes
    successfully when used with name as the identifier
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_provisioning_profile(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_update_mobile_device_provisioning_profile_uuid(classic):
    """
    Ensures that update_mobile_device_provisioning_profile completes
    successfully when used with name as the identifier
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/uuid/1ab2"),
            data_type="xml",
        )
    )
    assert (
        classic.update_mobile_device_provisioning_profile(EXPECTED_XML, uuid="1ab2")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_provisioning_profile_id(classic):
    """
    Ensures that delete_mobile_device_provisioning_profile completes
    successfully when used with id as the identifier
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/id/0"),
            data_type="xml",
        )
    )
    assert classic.delete_mobile_device_provisioning_profile(id=0) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_provisioning_profile_name(classic):
    """
    Ensures that delete_mobile_device_provisioning_profile completes
    successfully when used with name as the identifier
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_provisioning_profile(name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_mobile_device_provisioning_profile_uuid(classic):
    """
    Ensures that delete_mobile_device_provisioning_profile completes
    successfully when used with name as the identifier
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/mobiledeviceprovisioningprofiles/uuid/1ab2"),
            data_type="xml",
        )
    )
    assert (
        classic.delete_mobile_device_provisioning_profile(uuid="1ab2") == EXPECTED_XML
    )


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
def test_get_mobile_devices_incorrect_data_type(classic):
    """
    Ensures get_mobile_devices raises InvalidDataType when an option that is
    not "json" or "xml" is passed to data_type
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/mobiledevices")))
    with pytest.raises(InvalidDataType):
        classic.get_mobile_devices(data_type="invalid")


@responses.activate
def test_get_mobile_devices_match(classic):
    """
    Ensures get_mobile_devices returns content from the API and uses its
    authorization correctly.
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/mobiledevices/match/iPad%2A"))
    )
    assert classic.get_mobile_devices(match="iPad*") == EXPECTED_JSON


@responses.activate
def test_get_mobile_devices_500(classic):
    """
    Ensures that get_mobile_devices error out correctly when a 500 error
    is received.
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
            jps_url("/JSSResource/mobiledevices/id/1001/subset/General%26Network"),
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
    Ensures that get_mobile_device correctly raises a HTTPError when the
    request returns a 500 error.
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
    Ensures that update_mobile_device raises ClientError when the request
    returns a 400 status code.
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/mobiledevices/id/1001"), status=400
        )
    )
    with pytest.raises(ClientError):
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
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/mobiledevices/id/1001"), data_type="xml"
        )
    )
    assert classic.delete_mobile_device(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_mobile_device_id_500(classic):
    """
    Ensures that delete_mobile_device raises a HTTPError when processing an
    unrecognized HTTP error
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/mobiledevices/id/1001"), status=500
        )
    )
    with pytest.raises(HTTPError):
        classic.delete_mobile_device(id=1001)


"""
/networksegments
"""


@responses.activate
def test_get_network_segments_json(classic):
    """
    Ensures that network_segments returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/networksegments")))
    assert classic.get_network_segments() == EXPECTED_JSON


@responses.activate
def test_get_network_segments_xml(classic):
    """
    Ensures that network_segments returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/networksegments"), data_type="xml"
        )
    )
    assert classic.get_network_segments(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_network_segment_id_json(classic):
    """
    Ensures that get_network_segment returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/networksegments/id/1001"))
    )
    assert classic.get_network_segment(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_network_segment_name_xml(classic):
    """
    Ensures that get_network_segment returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/networksegments/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_network_segment(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_network_segment_id(classic):
    """
    Ensures that create_network_segment returns data when creating
    a network segment with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/networksegments/id/0"), data_type="xml"
        )
    )
    assert classic.create_network_segment(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_network_segment_id(classic):
    """
    Ensures that update_network_segment returns data when updating
    a network segment with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/networksegments/id/1001"), data_type="xml"
        )
    )
    assert classic.update_network_segment(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_network_segment_name(classic):
    """
    Ensures that update_network_segment returns data when updating
    a network segment with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/networksegments/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_network_segment(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_network_segment_id(classic):
    """
    Ensures that delete_network_segment returns data when deleting a
    network segment by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/networksegments/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_network_segment(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_network_segment_name(classic):
    """
    Ensures that delete_network_segment returns data when deleting a
    network segment by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/networksegments/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_network_segment(name="testname") == EXPECTED_XML


"""
/osxconfigurationprofiles
"""


@responses.activate
def test_get_osx_configuration_profiles_json(classic):
    """
    Ensures that get_osx_configuration_profiles returns a JSON dict when
    passing "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/osxconfigurationprofiles"))
    )
    assert classic.get_osx_configuration_profiles() == EXPECTED_JSON


@responses.activate
def test_get_osx_configuration_profiles_xml(classic):
    """
    Ensures that get_osx_configuration_profiles returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/osxconfigurationprofiles"), data_type="xml"
        )
    )
    assert classic.get_osx_configuration_profiles(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_osx_configuration_profile_id_json(classic):
    """
    Ensures that get_osx_configuration_profile returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/osxconfigurationprofiles/id/1001")
        )
    )
    assert classic.get_osx_configuration_profile(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_osx_configuration_profile_name_xml(classic):
    """
    Ensures that get_osx_configuration_profile returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/osxconfigurationprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_osx_configuration_profile(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_get_osx_configuration_profile_id_subset(classic):
    """
    Ensures that get_osx_configuration_profile returns data when used with id
    as an identifier and one subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/osxconfigurationprofiles/id/1001/subset/General"),
        )
    )
    assert (
        classic.get_osx_configuration_profile(1001, subsets=["General"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_osx_configuration_profile_id_subsets(classic):
    """
    Ensures that get_osx_configuration_profile returns data when used with id
    as an identifier and multiple subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/osxconfigurationprofiles/id/1001"
                "/subset/General%26SelfService"
            ),
        )
    )
    assert (
        classic.get_osx_configuration_profile(1001, subsets=["General", "SelfService"])
        == EXPECTED_JSON
    )


@responses.activate
def test_create_osx_configuration_profile_id(classic):
    """
    Ensures that create_osx_configuration_profile returns data when creating
    a OSX configuration profile with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/osxconfigurationprofiles/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_osx_configuration_profile(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_osx_configuration_profile_id(classic):
    """
    Ensures that update_osx_configuration_profile returns data when updating
    a OSX configuration profile with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/osxconfigurationprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_osx_configuration_profile(EXPECTED_XML, id=1001) == EXPECTED_XML
    )


@responses.activate
def test_update_osx_configuration_profile_name(classic):
    """
    Ensures that update_osx_configuration_profile returns data when updating
    a OSX configuration profile with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/osxconfigurationprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_osx_configuration_profile(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_osx_configuration_profile_id(classic):
    """
    Ensures that delete_osx_configuration_profile returns data when deleting a
    OSX configuration profile by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/osxconfigurationprofiles/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_osx_configuration_profile(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_osx_configuration_profile_name(classic):
    """
    Ensures that delete_osx_configuration_profile returns data when deleting a
    OSX configuration profile by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/osxconfigurationprofiles/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_osx_configuration_profile(name="testname") == EXPECTED_XML


"""
/packages
"""


@responses.activate
def test_get_packages_json(classic):
    """
    Ensures that packages returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/packages")))
    assert classic.get_packages() == EXPECTED_JSON


@responses.activate
def test_get_packages_xml(classic):
    """
    Ensures that packages returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/packages"), data_type="xml")
    )
    assert classic.get_packages(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_package_id_json(classic):
    """
    Ensures that get_package returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/packages/id/1001")))
    assert classic.get_package(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_package_name_xml(classic):
    """
    Ensures that get_package returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/packages/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_package(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_package_id(classic):
    """
    Ensures that create_package returns data when creating
    a package with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/packages/id/0"), data_type="xml")
    )
    assert classic.create_package(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_package_id(classic):
    """
    Ensures that update_package returns data when creating
    a package with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/packages/id/1001"), data_type="xml"
        )
    )
    assert classic.update_package(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_package_name(classic):
    """
    Ensures that update_package returns data when updating
    a package with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/packages/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_package(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_package_id(classic):
    """
    Ensures that delete_package returns data when deleting a
    package by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/packages/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_package(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_package_name(classic):
    """
    Ensures that delete_package returns data when deleting a
    package by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/packages/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_package(name="testname") == EXPECTED_XML


"""
/patchavailabletitles
"""


@responses.activate
def test_get_patch_available_titles_json(classic):
    """
    Ensures that get_patch_available_titles returns JSON when used with ID
    and no optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/patchavailabletitles/sourceid/1001")
        )
    )
    assert classic.get_patch_available_titles(1001) == EXPECTED_JSON


@responses.activate
def test_get_patch_available_titles_xml(classic):
    """
    Ensures that get_patch_available_titles returns XML when used with ID
    and "xml" set as the data_type
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/patchavailabletitles/sourceid/1001"),
            data_type="xml",
        )
    )
    assert classic.get_patch_available_titles(1001, "xml") == EXPECTED_XML


"""
/patches
"""

# Deprecated

"""
/patchexternalsources
"""


@responses.activate
def test_get_patch_external_sources_json(classic):
    """
    Ensures that external patch sources returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/patchexternalsources")))
    assert classic.get_patch_external_sources() == EXPECTED_JSON


@responses.activate
def test_get_patch_external_sources_xml(classic):
    """
    Ensures that external patch sources returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/patchexternalsources"), data_type="xml"
        )
    )
    assert classic.get_patch_external_sources(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_patch_external_source_id_json(classic):
    """
    Ensures that get_patch_external_source returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/patchexternalsources/id/1001"))
    )
    assert classic.get_patch_external_source(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_patch_external_source_name_xml(classic):
    """
    Ensures that get_patch_external_source returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/patchexternalsources/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_patch_external_source(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_patch_external_source_id(classic):
    """
    Ensures that create_patch_external_source returns data when creating
    an external patch source with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/patchexternalsources/id/0"), data_type="xml"
        )
    )
    assert classic.create_patch_external_source(EXPECTED_XML, id=0) == EXPECTED_XML


@responses.activate
def test_create_patch_external_source_name(classic):
    """
    Ensures that create_patch_external_source returns data when creating
    an external patch source with name
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/patchexternalsources/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.create_patch_external_source(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_update_patch_external_source_id(classic):
    """
    Ensures that update_patch_external_source returns data when updating
    a external patch source with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/patchexternalsources/id/1001"), data_type="xml"
        )
    )
    assert classic.update_patch_external_source(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_patch_external_source_name(classic):
    """
    Ensures that update_patch_external_source returns data when updating
    a external patch source with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/patchexternalsources/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_patch_external_source(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_patch_external_source_id(classic):
    """
    Ensures that delete_patch_external_source returns data when deleting a
    external patch source by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/patchexternalsources/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_patch_external_source(id=1001) == EXPECTED_XML


"""
/patchinternalsources
"""


@responses.activate
def test_get_patch_internal_sources_json(classic):
    """
    Ensures that internal patch sources returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/patchinternalsources")))
    assert classic.get_patch_internal_sources() == EXPECTED_JSON


@responses.activate
def test_get_patch_internal_sources_xml(classic):
    """
    Ensures that internal patch sources returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/patchinternalsources"), data_type="xml"
        )
    )
    assert classic.get_patch_internal_sources(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_patch_internal_source_id_json(classic):
    """
    Ensures that get_patch_internal_source returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/patchinternalsources/id/1001"))
    )
    assert classic.get_patch_internal_source(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_patch_internal_source_name_xml(classic):
    """
    Ensures that get_patch_internal_source returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/patchinternalsources/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_patch_internal_source(name="testname", data_type="xml")
        == EXPECTED_XML
    )


"""
/patchpolicies
"""


@responses.activate
def test_get_patch_policies_json(classic):
    """
    Ensures that get_patch_policies returns JSON data when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/patchpolicies")))
    assert classic.get_patch_policies() == EXPECTED_JSON


@responses.activate
def test_get_patch_policies_xml(classic):
    """
    Ensures that get_patch_policies returns XML data when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/patchpolicies"), data_type="xml")
    )
    assert classic.get_patch_policies("xml") == EXPECTED_XML


@responses.activate
def test_get_patch_policy_id_json(classic):
    """
    Ensures that get_patch_policy returns JSON when used with ID and no
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/patchpolicies/id/1001"))
    )
    assert classic.get_patch_policy(1001)


@responses.activate
def test_get_patch_policy_id_xml_subsets(classic):
    """
    Ensures that get_patch_policy returns XML when used with ID and multiple
    subsets along with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/patchpolicies/id/1001/subset/General%26Scope"),
            data_type="xml",
        )
    )
    assert classic.get_patch_policy(1001, ["General", "Scope"], "xml")


@responses.activate
def test_create_patch_policy_id(classic):
    """
    Ensures that create_patch_policy completes successfully when run with
    required params
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/patchpolicies/softwaretitleconfig/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_patch_policy(EXPECTED_XML, 0) == EXPECTED_XML


@responses.activate
def test_update_patch_policy_id(classic):
    """
    Ensures that update_patch_policy completes successfully when run with
    required params
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/patchpolicies/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_patch_policy(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_delete_patch_policy(classic):
    """
    Ensures that delete_patch_policy completes successfully when run with
    required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/patchpolicies/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_patch_policy(1001) == EXPECTED_XML


"""
/patchreports
"""


@responses.activate
def test_get_patch_report_id_json(classic):
    """
    Ensures that get_patch_report returns JSON when used with id and no
    optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/patchreports/patchsoftwaretitleid/1001")
        )
    )
    assert classic.get_patch_report(1001) == EXPECTED_JSON


@responses.activate
def test_get_patch_report_id_version_xml(classic):
    """
    Ensures that get_patch_report returns XML data when used with id and
    version and data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/patchreports/patchsoftwaretitleid/1001/version/0.1.0"
            ),
            data_type="xml",
        )
    )
    assert classic.get_patch_report(1001, "0.1.0", "xml") == EXPECTED_XML


"""
/patchsoftwaretitles
"""


@responses.activate
def test_get_patch_software_titles_json(classic):
    """
    Ensures that get_patch_software_titles returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/patchsoftwaretitles")))
    assert classic.get_patch_software_titles() == EXPECTED_JSON


@responses.activate
def test_get_patch_software_titles_xml(classic):
    """
    Ensures that get_patch_software_titles returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/patchsoftwaretitles"), data_type="xml"
        )
    )
    assert classic.get_patch_software_titles("xml") == EXPECTED_XML


@responses.activate
def test_get_patch_software_title_id_json(classic):
    """
    Ensures that get_patch_software_title returns JSON when used without
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/patchsoftwaretitles/id/1001"))
    )
    assert classic.get_patch_software_title(1001) == EXPECTED_JSON


@responses.activate
def test_get_patch_software_title_id_xml(classic):
    """
    Ensures that get_patch_software_title returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/patchsoftwaretitles/id/1001"), data_type="xml"
        )
    )
    assert classic.get_patch_software_title(1001, data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_patch_software_title(classic):
    """
    Ensures that create_patch_software_title completes successfully when
    run without optional params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/patchsoftwaretitles/id/0"), data_type="xml"
        )
    )
    assert classic.create_patch_software_title(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_patch_software_title(classic):
    """
    Ensures that update_patch_software_title completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/patchsoftwaretitles/id/1001"), data_type="xml"
        )
    )
    assert classic.update_patch_software_title(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_delete_patch_software_title(classic):
    """
    Ensures that delete_patch_software_title completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/patchsoftwaretitles/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_patch_software_title(1001) == EXPECTED_XML


"""
/peripherals
"""


@responses.activate
def test_get_peripherals_json(classic):
    """
    Ensures that get_peripherals returns JSON data when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/peripherals")))
    assert classic.get_peripherals() == EXPECTED_JSON


@responses.activate
def test_get_peripherals_xml(classic):
    """
    Ensures that get_peripherals returns XML data when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/peripherals"), data_type="xml")
    )
    assert classic.get_peripherals("xml") == EXPECTED_XML


@responses.activate
def test_get_peripheral_id_json(classic):
    """
    Ensures that get_peripheral returns JSON when used with ID and no
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/peripherals/id/1001")))
    assert classic.get_peripheral(1001)


@responses.activate
def test_get_peripheral_id_xml_subsets(classic):
    """
    Ensures that get_peripheral returns XML when used with ID and multiple
    subsets along with data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/peripherals/id/1001" "/subset/General%26Location"),
            data_type="xml",
        )
    )
    assert classic.get_peripheral(1001, ["General", "Location"], "xml")


@responses.activate
def test_update_peripheral_id(classic):
    """
    Ensures that update_peripheral completes successfully when run with
    required params
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/peripherals/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_peripheral(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_delete_peripheral(classic):
    """
    Ensures that delete_peripheral completes successfully when run with
    required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/peripherals/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_peripheral(1001) == EXPECTED_XML


"""
/peripheraltypes
"""


@responses.activate
def test_get_peripheral_types_json(classic):
    """
    Ensures that get_peripheral_types returns JSON data when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/peripheraltypes")))
    assert classic.get_peripheral_types() == EXPECTED_JSON


@responses.activate
def test_get_peripheral_types_xml(classic):
    """
    Ensures that get_peripheral_types returns XML data when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/peripheraltypes"), data_type="xml"
        )
    )
    assert classic.get_peripheral_types("xml") == EXPECTED_XML


@responses.activate
def test_get_peripheral_type_id_json(classic):
    """
    Ensures that get_peripheral_type returns JSON when used with ID and no
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/peripheraltypes/id/1001"))
    )
    assert classic.get_peripheral_type(1001)


@responses.activate
def test_get_peripheral_type_id_xml(classic):
    """
    Ensures that get_peripheral_type returns XML when used with ID and
    data_type set to "xml"
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/peripheraltypes/id/1001"),
            data_type="xml",
        )
    )
    assert classic.get_peripheral_type(1001, "xml")


@responses.activate
def test_update_peripheral_type_id(classic):
    """
    Ensures that update_peripheral_type completes successfully when run with
    required params
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/peripheraltypes/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_peripheral_type(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_delete_peripheral_type(classic):
    """
    Ensures that delete_peripheral_type completes successfully when run with
    required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/peripheraltypes/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_peripheral_type(1001) == EXPECTED_XML


"""
/policies
"""


@responses.activate
def test_get_policies_json(classic):
    """
    Ensures that get_policies returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/policies")))
    assert classic.get_policies() == EXPECTED_JSON


@responses.activate
def test_get_policies_category_xml(classic):
    """
    Ensures that get_policies returns a XML str when passing
    "xml" as the data_type and category set to None
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/policies/category/None"), data_type="xml"
        )
    )
    assert classic.get_policies(category="None", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_policies_createdby(classic):
    """
    Ensures that get_policies returns JSON when used with createdby set to
    jss
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/policies/createdBy/jss"))
    )
    assert classic.get_policies(createdby="jss") == EXPECTED_JSON


def test_get_policies_invalid_createdby(classic):
    """
    Ensures that get_policies raises ValueError when used with createdby set
    to an invalid value
    """
    with pytest.raises(ValueError):
        classic.get_policies(createdby="invalid")


@responses.activate
def test_get_policy_id_json(classic):
    """
    Ensures that get_policy returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/policies/id/1001")))
    assert classic.get_policy(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_policy_name_xml(classic):
    """
    Ensures that get_policy returns XML when passing "xml" as the data_type
    and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/policies/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_policy(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_policy_id_subset(classic):
    """
    Ensures that get_policy returns data when used with id as an identifier
    and one subset options
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/policies/id/1001/subset/General"))
    )
    assert classic.get_policy(1001, subsets=["General"]) == EXPECTED_JSON


@responses.activate
def test_get_policy_id_subsets(classic):
    """
    Ensures that get_policy returns data when used with id as an identifier
    and multiple subset options
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/policies/id/1001/subset/General%26Scope%26"
                "SelfService%26PackageConfiguration%26Scripts%26Printers%26DockItems%26"
                "AccountMaintenance%26Reboot%26Maintenance%26FilesProcesses%26"
                "UserInteraction%26DiskEncryption"
            ),
        )
    )
    assert (
        classic.get_policy(
            1001,
            subsets=[
                "General",
                "Scope",
                "SelfService",
                "PackageConfiguration",
                "Scripts",
                "Printers",
                "DockItems",
                "AccountMaintenance",
                "Reboot",
                "Maintenance",
                "FilesProcesses",
                "UserInteraction",
                "DiskEncryption",
            ],
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_policy_id(classic):
    """
    Ensures that create_policy returns data when updating a policy with ID
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/policies/id/0"), data_type="xml")
    )
    assert classic.create_policy(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_policy_id(classic):
    """
    Ensures that update_policy returns data when updating a policy with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/policies/id/1001"), data_type="xml"
        )
    )
    assert classic.update_policy(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_policy_name(classic):
    """
    Ensures that update_policy returns data when updating a policy with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/policies/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_policy(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_policy_id(classic):
    """
    Ensures that delete_policy returns data when deleting a policy by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/policies/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_policy(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_policy_name(classic):
    """
    Ensures that delete_policy returns data when deleting a policy by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/policies/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_policy(name="testname") == EXPECTED_XML


"""
/printers
"""


@responses.activate
def test_get_printers_json(classic):
    """
    Ensures that printers returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/printers")))
    assert classic.get_printers() == EXPECTED_JSON


@responses.activate
def test_get_printers_xml(classic):
    """
    Ensures that printers returns a XML str when passing "xml" as the
    data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/printers"), data_type="xml")
    )
    assert classic.get_printers(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_printer_id_json(classic):
    """
    Ensures that get_printer returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/printers/id/1001")))
    assert classic.get_printer(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_printer_name_xml(classic):
    """
    Ensures that get_printer returns XML when passing "xml" as the data_type
    and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/printers/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_printer(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_printer_id(classic):
    """
    Ensures that create_printer returns data when creating a printer with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/printers/id/0"), data_type="xml")
    )
    assert classic.create_printer(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_printer_id(classic):
    """
    Ensures that update_printer returns data when creating a printer with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/printers/id/1001"), data_type="xml"
        )
    )
    assert classic.update_printer(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_printer_name(classic):
    """
    Ensures that update_printer returns data when updating a printer with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/printers/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_printer(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_printer_id(classic):
    """
    Ensures that delete_printer returns data when deleting a printer by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/printers/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_printer(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_printer_name(classic):
    """
    Ensures that delete_printer returns data when deleting a printer by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/printers/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_printer(name="testname") == EXPECTED_XML


"""
/removablemacaddresses
"""


@responses.activate
def test_get_removable_mac_addresses_json(classic):
    """
    Ensures that get_removable_mac_addresses returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/removablemacaddresses"))
    )
    assert classic.get_removable_mac_addresses() == EXPECTED_JSON


@responses.activate
def test_get_removable_mac_addresses_xml(classic):
    """
    Ensures that get_removable_mac_addresses returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/removablemacaddresses"), data_type="xml"
        )
    )
    assert classic.get_removable_mac_addresses(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_removable_mac_address_id_json(classic):
    """
    Ensures that get_removable_mac_address returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/removablemacaddresses/id/1001"))
    )
    assert classic.get_removable_mac_address(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_removable_mac_address_name_xml(classic):
    """
    Ensures that get_removable_mac_address returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/removablemacaddresses/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_removable_mac_address(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_removable_mac_address_id(classic):
    """
    Ensures that create_removable_mac_address returns data when creating
    a removable MAC address with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/removablemacaddresses/id/0"), data_type="xml"
        )
    )
    assert classic.create_removable_mac_address(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_removable_mac_address_id(classic):
    """
    Ensures that update_removable_mac_address returns data when creating
    a removable MAC address with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/removablemacaddresses/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_removable_mac_address(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_removable_mac_address_name(classic):
    """
    Ensures that update_removable_mac_address returns data when updating
    a removable MAC address with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/removablemacaddresses/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_removable_mac_address(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_removable_mac_address_id(classic):
    """
    Ensures that delete_removable_mac_address returns data when deleting a
    removable MAC address by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/removablemacaddresses/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_removable_mac_address(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_removable_mac_address_name(classic):
    """
    Ensures that delete_removable_mac_address returns data when deleting a
    removable MAC address by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/removablemacaddresses/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_removable_mac_address(name="testname") == EXPECTED_XML


"""
/restrictedsoftware
"""


@responses.activate
def test_get_restricted_software_all_json(classic):
    """
    Ensures that restricted software returns a JSON dict when passing "json"
    as the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/restrictedsoftware")))
    assert classic.get_restricted_software_all() == EXPECTED_JSON


@responses.activate
def test_get_restricted_software_all_xml(classic):
    """
    Ensures that restricted software returns a XML str when passing "xml" as
    the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/restrictedsoftware"), data_type="xml"
        )
    )
    assert classic.get_restricted_software_all(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_restricted_software_id_json(classic):
    """
    Ensures that get_restricted_software returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/restrictedsoftware/id/1001"))
    )
    assert classic.get_restricted_software(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_restricted_software_name_xml(classic):
    """
    Ensures that get_restricted_software returns XML when passing "xml" as the
    data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/restrictedsoftware/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_restricted_software(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_restricted_software_id(classic):
    """
    Ensures that create_restricted_software returns data when creating a
    restricted software with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/restrictedsoftware/id/0"), data_type="xml"
        )
    )
    assert classic.create_restricted_software(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_restricted_software_id(classic):
    """
    Ensures that update_restricted_software returns data when creating a
    restricted software with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/restrictedsoftware/id/1001"), data_type="xml"
        )
    )
    assert classic.update_restricted_software(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_restricted_software_name(classic):
    """
    Ensures that update_restricted_software returns data when updating a
    restricted software with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/restrictedsoftware/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_restricted_software(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_restricted_software_id(classic):
    """
    Ensures that delete_restricted_software returns data when deleting a
    restricted software by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/restrictedsoftware/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_restricted_software(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_restricted_software_name(classic):
    """
    Ensures that delete_restricted_software returns data when deleting a
    restricted software by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/restrictedsoftware/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_restricted_software(name="testname") == EXPECTED_XML


"""
/savedsearches
"""

# Deprecated - use advancedcomputersearches, advancedmobiledevicesearches
# and advancedusersearches

"""
/scripts
"""


@responses.activate
def test_get_scripts_json(classic):
    """
    Ensures that get_scripts returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/scripts")))
    assert classic.get_scripts() == EXPECTED_JSON


@responses.activate
def test_get_scripts_xml(classic):
    """
    Ensures that get_scripts returns a XML str when passing "xml" as the
    data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/scripts"), data_type="xml")
    )
    assert classic.get_scripts(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_script_id_json(classic):
    """
    Ensures that get_script returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/scripts/id/1001")))
    assert classic.get_script(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_script_name_xml(classic):
    """
    Ensures that get_script returns XML when passing "xml" as the data_type
    and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/scripts/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_script(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_script_id(classic):
    """
    Ensures that create_script returns data when creating a script with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/scripts/id/0"), data_type="xml")
    )
    assert classic.create_script(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_script_id(classic):
    """
    Ensures that update_script returns data when creating a script with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/scripts/id/1001"), data_type="xml"
        )
    )
    assert classic.update_script(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_script_name(classic):
    """
    Ensures that update_script returns data when updating a script with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/scripts/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_script(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_script_id(classic):
    """
    Ensures that delete_script returns data when deleting a script by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/scripts/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_script(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_script_name(classic):
    """
    Ensures that delete_script returns data when deleting a script by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/scripts/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_script(name="testname") == EXPECTED_XML


"""
/sites
"""


@responses.activate
def test_get_sites_json(classic):
    """
    Ensures that get_sites returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/sites")))
    assert classic.get_sites() == EXPECTED_JSON


@responses.activate
def test_get_sites_xml(classic):
    """
    Ensures that get_sites returns a XML str when passing "xml" as the
    data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/sites"), data_type="xml")
    )
    assert classic.get_sites(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_site_id_json(classic):
    """
    Ensures that get_site returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/sites/id/1001")))
    assert classic.get_site(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_site_name_xml(classic):
    """
    Ensures that get_site returns XML when passing "xml" as the data_type and
    using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/sites/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_site(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_site_id(classic):
    """
    Ensures that create_site returns data when creating a site with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/sites/id/0"), data_type="xml")
    )
    assert classic.create_site(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_site_id(classic):
    """
    Ensures that update_site returns data when creating a site with id
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/sites/id/1001"), data_type="xml")
    )
    assert classic.update_site(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_site_name(classic):
    """
    Ensures that update_site returns data when updating a site with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/sites/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_site(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_site_id(classic):
    """
    Ensures that delete_site returns data when deleting a site by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/sites/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_site(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_site_name(classic):
    """
    Ensures that delete_site returns data when deleting a site by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/sites/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_site(name="testname") == EXPECTED_XML


"""
/smtpserver
"""


@responses.activate
def test_get_smtp_server_json(classic):
    """
    Ensures that get_smtp_server returns JSON when run without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/smtpserver")))
    assert classic.get_smtp_server() == EXPECTED_JSON


@responses.activate
def test_get_smtp_server_xml(classic):
    """
    Ensures that get_smtp_server returns XML when run with data_type set to
    "xml"
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/smtpserver"), data_type="xml")
    )
    assert classic.get_smtp_server("xml") == EXPECTED_XML


@responses.activate
def test_update_smtp_server(classic):
    """
    Ensures that update_smtp_server completes successfully when run with
    required params
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/smtpserver"), data_type="xml")
    )
    assert classic.update_smtp_server(EXPECTED_XML) == EXPECTED_XML


"""
/softwareupdateservers
"""


@responses.activate
def test_get_software_update_servers_json(classic):
    """
    Ensures that get_software_update_servers returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/softwareupdateservers"))
    )
    assert classic.get_software_update_servers() == EXPECTED_JSON


@responses.activate
def test_get_software_update_servers_xml(classic):
    """
    Ensures that get_software_update_servers returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/softwareupdateservers"), data_type="xml"
        )
    )
    assert classic.get_software_update_servers(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_software_update_server_id_json(classic):
    """
    Ensures that get_software_update_server returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/softwareupdateservers/id/1001"))
    )
    assert classic.get_software_update_server(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_software_update_server_name_xml(classic):
    """
    Ensures that get_software_update_server returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/softwareupdateservers/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_software_update_server(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_software_update_server_id(classic):
    """
    Ensures that create_software_update_server returns data when creating
    a software update server with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/softwareupdateservers/id/0"), data_type="xml"
        )
    )
    assert classic.create_software_update_server(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_software_update_server_id(classic):
    """
    Ensures that update_software_update_server returns data when creating
    a software update server with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/softwareupdateservers/id/1001"),
            data_type="xml",
        )
    )
    assert classic.update_software_update_server(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_software_update_server_name(classic):
    """
    Ensures that update_software_update_server returns data when updating
    a software update server with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/softwareupdateservers/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_software_update_server(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_software_update_server_id(classic):
    """
    Ensures that delete_software_update_server returns data when deleting a
    software update server by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/softwareupdateservers/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_software_update_server(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_software_update_server_name(classic):
    """
    Ensures that delete_software_update_server returns data when deleting a
    software update server by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/softwareupdateservers/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_software_update_server(name="testname") == EXPECTED_XML


"""
/userextensionattributes
"""


@responses.activate
def test_get_user_extension_attributes_json(classic):
    """
    Ensures that get_user_extension_attributes returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/userextensionattributes"))
    )
    assert classic.get_user_extension_attributes() == EXPECTED_JSON


@responses.activate
def test_get_user_extension_attributes_xml(classic):
    """
    Ensures that get_user_extension_attributes returns a XML str when passing
    "xml" as the data_type param
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/userextensionattributes"), data_type="xml"
        )
    )
    assert classic.get_user_extension_attributes(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_user_extension_attribute_id_json(classic):
    """
    Ensures that get_user_extension_attribute returns a JSON dict when passing
    "json" as the data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/userextensionattributes/id/1001"))
    )
    assert classic.get_user_extension_attribute(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_user_extension_attribute_name_xml(classic):
    """
    Ensures that get_user_extension_attribute returns XML when passing "xml"
    as the data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/userextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.get_user_extension_attribute(name="testname", data_type="xml")
        == EXPECTED_XML
    )


@responses.activate
def test_create_user_extension_attribute_id(classic):
    """
    Ensures that create_user_extension_attribute returns data when creating
    a user extension attribute with id
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/JSSResource/userextensionattributes/id/0"),
            data_type="xml",
        )
    )
    assert classic.create_user_extension_attribute(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_user_extension_attribute_id(classic):
    """
    Ensures that update_user_extension_attribute returns data when creating
    a user extension attribute with id
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/userextensionattributes/id/1001"),
            data_type="xml",
        )
    )
    assert (
        classic.update_user_extension_attribute(EXPECTED_XML, id=1001) == EXPECTED_XML
    )


@responses.activate
def test_update_user_extension_attribute_name(classic):
    """
    Ensures that update_user_extension_attribute returns data when updating
    a user extension attribute with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/userextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert (
        classic.update_user_extension_attribute(EXPECTED_XML, name="testname")
        == EXPECTED_XML
    )


@responses.activate
def test_delete_user_extension_attribute_id(classic):
    """
    Ensures that delete_user_extension_attribute returns data when deleting a
    user extension attribute by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/userextensionattributes/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_user_extension_attribute(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_user_extension_attribute_name(classic):
    """
    Ensures that delete_user_extension_attribute returns data when deleting a
    user extension attribute by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/userextensionattributes/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_user_extension_attribute(name="testname") == EXPECTED_XML


"""
/usergroups
"""


@responses.activate
def test_get_user_groups_json(classic):
    """
    Ensures that get_user_groups returns a JSON dict when passing "json" as
    the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/usergroups")))
    assert classic.get_user_groups() == EXPECTED_JSON


@responses.activate
def test_get_user_groups_xml(classic):
    """
    Ensures that get_user_groups returns a XML str when passing "xml" as the
    data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/usergroups"), data_type="xml")
    )
    assert classic.get_user_groups(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_user_group_id_json(classic):
    """
    Ensures that get_user_group returns a JSON dict when passing "json" as
    the data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/usergroups/id/1001")))
    assert classic.get_user_group(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_user_group_name_xml(classic):
    """
    Ensures that get_user_group returns XML when passing "xml" as the
    data_type and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/usergroups/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_user_group(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_user_group_id(classic):
    """
    Ensures that create_user_group returns data when creating a user group
    with id
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/usergroups/id/0"), data_type="xml"
        )
    )
    assert classic.create_user_group(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_user_group_id(classic):
    """
    Ensures that update_user_group returns data when creating a user group
    with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/usergroups/id/1001"), data_type="xml"
        )
    )
    assert classic.update_user_group(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_user_group_name(classic):
    """
    Ensures that update_user_group returns data when updating a user group
    with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/usergroups/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_user_group(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_user_group_id(classic):
    """
    Ensures that delete_user_group returns data when deleting a user group by
    ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/usergroups/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_user_group(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_user_group_name(classic):
    """
    Ensures that delete_user_group returns data when deleting a user group by
    name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/usergroups/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_user_group(name="testname") == EXPECTED_XML


"""
/users
"""


@responses.activate
def test_get_users_json(classic):
    """
    Ensures that get_users returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/users")))
    assert classic.get_users() == EXPECTED_JSON


@responses.activate
def test_get_users_xml(classic):
    """
    Ensures that get_users returns a XML str when passing "xml" as the
    data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/users"), data_type="xml")
    )
    assert classic.get_users(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_user_id_json(classic):
    """
    Ensures that get_user returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/users/id/1001")))
    assert classic.get_user(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_user_name_xml(classic):
    """
    Ensures that get_user returns XML when passing "xml" as the data_type and
    using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/users/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_user(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_user_email(classic):
    """
    Ensures that get_user works with email as the identifier
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/users/email/test%40email.com"))
    )
    assert classic.get_user(email="test@email.com") == EXPECTED_JSON


@responses.activate
def test_create_user_id(classic):
    """
    Ensures that create_user returns data when creating a user with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/users/id/0"), data_type="xml")
    )
    assert classic.create_user(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_user_id(classic):
    """
    Ensures that update_user returns data when creating a user with id
    """
    responses.add(
        response_builder("PUT", jps_url("/JSSResource/users/id/1001"), data_type="xml")
    )
    assert classic.update_user(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_user_name(classic):
    """
    Ensures that update_user returns data when updating a user with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/users/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_user(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_update_user_email(classic):
    """
    Ensures that update_user works with email as the identifier
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/users/email/test%40email.com"), data_type="xml"
        )
    )
    assert classic.update_user(EXPECTED_XML, email="test@email.com") == EXPECTED_XML


@responses.activate
def test_delete_user_id(classic):
    """
    Ensures that delete_user returns data when deleting a user by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/users/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_user(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_user_name(classic):
    """
    Ensures that delete_user returns data when deleting a user by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/users/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_user(name="testname") == EXPECTED_XML


@responses.activate
def test_delete_user_email(classic):
    """
    Ensures that delete_user works with email as the identifier
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/users/email/test%40email.com"),
            data_type="xml",
        )
    )
    assert classic.delete_user(email="test@email.com") == EXPECTED_XML


"""
/vppaccounts
"""


@responses.activate
def test_get_vpp_accounts_json(classic):
    """
    Ensures that get_vpp_accounts returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/vppaccounts")))
    assert classic.get_vpp_accounts() == EXPECTED_JSON


@responses.activate
def test_get_vpp_accounts_xml(classic):
    """
    Ensures that get_vpp_accounts returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/vppaccounts"), data_type="xml")
    )
    assert classic.get_vpp_accounts("xml") == EXPECTED_XML


@responses.activate
def test_get_vpp_account_id_json(classic):
    """
    Ensures that get_vpp_account returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/vppaccounts/id/1001")))
    assert classic.get_vpp_account(1001) == EXPECTED_JSON


@responses.activate
def test_get_vpp_account_id_xml(classic):
    """
    Ensures that get_vpp_account returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/vppaccounts/id/1001"), data_type="xml"
        )
    )
    assert classic.get_vpp_account(1001, data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_vpp_account(classic):
    """
    Ensures that create_vpp_account completes successfully when
    run without optional params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/vppaccounts/id/0"), data_type="xml"
        )
    )
    assert classic.create_vpp_account(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_vpp_account(classic):
    """
    Ensures that update_vpp_account completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/vppaccounts/id/1001"), data_type="xml"
        )
    )
    assert classic.update_vpp_account(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_delete_vpp_account(classic):
    """
    Ensures that delete_vpp_account completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/vppaccounts/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_vpp_account(1001) == EXPECTED_XML


"""
/vppassignments
"""


@responses.activate
def test_get_vpp_assignments_json(classic):
    """
    Ensures that get_vpp_assignments returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/vppassignments")))
    assert classic.get_vpp_assignments() == EXPECTED_JSON


@responses.activate
def test_get_vpp_assignments_xml(classic):
    """
    Ensures that get_vpp_assignments returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/vppassignments"), data_type="xml")
    )
    assert classic.get_vpp_assignments("xml") == EXPECTED_XML


@responses.activate
def test_get_vpp_assignment_id_json(classic):
    """
    Ensures that get_vpp_assignment returns JSON when used without
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/vppassignments/id/1001"))
    )
    assert classic.get_vpp_assignment(1001) == EXPECTED_JSON


@responses.activate
def test_get_vpp_assignment_id_xml(classic):
    """
    Ensures that get_vpp_assignment returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/vppassignments/id/1001"), data_type="xml"
        )
    )
    assert classic.get_vpp_assignment(1001, data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_vpp_assignment(classic):
    """
    Ensures that create_vpp_assignment completes successfully when
    run without optional params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/vppassignments/id/0"), data_type="xml"
        )
    )
    assert classic.create_vpp_assignment(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_vpp_assignment(classic):
    """
    Ensures that update_vpp_assignment completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/vppassignments/id/1001"), data_type="xml"
        )
    )
    assert classic.update_vpp_assignment(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_delete_vpp_assignment(classic):
    """
    Ensures that delete_vpp_assignment completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/vppassignments/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_vpp_assignment(1001) == EXPECTED_XML


"""
/vppinvitations
"""


@responses.activate
def test_get_vpp_invitations_json(classic):
    """
    Ensures that get_vpp_invitations returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/vppinvitations")))
    assert classic.get_vpp_invitations() == EXPECTED_JSON


@responses.activate
def test_get_vpp_invitations_xml(classic):
    """
    Ensures that get_vpp_invitations returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/vppinvitations"), data_type="xml")
    )
    assert classic.get_vpp_invitations("xml") == EXPECTED_XML


@responses.activate
def test_get_vpp_invitation_id_json(classic):
    """
    Ensures that get_vpp_invitation returns JSON when used without optional
    params
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/vppinvitations/id/1001"))
    )
    assert classic.get_vpp_invitation(1001) == EXPECTED_JSON


@responses.activate
def test_get_vpp_invitation_id_xml(classic):
    """
    Ensures that get_vpp_invitation returns XML when used with data_type
    set to "xml"
    """
    responses.add(
        response_builder(
            "GET", jps_url("/JSSResource/vppinvitations/id/1001"), data_type="xml"
        )
    )
    assert classic.get_vpp_invitation(1001, data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_vpp_invitation_id_subsets(classic):
    """
    Ensures that get_vpp_incitation returns JSON when used with id as the
    identifier and all subsets
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/JSSResource/vppinvitations/id/1001"
                "/subset/General%26Scope%26InvitationUsages"
            ),
        )
    )
    assert (
        classic.get_vpp_invitation(
            1001, subsets=["General", "Scope", "InvitationUsages"]
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_vpp_invitation(classic):
    """
    Ensures that create_vpp_invitation completes successfully when
    run without optional params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/JSSResource/vppinvitations/id/0"), data_type="xml"
        )
    )
    assert classic.create_vpp_invitation(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_vpp_invitation(classic):
    """
    Ensures that update_vpp_invitation completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/vppinvitations/id/1001"), data_type="xml"
        )
    )
    assert classic.update_vpp_invitation(EXPECTED_XML, 1001) == EXPECTED_XML


@responses.activate
def test_delete_vpp_invitation(classic):
    """
    Ensures that delete_vpp_invitation completes successfully when run
    with required params
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/vppinvitations/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_vpp_invitation(1001) == EXPECTED_XML


"""
/webhooks
"""


@responses.activate
def test_get_webhooks_json(classic):
    """
    Ensures that get_webhooks returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/webhooks")))
    assert classic.get_webhooks() == EXPECTED_JSON


@responses.activate
def test_get_webhooks_xml(classic):
    """
    Ensures that get_webhooks returns a XML str when passing "xml" as the
    data_type param
    """
    responses.add(
        response_builder("GET", jps_url("/JSSResource/webhooks"), data_type="xml")
    )
    assert classic.get_webhooks(data_type="xml") == EXPECTED_XML


@responses.activate
def test_get_webhook_id_json(classic):
    """
    Ensures that get_webhook returns a JSON dict when passing "json" as the
    data_type param
    """
    responses.add(response_builder("GET", jps_url("/JSSResource/webhooks/id/1001")))
    assert classic.get_webhook(id=1001) == EXPECTED_JSON


@responses.activate
def test_get_webhook_name_xml(classic):
    """
    Ensures that get_webhook returns XML when passing "xml" as the data_type
    and using name as the identifier
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/JSSResource/webhooks/name/testname"),
            data_type="xml",
        )
    )
    assert classic.get_webhook(name="testname", data_type="xml") == EXPECTED_XML


@responses.activate
def test_create_webhook_id(classic):
    """
    Ensures that create_webhook returns data when creating a webhook with id
    """
    responses.add(
        response_builder("POST", jps_url("/JSSResource/webhooks/id/0"), data_type="xml")
    )
    assert classic.create_webhook(EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_update_webhook_id(classic):
    """
    Ensures that update_webhook returns data when creating a webhook with id
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/JSSResource/webhooks/id/1001"), data_type="xml"
        )
    )
    assert classic.update_webhook(EXPECTED_XML, id=1001) == EXPECTED_XML


@responses.activate
def test_update_webhook_name(classic):
    """
    Ensures that update_webhook returns data when updating a webhook with name
    """
    responses.add(
        response_builder(
            "PUT",
            jps_url("/JSSResource/webhooks/name/testname"),
            data_type="xml",
        )
    )
    assert classic.update_webhook(EXPECTED_XML, name="testname") == EXPECTED_XML


@responses.activate
def test_delete_webhook_id(classic):
    """
    Ensures that delete_webhook returns data when deleting a webhook by ID
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/webhooks/id/1001"),
            data_type="xml",
        )
    )
    assert classic.delete_webhook(id=1001) == EXPECTED_XML


@responses.activate
def test_delete_webhook_name(classic):
    """
    Ensures that delete_webhook returns data when deleting a webhook by name
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/JSSResource/webhooks/name/testname"),
            data_type="xml",
        )
    )
    assert classic.delete_webhook(name="testname") == EXPECTED_XML
