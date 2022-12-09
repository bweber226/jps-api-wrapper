import pytest
import requests
import responses
from requests.auth import AuthBase
from unittest import mock

from pro import Pro
from request_builder import InvalidDataType, NotFound


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


@responses.activate
def test_get_client_check_in(pro):
    """
    Ensures that get_client_check_in returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v3/check-in")))
    assert pro.get_client_check_in() == EXPECTED_JSON


@responses.activate
def test_get_client_check_in_history(pro):
    """
    Ensures that get_client_check_in_history returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v3/check-in/history")))
    assert pro.get_client_check_in_history() == EXPECTED_JSON


@responses.activate
def test_get_client_check_in_history_params(pro):
    """
    Ensures that get_client_check_in_history returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v3/check-in/history")))
    assert pro.get_client_check_in_history(
        0, 100, ["id:asc"], "username!=admin and details==disabled and date<2019-12-15"
    )


@responses.activate
def test_create_client_check_in_history_note(pro):
    """
    Ensures that create_client_check_in_history_note completes successfully
    when used with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v3/check-in/history")))
    assert pro.create_client_check_in_history_note(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_client_check_in(pro):
    """
    Ensures that update_client_check_in completes successfully when used with
    required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v3/check-in")))
    assert pro.update_client_check_in(EXPECTED_JSON) == EXPECTED_JSON


"""
cloud-azure
"""


@responses.activate
def test_get_cloud_azure_default_server_configuration(pro):
    """
    Ensures that get_cloud_azure_default_server_configuration returns JSON when
    used
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/cloud-azure/defaults/server-configuration")
        )
    )
    assert pro.get_cloud_azure_default_server_configuration() == EXPECTED_JSON


@responses.activate
def test_get_cloud_azure_default_mappings(pro):
    """
    Ensures that get_cloud_azure_default_mappings returns JSON when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/cloud-azure/defaults/mappings"))
    )
    assert pro.get_cloud_azure_default_mappings() == EXPECTED_JSON


@responses.activate
def test_get_cloud_azure_identity_provider_configuration(pro):
    """
    Ensures that get_cloud_azure_identity_provider_configuration returns JSON
    when used with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/cloud-azure/1001")))
    assert pro.get_cloud_azure_identity_provider_configuration(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_azure_report(pro):
    """
    Ensures that get_cloud_azure_report completes succesfully when run with
    required pararms
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/azure-ad-migration/reports/1001/download")
        )
    )
    assert pro.get_cloud_azure_report(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_azure_report_status(pro):
    """
    Ensures that get_cloud_azure_report_status completes successfully when
    run with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/azure-ad-migration/reports/1001"))
    )
    assert pro.get_cloud_azure_report_status(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_azure_pending_report(pro):
    """
    Ensures that get_cloud_azure_pending_report completes successfully when
    run with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/azure-ad-migration/reports/pending"))
    )
    assert pro.get_cloud_azure_pending_report() == EXPECTED_JSON


@responses.activate
def test_create_cloud_azure_report(pro):
    """
    Ensures that create_cloud_azure_report completes successfully when run with
    required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/azure-ad-migration/reports"))
    )
    assert pro.create_cloud_azure_report(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_cloud_azure_identity_provider_configuration(pro):
    """
    Ensures that create_cloud_azure_identity_provider_configuration completes
    successfully when run with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/cloud-azure")))
    assert (
        pro.create_cloud_azure_identity_provider_configuration(EXPECTED_JSON)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_cloud_azure_identity_provider_configuration(pro):
    """
    Ensures that update_cloud_azure_identity_provider_configuration completes
    successfully when run with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/cloud-azure/1001")))
    assert (
        pro.update_cloud_azure_identity_provider_configuration(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_delete_cloud_azure_identity_provider_configuration(pro):
    """
    Ensures that delete_cloud_azure_identity_provider_configuration completes
    successfully when run with required params
    """
    responses.add(response_builder("DELETE", jps_url("/api/v1/cloud-azure/1001")))
    assert (
        pro.delete_cloud_azure_identity_provider_configuration(1001)
        == "Cloud identity provider 1001 successfully deleted."
    )


"""
cloud-idp
"""


@responses.activate
def test_get_cloud_idps(pro):
    """
    Ensures that get_cloud_idps returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/cloud-idp")))
    assert pro.get_cloud_idps() == EXPECTED_JSON


@responses.activate
def test_get_cloud_idps_params(pro):
    """
    Ensures that get_cloud_idps returns JSON when used with all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/cloud-idp")))
    assert pro.get_cloud_idps(0, 100, ["id:asc"]) == EXPECTED_JSON


@responses.activate
def test_get_cloud_idp(pro):
    """
    Ensures that get_cloud_idp returns JSON when used with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/cloud-idp/1001")))
    assert pro.get_cloud_idp(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_idp_history(pro):
    """
    Ensures that get_cloud_idp_history returns JSON when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/v1/cloud-idp/1001/history")))
    assert pro.get_cloud_idp_history(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_idp_history_params(pro):
    """
    Ensures that get_cloud_idp_history returns JSON when used with all optional
    params
    """
    responses.add(response_builder("GET", jps_url("/v1/cloud-idp/1001/history")))
    assert pro.get_cloud_idp_history(
        1001,
        0,
        100,
        ["id:asc", "date:asc"],
        "username!=admin and details==disabled and date<2019-12-15",
    )


@responses.activate
def test_get_cloud_idp_export(pro):
    """
    Ensures that get_cloud_idp_history returns a str when used without optional
    params
    """
    responses.add("POST", jps_url("/api/v1/cloud-idp/export"), status=200)
    assert pro.get_cloud_idp_export() == ""


@responses.activate
def test_get_cloud_idp_export_params(pro):
    """
    Ensures that get_cloud_idp_export returns a str when used with all optional
    params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/cloud-idp/export")))
    assert pro.get_cloud_idp_export(
        ["id", "username"],
        ["identifier", "name"],
        0,
        100,
        ["id:desc", "name:asc"],
        'name=="department"',
    )


@responses.activate
def test_create_cloud_idp_history_note(pro):
    """
    Ensures that create_cloud_idp_history_note completes successfully when run
    with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/cloud-idp/1001/history")))
    assert pro.create_cloud_idp_history_note(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_create_cloud_idp_group_test_search(pro):
    """
    Ensures that create_cloud_idp_group_test_search compeltes successfully when
    used with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/cloud-idp/1001/test-group"))
    )
    assert pro.create_cloud_idp_group_test_search(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_create_cloud_idp_user_test_search(pro):
    """
    Ensures that create_cloud_idp_user_test_search compeltes successfully when
    used with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/cloud-idp/1001/test-user")))
    assert pro.create_cloud_idp_user_test_search(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_create_cloud_idp_user_membership_test_search(pro):
    """
    Ensures that create_cloud_idp_user_membership_test_search compeltes
    successfully when used with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/cloud-idp/1001/test-user-membership"))
    )
    assert (
        pro.create_cloud_idp_user_membership_test_search(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


"""
cloud-ldap
"""


@responses.activate
def test_get_cloud_ldap_default_server_configuration(pro):
    """
    Ensures that get_cloud_ldap_defailt_server_configuration returns JSON when
    used with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v2/cloud-ldaps/defaults/google/server-configuration")
        )
    )
    assert pro.get_cloud_ldap_default_server_configuration("google") == EXPECTED_JSON


@responses.activate
def test_get_cloud_ldap_default_mappings(pro):
    """
    Ensures that get_cloud_ldap_default_mappings returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/cloud-ldaps/defaults/google/mappings"))
    )
    assert pro.get_cloud_ldap_default_mappings("google") == EXPECTED_JSON


@responses.activate
def test_get_cloud_ldap_configuration(pro):
    """
    Ensures that get_cloud_ldap_configuration returns JSON when used with
    required params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/cloud-ldaps/1001")))
    assert pro.get_cloud_ldap_configuration(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_ldap_mappings(pro):
    """
    Ensures that get_cloud_ldap_mappings returns JSON when used with required
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/cloud-ldaps/1001/mappings")))
    assert pro.get_cloud_ldap_mappings(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_ldap_connection_status(pro):
    """
    Ensures that get_cloud_ldap_connection_status returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/cloud-ldaps/1001/connection/status"))
    )
    assert pro.get_cloud_ldap_connection_status(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_ldap_bind_connection_pool(pro):
    """
    Ensures that get_cloud_ldap_bind_connection_pool returns JSON when used
    with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/cloud-ldaps/1001/connection/bind"))
    )
    assert pro.get_cloud_ldap_bind_connection_pool(1001) == EXPECTED_JSON


@responses.activate
def test_get_cloud_ldap_search_connection_pool(pro):
    """
    Ensures that get_cloud_ldap_search_connection_pool returns JSON when used
    with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/cloud-ldaps/1001/connection/search"))
    )
    assert pro.get_cloud_ldap_search_connection_pool(1001) == EXPECTED_JSON


@responses.activate
def test_create_cloud_ldap_configuration(pro):
    """
    Ensures that create_cloud_ldap_configuration completes successfully with
    required params
    """
    responses.add(response_builder("POST", jps_url("/api/v2/cloud-ldaps")))
    assert pro.create_cloud_ldap_configuration(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_cloud_ldap_keystore_validation(pro):
    """
    Ensures that create_cloud_ldap_keystore_validation completes successfully
    when used with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/ldap-keystore/verify")))
    assert pro.create_cloud_ldap_keystore_validation(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_cloud_ldap_configuration(pro):
    """
    Ensures that update_cloud_ldap_configuration compeltes successfully when
    used with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v2/cloud-ldaps/1001")))
    assert pro.update_cloud_ldap_configuration(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_cloud_ldap_mappings_configuration(pro):
    """
    Ensures that update_cloud_ldap_mappings_configuration compeltes
    successfully when used with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v2/cloud-ldaps/1001/mappings")))
    assert (
        pro.update_cloud_ldap_mappings_configuration(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_delete_cloud_ldap_configuration(pro):
    """
    Ensures that delete_cloud_ldap_configuration completes successfully when
    used with required params
    """
    responses.add(response_builder("DELETE", jps_url("/api/v2/cloud-ldaps/1001")))
    assert (
        pro.delete_cloud_ldap_configuration(1001)
        == "Cloud LDAP configuration 1001 successfully deleted."
    )


"""
computer_groups
"""


@responses.activate
def test_get_computer_groups(pro):
    """
    Ensures that get_computer_groups returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/computer-groups")))
    assert pro.get_computer_groups() == EXPECTED_JSON


"""
computer-inventory
"""


@responses.activate
def test_get_computer_inventories(pro):
    """
    Ensures that get_computer_inventories returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/computers-inventory")))
    assert pro.get_computer_inventories() == EXPECTED_JSON


@responses.activate
def test_get_computer_inventories_optional(pro):
    """
    Ensures that get_computer_inventories returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/computers-inventory")))
    assert pro.get_computer_inventories(
        ["ALL"], 0, 100, ["udid:desc", "general.name:asc"], 'general.name=="Orchard"'
    )


@responses.activate
def test_get_computer_inventory(pro):
    """
    Ensures that get_computer_inventory returns JSON when used with required
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/computers-inventory/1001")))
    assert pro.get_computer_inventory(1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_inventory_detail(pro):
    """
    Ensures that get_computer_inventory_detail returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/computers-inventory-detail/1001"))
    )
    assert pro.get_computer_inventory_detail(1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_inventory_filevaults(pro):
    """
    Ensures that get_computer_inventory_filevaults returns JSON when used
    without optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/computers-inventory/filevault"))
    )
    assert pro.get_computer_inventory_filevaults() == EXPECTED_JSON


@responses.activate
def test_get_computer_inventory_filevaults_optional_params(pro):
    """
    Ensures that get_computer_inventory_filevaults returns JSON when used with
    all optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/computers-inventory/filevault"))
    )
    assert pro.get_computer_inventory_filevaults(0, 100) == EXPECTED_JSON


@responses.activate
def test_get_computer_inventory_filevault(pro):
    """
    Ensures that get_computer_inventory_filevault returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/computers-inventory/1001/filevault"))
    )
    assert pro.get_computer_inventory_filevault(1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_inventory_recovery_lock_password(pro):
    """
    Ensures that get_computer_inventory_recovery_lock_password returns JSON
    when used with required params
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/api/v1/computers-inventory/1001/view-recovery-lock-password"),
        )
    )
    assert pro.get_computer_inventory_recovery_lock_password(1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_inventory_attachment_404(pro):
    """
    Ensures that get_computer_inventory_attachment_file raises NotFound when
    the file attachmemt is not found
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/api/v1/computers-inventory/1001/attachments/1002"),
            status=404,
        )
    )
    with pytest.raises(NotFound):
        pro.get_computer_inventory_attachment(1001, 1002)


@responses.activate
def test_create_computer_inventory_attachment(pro):
    """
    Ensures that create_computer_inventory_attachment runs successfully when
    uploading a txt file as a computer attachment
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            response_builder(
                "POST", jps_url("/api/v1/computers-inventory/1001/attachments")
            )
        )
        assert (
            pro.create_computer_inventory_attachment("/file.txt", 1001) == EXPECTED_JSON
        )


@responses.activate
def test_update_computer_inventory(pro):
    """
    Ensures that update_computer_inventory runs successfully when used with
    required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/computers-inventory-detail/1001"))
    )
    assert pro.update_computer_inventory(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_computer_inventory(pro):
    """
    Ensures that delete_computer_inventory returns a str success message after
    it successfully compeltes
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v1/computers-inventory/1001"))
    )
    assert pro.delete_computer_inventory(1001) == "Computer 1001 successfully deleted."


@responses.activate
def test_delete_computer_inventory_attachment(pro):
    """
    Ensures that delete_computer_inventory_attachment completes successfully
    when used with required params and returns a success message
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/computers-inventory/1001/attachments/1002")
        )
    )
    assert (
        pro.delete_computer_inventory_attachment(1001, 1002)
        == "Attachment 1002 from computer 1001 successfully deleted."
    )


"""
computer-inventory-collection-settings
"""


@responses.activate
def test_get_computer_inventory_collection_settings(pro):
    """
    Ensures that get_computer_inventory_collection_settings returns JSON
    when used
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/computer-inventory-collection-settings")
        )
    )
    assert pro.get_computer_inventory_collection_settings() == EXPECTED_JSON


