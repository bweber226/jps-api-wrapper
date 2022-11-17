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
                "?criteria=Managed&site=-1"
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
def test_update_advanced_movile_device(pro):
    """
    Ensures that update_advanced_mobile_device_search completes successfully
    when used with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/advanced-mobile-device-searches/1001"))
    )
    assert (
        pro.update_advanced_mobile_device_search(EXPECTED_JSON, 1001) == EXPECTED_JSON
    )


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


@responses.activate
def test_get_app_dynamics_configuration(pro):
    """
    Ensures that get_app_dynamics_configuration returns JSON data when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/app-dynamics/script-configuration"))
    )
    assert pro.get_app_dynamics_configuration() == EXPECTED_JSON


"""
app-request-preview
"""


@responses.activate
def test_get_app_request_settings(pro):
    """
    Ensures that get_app_request_settings returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/app-request/settings")))
    assert pro.get_app_request_settings() == EXPECTED_JSON


@responses.activate
def test_get_app_request_form_input_fields(pro):
    """
    Ensures that get_app_request_form_input_fields returns JSON when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/app-request/form-input-fields"))
    )
    assert pro.get_app_request_form_input_fields() == EXPECTED_JSON


@responses.activate
def test_get_app_request_form_input_field(pro):
    """
    Ensures that get_app_request_form_input_field returns JSON when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/app-request/form-input-fields/1001"))
    )
    assert pro.get_app_request_form_input_field(1001) == EXPECTED_JSON


@responses.activate
def test_create_app_request_form_input_field(pro):
    """
    Ensures that create_app_request_form_input_field completes successfully
    when used with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/app-request/form-input-fields"))
    )
    assert pro.create_app_request_form_input_field(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_app_request_settings(pro):
    """
    Ensures that update_app_request_settings completes successfully when run
    with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/app-request/settings")))
    assert pro.update_app_request_settings(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_app_request_form_input_field(pro):
    """
    Ensures that update_app_request_form_input_field completes successfully
    when run with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/app-request/form-input-fields/1001"))
    )
    assert pro.update_app_request_form_input_field(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_replace_app_request_form_input_fields(pro):
    """
    Ensures that replace_app_request_form_input_fields completes successfully
    when run with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/app-request/form-input-fields"))
    )
    assert pro.replace_app_request_form_input_fields(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_delete_app_request_form_input_field(pro):
    """
    Ensures that delete_app_request_form_input_field completes successfully
    when run with required params
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/app-request/form-input-fields/1001")
        )
    )
    assert (
        pro.delete_app_request_form_input_field(1001)
        == "App request form input field 1001 successfully deleted."
    )


"""
app-store-country-codes-preview
"""


@responses.activate
def test_get_app_store_country_codes(pro):
    """
    Ensures that get_app_store_country_codes completes successfully when run
    with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/app-store-country-codes")))
    assert pro.get_app_store_country_codes() == EXPECTED_JSON


"""
buildings
"""


@responses.activate
def test_get_buildings(pro):
    """
    Ensures that get_buildings returns JSON when run without optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/buildings")))
    assert pro.get_buildings() == EXPECTED_JSON


@responses.activate
def test_get_buildings_all_params(pro):
    """
    Ensures that get_buildings returns JSON when run with all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/buildings")))
    assert (
        pro.get_buildings(
            page=0,
            page_size=100,
            sort=["id:asc", "name:asc"],
            filter='filter=city=="Chicago" and name=="build"',
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_building(pro):
    """
    Ensures that get_building returns JSON when run with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/buildings/1001")))
    assert pro.get_building(1001) == EXPECTED_JSON


