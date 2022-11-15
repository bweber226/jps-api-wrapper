import pytest
import requests
import responses
from requests.auth import AuthBase

from pro import Pro
from request_builder import (
    InvalidDataType,

)


MOCK_AUTH_STRING = "This is a MockAuth"
EXPECTED_AUTH = {"Authorization": MOCK_AUTH_STRING}
EXAMPLE_JSS = "https://jss.example.com"
EXPECTED_JSON = {"test": "test_get_request"}
EXPECTED_XML = "<test />"


class ProTest(Pro):
    def __init__(self, base_url: str, auth: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth = auth


class MockAuth(AuthBase):
    def __call__(self, r):
        r.headers["Authorization"] = MOCK_AUTH_STRING
        return r


@pytest.fixture
def pro():
    return ProTest(EXAMPLE_JSS, MockAuth())


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
advanced-mobile-device-searches
"""


@responses.activate
def test_get_advanced_mobile_device_searches(pro):
    """
    Ensures that get_advanced_mobile_device_searches returns data when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/advanced-mobile-device-searches"))
    )
    assert pro.get_advanced_mobile_device_searches() == EXPECTED_JSON


@responses.activate
def test_get_advanced_mobile_device_search_criteria_choices(pro):
    """
    Ensures that get_advanced_mobile_device_search_criteria_choices returns
    data when used with the required criteria
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/api/v1/advanced-mobile-device-searches/choices"
                "?criteria=Managed&site=-1&contains=None"
            ),
        )
    )
    assert (
        pro.get_advanced_mobile_device_search_criteria_choices("Managed")
        == EXPECTED_JSON
    )


@responses.activate
def test_get_advanced_mobile_device_search_criteria_choices_optional(pro):
    """
    Ensures that get_advanced_mobile_device_search_criteria_choices returns
    data when used with the required criteria
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/api/v1/advanced-mobile-device-searches/choices"
                "?criteria=Managed&site=1&contains=Unmanaged"
            ),
        )
    )
    assert (
        pro.get_advanced_mobile_device_search_criteria_choices(
            "Managed", 1, "Unmanaged"
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_advanced_mobile_device_search(pro):
    """
    Ensures that get_advanced_mobile_device_search returns data when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/advanced-mobile-device-searches/1001"))
    )
    assert pro.get_advanced_mobile_device_search(1001) == EXPECTED_JSON


@responses.activate
def test_create_advanced_mobile_device_search(pro):
    """
    Ensures that create_advanced_mobile_device_search completes successfully
    when used with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/advanced-mobile-device-searches"))
    )
    assert pro.create_advanced_mobile_device_search(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_delete_advanced_mobile_device_search(pro):
    """
    Ensures that delete_advanced_mobile_device_search completes successfully
    when run with id as the identifier
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/advanced-mobile-device-searches/1001")
        )
    )
    assert (
        pro.delete_advanced_mobile_device_search(1001)
        == "Advanced mobile device search 1001 successfully deleted."
    )


@responses.activate
def test_delete_advanced_mobile_device_search_multiple(pro):
    """
    Ensures that delete_advanced_mobile_device_search completes successfully
    when run with ids
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/advanced-mobile-device-searches/delete-multiple")
        )
    )
    assert (
        pro.delete_advanced_mobile_device_search(ids=[1001, 1002])
        == "Advanced mobile device search(es) 1001, 1002 successfully deleted."
    )


def test_delete_advanced_mobile_search_id_typerror(pro):
    """
    Ensures that delete_advanced_mobile_device_search raises TypeError when
    id is not an int or str
    """
    with pytest.raises(TypeError):
        pro.delete_advanced_mobile_device_search([1001, 1002])


def test_delete_advanced_mobile_search_ids_typerror(pro):
    """
    Ensures that delete_advanced_mobile_device_search raises TypeError when
    ids is not a list
    """
    with pytest.raises(TypeError):
        pro.delete_advanced_mobile_device_search(ids=1001)


"""
advanced-user-content-searches
"""


@responses.activate
def test_get_advanced_user_content_searches(pro):
    """
    Ensures that get_advanced_user_content_searches returns JSON when run
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/advanced-user-content-searches"))
    )
    assert pro.get_advanced_user_content_searches() == EXPECTED_JSON


@responses.activate
def test_get_advanced_user_content_search(pro):
    """
    Ensures that get_advanced_user_content_search returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/advanced-user-content-searches/1001"))
    )
    assert pro.get_advanced_user_content_search(1001) == EXPECTED_JSON