@responses.activate
def test_create_computer_inventory_collection_settings(pro):
    """
    Ensures that create_computer_inventory_collection_settings_custom_path
    completes successfully when used with required params
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/api/v1/computer-inventory-collection-settings/custom-path"),
        )
    )
    assert (
        pro.create_computer_inventory_collection_settings_custom_path(EXPECTED_JSON)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_computer_inventory_collection_settings(pro):
    """
    Ensures that update_computer_inventory_collection_settings completes
    successfully when used with required params
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/api/v1/computer-inventory-collection-settings")
        )
    )
    assert (
        pro.update_computer_inventory_collection_settings(EXPECTED_JSON)
        == EXPECTED_JSON
    )


@responses.activate
def test_delete_computer_inventory_collection_settings_custom_path(pro):
    """
    Ensures that delete_computer_inventory_collection_settings_custom_path
    returns a success message when it completes successfully
    """
    responses.add(
        response_builder(
            "DELETE",
            jps_url("/api/v1/computer-inventory-collection-settings/custom-path/1001"),
        )
    )
    assert pro.delete_computer_inventory_collection_settings_custom_path(1001) == (
        "Computer inventory collection settings custom path 1001 "
        "successfully deleted."
    )


"""
computer-prestages
"""


@responses.activate
def test_get_computer_prestages(pro):
    """
    Ensures that get_computer_prestages returns JSON when used with no optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/computer-prestages")))
    assert pro.get_computer_prestages() == EXPECTED_JSON


@responses.activate
def test_get_computer_prestages_optional_params(pro):
    """
    Ensure that get_computer_prestages returns JSON when used with all optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/computer-prestages")))
    assert (
        pro.get_computer_prestages(0, 100, ["id:desc", "enrollmentCustomizationId:asc"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_computer_prestage_scopes(pro):
    """
    Ensures that get_computer_prestage_scopes returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v2/computer-prestages/scope")))
    assert pro.get_computer_prestage_scopes() == EXPECTED_JSON


@responses.activate
def test_get_computer_prestage(pro):
    """
    Ensures that get_computer_prestage returns JSON when used with required
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/computer-prestages/1001")))
    assert pro.get_computer_prestage(1001) == EXPECTED_JSON


@responses.activate
def test_get_computer_prestage_scope(pro):
    """
    Ensures that get_computer_prestage_scope returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/computer-prestages/1001/scope"))
    )
    assert pro.get_computer_prestage_scope(1001) == EXPECTED_JSON


@responses.activate
def test_create_computer_prestage(pro):
    """
    Ensures that create_computer_prestage returns JSON when used with required
    params and completes successfully
    """
    responses.add(response_builder("POST", jps_url("/api/v2/computer-prestages")))
    assert pro.create_computer_prestage(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_computer_prestage_scope(pro):
    """
    Ensures that create_computer_prestage_scope returns JSON when it completes
    successfully with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v2/computer-prestages/1001/scope"))
    )
    assert pro.create_computer_prestage_scope(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_computer_prestage(pro):
    """
    Ensures that update_computer_prestage returns JSON when completed
    successfully with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v2/computer-prestages/1001")))
    assert pro.update_computer_prestage(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_replace_computer_prestage_scope(pro):
    """
    Ensures that replace_computer_prestage_scope returns JSON when compelted
    successfully with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v2/computer-prestages/1001/scope"))
    )
    assert pro.replace_computer_prestage_scope(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_computer_prestage(pro):
    """
    Ensures that delete_computer_prestage returns a success message str when
    used with required params
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v2/computer-prestages/1001"))
    )
    assert (
        pro.delete_computer_prestage(1001)
        == "Computer prestage 1001 successfully deleted."
    )


@responses.activate
def test_delete_computer_prestage_scope(pro):
    """
    Ensures that delete_computer_prestage_scope returns JSON when completed
    successfully with required params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v2/computer-prestages/1001/scope/delete-multiple")
        )
    )
    assert pro.delete_computer_prestage_scope(EXPECTED_JSON, 1001) == EXPECTED_JSON


"""
computers-preview
"""


@responses.activate
def test_get_computers(pro):
    """
    Ensures that get_computers returns JSON when completed with no optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/preview/computers")))
    assert pro.get_computers() == EXPECTED_JSON


@responses.activate
def test_get_computer(pro):
    """
    Ensures that get_computers returns JSON when used with all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/preview/computers")))
    assert pro.get_computers(0, 100, ["id:desc", "name:asc"])


"""
conditional-access
"""


@responses.activate
def test_get_conditional_access_computer(pro):
    """
    Ensures that get_conditional_access_computer returns JSON when used with
    required params
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/api/v1/conditional-access/device-compliance-information/computer/1001"
            ),
        )
    )
    assert pro.get_conditional_access_computer(1001) == EXPECTED_JSON


@responses.activate
def test_get_conditional_access_mobile_device(pro):
    """
    Ensures that get_conditional_access_mobile_device returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "GET",
            jps_url(
                "/api/v1/conditional-access/device-compliance-information/mobile/1001"
            ),
        )
    )
    assert pro.get_conditional_access_mobile_device(1001) == EXPECTED_JSON


