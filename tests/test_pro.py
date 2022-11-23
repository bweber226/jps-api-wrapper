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
        responses.add("POST", jps_url("/api/v1/computers-inventory/1001/attachments"))
        assert (
            pro.create_computer_inventory_attachment("/file.txt", 1001)
            == "File uploaded successfully."
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