@responses.activate
def test_create_advanced_user_content_search(pro):
    """
    Ensures that create_advanced_user_content_search completes successfully
    when used with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/advanced-user-content-searches"))
    )
    assert pro.create_advanced_user_content_search(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_advanced_user_content_search(pro):
    """
    Ensures that update_advanced_user_content_search completes successfully
    when used with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/advanced-user-content-searches/1001"))
    )
    assert pro.update_advanced_user_content_search(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_advanced_user_content_search(pro):
    """
    Ensures that delete_advanced_user_content_search completes successfully
    when used with required params
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/advanced-user-content-searches/1001")
        )
    )
    assert (
        pro.delete_advanced_user_content_search(1001)
        == "Advanced user content search 1001 successfully deleted."
    )


"""
api-authentication
"""


@responses.activate
def test_get_api_authentication(pro):
    """
    Ensures that get_api_authentication returns JSON data when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/auth")))
    assert pro.get_api_authentication() == EXPECTED_JSON


"""
app-dynamics-configuration-preview
"""

"""
app-request-preview
"""

"""
app-store-country-codes-preview
"""

"""
buildings
"""

"""
cache-settings
"""

"""
categories
"""

"""
certificate-authority
"""

"""
classic-ldap
"""

"""
client-check-in
"""

"""
cloud-azure
"""

"""
cloud-idp
"""

"""
cloud-ldap
"""

"""
computer_groups
"""

"""
computer-inventory
"""

"""
computer-inventory-collection-settings
"""

"""
computer-prestages
"""

"""
computers-preview
"""

"""
conditional-access
"""

"""
csa
"""

"""
departments
"""

"""
device-communication-settings
"""

"""
device-enrollments
"""

"""
device-enrollments-devices
"""

"""
ebooks
"""

"""
engage
"""

"""
enrollment
"""

"""
enrollment-customization
"""

"""
enrollment-customization-preview
"""

"""
icon
"""

"""
inventory-information
"""

"""
inventory-preload
"""

"""
jamf-connect
"""

"""
jamf-management-framework
"""

"""
jamf-package
"""

"""
jamf-pro-information
"""

"""
jamf-pro-initialization
"""

"""
jamf-pro-initialization-preview
"""

"""
jamf-pro-notifications
"""

"""
jamf-pro-notifications-preview
"""

"""
jamf-pro-server-url-preview
"""

"""
jamf-pro-user-account-settings
"""

"""
jamf-pro-user-account-settings-preview
"""

"""
jamf-pro-version
"""

"""
jamf-protect
"""

"""
ldap
"""

"""
locales-preview
"""

"""
macos-managed-software-updates
"""

"""
mdm
"""

"""
mobile-device-enrollment-profile
"""

"""
mobile-device-extension-attributes-preview
"""

"""
mobile-device-groups-preview
"""

"""
mobile-device-prestages
"""

"""
mobile-devices
"""

"""
parent-app-preview
"""

"""
patch-policies-preview
"""

"""
patch-policy-logs-preview
"""

"""
patches
"""

"""
patches-preview
"""

"""
policies-preview
"""

"""
re-enrollment-preview
"""

"""
remote-administration
"""

"""
scripts
"""

"""
self-service
"""

"""
self-service-branding-ios
"""

"""
self-service-branding-macos
"""

"""
self-service-branding-preview
"""

"""
sites
"""

"""
sites-preview
"""

"""
smart-computer-groups-preview
"""

"""
smart-mobile-device-groups-preview
"""

"""
smart-user-groups-preview
"""

"""
sso-certificate
"""

"""
sso-certificate-preview
"""

"""
sso-settings
"""

"""
startup-status
"""

"""
static-user-groups-preview
"""

"""
supervision-identities-preview
"""

"""
teacher-app
"""

"""
team-viewer-remote-administration
"""

"""
time-zones-preview
"""

"""
tomcat-zones-preview
"""

"""
user-session-preview
"""

"""
venafi-preview
"""

"""
volume-purchasing-locations
"""

"""
volume-purchasing-subscriptions
"""

"""
vpp-admin-accounts-preview
"""

"""
vpp-subscriptions-preview
"""