"""
csa
"""


@responses.activate
def test_get_csa(pro):
    """
    Ensures that get_csa returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/csa/token")))
    assert pro.get_csa() == EXPECTED_JSON


@responses.activate
def test_create_csa(pro):
    """
    Ensures that create_csa returns JSON when used with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/csa/token")))
    assert pro.create_csa(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_csa(pro):
    """
    Ensures that update_csa returns JSON when used with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/csa/token")))
    assert pro.update_csa(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_delete_csa(pro):
    """
    Ensures that delete_csa returns a success message str when used with
    required params
    """
    responses.add(response_builder("DELETE", jps_url("/api/v1/csa/token")))
    assert pro.delete_csa() == "CSA Token Exchange successfully deleted."


"""
departments
"""


@responses.activate
def test_get_departments(pro):
    """
    Ensures that get_departments returns JSON when used without optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/departments")))
    assert pro.get_departments() == EXPECTED_JSON


@responses.activate
def test_get_departments_optional_params(pro):
    """
    Ensures that get_departments returns JSON when used with optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/departments")))
    assert (
        pro.get_departments(0, 100, ["id:desc", "name:asc"], 'name=="department"')
        == EXPECTED_JSON
    )


@responses.activate
def test_get_department(pro):
    """
    Ensures that get_department returns JSON when used with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/departments/1001")))
    assert pro.get_department(1001) == EXPECTED_JSON


@responses.activate
def test_get_department_history(pro):
    """
    Ensures that get_department_history returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/departments/1001/history")))
    assert pro.get_department_history(1001) == EXPECTED_JSON


@responses.activate
def test_get_department_history_optional_params(pro):
    """
    Ensures that get_department_history returns JSON when used with all
    optional parrams
    """
    responses.add(response_builder("GET", jps_url("/api/v1/departments/1001/history")))
    assert pro.get_department_history(
        1001,
        0,
        100,
        ["date:desc", "name:asc"],
        "username!=admin and details==disabled and date<2019-12-15",
    )


@responses.activate
def test_create_department(pro):
    """
    Ensures that create_department returns JSON when used with required params
    and completes successfully
    """
    responses.add(response_builder("POST", jps_url("/api/v1/departments")))
    assert pro.create_department(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_department_history_note(pro):
    """
    Ensures that create_department_history_note returns JSON when used with
    required params and completes successfully
    """
    responses.add(response_builder("POST", jps_url("/api/v1/departments/1001/history")))
    assert pro.create_department_history_note(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_department(pro):
    """
    Ensures that update_department returns JSON when used with required params
    and completes successfully
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/departments/1001")))
    assert pro.update_department(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_department_id(pro):
    """
    Ensures that delete_department returns a success message str when used
    with id
    """
    responses.add(response_builder("DELETE", jps_url("/api/v1/departments/1001")))
    assert pro.delete_department(1001) == "Department 1001 successfully deleted."


@responses.activate
def test_delete_department_ids(pro):
    """
    Ensures that delete_department returns a success message str when used with
    ids
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/departments/delete-multiple"))
    )
    assert (
        pro.delete_department(ids=[1001, 1002])
        == "Department(s) 1001, 1002 successfully deleted."
    )


"""
device-communication-settings
"""


@responses.activate
def test_get_device_communication_settings(pro):
    """
    Ensures that get_device_communication_settings returns JSON when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/device-communication-settings"))
    )
    assert pro.get_device_communication_settings() == EXPECTED_JSON


@responses.activate
def test_get_device_communication_settings_history(pro):
    """
    Ensures that get_device_communication_settings_history returns JSON when
    used without
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/device-communication-settings/history")
        )
    )
    assert pro.get_device_communication_settings_history() == EXPECTED_JSON


@responses.activate
def test_get_device_communication_settings_history_optional_params(pro):
    """
    Ensures that get_device_communication_settings_history returns JSON when
    used with optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/device-communication-settings/history")
        )
    )
    assert (
        pro.get_device_communication_settings_history(
            0,
            100,
            ["date:desc", "name:asc"],
            "username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_device_communication_settings_history_note(pro):
    """
    Ensures that create_device_communication_settings_history_note returns JSON
    when completed succesfully
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/device-communication-settings/history")
        )
    )
    assert (
        pro.create_device_communication_settings_history_note(EXPECTED_JSON)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_device_communication_settings(pro):
    """
    Ensures that update_device_communication_settings returns JSON when
    completed successfully with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/device-communication-settings"))
    )
    assert pro.update_device_communication_settings(EXPECTED_JSON) == EXPECTED_JSON


"""
device-enrollments
"""


@responses.activate
def test_get_device_enrollments(pro):
    """
    Ensures that get_device_enrollments returns JSON when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/device-enrollments")))
    assert pro.get_device_enrollments() == EXPECTED_JSON


@responses.activate
def test_get_device_enrollments_optional_params(pro):
    """
    Ensures that get_device_enrollments returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/device-enrollments")))
    assert pro.get_device_enrollments(0, 100, ["id:desc", "name:asc"]) == EXPECTED_JSON


@responses.activate
def test_get_device_enrollment(pro):
    """
    Ensures that get_device_enrollment returns JSON when used with required
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/device-enrollments/1001")))
    assert pro.get_device_enrollment(1001) == EXPECTED_JSON


@responses.activate
def test_get_device_enrollment_history(pro):
    """
    Ensures that get_device_enrollment_history returns JSON when used without
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/device-enrollments/1001/history"))
    )
    assert pro.get_device_enrollment_history(1001) == EXPECTED_JSON


@responses.activate
def test_get_device_enrollment_history_optional_params(pro):
    """
    Ensures that get_device_enrollment_history returns JSON when used with all
    optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/device-enrollments/1001/history"))
    )
    assert (
        pro.get_device_enrollment_history(
            1001,
            0,
            100,
            ["date:desc", "name:asc"],
            "username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_device_enrollments_public_key(pro):
    """
    Ensures that get_device_enrollments_public_key returns a str when used
    """
    responses.add("GET", jps_url("/api/v1/device-enrollments/public-key"), status=200)
    assert pro.get_device_enrollments_public_key() == ""


@responses.activate
def test_get_device_enrollments_instance_sync_states(pro):
    """
    Ensures that get_device_enrollments_instance_sync_states returns JSON when
    used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/device-enrollments/syncs")))
    assert pro.get_device_enrollments_instance_sync_states() == EXPECTED_JSON


@responses.activate
def test_get_device_enrollment_instance_sync_states(pro):
    """
    Ensures that get_device_enrollment_instance_sync_states returns JSON when
    with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/device-enrollments/1001/syncs"))
    )
    assert pro.get_device_enrollment_instance_sync_states(1001) == EXPECTED_JSON


@responses.activate
def test_get_device_enrollment_instance_sync_state_latest(pro):
    """
    Ensures that get_device_enrollment_instance_sync_state_latest returns JSON
    when used with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/device-enrollments/1001/syncs/latest"))
    )
    assert pro.get_device_enrollment_instance_sync_state_latest(1001) == EXPECTED_JSON


@responses.activate
def test_create_device_enrollment(pro):
    """
    Ensures that create_device_enrollment returns JSON when completed
    successfully
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/device-enrollments/upload-token"))
    )
    assert pro.create_device_enrollment(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_device_enrollment_history_note(pro):
    """
    Ensures that create_device_enrollment_history_note returns JSON when it
    completes successfully with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/device-enrollments/1001/history"))
    )
    assert (
        pro.create_device_enrollment_history_note(EXPECTED_JSON, 1001) == EXPECTED_JSON
    )


@responses.activate
def test_update_device_enrollment(pro):
    """
    Ensures that update_device_enrollment returns JSON when completed
    successfully with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/device-enrollments/1001")))
    assert pro.update_device_enrollment(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_device_enrollment_token(pro):
    """
    Ensures that update_device_enrollment_token returns JSON when completed
    successfully with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/device-enrollments/1001/upload-token"))
    )
    assert pro.update_device_enrollment_token(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_device_enrollment(pro):
    """
    Ensures that delete_device_enrollment returns a success message str
    when completed successfully
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v1/device-enrollments/1001"))
    )
    assert (
        pro.delete_device_enrollment(1001)
        == "Device enrollment instance 1001 successfully deleted."
    )


@responses.activate
def test_delete_device_enrollment_device(pro):
    """
    Ensures that delete_device_enrollment_device returns JSON when used with
    required params and it completes successfully
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/device-enrollments/1001/disown"))
    )
    assert pro.delete_device_enrollment_device(EXPECTED_JSON, 1001) == EXPECTED_JSON


"""
device-enrollments-devices
"""


@responses.activate
def test_get_device_enrollments_devices(pro):
    """
    Ensures that get_device_enrollments_devices returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/device-enrollments/1001/devices"))
    )
    assert pro.get_device_enrollments_devices(1001) == EXPECTED_JSON


"""
ebooks
"""


@responses.activate
def test_get_ebooks(pro):
    """
    Ensures that get_ebooks returns JSON when used without optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/ebooks")))
    assert pro.get_ebooks() == EXPECTED_JSON


@responses.activate
def test_get_ebooks_optional_params(pro):
    """
    Ensures that get_ebooks returns JSON when used with all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/ebooks")))
    assert pro.get_ebooks(0, 100, ["id:desc", "name:asc"]) == EXPECTED_JSON


@responses.activate
def test_get_ebook(pro):
    """
    Ensures that get_ebook returns JSON when used with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/ebooks/1001")))
    assert pro.get_ebook(1001) == EXPECTED_JSON


