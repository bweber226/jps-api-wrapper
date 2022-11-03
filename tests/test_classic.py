import pytest
from requests.exceptions import HTTPError
import requests
import responses
from requests.auth import AuthBase

from classic import Classic
from request_builder import (
    InvalidDataType,
    MalformedRequest,
    NotFound,
    RequestTimedOut,
)
from utils import (
    NoIdentification,
    MultipleIdentifications,
    InvalidSubset,
    NoParametersOrData,
    ParametersAndData,
    MissingParameters,
    InvalidParameterOptions,
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
    Ensures data is returned when get_acount_group us used with a name
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
    Ensures that delete_account_group returns data when updating an account
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
    Ensures data is returned when get_acount is used with a name
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
    Ensures that delete_account returns data when updating an account by name
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
    Ensures that delete_account returns data when updating an account by id
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
def test_udpate_activation_code(classic):
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
    Ensures that create_advanced_computer_search returns data when updating
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
    Ensures that create_advanced_user_search returns data when updating
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
    Ensures that create_building returns data when updating
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
    Ensures that create_byo_profile returns data when updating
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
    Ensures that create_category returns data when updating
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
    Ensures that create_class returns data when updating
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
def test_command_flush_params(classic):
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
    assert classic.command_flush("computers", 1001, "Pending") == EXPECTED_XML


@responses.activate
def test_command_flush_data(classic):
    """
    Ensures that command flush completes successfully when used with data and
    not parameters.
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/JSSResource/commandflush"), data_type="xml"
        )
    )
    assert classic.command_flush(data=EXPECTED_XML) == EXPECTED_XML


@responses.activate
def test_command_flush_no_parameters_or_data(classic):
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
        classic.command_flush()


@responses.activate
def test_command_flush_parameters_and_data(classic):
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
        classic.command_flush("computers", 1001, "Pending", EXPECTED_XML)


@responses.activate
def test_command_flush_missing_parameters(classic):
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
        classic.command_flush(idtype="computers", status="Pending")


@responses.activate
def test_command_flush_invalid_parameter_options(classic):
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
        classic.command_flush("commuters", 1001, "Pending")


"""
/computerapplications
"""


@responses.activate
def test_get_computer_application_json(classic):
    """
    Ensures get_computer_applcation returns data when given only the
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

"""
/computercheckin
"""

"""
/computercommands
"""

"""
/computerextensionattributes
"""

"""
/computergroups
"""

"""
/computerhardwaresoftwarereports
"""

"""
/computerhistory
"""

"""
/computerinventorycollection
"""

"""
/computerinvitations
"""

"""
/computermanagement
"""

"""
/computerreports
"""

"""
/computers
"""

"""
/departments
"""

"""
/directorybindings
"""

"""
/diskencryptionconfigurations
"""

"""
/distributionpoints
"""

"""
/dockitems
"""

"""
/ebooks
"""

"""
/fileuploads
"""

"""
/gsxconnection
"""

"""
/healthcaraelistener
"""

"""
/healthcarelistenerrule
"""

"""
/ibeacons
"""

"""
/infrastructuremanager
"""

"""
/jssuser
"""

"""
/jsonwebtokenconfigurations
"""

"""
/ldapservers
"""

"""
/licensedsoftware
"""

"""
/logflush
"""

"""
/macapplications
"""

"""
/managedpreferenceprofiles
"""

"""
/mobiledeviceapplications
"""

"""
/mobiledevicecommands
"""

"""
/mobiledeviceconfigurationprofiles
"""

"""
/mobiledeviceenrollmentprofiles
"""

"""
/mobiledeviceextensionattributes
"""

"""
/mobiledevicegroups
"""

"""
/mobiledevicehistory
"""

"""
/mobiledeviceinvitations
"""

"""
/mobiledeviceprovisioningprofiles
"""

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

"""
/osxconfigurationprofiles
"""

"""
/packages
"""

"""
/patchavailabletitles
"""

"""
/patches
"""

"""
/patchexternalsources
"""

"""
/patchinternalsources
"""

"""
/patchpolicies
"""

"""
/patchreports
"""

"""
/patchsoftwaretitles
"""

"""
/peripherals
"""

"""
/peripheraltypes
"""

"""
/policies
"""

"""
/printers
"""

"""
/removablemacaddresses
"""

"""
/restrictedsoftware
"""

"""
/savedsearches
"""

"""
/scripts
"""

"""
/sites
"""

"""
/smtpserver
"""

"""
/softwareupdateservers
"""

"""
/userextensionattributes
"""

"""
/usergroups
"""

"""
/users
"""

"""
/vppaccounts
"""

"""
/vppassignments
"""

"""
/vppinvitations
"""

"""
/webhooks
"""
