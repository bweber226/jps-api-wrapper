from typing import List, Union
from os.path import basename
from mimetypes import guess_type

from request_builder import RequestBuilder
from utils import (
    check_conflicting_params,
    identification_type,
    remove_empty_params,
    enforce_type,
)


class Pro(RequestBuilder):
    def __init__(self, base_url, username, password):
        super().__init__(base_url, username, password)  # pragma: no cover

    """
    advanced-mobile-device-searches
    """

    def get_advanced_mobile_device_searches(self) -> dict:
        """
        Returns all advanced mobile device searches in JSON
        """
        endpoint = "/api/v1/advanced-mobile-device-searches"

        return self._get(endpoint)

    def get_advanced_mobile_device_search_criteria_choices(
        self, criteria: str, site: Union[int, str] = -1, contains: str = None
    ) -> dict:
        """
        Returns the valid choices of an advanced mobile device search criteria

        :param criteria:
            Advanced mobile device search criteria, A list of potentially
            valid choices can be found by navigating to the Criteria page of
            the Advanced Mobile Device Search creation process.
        :param site: JPS server site, use -1 for none
        :param contains:
        """
        endpoint = "/api/v1/advanced-mobile-device-searches/choices"
        params = remove_empty_params(
            params={"criteria": criteria, "site": site, "contains": contains}
        )

        return self._get(endpoint, params=params)

    def get_advanced_mobile_device_search(self, id: Union[int, str]) -> dict:
        """
        Returns data on one advanced mobile device search criteria by ID

        :param id: Advanced mobile device search ID
        """
        endpoint = f"/api/v1/advanced-mobile-device-searches/{id}"

        return self._get(endpoint)

    def create_advanced_mobile_device_search(self, data: dict) -> dict:
        """
        Creates an advanced mobile device search with JSON data

        :param data: JSON data to create advanced mobile device search with
        """
        endpoint = "/api/v1/advanced-mobile-device-searches"

        return self._post(endpoint, data)

    def update_advanced_mobile_device_search(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Updates an advanced mobile device search with JSON data by ID

        :param data: JSON data to update advanced mobile device search with
        :param id: Advanced mobile device search ID
        """
        endpoint = f"/api/v1/advanced-mobile-device-searches/{id}"

        return self._put(endpoint, data)

    def delete_advanced_mobile_device_search(
        self, id: Union[int, str] = None, ids: List[Union[int, str]] = None
    ) -> str:
        """
        Deletes an advanced mobile device search by ID or IDS, use id for a
        single device and ids to delete multiple

        :param id: Advanced mobile device search ID
        :param ids: List of advanced mobile device search IDs
        """
        identifier_options = {"id": id, "ids": ids}
        identification_type(identifier_options)
        check_conflicting_params(identifier_options)
        if id:
            if enforce_type(id, (str, int)):
                endpoint = f"/api/v1/advanced-mobile-device-searches/{id}"
                return self._delete(
                    endpoint,
                    success_message=(
                        f"Advanced mobile device search {id} successfully deleted."
                    ),
                )
        if ids:
            if enforce_type(ids, (List)):
                ids = [str(id) for id in ids]
                endpoint = "/api/v1/advanced-mobile-device-searches/delete-multiple"
                return self._post(
                    endpoint,
                    data={"ids": ids},
                    success_message=(
                        "Advanced mobile device search(es) "
                        f"{', '.join(ids)} successfully deleted."
                    ),
                )

    """
    advanced-user-content-searches
    """

    def get_advanced_user_content_searches(self) -> dict:
        """
        Returns all advanced user content searches in JSON
        """
        endpoint = "/api/v1/advanced-user-content-searches"

        return self._get(endpoint)

    def get_advanced_user_content_search(self, id: Union[int, str]) -> dict:
        """
        Returns data on one advanced user content search in JSON

        :param id: Advanced user content search ID
        """
        endpoint = f"/api/v1/advanced-user-content-searches/{id}"

        return self._get(endpoint)

    def create_advanced_user_content_search(self, data: dict) -> dict:
        """
        Creates an advanced user content search with JSON data

        :param data: JSON data to create advanced user content search with
        """
        endpoint = "/api/v1/advanced-user-content-searches"

        return self._post(endpoint, data)

    def update_advanced_user_content_search(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Updates an advanced user content search with JSON data by ID

        :param data: JSON data to update advanced user content search with
        :param id: Advanced user content search ID
        """
        endpoint = f"/api/v1/advanced-user-content-searches/{id}"

        return self._put(endpoint, data)

    def delete_advanced_user_content_search(self, id: Union[int, str]) -> str:
        """
        Deletes an advances user content search by ID

        :param id: Advanced user content search ID
        """
        endpoint = f"/api/v1/advanced-user-content-searches/{id}"

        return self._delete(
            endpoint,
            success_message=f"Advanced user content search {id} successfully deleted.",
        )

    """
    api-authentication
    """
    # Only the get method is available here because the other endpoints will
    # cause the current session to fail and break the api wrapper

    def get_api_authentication(self) -> dict:
        """
        Returns all the authorization details associated with the current API
        token
        """
        endpoint = "/api/v1/auth"

        return self._get(endpoint)

    """
    app-dynamics-configuration-preview
    """

    # TODO Preview
    def get_app_dynamics_configuration(self) -> dict:
        """
        Returns AppDynamicsConfig object
        """
        endpoint = "/api/v1/app-dynamics/script-configuration"

        return self._get(endpoint)

    """
    app-request-preview
    """
    # TODO Preview

    def get_app_request_settings(self) -> dict:
        """
        Returns the app request settings in JSON
        """
        endpoint = "/api/v1/app-request/settings"

        return self._get(endpoint)

    def get_app_request_form_input_fields(self) -> dict:
        """
        Returns the app request form input fields in JSON
        """
        endpoint = "/api/v1/app-request/form-input-fields"

        return self._get(endpoint)

    def get_app_request_form_input_field(self, id: Union[int, str]) -> dict:
        """
        Returns specified app request form input field object by ID

        :param id: App request form input field ID
        """
        endpoint = f"/api/v1/app-request/form-input-fields/{id}"

        return self._get(endpoint)

    def create_app_request_form_input_field(self, data: dict) -> dict:
        """
        Creates a app request form input field record with JSON data

        :param data: JSON data to create the app request form input field with
        """
        endpoint = "/api/v1/app-request/form-input-fields"

        return self._post(endpoint, data)

    def update_app_request_settings(self, data: dict) -> dict:
        """
        Updates the app request settings with JSON data

        :param data: JSON data to update the app request settings with
        """
        endpoint = "/api/v1/app-request/settings"

        return self._put(endpoint, data)

    def update_app_request_form_input_field(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Updates the specified app request form input field object by ID with
        JSON data

        :param id: App request form input field ID
        :param data: JSON data to update the app request form input field with
        """
        endpoint = f"/api/v1/app-request/form-input-fields/{id}"

        return self._put(endpoint, data)

    def replace_app_request_form_input_fields(self, data: List[dict]) -> dict:
        """
        Replaces all app request form input fields with JSON data

        :param data:
            List of JSON dicts to replace all app request form input
            fields with
        """
        endpoint = "/api/v1/app-request/form-input-fields"

        return self._put(endpoint, data)

    def delete_app_request_form_input_field(self, id: Union[int, str]) -> str:
        """
        Deletes a specified app request form input field by ID

        :param id: App request form input field ID
        """
        endpoint = f"/api/v1/app-request/form-input-fields/{id}"

        return self._delete(
            endpoint,
            success_message=(
                f"App request form input field {id} successfully deleted."
            ),
        )

    """
    app-store-country-codes-preview
    """

    def get_app_store_country_codes(self) -> dict:
        """
        Returns a list of countries and the associated codes that can be use
        for the App Store locale
        """
        endpoint = "/api/v1/app-store-country-codes"

        return self._get(endpoint)

    """
    branding
    """

    # TODO

    """
    buildings
    """

    def get_buildings(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns all buildings or search for sorted and paged buildings

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["date:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter buildings collection.
            Default filter is empty query - returning all results for the
            requested page. Fields allowed in the query: name, streetAddress1,
            streetAddress2, city, stateProvince, zipPostalCode, country. This
            param can be combined with paging and sorting.

            Example: city=="Chicago" and name=="build"
        """
        endpoint = "/api/v1/buildings"
        params = remove_empty_params(
            {"page": page, "page-size": page_size, "sort": sort, "filter": filter}
        )

        return self._get(endpoint, params=params)

    def get_building(self, id: Union[int, str]) -> dict:
        """
        Returns specified building object by ID in JSON

        :param id: Building ID
        """
        endpoint = f"/api/v1/buildings/{id}"

        return self._get(endpoint)

    def get_building_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns specified building history object by ID in JSON

        :param id: Building ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: username,
            date, note, details. This param can be combined with paging and
            sorting.

            Example: username!=admin and details==disabled and date<2019-12-15
        """
        endpoint = f"/api/v1/buildings/{id}/history"
        params = remove_empty_params(
            {"page": page, "page-size": page_size, "sort": sort, "filter": filter}
        )

        return self._get(endpoint, params=params)

    def get_building_export(
        self,
        export_fields: List[str] = None,
        export_labels: List[str] = None,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> str:
        """
        Exports buildings collection in CSV

        :param export_fields:
            Export fields parameter, used to change default order or ignore
            some of the response properties. Default is empty array, which
            means that all fields of the response entity will be serialized.

            Options: id, name, streetAddress1, streetAddress2, city,
            stateProvince, zipPostalCode, country

            Example: ["id", "name"]

        :param export_labels:
            Export labels parameter, used to customize fieldnames/columns in
            the exported file. Default is empty array, which means that
            response properties names will be used. Number of the provided
            labels must match the number of export-fields

            Example: export_labels=["identification", "buildingName"] with
            matching: export_fields=["id", "name"]

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["id:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: id, name.
            This param can be combined with paging and sorting.

            Example: name=="buildings"

        """
        endpoint = "/api/v1/buildings/export"
        headers = {"Content-type": "application/json", "Accept": "text/csv"}
        params = remove_empty_params(
            {
                "export-fields": export_fields,
                "export-labels": export_labels,
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )

        return self._post(endpoint, params=params, headers=headers, data_type=None)

    def get_building_history_export(
        self,
        id: Union[int, str],
        export_fields: List[str] = None,
        export_labels: List[str] = None,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> str:
        """
        Exports building history in specified format by ID

        :param id: Building ID
        :param export_fields:
            Export fields parameter, used to change default order or ignore
            some of the response properties. Default is empty array, which
            means that all fields of the response entity will be serialized.

            Options: id, username, date, note, details

            Example: ["id", "username"]

        :param export_labels:
            Export labels parameter, used to customize fieldnames/columns in
            the exported file. Default is empty array, which means that
            response properties names will be used. Number of the provided
            labels must match the number of export-fields

            Example: export_labels=["identification", "name"] with
            matching: export_fields=["id", "username"]

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["id:desc", "date:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: id, name.
            This param can be combined with paging and sorting.

            Example: username=="exampleuser"
        """
        endpoint = f"/api/v1/buildings/{id}/history/export"
        headers = {"Content-type": "application/json", "Accept": "text/csv"}
        params = remove_empty_params(
            {
                "export-fields": export_fields,
                "export-labels": export_labels,
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )

        return self._post(endpoint, params=params, headers=headers, data_type=None)

    def create_building(self, data: dict) -> dict:
        """
        Creates a building record with JSON data

        :param data: JSON data to create the building record with
        """
        endpoint = "/api/v1/buildings"

        return self._post(endpoint, data)

    def create_building_history_note(self, data: dict, id: Union[int, str]) -> dict:
        """
        Creates specified building history notes with JSON data by ID

        :param data: JSON data to create building note with
        :param id: Building ID
        """
        endpoint = f"/api/v1/buildings/{id}/history"

        return self._post(endpoint, data)

    def update_building(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates a specified building with JSON data by ID

        :param data: JSON data to create building record with
        :param id: Building ID
        """
        endpoint = f"/api/v1/buildings/{id}"

        return self._put(endpoint, data)

    def delete_building(
        self, id: Union[int, str] = None, ids: List[Union[int, str]] = None
    ) -> str:
        """
        Deletes a building by ID or IDS, use id for a single building and ids
        to delete multiple

        :param id: Building ID
        :param ids: List of building IDs
        """
        identifier_options = {"id": id, "ids": ids}
        identification_type(identifier_options)
        check_conflicting_params(identifier_options)
        if id:
            if enforce_type(id, (int, str)):
                endpoint = f"/api/v1/buildings/{id}"
                return self._delete(
                    endpoint,
                    success_message=(f"Building {id} successfully deleted."),
                )
        if ids:
            if enforce_type(ids, (List)):
                ids = [str(id) for id in ids]
                endpoint = "/api/v1/buildings/delete-multiple"
                return self._post(
                    endpoint,
                    data={"ids": ids},
                    success_message=(
                        f"Building(s) {', '.join(ids)} successfully deleted."
                    ),
                )

    """
    cache-settings
    """

    def get_cache_settings(self):
        """
        Returns cache settings of the JPS server in JSON
        """
        endpoint = "/api/v1/cache-settings"

        return self._get(endpoint)

    def update_cache_settings(self, data: dict) -> dict:
        """
        Updates cache settings of the JPS server in JSON

        :param data: JSON data to update cache settings with
        """
        endpoint = "/api/v1/cache-settings"

        return self._put(endpoint, data)

    """
    categories
    """

    def get_categories(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns all category objects in JSON

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter categories
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: name,
            priority. This param can be combined with paging and sorting.

            Example: name=="Apps*" and priority>=5
        """
        endpoint = "/api/v1/categories"
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )

        return self._get(endpoint, params=params)

    def get_category(self, id: Union[int, str]) -> dict:
        """
        Returns specified category object by ID in JSON

        :param id: Category ID
        """
        endpoint = f"/api/v1/categories/{id}"

        return self._get(endpoint)

    def get_category_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns specified category history object by ID in JSON

        :param id: Category ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: username,
            date, note, details. This param can be combined with paging and
            sorting.

            Example: username!=admin and details==disabled and date<2019-12-15
        """
        endpoint = f"/api/v1/categories/{id}/history"
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )

        return self._get(endpoint, params=params)

    def create_category(self, data: dict) -> dict:
        """
        Creates a category record with JSON data

        :param data: JSON data to create the category with
        """
        endpoint = "/api/v1/categories"

        return self._post(endpoint, data)

    def create_category_history_note(self, data: dict, id: Union[int, str]) -> dict:
        """
        Creates a category history object note by ID with JSON data

        :param data: JSON data to create the category history note with
        :param id: Category ID
        """
        endpoint = f"/api/v1/categories/{id}/history"

        return self._post(endpoint, data)

    def update_category(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates a category by with by ID with JSON data

        :param data: JSON data to update the category with
        :param id: Category ID
        """
        endpoint = f"/api/v1/categories/{id}"

        return self._put(endpoint, data)

    def delete_category(
        self, id: Union[int, str] = None, ids: List[Union[int, str]] = None
    ) -> str:
        """
        Deletes a category by ID or IDS, use id for a single category and ids
        to delete multiple

        :param id: Category ID
        :param ids: List of categories IDs
        """
        identifier_options = {"id": id, "ids": ids}
        identification_type(identifier_options)
        check_conflicting_params(identifier_options)
        if id:
            if enforce_type(id, (int, str)):
                endpoint = f"/api/v1/categories/{id}"
                return self._delete(
                    endpoint,
                    success_message=(f"Category {id} successfully deleted."),
                )
        if ids:
            if enforce_type(ids, (List)):
                ids = [str(id) for id in ids]
                endpoint = "/api/v1/categories/delete-multiple"
                return self._post(
                    endpoint,
                    data={"ids": ids},
                    success_message=(
                        f"Category(s) {', '.join(ids)} successfully deleted."
                    ),
                )

    """
    certificate-authority
    """

    def get_certificate_authority_active(
        self, der: bool = None, pem: bool = None
    ) -> Union[dict, str]:
        """
        Returns X.509 details of the active certificate authority in JSON,
        der, or pem format

        :param der: Set to True to return the certificate info in der format
        :param pem: Set to True to return the certificate info in pem format
        """
        check_conflicting_params({"der": der, "pem": pem})
        if der:
            data_type = None
            headers = {"accept": "application/pkix-cert"}
            endpoint = "/api/v1/pki/certificate-authority/active/der"
        elif pem:
            data_type = None
            headers = {"accept": "application/pem-certificate-chain"}
            endpoint = "/api/v1/pki/certificate-authority/active/pem"
        else:
            data_type = "json"
            headers = None
            endpoint = "/api/v1/pki/certificate-authority/active"

        return self._get(endpoint, headers=headers, data_type=data_type)

    def get_certificate_authority(
        self, uuid: str, der: bool = None, pem: bool = None
    ) -> Union[dict, str]:
        """
        Returns X.509 details of certificate authority by ID in JSON, der,
        or pem format

        :param uuid: Certificate ID
        :param der: Set to True to return the certificate info in der format
        :param pem: Set to True to return the certificate info in pem format
        """
        check_conflicting_params({"der": der, "pem": pem})
        if der:
            data_type = None
            headers = {"accept": "application/pkix-cert"}
            endpoint = f"/api/v1/pki/certificate-authority/{uuid}/der"
        elif pem:
            data_type = None
            headers = {"accept": "application/pem-certificate-chain"}
            endpoint = f"/api/v1/pki/certificate-authority/{uuid}/pem"
        else:
            data_type = "json"
            headers = None
            endpoint = f"/api/v1/pki/certificate-authority/{uuid}"

        return self._get(endpoint, headers=headers, data_type=data_type)

    """
    classic-ldap
    """

    def get_classic_ldap(self, id: Union[int, str]) -> dict:
        """
        Returns mappings for OnPrem LDAP configuration with given id

        :param id: Classic LDAP ID
        """
        endpoint = f"/api/v1/classic-ldap/{id}"

        return self._get(endpoint)

    """
    client-check-in
    """

    def get_client_check_in(self) -> dict:
        """
        Returns client check-in settings in JSON
        """
        endpoint = "/api/v3/check-in"

        return self._get(endpoint)

    def get_client_check_in_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns client check-in settings history in JSON

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            is date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "username:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: username,
            date, note, details. This param can be combined with paging and
            sorting.

            Example: username!=admin and details==disabled and date<2019-12-15
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v3/check-in/history"

        return self._get(endpoint, params=params)

    def create_client_check_in_history_note(self, data: dict) -> dict:
        """
        Creates a client check-in history note with JSON data

        :param data: JSON data to create client check-in history note with
        """
        endpoint = "/api/v3/check-in/history"

        return self._post(endpoint, data)

    def update_client_check_in(self, data) -> dict:
        """
        Updates client check-in settings with JSON data

        :param data: JSON data to updatae client check-in settings with
        """
        endpoint = "/api/v3/check-in"

        return self._put(endpoint, data)

    """
    cloud-azure
    """

    def get_cloud_azure_default_server_configuration(self) -> dict:
        """
        Returns the default set of server attributes that allows you to return
        the data you need from Azure AD. Some fields may be empty and may be
        edited when creating a new configuration.
        """
        endpoint = "/api/v1/cloud-azure/defaults/server-configuration"

        return self._get(endpoint)

    def get_cloud_azure_default_mappings(self) -> dict:
        """
        Returns the default set of mapping attributes that allows you to return
        the data you need from Azure AD. Some fields may be empty and may be
        edited when creating a new configuration.
        """
        endpoint = "/api/v1/cloud-azure/defaults/mappings"

        return self._get(endpoint)

    def get_cloud_azure_identity_provider_configuration(
        self, id: Union[int, str]
    ) -> dict:
        """
        Returns Azure cloud identity provider configuration with given ID
        in JSON
        """
        endpoint = f"/api/v1/cloud-azure/{id}"

        return self._get(endpoint)

    def get_cloud_azure_report(self, id: Union[int, str]):
        """
        Returns excel file of generated cloud azure report

        :param id: Existing report ID
        """
        headers = {
            "accept": "application/vnd.openxmlformats-officedocument"
            ".spreadsheetml.sheet",
            "Content-type": "application/json",
        }
        endpoint = f"/api/v1/azure-ad-migration/reports/{id}/download"

        return self._get(endpoint, headers=headers)

    def get_cloud_azure_report_status(self, id: Union[int, str]) -> dict:
        """
        Returns status of Azure AD migration report

        :param id: Existing report ID
        """
        endpoint = f"/api/v1/azure-ad-migration/reports/{id}"

        return self._get(endpoint)

    def get_cloud_azure_pending_report(self):
        """
        Returns info about pending report
        """
        endpoint = "/api/v1/azure-ad-migration/reports/pending"

        return self._get(endpoint)

    def create_cloud_azure_report(self, data: dict) -> dict:
        """
        Starts a new process in background that will generate Excel report
        with JSON data

        :param data: JSON data to create the report with
        """
        endpoint = "/api/v1/azure-ad-migration/reports"

        return self._post(endpoint, data)

    def create_cloud_azure_identity_provider_configuration(self, data: dict) -> dict:
        """
        Create new Azure Cloud Identity Provider configuration with unique
        display name

        :param data:
            JSON data to create the azure vloud identity provider configuration
            with
        """
        endpoint = "/api/v1/cloud-azure"

        return self._post(endpoint, data)

    def update_cloud_azure_identity_provider_configuration(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Updates an Azure Cloud Identity Provider configuration. Cannot be used
        for partial updates, all content body parameters must be sent.
        """
        endpoint = f"/api/v1/cloud-azure/{id}"

        return self._put(endpoint, data)

    def delete_cloud_azure_identity_provider_configuration(
        self, id: Union[int, str]
    ) -> str:
        """
        Deletes a Cloud Identity Provider configuration by ID

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v1/cloud-azure/{id}"

        return self._delete(
            endpoint,
            success_message=f"Cloud identity provider {id} successfully deleted.",
        )

    """
    cloud-idp
    """

    def get_cloud_idps(
        self, page: int = None, page_size=None, sort: List[str] = ["id:desc"]
    ) -> dict:
        """
        Returns basic informations about all configured Cloud Identity
        Providers

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:desc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["date:desc", "name:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/cloud-idp"

        return self._get(endpoint, params=params)

    def get_cloud_idp(self, id: Union[int, str]) -> dict:
        """
        Returns cloud identity provider configuration by ID

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v1/cloud-idp/{id}"

        return self._get(endpoint)

    def get_cloud_idp_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns specified cloud identity provider history by ID

        :param id: Cloud identity provider ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: username,
            date, note, details. This param can be combined with paging and
            sorting.

            Example: username!=admin and details==disabled and date<2019-12-15
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = f"/v1/cloud-idp/{id}/history"

        return self._get(endpoint, params=params)

    def get_cloud_idp_export(
        self,
        export_fields: List[str] = None,
        export_labels: List[str] = None,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> str:
        """
        Returns CSV export of cloud identity providers collection

        :param export_fields:
            Export fields parameter, used to change default order or ignore
            some of the response properties. Default is empty array, which
            means that all fields of the response entity will be serialized.

            Example: ["id", "username"]

        :param export_labels:
            Export labels parameter, used to customize fieldnames/columns in
            the exported file. Default is empty array, which means that
            response properties names will be used. Number of the provided
            labels must match the number of export-fields

            Example: ["identifier", "name"] with matching export-fields
            ["id", "username"]

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be seperated
            with a comma.

            Example: ["id:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: id, name.
            This param can be combined with paging and sorting.

            Example: name=="department"
        """
        params = remove_empty_params(
            {
                "export-fields": export_fields,
                "export-labels": export_labels,
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        headers = {"accept": "text/csv", "content-type": "application/json"}
        endpoint = "/api/v1/cloud-idp/export"

        return self._post(endpoint, params=params, headers=headers, data_type=None)

    def create_cloud_idp_history_note(self, data: dict, id: Union[int, str]) -> dict:
        """
        Creates specified cloud identity provider history note by ID

        :param data: JSON data to create cloud identity provider history with
        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v1/cloud-idp/{id}/history"

        return self._post(endpoint, data)

    def create_cloud_idp_group_test_search(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a cloud identify provider group test search and returns the
        result

        :param data: JSON data to run group test search with
        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v1/cloud-idp/{id}/test-group"

        return self._post(endpoint, data)

    def create_cloud_idp_user_test_search(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a cloud identify provider user test search and returns result

        :param data: JSON data to run user test search with
        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v1/cloud-idp/{id}/test-user"

        return self._post(endpoint, data)

    def create_cloud_idp_user_membership_test_search(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a cloud identify provider user membership test search and
        returns the result

        :param data: JSON data to run user membership test search with
        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v1/cloud-idp/{id}/test-user-membership"

        return self._post(endpoint, data)

    """
    cloud-ldap
    """

    def get_cloud_ldap_default_server_configuration(self, provider: str) -> dict:
        """
        Returns default server configuration for cloud identity provider by
        provider name

        :param provider: Cloud identity provider name
        """
        endpoint = f"/api/v2/cloud-ldaps/defaults/{provider}/server-configuration"

        return self._get(endpoint)

    def get_cloud_ldap_default_mappings(self, provider: str) -> dict:
        """
        Returns default mapping configuration for cloud identity provider
        by provider name

        :param provider: Cloud identity provider name
        """
        endpoint = f"/api/v2/cloud-ldaps/defaults/{provider}/mappings"

        return self._get(endpoint)

    def get_cloud_ldap_configuration(self, id: Union[int, str]) -> dict:
        """
        Returns the cloud identity provider configuration by ID

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}"

        return self._get(endpoint)

    def get_cloud_ldap_mappings(self, id: Union[int, str]) -> dict:
        """
        Returns the cloud identity provider mappings configuratiion by ID

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}/mappings"

        return self._get(endpoint)

    def get_cloud_ldap_connection_status(self, id: Union[int, str]) -> dict:
        """
        Returns the cloud identity provider connection status

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}/connection/status"

        return self._get(endpoint)

    def get_cloud_ldap_bind_connection_pool(self, id: Union[int, str]) -> dict:
        """
        Returns the cloud identity provider bind connection pool statistics

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}/connection/bind"

        return self._get(endpoint)

    def get_cloud_ldap_search_connection_pool(self, id: Union[int, str]) -> dict:
        """
        Returns the cloud identity provider search connection pool statistics

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}/connection/search"

        return self._get(endpoint)

    def create_cloud_ldap_configuration(self, data: dict) -> dict:
        """
        Creates new Cloud Identity Provider configuration with unique display
        name. If mappings not provided, then defaults will be generated
        instead.

        :param data: JSON data to create the cloud LDAP configuration with
        """
        endpoint = "/api/v2/cloud-ldaps"

        return self._post(endpoint, data)

    def create_cloud_ldap_keystore_validation(self, data: dict) -> dict:
        """
        Validates keystore for Cloud Identity Provider secure connection

        :param data: JSON data to create validation of keystore with
        """
        endpoint = "/api/v1/ldap-keystore/verify"

        return self._post(endpoint, data)

    def update_cloud_ldap_configuration(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates Cloud Identity Provider configuration. Cannot be used for
        partial updates, all content body params must be sent.

        :param data: JSON data to update the cloud LDAP configuration with
        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}"

        return self._put(endpoint, data)

    def update_cloud_ldap_mappings_configuration(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Updates Cloud Identity Provider mappings configuration. Cannot be used
        for partial updates, all content body params must be sent.

        :param data:
            JSON data to update the cloud LDAP mappings coniguration with
        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}/mappings"

        return self._put(endpoint, data)

    def delete_cloud_ldap_configuration(self, id: Union[int, str]) -> str:
        """
        Deletes Cloud Identity Provider configuration.

        :param id: Cloud identity provider ID
        """
        endpoint = f"/api/v2/cloud-ldaps/{id}"

        return self._delete(
            endpoint,
            success_message=f"Cloud LDAP configuration {id} successfully deleted.",
        )

    """
    computer-groups
    """

    def get_computer_groups(self) -> dict:
        """
        Returns all computer groups in JSON
        """
        endpoint = "/api/v1/computer-groups"

        return self._get(endpoint)

    """
    computer-inventory
    """

    def get_computer_inventories(
        self,
        section: List[str] = None,
        page: int = None,
        page_size: int = None,
        sort: List[str] = None,
        filter: str = None,
    ) -> dict:
        """
        Returns paginated list of computer inventory records
        :param section:
            Section of computer details, if not specified, General section
            data is returned. Multiple section parameters are supported,

            Options:
            ALL, GENERAL, DISK_ENCRYPTION, PURCHASING, APPLICATIONS, STORAGE,
            USER_AND_LOCATION, CONFIGURATION_PROFILES, PRINTERS, SERVICES,
            HARDWARE, LOCAL_USER_ACCOUNTS, CERTIFICATES, ATTACHMENTS,
            PLUGINS, PACKAGE_RECEIPTS, FONTS, SECURITY, OPERATING_SYSTEM,
            LICENSED_SOFTWARE, IBEACONS, SOFTWARE_UPDATES,
            EXTENSION_ATTRIBUTES, CONTENT_CACHING, GROUP_MEMBERSHIPS

            Example ["GENERAL", "HARDWARE"]

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            is general.name:asc. Multiple sort criteria are supported and must
            be separated with a comma.

            Fields allowed in the sort:
            general.name, udid, id, general.assetTag,
            general.jamfBinaryVersion, general.lastContactTime,
            general.lastEnrolledDate, general.lastCloudBackupDate,
            general.reportDate, general.remoteManagement.managementUsername,
            general.mdmCertificateExpiration, general.platform,
            hardware.make, hardware.model, operatingSystem.build,
            operatingSystem.name, operatingSystem.version,
            userAndLocation.realname, purchasing.lifeExpectancy,
            purchasing.warrantyDate

            Example: ["udid:desc", "general.name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter computer inventory
            collection. Default filter is empty query - returning all results
            for the requested page. This param can be combined with paging and
            sorting.

            Fields allowed in the query:
            general.name, udid, id, general.assetTag, general.barcode1,
            general.barcode2, general.enrolledViaAutomatedDeviceEnrollment,
            general.lastIpAddress, general.itunesStoreAccountActive,
            general.jamfBinaryVersion, general.lastContactTime,
            general.lastEnrolledDate, general.lastCloudBackupDate,
            general.reportDate, general.lastReportedIp,
            general.remoteManagement.managed, general.
            remoteManagement.managementUsername,
            general.mdmCapable.capable, general.mdmCertificateExpiration,
            general.platform, general.supervised, general.userApprovedMdm,
            hardware.bleCapable, hardware.macAddress, hardware.make,
            hardware.model, hardware.modelIdentifier, hardware.serialNumber,
            hardware.supportsIosAppInstalls, hardware.isAppleSilicon,
            operatingSystem.activeDirectoryStatus,
            operatingSystem.fileVault2Status, operatingSystem.build,
            operatingSystem.name, operatingSystem.version,
            operatingSystem.softwareUpdateDeviceId,
            security.activationLockEnabled, security.recoveryLockEnabled,
            security.firewallEnabled, userAndLocation.buildingId,
            userAndLocation.departmentId, userAndLocation.email,
            userAndLocation.realname, userAndLocation.phone,
            userAndLocation.position, userAndLocation.room,
            userAndLocation.username, purchasing.appleCareId,
            purchasing.lifeExpectancy, purchasing.purchased, purchasing.leased,
            purchasing.vendor, purchasing.warrantyDate

            Example: general.name=="Orchard"
        """
        if section == ["ALL"]:
            section = [
                "GENERAL",
                "DISK_ENCRYPTION",
                "PURCHASING",
                "APPLICATIONS",
                "STORAGE",
                "USER_AND_LOCATION",
                "CONFIGURATION_PROFILES",
                "PRINTERS",
                "SERVICES",
                "HARDWARE",
                "LOCAL_USER_ACCOUNTS",
                "CERTIFICATES",
                "ATTACHMENTS",
                "PLUGINS",
                "PACKAGE_RECEIPTS",
                "FONTS",
                "SECURITY",
                "OPERATING_SYSTEM",
                "LICENSED_SOFTWARE",
                "IBEACONS",
                "SOFTWARE_UPDATES",
                "EXTENSION_ATTRIBUTES",
                "CONTENT_CACHING",
                "GROUP_MEMBERSHIPS",
            ]
        params = remove_empty_params(
            {
                "section": section,
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v1/computers-inventory"

        return self._get(endpoint, params=params)

    def get_computer_inventory(self, id: Union[int, str]) -> dict:
        """
        Returns general section of a computer by ID

        :param id: Computer ID
        """
        endpoint = f"/api/v1/computers-inventory/{id}"

        return self._get(endpoint)

    def get_computer_inventory_detail(self, id: Union[int, str]) -> dict:
        """
        Returns all sections of a computer by ID

        :param id: Computer ID
        """
        endpoint = f"/api/v1/computers-inventory-detail/{id}"

        return self._get(endpoint)

    def get_computer_inventory_filevaults(
        self, page: int = None, page_size: int = None
    ) -> dict:
        """
        BETA: THIS ENDPOINT ONLY WORKS ON BETA INSTANCES

        Returns paginated FileVault information for all computers

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
            }
        )
        endpoint = "/api/v1/computers-inventory/filevault"

        return self._get(endpoint, params=params)

    def get_computer_inventory_filevault(self, id: Union[int, str]) -> dict:
        """
        BETA: THIS ENDPOINT ONLY WORKS ON BETA INSTANCES

        Returns FileVault information for a specific computer

        :param id: Computer ID
        """
        endpoint = f"/api/v1/computers-inventory/{id}/filevault"

        return self._get(endpoint)

    def get_computer_inventory_recovery_lock_password(
        self, id: Union[int, str]
    ) -> dict:
        """
        Returns a computers recovery lock password by ID in JSON

        :param id: Computer ID
        """
        endpoint = f"/api/v1/computers-inventory/{id}/view-recovery-lock-password"

        return self._get(endpoint)

    def get_computer_inventory_attachment(
        self, id: Union[int, str], attachmentId: Union[int, str]
    ) -> str:
        """
        Downloads specified attachment file by the ID of the computer and ID
        of the attachment

        :param id: Computer ID
        :param attachmentID: Attachment ID
        """
        endpoint = f"/api/v1/computers-inventory/{id}/attachments/{attachmentId}"

        return self._download(endpoint)

    def create_computer_inventory_attachment(
        self, filepath: str, id: Union[int, str]
    ) -> str:
        """
        Uploads attachment to a specified computer by ID

        :param filepath: Filepath to the file to upload
        :param id: Computer ID
        """
        filename = basename(filepath)
        content_type = guess_type(filename.lower())[0]
        file = {"file": (filename, open(filepath, "rb"), content_type)}

        endpoint = f"/api/v1/computers-inventory/{id}/attachments"

        return self._post(
            endpoint,
            file=file,
            data_type=None,
            success_message="File uploaded successfully.",
        )

    def update_computer_inventory(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates specific fields on a computer by ID, then returns the updated
        computer object in JSON

        :param data: JSON data to update the computer with
        :param id: Computer ID
        """
        endpoint = f"/api/v1/computers-inventory-detail/{id}"

        return self._put(endpoint, data)

    def delete_computer_inventory(self, id: Union[int, str]) -> str:
        """
        Deletes specified computer record by ID

        :param id: Computer ID
        """
        endpoint = f"/api/v1/computers-inventory/{id}"

        return self._delete(
            endpoint, success_message=f"Computer {id} successfully deleted."
        )

    def delete_computer_inventory_attachment(
        self, id: Union[int, str], attachmentId: str
    ) -> str:
        """
        Deletes specified computer attachment by computer ID and computer
        attachment ID

        :param id: Computer ID
        :param attachmnetId: Computer attachment ID
        """
        endpoint = f"/api/v1/computers-inventory/{id}/attachments/{attachmentId}"

        return self._delete(
            endpoint,
            success_message=(
                f"Attachment {attachmentId} from computer {id} successfully deleted."
            ),
        )

    """
    computer-inventory-collection-settings
    """

    def get_computer_inventory_collection_settings(self) -> dict:
        """
        Returns computer inventory collection settings in JSON
        """
        endpoint = "/api/v1/computer-inventory-collection-settings"

        return self._get(endpoint)

    def create_computer_inventory_collection_settings_custom_path(
        self, data: dict
    ) -> dict:
        """
        Creates a custom search path to use when collecting applications,
        fonts, and plug-ins.

        :param data:
            JSON data to create computer inventory collection settings  custom
            path with
        """
        endpoint = "/api/v1/computer-inventory-collection-settings/custom-path"

        return self._post(endpoint, data)

    def update_computer_inventory_collection_settings(self, data: dict) -> dict:
        """
        Updates computer inventory settings

        :param data:
            JSON data to update computer inventory collection settings with
        """
        endpoint = "/api/v1/computer-inventory-collection-settings"

        return self._put(endpoint, data)

    def delete_computer_inventory_collection_settings_custom_path(
        self, id: Union[int, str]
    ) -> str:
        """
        Deletes Custom Path from Computer Inventory Collection Settings

        :param id: Custom path ID
        """
        endpoint = f"/api/v1/computer-inventory-collection-settings/custom-path/{id}"

        return self._delete(
            endpoint,
            success_message=(
                f"Computer inventory collection settings custom path {id} "
                "successfully deleted."
            ),
        )

    """
    computer-prestages
    """

    def get_computer_prestages(
        self, page: int = None, page_size: int = None, sort: List[str] = ["id:desc"]
    ) -> dict:
        """
        Returns sorted and paged computer prestages

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            is id:desc. Multiple sort criteria are supported and must
            be separated with a comma.

            Example: ["id:desc", "enrollmentCustomizationId:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v2/computer-prestages"

        return self._get(endpoint, params=params)

    def get_computer_prestage_scopes(self) -> dict:
        """
        Returns all device scopes for all computer prestages
        """
        endpoint = "/api/v2/computer-prestages/scope"

        return self._get(endpoint)

    def get_computer_prestage(self, id: Union[int, str]) -> dict:
        """
        Returns a computer prestage with the supplied ID

        :param id: Computer prestage ID
        """
        endpoint = f"/api/v2/computer-prestages/{id}"

        return self._get(endpoint)

    def get_computer_prestage_scope(self, id: Union[int, str]) -> dict:
        """
        Returns device scope for a specified computer prestage by ID

        :param id: Computer prestage ID
        """
        endpoint = f"/api/v2/computer-prestages/{id}/scope"

        return self._get(endpoint)

    def create_computer_prestage(self, data: dict) -> dict:
        """
        Creates a computer prestage with supplied JSON data

        :param data: JSON data to create computer prestage with
        """
        endpoint = "/api/v2/computer-prestages"

        return self._post(endpoint, data)

    def create_computer_prestage_scope(self, data: dict, id: Union[int, str]) -> dict:
        """
        Adds device(s) to a specific computer prestage's scope by ID

        :param data: JSON data to create the new computer prestage scope with
        :param id: Computer prestage scope
        """
        endpoint = f"/api/v2/computer-prestages/{id}/scope"

        return self._post(endpoint, data)

    def update_computer_prestage(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates a computer prestage by ID with JSON data

        :param data: JSON data to update the computer prestage with
        :param id: Computer prestage ID
        """
        endpoint = f"/api/v2/computer-prestages/{id}"

        return self._put(endpoint, data)

    def replace_computer_prestage_scope(self, data: dict, id: Union[int, str]) -> dict:
        """
        Replaces device scope for a specified computer prestage

        :param data: JSON data to place the computer prestage scope with
        :param id: Computer prestage ID
        """
        endpoint = f"/api/v2/computer-prestages/{id}/scope"

        return self._put(endpoint, data)

    def delete_computer_prestage(self, id: Union[int, str]) -> str:
        """
        Deletes a computer prestage with the supplied ID

        :param id: Computer prestage ID
        """
        endpoint = f"/api/v2/computer-prestages/{id}"

        return self._delete(
            endpoint, success_message=f"Computer prestage {id} successfully deleted."
        )

    def delete_computer_prestage_scope(self, data: dict, id: Union[int, str]) -> dict:
        """
        Removes device scope for a specified computer prestage by ID

        :param data: JSON data to remove the computer prestage scope with
        :param id: Computer prestage ID
        """
        endpoint = f"/api/v2/computer-prestages/{id}/scope/delete-multiple"

        return self._post(endpoint, data)

    """
    computers-preview
    """

    def get_computers(
        self, page: int = None, page_size: int = None, section: List[str] = ["name:asc"]
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Returns a paginated list of computers

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param section:
            Sorting criteria in the format: property:asc/desc. Default sort is
            name:asc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["id:desc", "name:asc"]
        """
        endpoint = "/api/preview/computers"

        return self._get(endpoint)

    """
    conditional-access
    """

    def get_conditional_access_computer(self, id: Union[int, str]) -> dict:
        """
        Returns basic compliance information for the given computer by ID

        :param id: Computer ID
        """
        endpoint = (
            f"/api/v1/conditional-access/device-compliance-information/computer/{id}"
        )

        return self._get(endpoint)

    def get_conditional_access_mobile_device(self, id: Union[int, str]) -> dict:
        """
        Returns basic compliance information for the given mobile device by ID

        :param id: Mobile device ID
        """
        endpoint = (
            f"/api/v1/conditional-access/device-compliance-information/mobile/{id}"
        )

        return self._get(endpoint)

    """
    csa
    """

    def get_csa(self) -> dict:
        """
        Returns details regarding the CSA token exchange
        """
        endpoint = "/api/v1/csa/token"

        return self._get(endpoint)

    def create_csa(self, data: dict) -> dict:
        """
        Initializes the CSA token exchange - This will allow Jamf Pro to
        authenticate with cloud-hosted services

        :param data: JSON data to initialize the CSA token exchange with
        """
        endpoint = "/api/v1/csa/token"

        return self._post(endpoint, data)

    def update_csa(self, data: dict) -> dict:
        """
        Re-initializes the CSA token exchange with new credentials

        :param data: JSON data to re-initialize the CSA token exchange with
        """
        endpoint = "/api/v1/csa/token"

        return self._put(endpoint, data)

    def delete_csa(self) -> str:
        """
        Deletes the CSA token exchange - This will disable Jamf Pro's ability
        to authenticate with cloud-hosted services
        """
        endpoint = "/api/v1/csa/token"

        return self._delete(
            endpoint, success_message="CSA Token Exchange successfully deleted."
        )

    """
    departments
    """

    def get_departments(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns a paginated list of departments

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter department collection.
            Default filter is empty query - returning all results for the
            requested page. Fields allowed in the query: id, name.

            Example: name=="department"
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v1/departments"

        return self._get(endpoint, params=params)

    def get_department(self, id: Union[int, str]) -> dict:
        """
        Returns specified department

        :param id: Department ID
        """
        endpoint = f"/api/v1/departments/{id}"

        return self._get(endpoint)

    def get_department_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns specified, paginated department history

        :param id: Department ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "note:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: username,
            date, note, details. This param can be combined with paging and
            sorting.

            Example: username!=admin and details==disabled and date<2019-12-15
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = f"/api/v1/departments/{id}/history"

        return self._get(endpoint, params=params)

    def create_department(self, data: dict) -> dict:
        """
        Creates department record with JSON data

        :param data: JSON data to create the department with
        """
        endpoint = "/api/v1/departments"

        return self._post(endpoint, data)

    def create_department_history_note(self, data: dict, id: Union[int, str]) -> dict:
        """
        Creates note in specifed department history with JSON data

        :param data: JSON data to create department history note with
        :param id: Department ID
        """
        endpoint = f"/api/v1/departments/{id}/history"

        return self._post(endpoint, data)

    def update_department(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates specified department by ID with JSON data

        :param data: JSON data to update department with
        :param id: Department ID
        """
        endpoint = f"/api/v1/departments/{id}"

        return self._put(endpoint, data)

    def delete_department(
        self, id: Union[int, str] = None, ids: List[Union[int, str]] = None
    ) -> str:
        """
        Deletes a department search by ID or IDS, use id for a single device
        and ids to delete multiple.

        :param id: Department ID
        :param ids: List of department IDs
        """
        identifier_options = {"id": id, "ids": ids}
        identification_type(identifier_options)
        check_conflicting_params(identifier_options)
        if id:
            if enforce_type(id, (str, int)):
                endpoint = f"/api/v1/departments/{id}"
                return self._delete(
                    endpoint,
                    success_message=(f"Department {id} successfully deleted."),
                )
        if ids:
            if enforce_type(ids, (List)):
                ids = [str(id) for id in ids]
                endpoint = "/api/v1/departments/delete-multiple"
                return self._post(
                    endpoint,
                    data={"ids": ids},
                    success_message=(
                        f"Department(s) {', '.join(ids)} successfully deleted."
                    ),
                )

    """
    device-communication-settings
    """

    def get_device_communication_settings(self):
        """
        Returns all device communication settings, including automatic renewal
        of the MDM profile.
        """
        endpoint = "/api/v1/device-communication-settings"

        return self._get(endpoint)

    def get_device_communication_settings_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns paginated device communication settings history

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: username,
            date, note, details. This param can be combined with paging and
            sorting.

            Example: username!=admin and details==disabled and date<2019-12-15
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v1/device-communication-settings/history"

        return self._get(endpoint, params=params)

    def create_device_communication_settings_history_note(self, data: dict) -> dict:
        """
        Creates a note on the device communication settings history by JSON
        data

        :param data:
            JSON data to create the device communication settings history note
        """
        endpoint = "/api/v1/device-communication-settings/history"

        return self._post(endpoint, data)

    def update_device_communication_settings(self, data: dict) -> dict:
        """
        Updates device communication settings with JSON

        :param data: JSON data to update device communication settings with
        """
        endpoint = "/api/v1/device-communication-settings"

        return self._put(endpoint, data)

    """
    device-enrollments
    """

    def get_device_enrollments(
        self, page: int = None, page_size: int = None, sort: List[str] = ["id:asc"]
    ) -> dict:
        """
        Returns sorted and paged device enrollment instances

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "name:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/device-enrollments"

        return self._get(endpoint, params=params)

    def get_device_enrollment(self, id: Union[int, str]) -> dict:
        """
        Returns a device enrollment instance with the supplied ID

        :param id: Device enrollment instance ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}"

        return self._get(endpoint)

    def get_device_enrollment_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns sorted and paged device enrollment history by ID in JSON

        :param id: Device enrollment instance ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "note:asc"]
        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default search is empty query - returning all results
            for the requested page. Fields allowed in the query: username,
            date, note, details. This param can be combined with paging and
            sorting.

            Example: username!=admin and details==disabled and date<2019-12-15
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = f"/api/v1/device-enrollments/{id}/history"

        return self._get(endpoint, params=params)

    def get_device_enrollments_public_key(self) -> str:
        """
        Returns the Jamf Pro device enrollment public key in a string
        """
        endpoint = "/api/v1/device-enrollments/public-key"

        return self._get(endpoint, data_type=None)

    def get_device_enrollments_instance_sync_states(self) -> dict:
        """
        Returns all device enrollments instance sync states
        """
        endpoint = "/api/v1/device-enrollments/syncs"

        return self._get(endpoint)

    def get_device_enrollment_instance_sync_states(self, id: Union[int, str]) -> dict:
        """
        Returns all instance sync states for a single instance by ID

        :param id: Device enrollment ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}/syncs"

        return self._get(endpoint)

    def get_device_enrollment_instance_sync_state_latest(
        self, id: Union[int, str]
    ) -> dict:
        """
        Returns the latest sync state for a single device enrollment

        :param id: Device enrollment ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}/syncs/latest"

        return self._get(endpoint)

    def create_device_enrollment(self, data: dict) -> dict:
        """
        Creates a device enrollment instance with JSON data

        :param data: JSON data to create the device enrollment instance with
        """
        endpoint = "/api/v1/device-enrollments/upload-token"

        return self._post(endpoint, data)

    def create_device_enrollment_history_note(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a device enrollment history note by ID with JSON data

        :param data:
            JSON data to create the device enrollment history note with
        :param id: Device enrollment ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}/history"

        return self._post(endpoint, data)

    def update_device_enrollment(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates a Device Enrollment Instance by ID with JSON data

        :param data: JSON data to update device enrollment instance with
        :param id: Device enrollment ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}"

        return self._put(endpoint, data)

    def update_device_enrollment_token(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates a device enrollment instance with the supplied token by ID with
        JSON

        :param data: JSON data to update device enrollment instance with
        :param id: Device enrollment ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}/upload-token"

        return self._put(endpoint, data)

    def delete_device_enrollment(self, id: Union[int, str]) -> str:
        """
        Deletes a device enrollment instance by ID

        :param id: Device enrollment ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}"

        return self._delete(
            endpoint,
            success_message=f"Device enrollment instance {id} successfully deleted.",
        )

    def delete_device_enrollment_device(self, data: dict, id: Union[int, str]) -> dict:
        """
        Disowns devices from the given device enrollment instance by ID with
        JSON

        :param data: JSON data to disown device enrollment devices with
        :param id: Device Enrollment ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}/disown"

        return self._post(endpoint, data)

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