@responses.activate
def test_get_ebook_scope(pro):
    """
    Ensures that get_ebook_scope returns JSON when used with the required
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/ebooks/1001/scope")))
    assert pro.get_ebook_scope(1001) == EXPECTED_JSON


"""
engage
"""


@responses.activate
def test_get_engage_settings(pro):
    """
    Ensures that get_engage_settings returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/engage")))
    assert pro.get_engage_settings() == EXPECTED_JSON


@responses.activate
def test_get_engage_settings_history(pro):
    """
    Ensures that get_engage_settings_history returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/engage/history")))
    assert pro.get_engage_settings_history() == EXPECTED_JSON


@responses.activate
def test_get_engage_settings_history_optional_params(pro):
    """
    Ensures that get_engage_settings_history returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/engage/history")))
    assert (
        pro.get_engage_settings_history(
            0,
            100,
            ["date:desc", "note:asc"],
            "username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_engage_settings_history_note(pro):
    """
    Ensures that create_engage_settings_history_note returns JSON when
    completes successfully with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/engage/history")))
    assert pro.create_engage_settings_history_note(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_engage_settings(pro):
    """
    Ensures that update_engage_settings returns JSON when completed
    successfully with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/engage")))
    assert pro.update_engage_settings(EXPECTED_JSON) == EXPECTED_JSON


"""
enrollment
"""


@responses.activate
def test_get_enrollment_settings(pro):
    """
    Ensures that get_enrollment_settings returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v2/enrollment")))
    assert pro.get_enrollment_settings() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_history(pro):
    """
    Ensures that get_enrollment_history returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/enrollment/history")))
    assert pro.get_enrollment_history() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_history_optional_params(pro):
    """
    Ensures that get_enrollment_history returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/enrollment/history")))
    assert (
        pro.get_enrollment_history(0, 100, ["date:desc", "note:asc"]) == EXPECTED_JSON
    )


@responses.activate
def test_get_enrollment_adue_session_token_settings(pro):
    """
    Ensures that get_enrollment_adue_session_token_settings returns JSON when
    used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/adue-session-token-settings"))
    )
    assert pro.get_enrollment_adue_session_token_settings() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_ldap_groups(pro):
    """
    Ensures that get_enrollment_ldap_groups returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v3/enrollment/access-groups")))
    assert pro.get_enrollment_ldap_groups() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_ldap_groups_optional_params(pro):
    """
    Ensures that get_enrollment_ldap_groups returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v3/enrollment/access-groups")))
    assert pro.get_enrollment_ldap_groups(0, 100, ["name:asc"], True) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_ldap_group(pro):
    """
    Ensures that get_enrollment_ldap_group returns JSON when used with required
    params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v3/enrollment/access-groups/1001"))
    )
    assert pro.get_enrollment_ldap_group(1001) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_languages_messaging(pro):
    """
    Ensures that get_enrollment_languages_messaging returns JSON when used
    without optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v3/enrollment/languages")))
    assert pro.get_enrollment_languages_messaging() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_languages_messaging_optional_params(pro):
    """
    Ensures that get_enrollment_languages_messaging returns JSON when used with
    all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v3/enrollment/languages")))
    assert pro.get_enrollment_languages_messaging(0, 100, ["languageCode:asc"])


@responses.activate
def test_get_enrollment_language_messaging(pro):
    """
    Ensures that get_enrollment_language_messaging returns JSON when used with
    required params
    """
    responses.add(response_builder("GET", jps_url("/api/v3/enrollment/languages/en")))
    assert pro.get_enrollment_language_messaging("en") == EXPECTED_JSON


@responses.activate
def test_get_enrollment_language_codes(pro):
    """
    Ensures that get_enrollment_language_codes returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v3/enrollment/language-codes")))
    assert pro.get_enrollment_language_codes() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_unused_language_codes(pro):
    """
    Ensures that get_enrollment_usused_language_codes returns JSON when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v3/enrollment/filtered-language-codes"))
    )
    assert pro.get_enrollment_unused_language_codes() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_history_export(pro):
    """
    Ensures that get_enrollment_history_export returns a csv when used without
    optional params
    """
    responses.add("POST", jps_url("/api/v2/enrollment/history/export"), status=200)
    assert pro.get_enrollment_history_export() == ""


@responses.activate
def test_get_enrollment_history_export_optional_params(pro):
    """
    Ensures that get_enrollment_history_export returns a csv when used with all
    optional params
    """
    responses.add("POST", jps_url("/api/v2/enrollment/history/export"), status=200)
    assert (
        pro.get_enrollment_history_export(
            ["id", "username"],
            ["ident", "name"],
            0,
            100,
            ["id:desc", "note:asc"],
            'username!="admin"',
        )
        == ""
    )


@responses.activate
def test_create_enrollment_history_note(pro):
    """
    Ensures that create_enrollment_history_note returns JSON when used with
    required params
    """
    responses.add(response_builder("POST", jps_url("/api/v2/enrollment/history")))
    assert pro.create_enrollment_history_note(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_enrollment_ldap_group(pro):
    """
    Ensures that create_enrollment_ldap_group returns JSON when used with
    required params
    """
    responses.add(response_builder("POST", jps_url("/api/v3/enrollment/access-groups")))
    assert pro.create_enrollment_ldap_group(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_enrollment_settings(pro):
    """
    Ensures that update_enrollment_settings returns JSON when used with
    required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v2/enrollment")))
    assert pro.update_enrollment_settings(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_enrollment_adue_session_token_settings(pro):
    """
    Ensures that update_enrollment_adue_session_token_Settings returns JSON
    when used with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v1/adue-session-token-settings"))
    )
    assert (
        pro.update_enrollment_adue_session_token_settings(EXPECTED_JSON)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_enrollment_ldap_group(pro):
    """
    Ensures that udpate_enrollment_ldap_group returns JSON when used with
    required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v3/enrollment/access-groups/1001"))
    )
    assert pro.update_enrollment_ldap_group(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_enrollment_language_messaging(pro):
    """
    Ensures that update_enrollment_language_messaging returns JSON when used
    with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v3/enrollment/languages/en")))
    assert (
        pro.update_enrollment_language_messaging(EXPECTED_JSON, "en") == EXPECTED_JSON
    )


@responses.activate
def test_delete_enrollment_ldap_group(pro):
    """
    Ensures that delete_enrollment_ldap_group returns success message str when
    completed successfully
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v3/enrollment/access-groups/1001"))
    )
    assert (
        pro.delete_enrollment_ldap_group(1001)
        == "Enrollment LDAP group 1001 successfully deleted."
    )


@responses.activate
def test_delete_enrollment_language_messaging_id(pro):
    """
    Ensures that delete_enrollment_language_messaging returns a success message
    str when completed successfully using languageId
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v3/enrollment/languages/en"))
    )
    assert (
        pro.delete_enrollment_language_messaging("en")
        == "Enrollment language messaging for en successfully deleted."
    )


@responses.activate
def test_delete_enrollment_language_messaging_ids(pro):
    """
    Ensures that delete_enrollment_language_messaging returns a success message
    str when completed successfully using languageIds
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v3/enrollment/languages/delete-multiple")
        )
    )
    assert (
        pro.delete_enrollment_language_messaging(languageIds=["en", "no"])
        == "Enrollment language messaging for en, no successfully deleted."
    )


"""
enrollment-customization
"""


@responses.activate
def test_get_enrollment_customizations(pro):
    """
    Ensures that get_enrollment_customization returns JSON when used without
    optoonal params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/enrollment-customizations")))
    assert pro.get_enrollment_customizations() == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customizations_optional_params(pro):
    """
    Ensures that get_enrollment_customization returns JSON when used with all
    optoonal params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/enrollment-customizations")))
    assert (
        pro.get_enrollment_customizations(0, 100, ["id:desc", "displayName:asc"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_enrollment_customization(pro):
    """
    Ensures that get_enrollment_customization returns JSON when completed
    successfully
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/enrollment-customizations/1001"))
    )
    assert pro.get_enrollment_customization(1001) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_history(pro):
    """
    Ensures that get_enrollment_customization_history returns JSON when used
    without optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v2/enrollment-customizations/1001/history")
        )
    )
    assert pro.get_enrollment_customization_history(1001) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_history_optional_params(pro):
    """
    Ensures that get_enrollment_customization_history returns JSON when used
    with all optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v2/enrollment-customizations/1001/history")
        )
    )
    assert (
        pro.get_enrollment_customization_history(
            1001, 0, 100, ["date:desc", "note:asc"]
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_enrollment_customization_prestages(pro):
    """
    Ensures that get_enrollment_customization_prestages returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v2/enrollment-customizations/1001/prestages")
        )
    )
    assert pro.get_enrollment_customization_prestages(1001) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_image(pro):
    """
    Ensures that get_enrollment_customization_image raises NotFound when
    a 404 HTTPError is returned
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v2/enrollment-customizations/images/1001"), status=404
        )
    )
    with pytest.raises(NotFound):
        pro.get_enrollment_customization_image(1001)


@responses.activate
def test_create_enrollment_customization(pro):
    """
    Ensures that create_enrollment_customization returns JSON when used with
    required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v2/enrollment-customizations"))
    )
    assert pro.create_enrollment_customization(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_enrollment_customization_history_note(pro):
    """
    Ensures that create_enrollment_history_note returns JSON when used with
    required params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v2/enrollment-customizations/1001/history")
        )
    )
    assert (
        pro.create_enrollment_customization_history_note(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_create_enrollment_customization_image(pro):
    """
    Ensures that create_enrollment_customization_image returns a success
    message str when used with required params
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            response_builder(
                "POST", jps_url("/api/v2/enrollment-customizations/images")
            )
        )
        assert pro.create_enrollment_customization_image("/file.jpg") == EXPECTED_JSON