@responses.activate
def test_get_building_history(pro):
    """
    Ensures that get_building_history returns JSON when run with required
    params and all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/buildings/1001/history")))
    assert (
        pro.get_building_history(
            1001,
            page=0,
            page_size=100,
            sort=["date:desc"],
            filter="username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_building_export(pro):
    """
    Ensures that get_building_export returns a CSV formatted str when
    used without optional params
    """
    responses.add("POST", jps_url("/api/v1/buildings/export"), status=200)
    assert pro.get_building_export() == ""


@responses.activate
def test_get_building_export_params(pro):
    """
    Ensures that get_building_export returns a CSV formatted str when
    used with all optional params
    """
    responses.add("POST", jps_url("/api/v1/buildings/export"), status=200)
    assert (
        pro.get_building_export(
            ["id", "name"],
            ["identification", "buildingName"],
            0,
            100,
            ["id:desc"],
            "name=='example",
        )
        == ""
    )


@responses.activate
def test_get_building_history_export(pro):
    """
    Ensures that get_building_history_export returns a str when used without
    optional params
    """
    responses.add("POST", jps_url("/api/v1/buildings/1001/history/export"), status=200)
    assert pro.get_building_history_export(1001) == ""


@responses.activate
def test_get_building_history_export_params(pro):
    """
    Ensures that get_building_history_export returns a  str when used with all
    optional params
    """
    responses.add("POST", jps_url("/api/v1/buildings/1001/history/export"), status=200)
    assert (
        pro.get_building_history_export(
            1001,
            ["id", "username"],
            ["identification", "name"],
            0,
            100,
            ["id:desc", "date:asc"],
            "username=='example'",
        )
        == ""
    )


@responses.activate
def test_create_building(pro):
    """
    Ensures that create_building completes successfully when used with required
    params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/buildings")))
    assert pro.create_building(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_building_history_note(pro):
    """
    Ensures that create_building_history_note completes successfully when used
    with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/buildings/1001/history")))
    assert pro.create_building_history_note(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_building(pro):
    """
    Ensures that update_building completes successfully when used with required
    params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/buildings/1001")))
    assert pro.update_building(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_building_id(pro):
    """
    Ensures that delete_building completes successfully when used with ID
    """
    responses.add(response_builder("DELETE", jps_url("/api/v1/buildings/1001")))
    assert pro.delete_building(1001) == "Building 1001 successfully deleted."


@responses.activate
def test_delete_building_ids(pro):
    """
    Ensures that delete_building completes successfully when used with IDs
    """
    responses.add("POST", jps_url("/api/v1/buildings/delete-multiple"))
    assert (
        pro.delete_building(ids=[1001, 1002])
        == "Building(s) 1001, 1002 successfully deleted."
    )


def test_delete_building_id_list(pro):
    """
    Ensures that delete_building raises TypeError when the value that is not
    a str or int is passed as id
    """
    with pytest.raises(TypeError):
        pro.delete_building(id=[1001])


def test_delete_building_ids_str(pro):
    """
    Ensures that delete_building raises TypeError when the value that is not
    a list is passed as ids
    """
    with pytest.raises(TypeError):
        pro.delete_building(ids=1001)


"""
cache-settings
"""


@responses.activate
def test_get_cache_settings(pro):
    """
    Ensures that get_cache_settings returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/cache-settings")))
    assert pro.get_cache_settings() == EXPECTED_JSON


@responses.activate
def test_update_cache_settings(pro):
    """
    Ensures that update_cache_settings completes successfully when used with
    required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/cache-settings")))
    assert pro.update_cache_settings(EXPECTED_JSON) == EXPECTED_JSON


"""
categories
"""


@responses.activate
def test_get_categories(pro):
    """
    Ensures taht get_categories returns JSON when used without optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/categories")))
    assert pro.get_categories() == EXPECTED_JSON


@responses.activate
def test_get_categories_optional_params(pro):
    """
    Ensures that get_categories returns JSON when used with all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/categories")))
    assert pro.get_categories(0, 50, ["name:asc"], "name=='*-*'") == EXPECTED_JSON


@responses.activate
def test_get_category(pro):
    responses.add(response_builder("GET", jps_url("/api/v1/categories/1001")))
    assert pro.get_category(1001) == EXPECTED_JSON


@responses.activate
def test_get_category_history(pro):
    responses.add(response_builder("GET", jps_url("/api/v1/categories/1001/history")))
    assert pro.get_category_history(1001) == EXPECTED_JSON


@responses.activate
def test_get_category_history_optional_params(pro):
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/api/v1/categories/1001/history?page=0&page-size=100&"
                "sort=date%3Aasc&sort=id%3Adesc&filter=username%21%3Dadmin+"
                "and+details%3D%3Ddisabled+and+date%3C2019-12-15"
            ),
        )
    )
    assert (
        pro.get_category_history(
            1001,
            0,
            100,
            ["date:asc", "id:desc"],
            "username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_category(pro):
    """
    Ensures that create_category completes successfully when used with required
    params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/categories")))
    assert pro.create_category(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_category_history_note(pro):
    """
    Ensures that create_category_history_note completes successfully when used
    with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/categories/1001/history")))
    assert pro.create_category_history_note(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_category(pro):
    """
    Ensures that update_category completes successfully when used with required
    params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/categories/1001")))
    assert pro.update_category(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_category_id(pro):
    """
    Ensures that delete_category completes successfully when used with id
    params
    """
    responses.add(response_builder("DELETE", jps_url("/api/v1/categories/1001")))
    assert pro.delete_category(1001) == "Category 1001 successfully deleted."


@responses.activate
def test_delete_category_ids(pro):
    """
    Ensures that delete_category completes successfully when used with ids
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/categories/delete-multiple"))
    )
    assert (
        pro.delete_category(ids=[1001, 1002])
        == "Category(s) 1001, 1002 successfully deleted."
    )


"""
certificate-authority
"""


@responses.activate
def test_get_certificate_authority_active_json(pro):
    """
    Ensures that get_certificate_authority_active returns JSON when used
    without optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/pki/certificate-authority/active"))
    )
    assert pro.get_certificate_authority_active() == EXPECTED_JSON


@responses.activate
def test_get_certificate_authority_active_der(pro):
    """
    Ensures that get_certificate_authority_active returns a str when used with
    der set to True
    """
    responses.add(
        "GET", jps_url("/api/v1/pki/certificate-authority/active/der"), status=200
    )
    assert pro.get_certificate_authority_active(der=True) == ""


@responses.activate
def test_get_certificate_authority_active_pem(pro):
    """
    Ensures that get_certificate_authority_active returns a str when used with
    der set to True
    """
    responses.add(
        "GET", jps_url("/api/v1/pki/certificate-authority/active/pem"), status=200
    )
    assert pro.get_certificate_authority_active(pem=True) == ""


@responses.activate
def test_get_certificate_authority_json(pro):
    """
    Ensures that get_certificate_authority returns JSON when used without
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/pki/certificate-authority/1a2b3c4d"))
    )
    assert pro.get_certificate_authority("1a2b3c4d") == EXPECTED_JSON


@responses.activate
def test_get_certificate_authority_der(pro):
    """
    Ensures that get_certificate_authority returns a str when used with der set
    to True
    """
    responses.add(
        "GET", jps_url("/api/v1/pki/certificate-authority/1a2b3c4d/der"), status=200
    )
    assert pro.get_certificate_authority("1a2b3c4d", der=True) == ""


@responses.activate
def test_get_certificate_authority_pem(pro):
    """
    Ensures that get_certificate_authority returns a str when used with pem set
    to True
    """
    responses.add(
        "GET", jps_url("/api/v1/pki/certificate-authority/1a2b3c4d/pem"), status=200
    )
    assert pro.get_certificate_authority("1a2b3c4d", pem=True) == ""


"""
classic-ldap
"""


@responses.activate
def test_get_classic_ldap(pro):
    """
    Ensures that get_classic_ldap returns JSON when run with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/classic-ldap/1001")))
    assert pro.get_classic_ldap(1001) == EXPECTED_JSON


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