@responses.activate
def test_update_enrollment_customization(pro):
    """
    Ensures that update_enrollment_customization returns JSON when used with
    all required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v2/enrollment-customizations/1001"))
    )
    assert pro.update_enrollment_customization(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_enrollment_customization(pro):
    """
    Ensures that delete_enrollment_customization returns JSON when used with
    required params
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v2/enrollment-customizations/1001"))
    )
    assert (
        pro.delete_enrollment_customization(1001)
        == "Enrollment customization 1001 successfully deleted."
    )


"""
enrollment-customization-preview
"""


@responses.activate
def test_get_enrollment_customization_panels(pro):
    """
    Ensures that get_enrollment_customization_panels returns JSON when used
    with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/enrollment-customization/1001/all"))
    )
    assert pro.get_enrollment_customization_panels(1001) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_panel(pro):
    """
    Ensures that get_enrollment_customization_panel returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/enrollment-customization/1001/all/1002")
        )
    )
    assert pro.get_enrollment_customization_panel(1001, 1002) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_ldap_panel(pro):
    """
    Ensures that get_enrollment_customization_ldap_panel returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/enrollment-customization/1001/ldap/1002")
        )
    )
    assert pro.get_enrollment_customization_ldap_panel(1001, 1002) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_sso_panel(pro):
    """
    Ensures that get_enrollment_customization_sso_panel returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/enrollment-customization/1001/sso/1002")
        )
    )
    assert pro.get_enrollment_customization_sso_panel(1001, 1002) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_text_panel(pro):
    """
    Ensures that get_enrollment_customization_text_panel returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/enrollment-customization/1001/text/1002")
        )
    )
    assert pro.get_enrollment_customization_text_panel(1001, 1002) == EXPECTED_JSON


@responses.activate
def test_get_enrollment_customization_text_panel_markdown(pro):
    """
    Ensures that get_enrollment_customization_text_panel_markdown returns JSON
    when used with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/enrollment-customization/1001/text/1002/markdown")
        )
    )
    assert (
        pro.get_enrollment_customization_text_panel_markdown(1001, 1002)
        == EXPECTED_JSON
    )


@responses.activate
def test_get_enrollment_customization_parsed_markdown(pro):
    """
    Ensures that get_enrollment_customization_parsed_markdown returns JSON
    when used with required params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/enrollment-customization/parse-markdown")
        )
    )
    assert (
        pro.get_enrollment_customization_parsed_markdown(EXPECTED_JSON) == EXPECTED_JSON
    )


@responses.activate
def test_create_enrollment_customization_ldap_panel(pro):
    """
    Ensures that create_enrollment_customization_ldap_panel returns JSON when
    completed successfully
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/enrollment-customization/1001/ldap"))
    )
    assert (
        pro.create_enrollment_customization_ldap_panel(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_create_enrollment_customization_sso_panel(pro):
    """
    Ensures that create_enrollment_customization_sso_panel returns JSON when
    completed successfully
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/enrollment-customization/1001/sso"))
    )
    assert (
        pro.create_enrollment_customization_sso_panel(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_create_enrollment_customization_text_panel(pro):
    """
    Ensures that create_enrollment_customization_text_panel returns JSON when
    completed successfully
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/enrollment-customization/1001/text"))
    )
    assert (
        pro.create_enrollment_customization_text_panel(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_enrollment_customization_ldap_panel(pro):
    """
    Ensures that update_enrollment_customization_ldap_panel returns JSON when
    completed successfully
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/api/v1/enrollment-customization/1001/ldap/1002")
        )
    )
    assert (
        pro.update_enrollment_customization_ldap_panel(EXPECTED_JSON, 1001, 1002)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_enrollment_customization_sso_panel(pro):
    """
    Ensures that update_enrollment_customization_sso_panel returns JSON when
    completed successfully
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/api/v1/enrollment-customization/1001/sso/1002")
        )
    )
    assert (
        pro.update_enrollment_customization_sso_panel(EXPECTED_JSON, 1001, 1002)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_enrollment_customization_text_panel(pro):
    """
    Ensures that update_enrollment_customization_text_panel returns JSON when
    completed successfully
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/api/v1/enrollment-customization/1001/text/1002")
        )
    )
    assert (
        pro.update_enrollment_customization_text_panel(EXPECTED_JSON, 1001, 1002)
        == EXPECTED_JSON
    )


@responses.activate
def test_delete_enrollment_customization_panel(pro):
    """
    Ensures that delete_enrollment_customization_panel returns a success
    message str when completed successfully
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/enrollment-customization/1001/all/1002")
        )
    )
    assert (
        pro.delete_enrollment_customization_panel(1001, 1002)
        == "Panel 1002 of enrollment customization 1001 successfully deleted."
    )


@responses.activate
def test_delete_enrollment_customization_ldap_panel(pro):
    """
    Ensures that delete_enrollment_customization_ldap_panel returns a success
    message str when completed successfully
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/enrollment-customization/1001/ldap/1002")
        )
    )
    assert (
        pro.delete_enrollment_customization_ldap_panel(1001, 1002)
        == "LDAP panel 1002 of enrollment customization 1001 successfully deleted."
    )


@responses.activate
def test_delete_enrollment_customization_sso_panel(pro):
    """
    Ensures that delete_enrollment_customization_sso_panel returns a success
    message str when completed successfully
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/enrollment-customization/1001/sso/1002")
        )
    )
    assert (
        pro.delete_enrollment_customization_sso_panel(1001, 1002)
        == "SSO panel 1002 of enrollment customization 1001 successfully deleted."
    )


@responses.activate
def test_delete_enrollment_customization_text_panel(pro):
    """
    Ensures that delete_enrollment_customization_text_panel returns a success
    message str when completed successfully
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/enrollment-customization/1001/text/1002")
        )
    )
    assert (
        pro.delete_enrollment_customization_text_panel(1001, 1002)
        == "Text panel 1002 of enrollment customization 1001 successfully deleted."
    )


"""
icon
"""


@responses.activate
def test_get_icon(pro):
    """
    Ensures that get_icon returns JSON when used with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/icon/1001")))
    assert pro.get_icon(1001) == EXPECTED_JSON


@responses.activate
def test_get_icon_image_404(pro):
    """
    Ensures that get_icon_image raises NotFound when it returns a 404 response
    code
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/icon/download/1001"), status=404)
    )
    with pytest.raises(NotFound):
        pro.get_icon_image(1001)


@responses.activate
def test_create_icon(pro):
    """
    Ensures that create_icon returns JSON when used with required params
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(response_builder("POST", jps_url("/api/v1/icon")))
        assert pro.create_icon("/file.txt") == EXPECTED_JSON


"""
inventory-information
"""


@responses.activate
def test_get_inventory_information(pro):
    """
    Ensures that get_inventory_information returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/inventory-information")))
    assert pro.get_inventory_information() == EXPECTED_JSON


"""
inventory-preload
"""


@responses.activate
def test_get_inventory_preloads(pro):
    """
    Ensures that get_inventory_preload returns JSON when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/inventory-preload/records")))
    assert pro.get_inventory_preloads() == EXPECTED_JSON


@responses.activate
def test_get_inventory_preloads_optional_params(pro):
    """
    Ensures that get_inventory_preload returns JSON when used with all optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/inventory-preload/records")))
    assert (
        pro.get_inventory_preloads(
            0, 100, ["id:desc", "deviceType:1"], 'username=="admin"'
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_inventory_preload(pro):
    """
    Ensures that get_inventory_preload returns JSON when used with required
    params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/inventory-preload/records/1001"))
    )
    assert pro.get_inventory_preload(1001) == EXPECTED_JSON


@responses.activate
def test_get_inventory_preloads_history(pro):
    """
    Ensures that get_inventory_preload returns JSON when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/inventory-preload/history")))
    assert pro.get_inventory_preloads_history() == EXPECTED_JSON


@responses.activate
def test_get_inventory_preloads_history_optional_params(pro):
    """
    Ensures that get_inventory_preload returns JSON when used with all optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/inventory-preload/history")))
    assert (
        pro.get_inventory_preloads_history(
            0, 100, ["date:desc", "note:asc"], 'username=="admin"'
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_inventory_preloads_extension_attributes(pro):
    """
    Ensures that get_inventory_preloads_extension_attributes returns JSON when
    used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/inventory-preload/ea-columns"))
    )
    assert pro.get_inventory_preloads_extension_attributes() == EXPECTED_JSON


@responses.activate
def test_get_inventory_preloads_csv_template(pro):
    """
    Ensures that get_inventory_preloads_csv_template returns a str when used
    """
    responses.add("GET", jps_url("/api/v2/inventory-preload/csv-template"))
    assert pro.get_inventory_preloads_csv_template() == ""


@responses.activate
def test_get_inventory_preloads_csv(pro):
    """
    Ensures that get_inventory_preloads_csv returns a str when used
    """
    responses.add("GET", jps_url("/api/v2/inventory-preload/csv"))
    assert pro.get_inventory_preloads_csv() == ""


@responses.activate
def test_get_inventory_preloads_export(pro):
    """
    Ensures that get_inventory_preloads_export returns str when used without
    optional params
    """
    responses.add("POST", jps_url("/api/v2/inventory-preload/export"))
    assert pro.get_inventory_preloads_export() == ""


@responses.activate
def test_get_inventory_preloads_export_optional_params(pro):
    """
    Ensures that get_inventory_preloads_export returns str when used with all
    optional params
    """
    responses.add("POST", jps_url("/api/v2/inventory-preload/export"))
    assert (
        pro.get_inventory_preloads_export(
            ["username", "department"],
            ["name", "dept"],
            0,
            100,
            ["department:desc", "username:asc"],
            'username=="admin"',
        )
        == ""
    )


@responses.activate
def test_create_inventory_preload(pro):
    """
    Ensures that create_inventory_preload returns JSON when run successfully
    """
    responses.add(
        response_builder("POST", jps_url("/api/v2/inventory-preload/records"))
    )
    assert pro.create_inventory_preload(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_inventory_preloads_history_note(pro):
    """
    Ensures that create_inventory_preloads_history_note returns JSON when
    completed successfully
    """
    responses.add(
        response_builder("POST", jps_url("/api/v2/inventory-preload/history"))
    )
    assert pro.create_inventory_preloads_history_note(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_inventory_preloads_csv_validation(pro):
    """
    Ensures that create_inventory_preloads_csv_validation returns JSON when
    used with required params
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            response_builder("POST", jps_url("/api/v2/inventory-preload/csv-validate"))
        )
        assert (
            pro.create_inventory_preloads_csv_validation("/file.txt") == EXPECTED_JSON
        )


@responses.activate
def test_create_inventory_preloads_csv(pro):
    """
    Ensures that create_inventory_preloads_csv returns JSON when used with
    required params
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            response_builder("POST", jps_url("/api/v2/inventory-preload/csv"))
        )
        assert pro.create_inventory_preloads_csv("/file.txt") == EXPECTED_JSON


@responses.activate
def test_update_inventory_preload(pro):
    """
    Ensures that update_inventory_preload returns JSON when used with required
    params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v2/inventory-preload/records/1001"))
    )
    assert pro.update_inventory_preload(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_delete_inventory_preload(pro):
    """
    Ensures that delete_inventory_preload returns a success message str when
    completed successfully
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v2/inventory-preload/records/1001"))
    )
    assert (
        pro.delete_inventory_preload(1001)
        == "Inventory preload 1001 successfully deleted."
    )


@responses.activate
def test_delete_inventory_preloads_all(pro):
    """
    Ensures that delete_inventory_preloads_all returns a success message str
    when used
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v2/inventory-preload/records/delete-all")
        )
    )
    assert (
        pro.delete_inventory_preloads_all()
        == "All inventory preloads successfully deleted."
    )


"""
jamf-connect
"""


@responses.activate
def test_get_jamf_connect_settings(pro):
    """
    Ensures that get_jamf_connect_settings returns a success message str when
    completed successfully
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-connect")))
    assert (
        pro.get_jamf_connect_settings()
        == "Success, this endpoint does not return content."
    )


@responses.activate
def test_get_jamf_connect_config_profiles(pro):
    """
    Ensures that get_jamf_connect_config_profiles returns JSON when used
    without optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/jamf-connect/config-profiles"))
    )
    assert pro.get_jamf_connect_config_profiles() == EXPECTED_JSON


@responses.activate
def test_get_jamf_connect_config_profiles_optional_params(pro):
    """
    Ensures that get_jamf_connect_config_profiles returns JSON when used
    with all optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/jamf-connect/config-profiles"))
    )
    assert (
        pro.get_jamf_connect_config_profiles(
            0, 100, ["profileId:asc", "version:desc"], 'profileId==180 and version==""'
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_jamf_connect_config_profile_deployment_tasks(pro):
    """
    Ensures that get_jamf_connect_config_profile_deployment_tasks returns JSON
    when used without optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/jamf-connect/deployments/1a2b3c4d/tasks")
        )
    )
    assert (
        pro.get_jamf_connect_config_profile_deployment_tasks("1a2b3c4d")
        == EXPECTED_JSON
    )


@responses.activate
def test_get_jamf_connect_config_profile_deployment_tasks_optional_params(pro):
    """
    Ensures that get_jamf_connect_config_profile_deployment_tasks return JSON
    when used with all optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/jamf-connect/deployments/1a2b3c4d/tasks")
        )
    )
    assert pro.get_jamf_connect_config_profile_deployment_tasks(
        "1a2b3c4d", 0, 100, ["status:asc", "updated:desc"], 'version==""'
    )


@responses.activate
def test_get_jamf_connect_history(pro):
    """
    Ensures that get_jamf_connect_history returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-connect/history")))
    assert pro.get_jamf_connect_history() == EXPECTED_JSON


@responses.activate
def test_get_jamf_connect_history_optional_params(pro):
    """
    Ensures that get_jamf_connect_history returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-connect/history")))
    assert (
        pro.get_jamf_connect_history(
            0,
            100,
            ["date:desc", "note:asc"],
            "username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_jamf_connect_config_profile_deployment_task_retry(pro):
    """
    Ensures that create_jamf_connect_config_profile_deployment_task_retry
    returns a success message str when used with required params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/jamf-connect/deployments/1a2b3c4d/tasks/retry")
        )
    )
    assert (
        pro.create_jamf_connect_config_profile_deployment_task_retry(
            EXPECTED_JSON, "1a2b3c4d"
        )
        == "Retrying specified tasks for Jamf Connect config profile 1a2b3c4d."
    )


@responses.activate
def test_create_jamf_connect_history_note(pro):
    """
    Ensures that create_jamf_connect_history_note returns JSON when used with
    required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/jamf-connect/history")))
    assert pro.create_jamf_connect_history_note(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_jamf_connect_app_update_method(pro):
    """
    Ensures that update_jamf_connect_app_update_method returns JSON when used
    """
    responses.add(
        response_builder(
            "PUT", jps_url("/api/v1/jamf-connect/config-profiles/1a2b3c4d")
        )
    )
    assert (
        pro.update_jamf_connect_app_update_method(EXPECTED_JSON, "1a2b3c4d")
        == EXPECTED_JSON
    )


"""
jamf-management-framework
"""


@responses.activate
def test_create_jamf_management_framework_redeploy(pro):
    """
    Ensures that create_jamf_management_framework_redeploy returns JSON when
    used
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/jamf-management-framework/redeploy/1001")
        )
    )
    assert pro.create_jamf_management_framework_redeploy(1001) == EXPECTED_JSON


"""
jamf-package
"""


@responses.activate
def test_get_jamf_package(pro):
    """
    Ensures that get_jamf_package returns JSON when used with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/jamf-package")))
    assert pro.get_jamf_package("protect") == EXPECTED_JSON


def test_get_jamf_package_valueerror(pro):
    """
    Ensures that get_jamf_package raises ValueError when setting application
    to a value that is not protect or connect
    """
    with pytest.raises(ValueError):
        pro.get_jamf_package("test")


"""
jamf-pro-information
"""


@responses.activate
def test_get_jamf_pro_information(pro):
    """
    Ensures that get_jamf_pro_information returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v2/jamf-pro-information")))
    assert pro.get_jamf_pro_information() == EXPECTED_JSON


"""
jamf-pro-initialization
"""


@responses.activate
def test_create_jamf_pro_initialization(pro):
    """
    Ensures that create_jamf_pro_initialization returns JSON when used
    """
    responses.add(response_builder("POST", jps_url("/api/v1/system/initialize")))
    assert pro.create_jamf_pro_initialization(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_jamf_pro_initialization_password(pro):
    """
    Ensures that create_jamf_pro_initialization_password returns JSON when used
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/system/initialize-database-connection")
        )
    )
    assert pro.create_jamf_pro_initialization_password(EXPECTED_JSON) == EXPECTED_JSON


"""
jamf-pro-initialization-preview
"""

# All deprecated

"""
jamf-pro-notifications
"""


@responses.activate
def test_get_jamf_pro_notifications(pro):
    """
    Ensures that get_jamf_pro_notifications returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/notifications")))
    assert pro.get_jamf_pro_notifications() == EXPECTED_JSON


@responses.activate
def test_delete_jamf_pro_notifications(pro):
    """
    Ensures that delete_jamf_pro_notifications returns a success message str
    when used with required params
    """
    responses.add(
        response_builder(
            "DELETE", jps_url("/api/v1/notifications/EXCEEDED_LICENSE_COUNT/-1")
        )
    )
    assert (
        pro.delete_jamf_pro_notifications("EXCEEDED_LICENSE_COUNT", -1)
        == "Notifications of type EXCEEDED_LICENSE_COUNT deleted from site -1."
    )


"""
jamf-pro-notifications-preview
"""

# All deprecated

"""
jamf-pro-server-url-preview
"""


@responses.activate
def test_get_jamf_pro_server_url_settings(pro):
    """
    Ensures that get_jamf_pro_server_url_settings returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-pro-server-url")))
    assert pro.get_jamf_pro_server_url_settings() == EXPECTED_JSON


@responses.activate
def test_get_jamf_pro_server_url_settings_history(pro):
    """
    Ensures that get_jamf_pro_server_url_settings_history returns JSON when
    used without optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/jamf-pro-server-url/history"))
    )
    assert pro.get_jamf_pro_server_url_settings_history() == EXPECTED_JSON


@responses.activate
def test_get_jamf_pro_server_url_settings_history_optional_params(pro):
    """
    Ensures that get_jamf_pro_server_url_settings_history returns JSON when
    used with all optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v1/jamf-pro-server-url/history"))
    )
    assert (
        pro.get_jamf_pro_server_url_settings_history(0, 100, ["date:desc", "note:asc"])
        == EXPECTED_JSON
    )


@responses.activate
def test_create_jamf_pro_server_url_settings_history_note(pro):
    """
    Ensures that create_jamf_pro_server_url_settings_history_note returns JSON
    when used with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v1/jamf-pro-server-url/history"))
    )
    assert (
        pro.create_jamf_pro_server_url_settings_history_note(EXPECTED_JSON)
        == EXPECTED_JSON
    )


@responses.activate
def test_update_jamf_pro_server_url_settings(pro):
    """
    Ensures that update_jamf_pro_server_url_settings returns JSON when used
    with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/jamf-pro-server-url")))
    assert pro.update_jamf_pro_server_url_settings(EXPECTED_JSON) == EXPECTED_JSON


"""
jamf-pro-user-account-settings
"""


@responses.activate
def test_get_jamf_pro_user_account_setting(pro):
    """
    Ensures that get_jamf_pro_user_account_setting returns JSON when used
    with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/user/preferences/1001")))
    assert pro.get_jamf_pro_user_account_setting(1001) == EXPECTED_JSON


@responses.activate
def test_update_jamf_pro_user_account_setting(pro):
    """
    Ensures that update_jamf_pro_user_account_setting returns JSON when used
    with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/user/preferences/1001")))
    assert (
        pro.update_jamf_pro_user_account_setting(EXPECTED_JSON, 1001) == EXPECTED_JSON
    )


@responses.activate
def test_delete_jamf_pro_user_account_setting(pro):
    """
    Ensures that delete_jamf_pro_user_account_setting returns a success
    messsage str when used with required params
    """
    responses.add(response_builder("DELETE", jps_url("/api/v1/user/preferences/1001")))
    assert (
        pro.delete_jamf_pro_user_account_setting(1001)
        == "User setting with key ID 1001 successfully deleted."
    )


"""
jamf-pro-user-account-settings-preview
"""

# All endpoints deprecated

"""
jamf-pro-version
"""


@responses.activate
def test_get_jamf_pro_version(pro):
    """
    Ensures that get_jamf_pro_version returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-pro-version")))
    assert pro.get_jamf_pro_version() == EXPECTED_JSON


"""
jamf-protect
"""


@responses.activate
def test_get_jamf_protect_integration_settings(pro):
    """
    Ensures that get_jamf_protect_integration_settings returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-protect")))
    assert pro.get_jamf_protect_integration_settings() == EXPECTED_JSON


@responses.activate
def test_get_jamf_protect_config_profile_deployment_tasks(pro):
    """
    Ensures that get_jamf_protect_config_deployment_deployment_tasks returns
    JSON when used without optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/jamf-protect/deployments/1a2b3c4d/tasks")
        )
    )
    assert (
        pro.get_jamf_protect_config_profile_deployment_tasks("1a2b3c4d")
        == EXPECTED_JSON
    )


@responses.activate
def test_get_jamf_protect_config_profile_deployment_tasks_optional_params(pro):
    """
    Ensures that get_jamf_protect_config_profile_deployment_tasks reurns JSON
    when used with all optional params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/jamf-protect/deployments/1a2b3c4d/tasks")
        )
    )
    assert (
        pro.get_jamf_protect_config_profile_deployment_tasks(
            "1a2b3c4d", 0, 100, ["id:asc", "name:desc"], 'name=="Test"'
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_jamf_protect_history(pro):
    """
    Ensures that get_jamf_protect_history returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-protect/history")))
    assert pro.get_jamf_protect_history() == EXPECTED_JSON


@responses.activate
def test_get_jamf_protect_history_optional_params(pro):
    """
    Ensures that get_jamf_protect_history returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-protect/history")))
    assert (
        pro.get_jamf_protect_history(
            0,
            100,
            ["date:desc", "note:asc"],
            "username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_get_jamf_protect_plans(pro):
    """
    Ensures that get_jamf_protect_plans returns JSON when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-protect/plans")))
    assert pro.get_jamf_protect_plans() == EXPECTED_JSON


@responses.activate
def test_get_jamf_protect_plans_optional_params(pro):
    """
    Ensures that get_jamf_protect_plans returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/jamf-protect/plans")))
    assert (
        pro.get_jamf_protect_plans(0, 100, ["id:desc", "name:asc"], "id=1001")
        == EXPECTED_JSON
    )


@responses.activate
def test_create_jamf_protect_config_profile_deployment_tasks_retry(pro):
    """
    Ensures that create_jamf_protect_config_profile_deployment_tasks_retry
    returns JSON when used with required params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/jamf-protect/deployments/1a2b3c4d/tasks/retry")
        )
    )
    assert (
        pro.create_jamf_protect_config_profile_deployment_tasks_retry(
            EXPECTED_JSON, "1a2b3c4d"
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_jamf_protect_history_note(pro):
    """
    Ensures that create_jamf_protect_history_note returns JSON when used
    with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/jamf-protect/history")))
    assert pro.create_jamf_protect_history_note(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_jamf_protect_plans_sync(pro):
    """
    Ensures that create_jamf_protect_plans_sync returns a success message str
    when used
    """
    responses.add(response_builder("POST", jps_url("/api/v1/jamf-protect/plans/sync")))
    assert (
        pro.create_jamf_protect_plans_sync()
        == "Jamf Protect plans successfully synced."
    )


@responses.activate
def test_create_jamf_protect_api_configuration(pro):
    """
    Ensures that create_jamf_protect_api_configuration returns JSON when used
    with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/jamf-protect/register")))
    assert pro.create_jamf_protect_api_configuration(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_jamf_protect_integration_settings(pro):
    """
    Ensures that update_jamf_protect_integration_settings returns JSON when
    used with required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/jamf-protect")))
    assert pro.update_jamf_protect_integration_settings(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_delete_jamf_protect_api_registration(pro):
    """
    Ensures that delete_jamf_protect_api_registration returns a success message
    str when used
    """
    responses.add(response_builder("DELETE", jps_url("/api/v1/jamf-protect")))
    assert (
        pro.delete_jamf_protect_api_registration()
        == "Jamf Protect API registration successfully deleted."
    )


"""
ldap
"""


@responses.activate
def test_get_ldap_servers(pro):
    """
    Ensures that get_ldap_servers returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/ldap/servers")))
    assert pro.get_ldap_servers() == EXPECTED_JSON


@responses.activate
def test_get_ldap_local_servers(pro):
    """
    Ensures that get_ldap_local_servers returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/ldap/ldap-servers")))
    assert pro.get_ldap_local_servers() == EXPECTED_JSON


@responses.activate
def test_get_ldap_group_search(pro):
    """
    Ensures that get_ldap_group_search returns JSON when used with required
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/ldap/groups")))
    assert pro.get_ldap_group_search("test") == EXPECTED_JSON


"""
locales-preview
"""


@responses.activate
def test_get_locales(pro):
    """
    Ensures that get_locales returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/locales")))
    assert pro.get_locales() == EXPECTED_JSON


"""
macos-managed-software-updates
"""


@responses.activate
def test_get_macos_managed_software_updates(pro):
    """
    Ensures that get_macos_managed_software_updates returns JSON when used
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v1/macos-managed-software-updates/available-updates")
        )
    )
    assert pro.get_macos_managed_software_updates() == EXPECTED_JSON


@responses.activate
def test_create_mac_managed_software_updates(pro):
    """
    Ensures that create_macos_managed_software_updates returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v1/macos-managed-software-updates/send-updates")
        )
    )
    assert pro.create_macos_managed_software_updates(EXPECTED_JSON) == EXPECTED_JSON


"""
mdm
"""


@responses.activate
def test_get_mdm_commands(pro):
    """
    Ensures that get_mdm_commands returns JSON when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/mdm/commands")))
    assert pro.get_mdm_commands() == EXPECTED_JSON


@responses.activate
def test_get_mdm_commands_optional_params(pro):
    """
    Ensures that get_mdm_commands returns JSON when used with all optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/mdm/commands")))
    assert (
        pro.get_mdm_commands(0, 100, ["dateSent:desc"], "status==Pending")
        == EXPECTED_JSON
    )


@responses.activate
def test_create_mdm_command(pro):
    """
    Ensures that create_mdm_command returns JSON when used with required params
    """
    responses.add(response_builder("POST", jps_url("/api/preview/mdm/commands")))
    assert pro.create_mdm_command(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_mdm_profile_renew(pro):
    """
    Ensures that create_mdm_profile_renew returns JSON when used with required
    params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/mdm/renew-profile")))
    assert pro.create_mdm_profile_renew(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_mdm_deploy_package(pro):
    """
    Ensures that create_mdm_deploy_package returns JSON when used with required
    params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/deploy-package")))
    assert pro.create_mdm_deploy_package(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_mdm_deploy_package_optional_params(pro):
    """
    Ensures that create_mdm_deploy_package returns JSON when used with all
    optional params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/deploy-package")))
    assert pro.create_mdm_deploy_package(EXPECTED_JSON, True) == EXPECTED_JSON


"""
mobile-device-enrollment-profile
"""


@responses.activate
def test_get_mobile_device_enrollment_profile_NotFound(pro):
    """
    Ensures that get_mobile_device_enrollment_profile raises NotFound when
    the response returns a 404 HTTPError
    """
    responses.add(
        response_builder(
            "GET",
            jps_url("/api/v1/mobile-device-enrollment-profile/1001/download-profile"),
            status=404,
        )
    )
    with pytest.raises(NotFound):
        pro.get_mobile_device_enrollment_profile(1001)


"""
mobile-device-extension-attributes-preview
"""


@responses.activate
def test_get_mobile_device_extension_attributes(pro):
    """
    Ensures that get_mobile_device_extension_attributes returns JSON when
    used
    """
    responses.add(response_builder("GET", jps_url("/api/devices/extensionAttributes")))
    assert pro.get_mobile_device_extension_attributes() == EXPECTED_JSON


"""
mobile-device-groups-preview
"""


@responses.activate
def test_get_mobile_device_groups(pro):
    """
    Ensures that get_mobile_device_extension_attributes returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/mobile-device-groups")))
    assert pro.get_mobile_device_groups() == EXPECTED_JSON


"""
mobile-device-prestages
"""


@responses.activate
def test_get_mobile_device_prestages(pro):
    """
    Ensures that get_mobile_device_prestages returns JSON when used without
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/mobile-device-prestages")))
    assert pro.get_mobile_device_prestages() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestages_optional_params(pro):
    """
    Ensures that get_mobile_device_prestages returns JSON when used with all
    optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/mobile-device-prestages")))
    assert (
        pro.get_mobile_device_prestages(0, 100, ["id:asc", "defaultPrestage:desc"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_prestages_scopes(pro):
    """
    Ensures that get_mobile_device_prestages_scopes returns JSON when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-device-prestages/scope"))
    )
    assert pro.get_mobile_device_prestages_scopes() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestages_sync_states(pro):
    """
    Ensures that get_mobile_device_prestages_sync_states returns JSON when used
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-device-prestages/syncs"))
    )
    assert pro.get_mobile_device_prestages_sync_states() == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestage(pro):
    """
    Ensures that get_mobile_device_prestage returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-device-prestages/1001"))
    )
    assert pro.get_mobile_device_prestage(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestage_attachments(pro):
    """
    Ensures that get_mobile_device_prestage_attachments return JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v2/mobile-device-prestages/1001/attachments")
        )
    )
    assert pro.get_mobile_device_prestage_attachments(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestage_history(pro):
    """
    Ensures that get_mobile_device_prestage_history returns JSON when used
    without optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-device-prestages/1001/history"))
    )
    assert pro.get_mobile_device_prestage_history(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestage_history_optional_params(pro):
    """
    Ensures that get_mobile_device_prestage_history returns JSON when used
    with all optional params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-device-prestages/1001/history"))
    )
    assert (
        pro.get_mobile_device_prestage_history(1001, 0, 100, ["date:desc", "note:asc"])
        == EXPECTED_JSON
    )


@responses.activate
def test_get_mobile_device_prestage_scope(pro):
    """
    Ensures that get_mobile_device_prestage_scope returns JSON when used with
    required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-device-prestages/1001/scope"))
    )
    assert pro.get_mobile_device_prestage_scope(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestage_sync_states(pro):
    """
    Ensures that get_mobile_device_prestage_sync_states returns JSON when used
    with required params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-device-prestages/1001/syncs"))
    )
    assert pro.get_mobile_device_prestage_sync_states(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_prestage_latest_sync_state(pro):
    """
    Ensures that get_mobile_device_prestage_latest_sync_state returns JSON when
    used with required params
    """
    responses.add(
        response_builder(
            "GET", jps_url("/api/v2/mobile-device-prestages/1001/syncs/latest")
        )
    )
    assert pro.get_mobile_device_prestage_latest_sync_state(1001) == EXPECTED_JSON


@responses.activate
def test_create_mobile_device_prestage(pro):
    """
    Ensures that create_mobile_device_prestage returns JSON when used with
    required params
    """
    responses.add(response_builder("POST", jps_url("/api/v2/mobile-device-prestages")))
    assert pro.create_mobile_device_prestage(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_create_mobile_device_prestage_attachment(pro):
    """
    Ensures that create_mobile_device_prestage_attachment returns JSON when
    uploading a txt file
    """
    read_data = "Test document content"
    mock_open = mock.mock_open(read_data=read_data)
    with mock.patch("builtins.open", mock_open):
        responses.add(
            response_builder(
                "POST", jps_url("/api/v2/mobile-device-prestages/1001/attachments")
            )
        )
        assert pro.create_mobile_device_prestage_attachment("/file.txt", 1001)


@responses.activate
def test_create_mobile_device_prestage_history_note(pro):
    """
    Ensures that create_mobile_device_prestage_history_note returns JSON when
    used
    """
    responses.add(
        response_builder(
            "POST", jps_url("/api/v2/mobile-device-prestages/1001/history")
        )
    )
    assert (
        pro.create_mobile_device_prestage_history_note(EXPECTED_JSON, 1001)
        == EXPECTED_JSON
    )


@responses.activate
def test_create_mobile_device_prestage_scope(pro):
    """
    Ensures that create_mobile_device_prestage_scope returns JSON when used
    with required params
    """
    responses.add(
        response_builder("POST", jps_url("/api/v2/mobile-device-prestages/1001/scope"))
    )
    assert pro.create_mobile_device_prestage_scope(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_update_mobile_device_prestage(pro):
    """
    Ensures that update_mobile_device_prestage returns JSON when used with
    required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v2/mobile-device-prestages/1001"))
    )
    assert pro.update_mobile_device_prestage(EXPECTED_JSON, 1001) == EXPECTED_JSON


@responses.activate
def test_replace_mobile_device_prestage_scope(pro):
    """
    Ensures that replace_mobile_device_pretage_scope returns JSON when used
    with required params
    """
    responses.add(
        response_builder("PUT", jps_url("/api/v2/mobile-device-prestages/1001/scope"))
    )
    assert (
        pro.replace_mobile_device_prestage_scope(EXPECTED_JSON, 1001) == EXPECTED_JSON
    )


@responses.activate
def test_delete_mobile_device_prestage(pro):
    """
    Ensures that delete_mobile_device_prestage returns a success message str
    when used with required params
    """
    responses.add(
        response_builder("DELETE", jps_url("/api/v2/mobile-device-prestages/1001"))
    )
    assert (
        pro.delete_mobile_device_prestage(1001)
        == "Mobile device prestage 1001 successfully deleted."
    )


@responses.activate
def test_delete_mobile_device_prestage_attachment(pro):
    """
    Ensures that delete_mobile_device_prestage_attachment returns a success
    message str when used with required params
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/api/v2/mobile-device-prestages/1001/attachments/delete-multiple"),
        )
    )
    assert (
        pro.delete_mobile_device_prestage_attachment({"ids": ["1", "2"]}, 1001)
        == "Attachment(s) 1, 2 of mobile device prestage 1001 successfully deleted."
    )


@responses.activate
def test_delete_mobile_device_prestage_scope(pro):
    """
    Ensures that delete_mobile_device_prestage_scope returns JSON when used
    with required params
    """
    responses.add(
        response_builder(
            "POST",
            jps_url("/api/v2/mobile-device-prestages/1001/scope/delete-multiple"),
        )
    )
    assert pro.delete_mobile_device_prestage_scope(EXPECTED_JSON, 1001) == EXPECTED_JSON


"""
mobile-devices
"""


@responses.activate
def test_get_mobile_devices(pro):
    """
    Ensures that get_mobile_devices returns JSON when used without optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/mobile-devices")))
    assert pro.get_mobile_devices() == EXPECTED_JSON


@responses.activate
def test_get_mobile_devices_optional_params(pro):
    """
    Ensures that get_mobile_device returns JSON when used with all optional
    params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/mobile-devices")))
    assert pro.get_mobile_devices(0, 100, ["id:desc", "name:asc"]) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device(pro):
    """
    Ensures that get_mobile_device returns JSON when used with required params
    """
    responses.add(response_builder("GET", jps_url("/api/v2/mobile-devices/1001")))
    assert pro.get_mobile_device(1001) == EXPECTED_JSON


@responses.activate
def test_get_mobile_device_detail(pro):
    """
    Ensures that get_mobile_device_detail returns JSON when used with required
    params
    """
    responses.add(
        response_builder("GET", jps_url("/api/v2/mobile-devices/1001/detail"))
    )
    assert pro.get_mobile_device_detail(1001) == EXPECTED_JSON


@responses.activate
def test_update_mobile_device(pro):
    """
    Ensures that update_mobile_device returns JSON when used with required
    params
    """
    responses.add(response_builder("PUT", jps_url("/api/v2/mobile-devices/1001")))
    assert pro.update_mobile_device(EXPECTED_JSON, 1001) == EXPECTED_JSON


"""
parent-app-preview
"""


@responses.activate
def test_get_parent_app_settings(pro):
    """
    Ensures that get_parent_app_settings returns JSON when used
    """
    responses.add(response_builder("GET", jps_url("/api/v1/parent-app")))
    assert pro.get_parent_app_settings() == EXPECTED_JSON


@responses.activate
def test_get_parent_app_settings_history(pro):
    """
    Ensures that get_parent_app_settings_history returns JSON when used
    without optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/parent-app/history")))
    assert pro.get_parent_app_settings_history() == EXPECTED_JSON


@responses.activate
def test_get_parent_app_settings_history_optional_params(pro):
    """
    Ensures that get_parent_app_settings_history returns JSON when used
    with all optional params
    """
    responses.add(response_builder("GET", jps_url("/api/v1/parent-app/history")))
    assert (
        pro.get_parent_app_settings_history(
            0,
            100,
            ["date:desc", "note:asc"],
            "username!=admin and details==disabled and date<2019-12-15",
        )
        == EXPECTED_JSON
    )


@responses.activate
def test_create_parent_app_settings_history_note(pro):
    """
    Ensures that create_parent_app_settings_history_note returns JSON when used
    with required params
    """
    responses.add(response_builder("POST", jps_url("/api/v1/parent-app/history")))
    assert pro.create_parent_app_settings_history_note(EXPECTED_JSON) == EXPECTED_JSON


@responses.activate
def test_update_parent_app_settings(pro):
    """
    Ensures that update_parent_app_settings returns JSON when used with
    required params
    """
    responses.add(response_builder("PUT", jps_url("/api/v1/parent-app")))
    assert pro.update_parent_app_settings(EXPECTED_JSON) == EXPECTED_JSON


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
