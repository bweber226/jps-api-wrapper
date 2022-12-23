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

    def get_app_dynamics_configuration(self) -> dict:
        """
        Returns AppDynamicsConfig object
        """
        endpoint = "/api/v1/app-dynamics/script-configuration"

        return self._get(endpoint)

    """
    app-request-preview
    """

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

            Example: ["date:desc", "note:asc"]

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
        Deletes a department search by ID or IDS, use id for a single
        department and ids to delete multiple.

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

    def get_device_enrollments_devices(self, id: Union[int, str]) -> dict:
        """
        Returns all devices assigned to the device enrollment instance by ID

        :param id: Device enrollment instance ID
        """
        endpoint = f"/api/v1/device-enrollments/{id}/devices"

        return self._get(endpoint)

    """
    ebooks
    """

    def get_ebooks(
        self, page: int = None, page_size: int = None, sort: List[str] = ["name:asc"]
    ) -> dict:
        """
        Returns sorted, paginated list of all eBooks

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            name:asc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["id:desc", "name:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/ebooks"

        return self._get(endpoint, params=params)

    def get_ebook(self, id: Union[int, str]) -> dict:
        """
        Returns the specified eBook by ID

        :param id: eBook ID
        """
        endpoint = f"/api/v1/ebooks/{id}"

        return self._get(endpoint)

    def get_ebook_scope(self, id: Union[int, str]) -> dict:
        """
        Returns the scope of the specified eBook by ID

        :param id: eBook ID
        """
        endpoint = f"/api/v1/ebooks/{id}/scope"

        return self._get(endpoint)

    """
    engage
    """

    def get_engage_settings(self) -> dict:
        """
        Returns Engage settings
        """
        endpoint = "/api/v1/engage"

        return self._get(endpoint)

    def get_engage_settings_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns Engage settings history

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "name:asc"]
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
        endpoint = "/api/v1/engage/history"

        return self._get(endpoint, params=params)

    def create_engage_settings_history_note(self, data: dict) -> dict:
        """
        Creates Engage settings history notes with JSON

        :param data: JSON data to create Engage settings history notes with
        """
        endpoint = "/api/v1/engage/history"

        return self._post(endpoint, data)

    def update_engage_settings(self, data: dict) -> dict:
        """
        Updates Engage settings with JSON

        :param data: JSON data to update the engage settings with
        """
        endpoint = "/api/v1/engage"

        return self._put(endpoint, data)

    """
    enrollment
    """

    def get_enrollment_settings(self) -> dict:
        """
        Returns Enrollment object and re-enrollment settings
        """
        endpoint = "/api/v2/enrollment"

        return self._get(endpoint)

    def get_enrollment_history(
        self, page: int = None, page_size: int = None, sort: List[str] = None
    ) -> dict:
        """
        Returns sorted and paged enrollment history

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            is date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "note:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v2/enrollment/history"

        return self._get(endpoint, params=params)

    def get_enrollment_history_export(
        self,
        export_fields: List[str] = None,
        export_labels: List[str] = None,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns CSV export of enrollment history collection

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

            Example: ["identifier", "name" with matching export-fields
            ["id", "username"]

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:desc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "note:asc"]
        :param filter:
            Query in the RSQL format, allowing to filter history notes
            collection. Default filter is empty query - returning all results
            for the requested page. Fields allowed in the query: id, name.
            This param can be combined with paging and sorting.

            Example: username!="admin"
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
        headers = {"Content-type": "application/json", "Accept": "text/csv"}
        endpoint = "/api/v2/enrollment/history/export"

        return self._post(endpoint, params=params, headers=headers, data_type=None)

    def get_enrollment_adue_session_token_settings(self):
        """
        Returns the Account Driven User Enrollment Session Token Settings
        """
        endpoint = "/api/v1/adue-session-token-settings"

        return self._get(endpoint)

    def get_enrollment_ldap_groups(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = None,
        all_users_option_first: bool = False,
    ) -> dict:
        """
        Returns the configured LDAP groups configured for user-initiated
        enrollment

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            name:asc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["name:asc"]

        :param all_users_opton_first:
            Return "All LDAP Users" option on the first position if it is
            present in the current page

            Options: True or False
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "all-users-option-first": all_users_option_first,
            }
        )
        endpoint = "/api/v3/enrollment/access-groups"

        return self._get(endpoint, params=params)

    def get_enrollment_ldap_group(self, id: Union[int, str]) -> dict:
        """
        Returns the configured LDAP group configured for User-Initiated
        Enrollment by ID
        """
        endpoint = f"/api/v3/enrollment/access-groups/{id}"

        return self._get(endpoint)

    def get_enrollment_languages_messaging(
        self, page: int = None, page_size: int = None, sort: List[str] = None
    ) -> dict:
        """
        Returns the language codes that have enrollment messaging currently
        configured

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            languageCode:asc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["languageCode:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v3/enrollment/languages"

        return self._get(endpoint, params=params)

    def get_enrollment_language_messaging(self, languageId: str) -> dict:
        """
        Returns the enrollment messaging for a language

        :param languageId:
            Two letter ISO 639-1 Language Code

            Example: en
        """
        endpoint = f"/api/v3/enrollment/languages/{languageId}"

        return self._get(endpoint)

    def get_enrollment_language_codes(self) -> dict:
        """
        Returns all languages and corresponding ISO 639-1 codes
        """
        endpoint = "/api/v3/enrollment/language-codes"

        return self._get(endpoint)

    def get_enrollment_unused_language_codes(self) -> dict:
        """
        Returns languages and corresponding ISO 639-1 Codes, but only those not
        already added to enrollment
        """
        endpoint = "/api/v3/enrollment/filtered-language-codes"

        return self._get(endpoint)

    def create_enrollment_history_note(self, data: dict) -> dict:
        """
        Creates enrollment history object note with JSON data

        :param date: JSON data to create the enrollment history note with
        """
        endpoint = "/api/v2/enrollment/history"

        return self._post(endpoint, data)

    def create_enrollment_ldap_group(self, data: dict) -> dict:
        """
        Creates the configured LDAP group for user-initiated enrollment with
        JSON data

        :param data: JSON data to create the enrollment LDAP group with
        """
        endpoint = "/api/v3/enrollment/access-groups"

        return self._post(endpoint, data)

    def update_enrollment_settings(self, data: dict) -> dict:
        """
        Updates enrollment settings with JSON data

        :param data: JSON data to update the enrollment settings with
        """
        endpoint = "/api/v2/enrollment"

        return self._put(endpoint, data)

    def update_enrollment_adue_session_token_settings(self, data: dict) -> dict:
        """
        Updates the account driven user enrollment session token settings

        :param data:
            JSON data to update the enrollment ADUE session token settings with
        """
        endpoint = "/api/v1/adue-session-token-settings"

        return self._put(endpoint, data)

    def update_enrollment_ldap_group(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates the configured LDAP groups configured for user-initiated
        enrollment by ID with JSON data

        :param data: JSON data to update the enrollment LDAP group with
        :param id: Enrollment LDAP group ID
        """
        endpoint = f"/api/v3/enrollment/access-groups/{id}"

        return self._put(endpoint, data)

    def update_enrollment_language_messaging(self, data: dict, languageId: str) -> dict:
        """
        Updates enrollment messaging for a specified language by languageId

        :param languageId: Two letter ISO 639-1 Language Code
        """
        endpoint = f"/api/v3/enrollment/languages/{languageId}"

        return self._put(endpoint, data)

    def delete_enrollment_ldap_group(self, id: Union[int, str]) -> str:
        """
        Deletes an LDAP group's access to user initiated enrollment. The group
        "All LDAP Users" cannot be deleted, but it can be modified to disallow
        User-Initiated Enrollment.

        :param id: Enrollment LDAP group ID
        """
        endpoint = f"/api/v3/enrollment/access-groups/{id}"

        return self._delete(
            endpoint,
            success_message=f"Enrollment LDAP group {id} successfully deleted.",
        )

    def delete_enrollment_language_messaging(
        self, languageId: str = None, languageIds: List[str] = None
    ) -> str:
        """
        Deletes a enrollment language messaging search by language ID or IDS,
        use languageId for a single language and languageIds to delete multiple

        :param id: Enrollment language ID, two letter ISO 639-1 Language Code
        :param ids:
            List of enrollment language IDs, two letter ISO 639-1 Language Code
        """
        identifier_options = {"id": languageId, "ids": languageIds}
        identification_type(identifier_options)
        check_conflicting_params(identifier_options)
        if languageId:
            if enforce_type(languageId, (str)):
                endpoint = f"/api/v3/enrollment/languages/{languageId}"
                return self._delete(
                    endpoint,
                    success_message=(
                        f"Enrollment language messaging for {languageId} "
                        "successfully deleted."
                    ),
                )
        if languageIds:
            if enforce_type(languageIds, (List)):
                endpoint = "/api/v3/enrollment/languages/delete-multiple"
                return self._post(
                    endpoint,
                    data={"ids": languageIds},
                    success_message=(
                        f"Enrollment language messaging for {', '.join(languageIds)} "
                        "successfully deleted."
                    ),
                )

    """
    enrollment-customization
    """

    def get_enrollment_customizations(
        self, page: int = None, page_size: int = None, sort: List[str] = ["id:asc"]
    ) -> dict:
        """
        Returns sorted and paged enrollment customizations

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "displayName:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v2/enrollment-customizations"

        return self._get(endpoint, params=params)

    def get_enrollment_customization(self, id: Union[int, str]) -> dict:
        """
        Returns an enrollment customization by ID

        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v2/enrollment-customizations/{id}"

        return self._get(endpoint)

    def get_enrollment_customization_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
    ) -> dict:
        """
        Returns sorted and paged enrollment customization history by ID

        :param id: Enrollment customization ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["date:desc", "note:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = f"/api/v2/enrollment-customizations/{id}/history"

        return self._get(endpoint, params=params)

    def get_enrollment_customization_prestages(self, id: Union[int, str]) -> dict:
        """
        Returns prestages using the specified enrollment customization by ID

        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v2/enrollment-customizations/{id}/prestages"

        return self._get(endpoint)

    def get_enrollment_customization_image(self, id: Union[int, str]) -> dict:
        """
        BETA: THIS ENDPOINT ONLY WORKS ON BETA INSTANCES

        Downloads the specified enrollment customization image to the current
        users Downloads folder

        :param id: Enrollment customization image ID
        """
        endpoint = f"/api/v2/enrollment-customizations/images/{id}"

        return self._download(endpoint)

    def create_enrollment_customization(self, data: dict) -> dict:
        """
        Creates an enrollment customization with JSON data

        :param data: JSON data to create the enrollment customization with
        """
        endpoint = "/api/v2/enrollment-customizations"

        return self._post(endpoint, data)

    def create_enrollment_customization_history_note(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates enrollment customization history note with JSON data by ID

        :param data:
            JSON data to create the enrollment customization history note with
        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v2/enrollment-customizations/{id}/history"

        return self._post(endpoint, data)

    def create_enrollment_customization_image(self, filepath: str) -> dict:
        """
        Uploads an enrollment customization image

        :param filepath: Filepath to the file to upload
        """
        filename = basename(filepath)
        content_type = guess_type(filename.lower())[0]
        file = {"file": (filename, open(filepath, "rb"), content_type)}

        endpoint = "/api/v2/enrollment-customizations/images"

        return self._post(endpoint, file=file)

    def update_enrollment_customization(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates an enrollment customization by ID with JSON data

        :param data: JSON data to update enrollment customization with
        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v2/enrollment-customizations/{id}"

        return self._put(endpoint, data)

    def delete_enrollment_customization(self, id: Union[int, str]) -> str:
        """
        Deletes an enrollment customization by ID

        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v2/enrollment-customizations/{id}"

        return self._delete(
            endpoint,
            success_message=f"Enrollment customization {id} successfully deleted.",
        )

    """
    enrollment-customization-preview
    """

    def get_enrollment_customization_panels(self, id: Union[int, str]) -> dict:
        """
        Returns all panels for a single enrollment customization by ID

        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/all"

        return self._get(endpoint)

    def get_enrollment_customization_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Returns a single panel for a single enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: Panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/all/{panel_id}"

        return self._get(endpoint)

    def get_enrollment_customization_ldap_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Returns a single LDAP panel for a single enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: LDAP panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/ldap/{panel_id}"

        return self._get(endpoint)

    def get_enrollment_customization_sso_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Returns a single SSO panel for a single enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: SSO panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/sso/{panel_id}"

        return self._get(endpoint)

    def get_enrollment_customization_text_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Returns a single text panel for a single enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: Text panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/text/{panel_id}"

        return self._get(endpoint)

    def get_enrollment_customization_text_panel_markdown(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Returns a single text panel markdown for a single enrollment
        customization by ID

        :param id: Enrollment customization ID
        :param panel_id: SSO panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/text/{panel_id}/markdown"

        return self._get(endpoint)

    def get_enrollment_customization_parsed_markdown(self, data: str) -> dict:
        """
        Returns HTML based on provided markdown string in JSON data

        :param data: JSON data with markdown to parse into HTML
        """
        endpoint = "/api/v1/enrollment-customization/parse-markdown"

        return self._post(endpoint, data)

    def create_enrollment_customization_ldap_panel(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a LDAP panel for a single enrollment customization by ID with
        JSON. If multiple LDAP access groups are defined with the same name and
        id, only one will be saved.

        :param data:
            JSON data to create enrollment customization LDAP panel with
        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/ldap"

        return self._post(endpoint, data)

    def create_enrollment_customization_sso_panel(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a SSO panel for a single enrollment customization by ID with
        JSON data

        :param data:
            JSON data to create enrollment customization SSO panel with
        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/sso"

        return self._post(endpoint, data)

    def create_enrollment_customization_text_panel(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a text panel for a single enrollment customization by ID with
        JSON data

        :param data:
            JSON data to create enrollment customization text panel with
        :param id: Enrollment customization ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/text"

        return self._post(endpoint, data)

    def update_enrollment_customization_ldap_panel(
        self, data: dict, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Updates a single LDAP panel for a single enrollment customization by ID
        with JSON. If  multiple LDAP access groups are defined with the same
        name and id, only one will be saved.

        :param data:
            JSON data to update enrollment customization LDAP panel with
        :param id: Enrollment customization ID
        :param panel_id: LDAP panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/ldap/{panel_id}"

        return self._put(endpoint, data)

    def update_enrollment_customization_sso_panel(
        self, data: dict, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Updates a single SSO panel for a single enrollment customization by ID
        with JSON

        :param data:
            JSON data to update enrollment customization SSO panel with
        :param id: Enrollment customization ID
        :param panel_id: LDAP panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/sso/{panel_id}"

        return self._put(endpoint, data)

    def update_enrollment_customization_text_panel(
        self, data: dict, id: Union[int, str], panel_id: Union[int, str]
    ) -> dict:
        """
        Updates a single text panel for a single enrollment customization by ID
        with JSON

        :param data:
            JSON data to update enrollment customization text panel with
        :param id: Enrollment customization ID
        :param panel_id: Text panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/text/{panel_id}"

        return self._put(endpoint, data)

    def delete_enrollment_customization_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> str:
        """
        Deletes a single panel from an enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: Panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/all/{panel_id}"

        return self._delete(
            endpoint,
            success_message=(
                f"Panel {panel_id} of enrollment customization {id} "
                "successfully deleted."
            ),
        )

    def delete_enrollment_customization_ldap_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> str:
        """
        Deletes a single LDAP panel from an enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: LDAP panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/ldap/{panel_id}"

        return self._delete(
            endpoint,
            success_message=(
                f"LDAP panel {panel_id} of enrollment customization {id} "
                "successfully deleted."
            ),
        )

    def delete_enrollment_customization_sso_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> str:
        """
        Deletes a single SSO panel from an enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: SSO panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/sso/{panel_id}"

        return self._delete(
            endpoint,
            success_message=(
                f"SSO panel {panel_id} of enrollment customization {id} "
                "successfully deleted."
            ),
        )

    def delete_enrollment_customization_text_panel(
        self, id: Union[int, str], panel_id: Union[int, str]
    ) -> str:
        """
        Deletes a single text panel from an enrollment customization by ID

        :param id: Enrollment customization ID
        :param panel_id: Text panel ID
        """
        endpoint = f"/api/v1/enrollment-customization/{id}/text/{panel_id}"

        return self._delete(
            endpoint,
            success_message=(
                f"Text panel {panel_id} of enrollment customization {id} "
                "successfully deleted."
            ),
        )

    """
    icon
    """

    def get_icon(self, id: Union[int, str]) -> dict:
        """
        Returns information on on a specified icon by ID

        :param id: Icon ID
        """
        endpoint = f"/api/v1/icon/{id}"

        return self._get(endpoint)

    def get_icon_image(
        self, id: Union[int, str], resolution: str = None, scale: str = None
    ) -> str:
        """
        BETA: THIS ENDPOINT ONLY WORKS ON BETA INSTANCES
        BETA: THIS ENDPOINT CURRENTLY DOES NOT WORK

        Downloads a self service icon by ID along with res and scale options

        :param id: Self service icon ID
        :param resolution:
            Request a specific resolution of original, 300, or 512; invalid
            options will result in original resolution
        :param scale:
            Request a scale; 0 results in original image, non-0 results in
            scaled to 300
        """
        params = remove_empty_params(
            {
                "res": resolution,
                "scale": scale,
            }
        )
        endpoint = f"/api/v1/icon/download/{id}"

        return self._download(endpoint, params=params)

    def create_icon(self, filepath: str) -> dict:
        """
        Uploads an icon with the specified local filepath

        :param filepath:
        """
        filename = basename(filepath)
        content_type = guess_type(filename.lower())[0]
        file = {"file": (filename, open(filepath, "rb"), content_type)}
        endpoint = "/api/v1/icon"

        return self._post(endpoint, file=file)

    """
    inventory-information
    """

    def get_inventory_information(self):
        """
        Returns statistics about managed/unmanaged devices and computers in the
        inventory
        """
        endpoint = "/api/v1/inventory-information"

        return self._get(endpoint)

    """
    inventory-preload
    """

    def get_inventory_preloads(
        self,
        page: int = None,
        page_size: int = None,
        sort: str = ["id:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns paged and sorted inventory preload records

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            is id:asc. Multiple sort criteria are supported and must be
            separated with a comma. All inventory preload fields are supported,
            however fields added by extension attributes are not supported. If
            sorting by deviceType, use 0 for Computer and 1 for Mobile Device.

            Example: ["id:desc", "deviceType:1"]

        :param filter:
            Allowing to filter inventory preload records. Default search is
            empty query - returning all results for the requested page.
            All inventory preload fields are supported, however fields added by
            extension attributes are not supported. If filtering by deviceType,
            use 0 for Computer and 1 for Mobile Device. Query in the RSQL
            format, allowing ==, !=, >, <, and =in=.

            Example: username=="admin"
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v2/inventory-preload/records"

        return self._get(endpoint, params=params)

    def get_inventory_preload(self, id: Union[int, str]) -> dict:
        """
        Returns an inventory preload record by ID

        :param id: Inventory preload ID
        """
        endpoint = f"/api/v2/inventory-preload/records/{id}"

        return self._get(endpoint)

    def get_inventory_preloads_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: str = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns inventory preload history entries

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            is date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "note:asc"]

        :param filter:
            Allows filtering inventory preload history records. Default search
            is empty query - returning all results for the requested page. All
            inventory preload history fields are supported. Query in the RSQL
            format, allowing ==, !=, >, <, and =in=.

            Example: username=="admin"
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v2/inventory-preload/history"

        return self._get(endpoint, params=params)

    def get_inventory_preloads_extension_attributes(self) -> dict:
        """
        Returns extension attribute columns currently associated with inventory
        preload records
        """
        endpoint = "/api/v2/inventory-preload/ea-columns"

        return self._get(endpoint)

    def get_inventory_preloads_csv_template(self) -> str:
        """
        Returns the inventory preload CSV file template
        """
        endpoint = "/api/v2/inventory-preload/csv-template"

        return self._get(endpoint, data_type=None)

    def get_inventory_preloads_csv(self) -> str:
        """
        Returns the inventory preload records as CSV data
        """
        endpoint = "/api/v2/inventory-preload/csv"

        return self._get(endpoint, data_type=None)

    # TODO export_fields and export_labels are not actually working correctly
    def get_inventory_preloads_export(
        self,
        export_fields: List[str] = None,
        export_labels: List[str] = None,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> str:
        """
        Exports a collection of inventory preload records in CSV format

        :param export_fields:
            Export fields parameter, used to change default order or ignore
            some of the response properties. Default is empty array, which
            means that all fields of the response entity will be serialized.

            Example: ["username", "department"]

        :param export_labels:
            Export labels parameter, used to customize fieldnames/columns in
            the exported file. Default is empty array, which means that
            response properties names will be used. Number of the provided
            labels must match the number of export-fields

            Example: export_labels=["name", "dept"] with matching:
            export_fields=["username", "department"]

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["department:desc", "username:asc"]

        :param filter:
            Allows filtering inventory preload history records. Default search
            is empty query - returning all results for the requested page. All
            inventory preload history fields are supported. Query in the RSQL
            format, allowing ==, !=, >, <, and =in=.

            Example: username=="admin"
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
        headers = {"Content-type": "application/json", "Accept": "text/csv"}
        endpoint = "/api/v2/inventory-preload/export"

        return self._post(endpoint, params=params, headers=headers, data_type=None)

    def create_inventory_preload(self, data: dict) -> dict:
        """
        Creates an inventory preload record with JSON

        :param data: JSON data to create inventory preload record with
        """
        endpoint = "/api/v2/inventory-preload/records"

        return self._post(endpoint, data)

    def create_inventory_preloads_history_note(self, data: dict) -> dict:
        """
        Creates inventory preload history note

        :param data: JSON data to create inventory preload history note with
        """
        endpoint = "/api/v2/inventory-preload/history"

        return self._post(endpoint, data)

    def create_inventory_preloads_csv_validation(self, filepath: str) -> dict:
        """
        Validates a given CSV file. Serial number and device type are required.
        All other fields are optional. A CSV template can be downloaded from
        Pro.get_inventory_preloads_csv_template

        :param filepath: Path to CSV file to be validated
        """
        filename = basename(filepath)
        content_type = guess_type(filename.lower())[0]
        file = {"file": (filename, open(filepath, "rb"), content_type)}
        endpoint = "/api/v2/inventory-preload/csv-validate"

        return self._post(endpoint, file=file)

    def create_inventory_preloads_csv(self, filepath: str) -> dict:
        """
        Creates one or more new Inventory Preload records using CSV.
        A CSV template can be downloaded from
        /v2/inventory-preload/csv-template. Serial number and device type are
        required. All other fields are optional. When a matching serial number
        exists in the Inventory Preload data, the record will be overwritten
        with the CSV data. If the CSV file contains a new username and an email
        address is provided, the new user is created in Jamf Pro. If the CSV
        file contains an existing username, the following user-related fields
        are updated in Jamf Pro. Full Name, Email Address, Phone Number,
        Position. This endpoint does not do full validation of each record in
        the CSV data. To do full validation, use the
        Pro.create_inventory_preloads_csv_validation module first.

        :param filepath:
            Path to the CSV file use for inventory preload creation
        """
        filename = basename(filepath)
        content_type = guess_type(filename.lower())[0]
        file = {"file": (filename, open(filepath, "rb"), content_type)}
        endpoint = "/api/v2/inventory-preload/csv"

        return self._post(endpoint, file=file)

    def update_inventory_preload(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates an inventory preload record by ID with JSON

        :param data: JSON data to update inventory preload with
        :param id: Inventory preload ID
        """
        endpoint = f"/api/v2/inventory-preload/records/{id}"

        return self._put(endpoint, data)

    def delete_inventory_preload(self, id: Union[int, str]) -> str:
        """
        Deletes an inventory preload record by ID

        :param id: Inventory preload ID
        """
        endpoint = f"/api/v2/inventory-preload/records/{id}"

        return self._delete(
            endpoint, success_message=f"Inventory preload {id} successfully deleted."
        )

    def delete_inventory_preloads_all(self) -> str:
        """
        Deletes all inventory preload records
        """
        endpoint = "/api/v2/inventory-preload/records/delete-all"

        return self._post(
            endpoint, success_message="All inventory preloads successfully deleted."
        )

    """
    jamf-connect
    """

    def get_jamf_connect_settings(self) -> dict:
        """
        Returns the Jamf Connect settings that you have access to see
        """
        endpoint = "/api/v1/jamf-connect"

        return self._get(
            endpoint, success_message="Success, this endpoint does not return content."
        )

    def get_jamf_connect_config_profiles(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["profileId:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns sorted, paginated config profiles linked to Jamf Connect

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            order is ["profileId:asc"]. Multiple sort criteria are supported
            and must be seperated by a comma. Options are status, updated.

            Example ["profileId:asc", "version:desc"]

        :param filter:
            Query in the RSQL format, allowing to filter results. Default
            filter is empty query - returning all results for the requested
            page. Fields allowed in the query: status, updated, version This
            param can be combined with paging and sorting.

            Example: profileId==1001 and version==""
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v1/jamf-connect/config-profiles"

        return self._get(endpoint, params=params)

    def get_jamf_connect_config_profile_deployment_tasks(
        self,
        uuid: str,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["status:desc"],
        filter: str = None,
    ):
        """
        Returns deployment tasks for specified config profile linked to Jamf
        Connect by ID

        :param uuid: Jamf Connect config profile UUID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            order is ["status:desc"]. Multiple sort criteria are supported
            and must be seperated by a comma. Options are status, updated.

            Example ["status:asc", "updated:desc"]

        :param filter:
            Query in the RSQL format, allowing to filter results. Default
            filter is empty query - returning all results for the requested
            page. Fields allowed in the query: status, updated, version This
            param can be combined with paging and sorting.

            Example: version==""
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = f"/api/v1/jamf-connect/deployments/{uuid}/tasks"

        return self._get(endpoint, params=params)

    def get_jamf_connect_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns sorted, paginated Jamf Connect history

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
        endpoint = "/api/v1/jamf-connect/history"
        params = remove_empty_params(
            {"page": page, "page-size": page_size, "sort": sort, "filter": filter}
        )

        return self._get(endpoint, params=params)

    def create_jamf_connect_config_profile_deployment_task_retry(
        self, data: dict, uuid: str
    ) -> str:
        """
        Requests a retry of deployment task(s) of specified Jamf Connect config
        profile by UUID with JSON

        :param data: JSON data to of deployment task ID(s) to retry
        :param uuid: Jamf Connect configuration profile UUID
        """
        endpoint = f"/api/v1/jamf-connect/deployments/{uuid}/tasks/retry"

        return self._post(
            endpoint,
            data,
            success_message=(
                f"Retrying specified tasks for Jamf Connect config profile {uuid}."
            ),
        )

    def create_jamf_connect_history_note(self, data: dict) -> dict:
        """
        Creates Jamf Connect history note with JSON

        :param data: JSON data to create Jamf Connect history note with
        """
        endpoint = "/api/v1/jamf-connect/history"

        return self._post(endpoint, data)

    def update_jamf_connect_app_update_method(self, data: dict, uuid: str) -> dict:
        """
        Updates the way the Jamf Connect app gets updated on computers with the
        scope of the specified configuration profile by UUID with JSON

        :param data: JSON data to update Jamf Connect app update method with
        :param uuid: Jamf Connect config profile UUID
        """
        endpoint = f"/api/v1/jamf-connect/config-profiles/{uuid}"

        return self._put(endpoint, data)

    """
    jamf-management-framework
    """

    def create_jamf_management_framework_redeploy(self, id: Union[int, str]):
        """
        Redeploys the Jamf Management Framework for enrolled computer by ID

        :param id: Computer ID
        """
        endpoint = f"/api/v1/jamf-management-framework/redeploy/{id}"

        return self._post(endpoint)

    """
    jamf-package
    """

    def get_jamf_package(self, application: str) -> dict:
        """
        Returns the packages for a given Jamf application by application key

        :param application:
            The Jamf Application key. The only supported values are protect
            and connect.
        """
        if application not in ["protect", "connect"]:
            raise ValueError(
                "The only supported values for application are protect and connect."
            )
        params = {"application": application}
        endpoint = "/api/v2/jamf-package"

        return self._get(endpoint, params=params)

    """
    jamf-pro-information
    """

    def get_jamf_pro_information(self) -> dict:
        """
        Returns basic information about the Jamf Pro Server
        """
        endpoint = "/api/v2/jamf-pro-information"

        return self._get(endpoint)

    """
    jamf-pro-initialization
    """

    def create_jamf_pro_initialization(self, data: dict) -> dict:
        """
        Set up a freshly installed Jamf Pro Server

        :param data: JSON data t set up Jamf Pro Server with
        """
        endpoint = "/api/v1/system/initialize"

        return self._post(endpoint, data)

    def create_jamf_pro_initialization_password(self, data: dict) -> dict:
        """
        Provides database password during startup. Endpoint is accessible when
        database password was not configured and Jamf Pro server has not been
        initialized yet.

        :param data: JSON data to provide the database password with
        """
        endpoint = "/api/v1/system/initialize-database-connection"

        return self._post(endpoint, data)

    """
    jamf-pro-initialization-preview
    """

    # All deprecated

    """
    jamf-pro-notifications
    """

    def get_jamf_pro_notifications(self) -> dict:
        """
        Returns notifications for user and site
        """
        endpoint = "/api/v1/notifications"

        return self._get(endpoint)

    def delete_jamf_pro_notifications(self, type: str, id: Union[int, str]) -> str:
        """
        Deletes notifications with give type and ID

        :param type: Type of the notification
        :param id: Instance ID of the notification
        """
        endpoint = f"/api/v1/notifications/{type}/{id}"

        return self._delete(
            endpoint,
            success_message=f"Notifications of type {type} deleted from site {id}.",
        )

    """
    jamf-pro-notifications-preview
    """

    # All deprecated

    """
    jamf-pro-server-url-preview
    """

    def get_jamf_pro_server_url_settings(self) -> dict:
        """
        Returns Jamf Pro URL settings
        """
        endpoint = "/api/v1/jamf-pro-server-url"

        return self._get(endpoint)

    def get_jamf_pro_server_url_settings_history(
        self, page: int = None, page_size: int = None, sort: List[str] = ["date:desc"]
    ) -> dict:
        """
        Returns sorted, paginated Jamf Pro Server URL settings history

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "note:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/jamf-pro-server-url/history"

        return self._get(endpoint, params=params)

    def create_jamf_pro_server_url_settings_history_note(self, data: dict) -> dict:
        """
        Creates Jamf Pro Server URL settings history note with JSON. Only
        usable on non-hosted JPS environments.

        :param data:
            JSON data to create Jamf Pro Server URL settings history note with
        """
        endpoint = "/api/v1/jamf-pro-server-url/history"

        return self._post(endpoint, data)

    def update_jamf_pro_server_url_settings(self, data: dict) -> dict:
        """
        Updates Jamf Pro Server URL settings with JSON. Only usable on
        non-hosted JPS environments.

        :param data: JSON data to update the Jamf Pro Server URL settings with
        """
        endpoint = "/api/v1/jamf-pro-server-url"

        return self._put(endpoint, data)

    """
    jamf-pro-user-account-settings
    """

    def get_jamf_pro_user_account_setting(self, keyId: str) -> dict:
        """
        Returns the user setting for the authennticated user and key by key ID

        :param keyId: User setting to be retrieved
        """
        endpoint = f"/api/v1/user/preferences/{keyId}"

        return self._get(endpoint)

    def update_jamf_pro_user_account_setting(self, data: dict, keyId: str) -> dict:
        """
        Updates the user setting with JSON by key ID

        :param data: JSON data to update user setting with
        :param keyId: Unique key of user setting to be updated
        """
        endpoint = f"/api/v1/user/preferences/{keyId}"

        return self._put(endpoint, data)

    def delete_jamf_pro_user_account_setting(self, keyId) -> str:
        """
        Deletes specified setting for the authenticated user by key ID

        :param keyID: Unique key of user setting to be deleted
        """
        endpoint = f"/api/v1/user/preferences/{keyId}"

        return self._delete(
            endpoint,
            success_message=f"User setting with key ID {keyId} successfully deleted.",
        )

    """
    jamf-pro-user-account-settings-preview
    """

    # All endpoints deprecated

    """
    jamf-pro-version
    """

    def get_jamf_pro_version(self) -> dict:
        """
        Returns information about the Jamf Pro Server including the current
        version
        """
        endpoint = "/api/v1/jamf-pro-version"

        return self._get(endpoint)

    """
    jamf-protect
    """

    def get_jamf_protect_integration_settings(self) -> dict:
        """
        Returns Jamf Protect integration settings for the Jamf Pro server
        """
        endpoint = "/api/v1/jamf-protect"

        return self._get(endpoint)

    def get_jamf_protect_config_profile_deployment_tasks(
        self,
        uuid: str,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["status:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns deployment tasks linked to Jamf Protect config profiles by UUID

        :param uuid: Jamf Protect config profile UUID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort
            order is ["status:desc"]. Multiple sort criteria are supported
            and must be seperated by a comma.

            Example ["id:asc", "version:desc"]

        :param filter:
            Query in the RSQL format, allowing to filter results. Default
            filter is empty query - returning all results for the requested
            page. Fields allowed in the query: version, updated, status This
            param can be combined with paging and sorting.

            Example: name=="Test"
        """
        params = remove_empty_params(
            {"page": page, "page-size": page_size, "sort": sort, "filter": filter}
        )
        endpoint = f"/api/v1/jamf-protect/deployments/{uuid}/tasks"

        return self._get(endpoint, params=params)

    def get_jamf_protect_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns sorted, paginated Jamf Protect history

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
            {"page": page, "page-size": page_size, "sort": sort, "filter": filter}
        )
        endpoint = "/api/v1/jamf-protect/history"

        return self._get(endpoint, params=params)

    def get_jamf_protect_plans(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns all of the previously synced Jamf Portect Plans with
        information about their associated configuration profile

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
            for the requested page. Fields allowed in the query:  profileId,
            name, description, id, uuid. This param can be combined with paging
            and sorting.

            Example: id==1001
        """
        params = remove_empty_params(
            {"page": page, "page-size": page_size, "sort": sort, "filter": filter}
        )
        endpoint = "/api/v1/jamf-protect/plans"

        return self._get(endpoint, params=params)

    def create_jamf_protect_config_profile_deployment_tasks_retry(
        self, data: dict, uuid: str
    ) -> dict:
        """
        Requests a retry of Jamf Protect install tasks with JSON by UUID

        :param data: JSON data containing the IDs of the tasks to retry
        :param uuid: Jamf Protect config profile UUID
        """
        endpoint = f"/api/v1/jamf-protect/deployments/{uuid}/tasks/retry"

        return self._post(endpoint, data)

    def create_jamf_protect_history_note(self, data: dict) -> dict:
        """
        Creates a Jamf Protect history note with JSON

        :param data: JSON data to create the Jamf Protect history note
        """
        endpoint = "/api/v1/jamf-protect/history"

        return self._post(endpoint, data)

    def create_jamf_protect_plans_sync(self) -> str:
        """
        Syncs plans with Jamf Protect. Configuration profiles associated with
        new plans will be imported to Jamf Pro.
        """
        endpoint = "/api/v1/jamf-protect/plans/sync"

        return self._post(
            endpoint, success_message="Jamf Protect plans successfully synced."
        )

    def create_jamf_protect_api_configuration(self, data: dict) -> dict:
        """
        Registers a Jamf Protect API configuration with Jamf Pro with JSON

        :param data:
            JSON data to register the Jamf Protect API configuration with
        """
        endpoint = "/api/v1/jamf-protect/register"

        return self._post(endpoint, data)

    def update_jamf_protect_integration_settings(self, data: dict) -> dict:
        """
        Updates the Jamf Protect integration settings with JSON

        :param data:
            JSON data to update the Jamf Protect integration settings with
        """
        endpoint = "/api/v1/jamf-protect"

        return self._put(endpoint, data)

    def delete_jamf_protect_api_registration(self) -> dict:
        """
        Deletes an existing Jamf Protect API registration if present. Jamf
        Protect API integration will be disabled.
        """
        endpoint = "/api/v1/jamf-protect"

        return self._delete(
            endpoint,
            success_message="Jamf Protect API registration successfully deleted.",
        )

    """
    ldap
    """

    def get_ldap_servers(self) -> dict:
        """
        Returns all active servers including LDAP and cloud identity providers
        """
        endpoint = "/api/v1/ldap/servers"

        return self._get(endpoint)

    def get_ldap_local_servers(self) -> dict:
        """
        Returns all not migrated, LDAP servers
        """
        endpoint = "/api/v1/ldap/ldap-servers"

        return self._get(endpoint)

    def get_ldap_group_search(self, search: str) -> dict:
        """
        Returns the configured acess groups that containt the text in the
        search param
        """
        params = {"q": search}
        endpoint = "/api/v1/ldap/groups"

        return self._get(endpoint, params=params)

    """
    locales-preview
    """

    def get_locales(self) -> dict:
        """
        Returns locales that can be used in other features
        """
        endpoint = "/api/v1/locales"

        return self._get(endpoint)

    """
    macos-managed-software-updates
    """

    def get_macos_managed_software_updates(self) -> dict:
        """
        Returns available macOS manages software updates
        """
        endpoint = "/api/v1/macos-managed-software-updates/available-updates"

        return self._get(endpoint)

    def create_macos_managed_software_updates(self, data: dict) -> dict:
        """
        Sends macOS manged software updates

        :param data: JSON data to send MacO
        """
        endpoint = "/api/v1/macos-managed-software-updates/send-updates"

        return self._post(endpoint, data)

    """
    mdm
    """

    # Filter needs to be set to something otherwise it will return a 400 error
    def get_mdm_commands(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["dateSent:asc"],
        filter: str = "dateSent>=1970-01-01T00:00:00Z",
    ) -> dict:
        """
        Returns information about MDM commands made by Jamf Pro

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Default sort is dateSent:asc. Multiple sort criteria are supported
            and must be separated with a comma.

            ["dateSent:desc", "command:asc"]
        :param filter:
            Query in the RSQL format, allowing to filter, for a list of
            commands. All url must contain minimum one filter field. Fields
            allowed in the query: uuid, clientManagementId, command, status,
            clientType, dateSent, validAfter, dateCompleted, profileIdentifier,
            and active. This param can be combined with paging.

            Example: status==Pending
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v2/mdm/commands"

        return self._get(endpoint, params=params)

    def create_mdm_command(self, data: dict) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Create and queue an MDM command with given JSON data

        :param data: JSON data to create the MDM command with
        """
        endpoint = "/api/preview/mdm/commands"

        return self._post(endpoint, data)

    def create_mdm_profile_renew(self, data: dict) -> dict:
        """
        Renews the device's MDM Profile, including the device identity
        certificate within the MDM Profile with JSON data.

        :param data: JSON data to define which profiles to renew
        """
        endpoint = "/api/v1/mdm/renew-profile"

        return self._post(endpoint, data)

    def create_mdm_deploy_package(self, data: dict, verbose: bool = False) -> dict:
        """
        Deploys packages to macOS devices using the
        InstallEnterpriseApplication MDM command.

        :param data: JSON data to deploy package with
        :param verbose:
            Deploys packages to macOS devices using the
            InstallEnterpriseApplication MDM command.
        """
        params = {"verbose": verbose}
        endpoint = "/api/v1/deploy-package"

        return self._post(endpoint, data, params=params)

    """
    mobile-device-enrollment-profile
    """

    def get_mobile_device_enrollment_profile(self, id: Union[int, str]) -> dict:
        """
        Downloads the MDM enrollment profile to the current users Downloads
        folder by ID

        :param id: MDM enrollment profile ID
        """
        endpoint = f"/api/v1/mobile-device-enrollment-profile/{id}/download-profile"

        return self._download(endpoint)

    """
    mobile-device-extension-attributes-preview
    """

    def get_mobile_device_extension_attributes(self, select: str = "name") -> dict:
        """
        Returns mobile device extension attribute values placed in select
        parameter. The only supported select value curently is name.

        :param select:
            Extension attribute value to return, the only supported value
            currently is name. Default value is name.
        """
        params = {"select": select}
        endpoint = "/api/devices/extensionAttributes"

        return self._get(endpoint, params=params)

    """
    mobile-device-groups-preview
    """

    def get_mobile_device_groups(self) -> dict:
        """
        Returns all mobile device groups
        """
        endpoint = "/api/v1/mobile-device-groups"

        return self._get(endpoint)

    """
    mobile-device-prestages
    """

    def get_mobile_device_prestages(
        self, page: int = None, page_size: int = None, sort: int = ["id:desc"]
    ) -> dict:
        """
        Returns sorted and paged mobile device prestages

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Multiple sort
            criteria are supported and must be separated with a comma. Default
            sort is id:desc.

            Example: ["id:asc", "defaultPrestage:desc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v2/mobile-device-prestages"

        return self._get(endpoint, params=params)

    def get_mobile_device_prestages_scopes(self) -> dict:
        """
        Returns all device scopes for all mobile device prestages
        """
        endpoint = "/api/v2/mobile-device-prestages/scope"

        return self._get(endpoint)

    def get_mobile_device_prestages_sync_states(self) -> dict:
        """
        Returns all prestage sync states for all prestages
        """
        endpoint = "/api/v2/mobile-device-prestages/syncs"

        return self._get(endpoint)

    def get_mobile_device_prestage(self, id: Union[int, str]) -> dict:
        """
        Returns a mobile device prestage by ID

        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}"

        return self._get(endpoint)

    def get_mobile_device_prestage_attachments(self, id: Union[int, str]) -> dict:
        """
        Returns attachments for a mobile device prestage by ID

        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/attachments"

        return self._get(endpoint)

    def get_mobile_device_prestage_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: int = ["date:desc"],
    ) -> dict:
        """
        Returns sorted and paged mobile device prestage history by ID

        :param id: Mobile device prestage ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "note:asc"]
        """
        params = remove_empty_params(
            {"page": page, "page-size": page_size, "sort": sort}
        )
        endpoint = f"/api/v2/mobile-device-prestages/{id}/history"

        return self._get(endpoint, params=params)

    def get_mobile_device_prestage_scope(self, id: Union[int, str]) -> dict:
        """
        Returns device scope for a specific mobile device prestage by ID

        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/scope"

        return self._get(endpoint)

    def get_mobile_device_prestage_sync_states(self, id: Union[int, str]) -> dict:
        """
        Returns all prestage sync states for a single prestage by ID

        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/syncs"

        return self._get(endpoint)

    def get_mobile_device_prestage_latest_sync_state(self, id: Union[int, str]) -> dict:
        """
        Returns the latest sync state for a single prestage by ID

        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/syncs/latest"

        return self._get(endpoint)

    def create_mobile_device_prestage(self, data: dict) -> dict:
        """
        Creates a mobile device prestage with JSON data

        :param data: JSON data to create mobile device prestage with
        """
        endpoint = "/api/v2/mobile-device-prestages"

        return self._post(endpoint, data)

    def create_mobile_device_prestage_attachment(
        self, filepath: str, id: Union[int, str]
    ) -> dict:
        """
        Uploads a mobile device prestage attachment by ID and filepath

        :param filepath: Literal path to file to upload
        :param id: Mobile device prestage ID
        """
        filename = basename(filepath)
        content_type = guess_type(filename.lower())[0]
        file = {"file": (filename, open(filepath, "rb"), content_type)}
        endpoint = f"/api/v2/mobile-device-prestages/{id}/attachments"

        return self._post(endpoint, file=file)

    def create_mobile_device_prestage_history_note(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Creates a mobile device prestage history note by ID with JSON

        :param data:
            JSON data to create mobile device prestage history note with
        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/history"

        return self._post(endpoint, data)

    def create_mobile_device_prestage_scope(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Adds device scope for a specific mobile device prestage by ID

        :param data: JSON data to add device scope with
        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/scope"

        return self._post(endpoint, data)

    def update_mobile_device_prestage(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates a mobile device prestage by ID with JSON

        :param data: JSON data to update mobile device prestage with
        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}"

        return self._put(endpoint, data)

    def replace_mobile_device_prestage_scope(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Replaces device scope for a specific mobiule device prestage by ID with
        JSON

        :param data: JSON data to replace device scope with
        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/scope"

        return self._put(endpoint, data)

    def delete_mobile_device_prestage(self, id: Union[int, str]) -> str:
        """
        Deletes a mobile device prestage by ID

        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}"

        return self._delete(
            endpoint,
            success_message=f"Mobile device prestage {id} successfully deleted.",
        )

    def delete_mobile_device_prestage_attachment(
        self, data: dict, id: Union[int, str]
    ) -> str:
        """
        Deletes mobile device prestage attachment(s) by ID with JSON

        :param data:
            JSON data to delete mobile device prestage attachments with
        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/attachments/delete-multiple"

        return self._post(
            endpoint,
            data,
            success_message=(
                f"Attachment(s) {', '.join(data['ids'])} of mobile device "
                f"prestage {id} successfully deleted."
            ),
        )

    def delete_mobile_device_prestage_scope(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Removes device scope for a specific mobile device prestage by ID with
        JSON

        :param data: JSON data to remove device scope with
        :param id: Mobile device prestage ID
        """
        endpoint = f"/api/v2/mobile-device-prestages/{id}/scope/delete-multiple"

        return self._post(endpoint, data)

    """
    mobile-devices
    """

    def get_mobile_devices(
        self, page: int = None, page_size: int = None, sort: List["str"] = None
    ) -> dict:
        """
        Returns sorted and paginated mobile devices

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
        endpoint = "/api/v2/mobile-devices"

        return self._get(endpoint, params=params)

    def get_mobile_device(self, id: Union[int, str]) -> dict:
        """
        Returns mobile device with limited details by ID

        :param id: Mobile device ID
        """
        endpoint = f"/api/v2/mobile-devices/{id}"

        return self._get(endpoint)

    def get_mobile_device_detail(self, id: Union[int, str]) -> dict:
        """
        Returns mobile device with all info by ID

        :param id: Mobile device ID
        """
        endpoint = f"/api/v2/mobile-devices/{id}/detail"

        return self._get(endpoint)

    def update_mobile_device(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates mobile device by ID with JSON

        :param data: JSON data to update mobile device with
        :param id: Mobile device ID
        """
        endpoint = f"/api/v2/mobile-devices/{id}"

        return self._put(endpoint, data)

    """
    parent-app-preview
    """

    def get_parent_app_settings(self) -> dict:
        """
        Returns the current Jamf Parent app settings
        """
        endpoint = "/api/v1/parent-app"

        return self._get(endpoint)

    def get_parent_app_settings_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns Jamf Paret app settings history

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
            {"page": page, "page-size": page_size, "sort": sort, "filter": filter}
        )
        endpoint = "/api/v1/parent-app/history"

        return self._get(endpoint, params=params)

    def create_parent_app_settings_history_note(self, data: dict) -> dict:
        """
        Creates a Jamf Parent app settings history note with JSON

        :param data:
            JSON data to create the jamf parent app settings history note with
        """
        endpoint = "/api/v1/parent-app/history"

        return self._post(endpoint, data)

    def update_parent_app_settings(self, data: dict) -> dict:
        """
        Updates Jamf Parent app settings with JSON

        :param data: JSON data to udpate Jamf Parent app settings with
        """
        endpoint = "/api/v1/parent-app"

        return self._put(endpoint, data)

    """
    patch-policies-preview
    """

    def get_patch_policy_dashboard(self, id: Union[int, str]) -> dict:
        """
        Returns whether or not the requested patch policy is on the dashboard
        by ID

        :param id: Patch policy ID
        """
        endpoint = f"/api/patch/patch-policies/{id}/dashboard"

        return self._get(endpoint)

    def create_patch_policy_dashboard(self, id: Union[int, str]) -> dict:
        """
        Adds a patch policy to the dashboard by ID

        :param id: Patch policy ID
        """
        endpoint = f"/api/patch/patch-policies/{id}/dashboard"

        return self._post(endpoint)

    def delete_patch_policy_dashboard(self, id: Union[int, str]) -> dict:
        """
        Removes a patch policy from the dashboard by ID

        :param id: Patch policy ID
        """
        endpoint = f"/api/patch/patch-policies/{id}/dashboard"

        return self._delete(
            endpoint, success_message=f"Patch policy {id} removed from dashboard."
        )

    """
    patch-policy-logs-preview
    """

    # All endpoints deprecated

    """
    patches
    """

    # All endpoints deprecated

    """
    patches-preview
    """

    def get_patch_dashboards(self) -> dict:
        """
        Returns list of patch IDs on dashboard
        """
        endpoint = "/api/patch/onDashboard"

        return self._get(endpoint)

    def get_patch_summary(self, id: Union[int, str]) -> dict:
        """
        Returns patch policy summary by ID

        :param id: Patch policy ID
        """
        endpoint = f"/api/patch/objs/policy/{id}"

        return self._get(endpoint)

    def get_patch_software_summary(self, id: Union[int, str]) -> dict:
        """
        Returns the summaries of the patch policies for the software title by
        ID

        :param id: Software title ID
        """
        endpoint = f"/api/patch/obj/softwareTitle/{id}/policies"

        return self._get(endpoint)

    def get_patch_software_title_configuration_id(self, id: Union[int, str]) -> dict:
        """
        Returns the software title configuration ID for the given patch policy
        by ID

        :param ID: Policy ID
        """
        endpoint = f"/api/patch/obj/policy/{id}/softwareTitleConfigurationId"

        return self._get(endpoint)

    def create_patch_disclaimer_accept(self) -> str:
        """
        Accepts patch reporting disclaimer
        """
        endpoint = "/api/patch/disclaimerAgree"

        return self._post(
            endpoint, success_message="Patch reporting disclaimer accepted."
        )

    def update_patch_report(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates patch report by ID with JSON

        :param data: JSON data to update patch report with
        :param id: Patch ID
        """
        endpoint = f"/api/patch/obj/{id}"

        return self._put(endpoint, data)

    """
    policies-preview
    """

    def get_policy_properties(self) -> dict:
        """
        Returns policy properties
        """
        endpoint = "/api/v1/policy-properties"

        return self._get(endpoint)

    def update_policy_properties(self, data: dict) -> dict:
        """
        Updates policy properties with JSON

        :param data: JSON data to update policy properties with
        """
        endpoint = "/api/v1/policy-properties"

        return self._put(endpoint, data)

    """
    re-enrollment-preview
    """

    def get_reenrollment_settings(self) -> dict:
        """
        Returns re-enrollment settings
        """
        endpoint = "/api/v1/reenrollment"

        return self._get(endpoint)

    def get_reenrollment_history(
        self, page: int = None, page_size: int = None, sort: List[str] = ["date:desc"]
    ) -> dict:
        """
        Returns paginated and sorted re-enrollment history

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            date:desc. Multiple sort criteria are supported and must be
            separated with a comma.

            Example: ["date:desc", "note:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/reenrollment/history"

        return self._get(endpoint, params=params)

    def get_reenrollment_history_export(
        self,
        export_fields: List[str] = None,
        export_labels: List[str] = None,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["id:asc"],
        filter: str = None,
    ) -> str:
        """
        Exports reenrollment history collection in CSV format

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
        headers = {"Content-type": "application/json", "Accept": "text/csv"}
        endpoint = "/api/v1/reenrollment/history/export"

        return self._post(endpoint, headers=headers, params=params, data_type=None)

    def create_reenrollment_history_note(self, data: dict) -> dict:
        """
        Adds specified re-enrollment history note with JSON

        :param data: JSON data to create re-enrollment history note with
        """
        endpoint = "/api/v1/reenrollment/history"

        return self._post(endpoint, data)

    def update_reenrollment_settings(self, data: dict) -> dict:
        """
        Updates the re-enrollment settings

        :param data: JSON data to update re-enrollment settings with
        """
        endpoint = "/api/v1/reenrollment"

        return self._put(endpoint, data)

    """
    remote-administration
    """

    def get_remote_administration_configurations(
        self, page: int = None, page_size: int = None
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Returns remote administration configurations

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
            }
        )
        endpoint = "/api/preview/remote-administration-configurations"

        return self._get(endpoint, params=params)

    """
    scripts
    """

    def get_scripts(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["name:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns sorted and paged scripts

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            name:asc. Multiple sort criteria are supported and must be
            separated with a comma. Fields allowed in the query: id, name,
            info, notes, priority, categoryId, categoryName, parameter4 up to
            parameter11, osRequirements, scriptContents.

            Example: ["id:desc", "name:asc"]

        :param filter:
            Query in the RSQL format, allowing to filter scripts collection.
            Default search is empty query - returning all results for the
            requested page. Fields allowed in the query: id, name, info, notes,
            priority, categoryId, categoryName, parameter4 up to parameter11,
            osRequirements, scriptContents. This param can be combined with
            paging and sorting.

            Example: categoryName=="Category" and name=="script name"
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
                "filter": filter,
            }
        )
        endpoint = "/api/v1/scripts"

        return self._get(endpoint, params=params)

    def get_script(self, id: Union[int, str]) -> dict:
        """
        Returns script by ID

        :param id: Script ID
        """
        endpoint = f"/api/v1/scripts/{id}"

        return self._get(endpoint)

    def get_script_history(
        self,
        id: Union[int, str],
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["name:asc"],
        filter: str = None,
    ) -> dict:
        """
        Returns sorted and paged script history by ID

        :param id: Script ID
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
        endpoint = f"/api/v1/scripts/{id}/history"

        return self._get(endpoint, params=params)

    def get_script_file(self, id: Union[int, str]) -> str:
        """
        Not working in Swagger documentation or here, returns 500 error

        Downloads a text file of the script contents by ID

        :param id: Script ID
        """
        endpoint = f"/api/v1/scripts/{id}/download"

        return self._download(endpoint)

    def create_script(self, data: dict) -> dict:
        """
        Creates a script with JSON

        :param data: JSON data to create script with
        """
        endpoint = "/api/v1/scripts"

        return self._post(endpoint, data)

    def create_script_history_note(self, data: dict, id: Union[int, str]) -> dict:
        """
        Creates specified script history note by ID with JSON

        :param data: JSON data to create the script history note with
        :param id: Script ID
        """
        endpoint = f"/api/v1/scripts/{id}/history"

        return self._post(endpoint, data)

    def update_script(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates the script with ID by JSON

        :param data: JSON data to update script with
        :param id: Script ID
        """
        endpoint = f"/api/v1/scripts/{id}"

        return self._put(endpoint, data)

    def delete_script(self, id: Union[int, str]) -> dict:
        """
        Deletes a script by ID

        :param id: Script ID
        """
        endpoint = f"/api/v1/scripts/{id}"

        return self._delete(
            endpoint, success_message=f"Script {id} successfully deleted."
        )

    """
    self-service
    """

    def get_self_service_settings(self) -> dict:
        """
        Returns the self service settings of the Jamf Pro server
        """
        endpoint = "/api/v1/self-service/settings"

        return self._get(endpoint)

    def update_self_service_settings(self, data: dict) -> dict:
        """
        Updates the self service settings with JSON

        :param data: JSON data to update self service settings with
        """
        endpoint = "/api/v1/self-service/settings"

        return self._put(endpoint, data)

    """
    self-service-branding-ios
    """

    def get_self_service_branding_ios_configurations(
        self, page: int = None, page_size: int = None, sort: List[str] = ["id:asc"]
    ) -> dict:
        """
        Returns paged and sorted Self Service branding configuration for iOS

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "brandingName:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/self-service/branding/ios"

        return self._get(endpoint, params=params)

    def get_self_service_branding_ios_configuration(self, id: Union[int, str]) -> dict:
        """
        Returns iOS Self Service branding configuration by ID

        :param id: iOS Self Service branding configuration ID
        """
        endpoint = f"/api/v1/self-service/branding/ios/{id}"

        return self._get(endpoint)

    def create_self_service_branding_ios_configuration(self, data: dict) -> dict:
        """
        Creates iOS Self Service branding configuration with JSON

        :param data:
            JSON data to create iOS Self Service branding configuration with
        """
        endpoint = "/api/v1/self-service/branding/ios"

        return self._post(endpoint, data)

    def update_self_service_branding_ios_configuration(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Updates iOS Self Service branding configuration with JSON by ID

        :param data:
            JSON data to update iOS Self Service branding configuration with
        :param id: iOS Self Service branding configuration ID
        """
        endpoint = f"/api/v1/self-service/branding/ios/{id}"

        return self._put(endpoint, data)

    def delete_self_service_branding_ios_configuration(
        self, id: Union[int, str]
    ) -> dict:
        """
        Deletes iOS Self Service branding configuration by ID

        :param id: iOS Self Service branding configuration by ID
        """
        endpoint = f"/api/v1/self-service/branding/ios/{id}"

        return self._delete(
            endpoint,
            success_message=(
                f"iOS Self Service branding configuration {id} successfully deleted."
            ),
        )

    """
    self-service-branding-macos
    """

    def get_self_service_branding_macos_configurations(
        self, page: int = None, page_size: int = None, sort: List[str] = ["id:asc"]
    ) -> dict:
        """
        Returns paged and sorted Self Service branding configuration for macOS

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "brandingName:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/self-service/branding/macos"

        return self._get(endpoint, params=params)

    def get_self_service_branding_macos_configuration(
        self, id: Union[int, str]
    ) -> dict:
        """
        Returns macOS Self Service branding configuration by ID

        :param id: macOS Self Service branding configuration ID
        """
        endpoint = f"/api/v1/self-service/branding/macos/{id}"

        return self._get(endpoint)

    def create_self_service_branding_macos_configuration(self, data: dict) -> dict:
        """
        Creates macOS Self Service branding configuration with JSON

        :param data:
            JSON data to create macOS Self Service branding configuration with
        """
        endpoint = "/api/v1/self-service/branding/macos"

        return self._post(endpoint, data)

    def update_self_service_branding_macos_configuration(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        Updates macOS Self Service branding configuration with JSON by ID

        :param data:
            JSON data to update macOS Self Service branding configuration with
        :param id: macOS Self Service branding configuration ID
        """
        endpoint = f"/api/v1/self-service/branding/macos/{id}"

        return self._put(endpoint, data)

    def delete_self_service_branding_macos_configuration(
        self, id: Union[int, str]
    ) -> dict:
        """
        Deletes macOS Self Service branding configuration by ID

        :param id: macOS Self Service branding configuration by ID
        """
        endpoint = f"/api/v1/self-service/branding/macos/{id}"

        return self._delete(
            endpoint,
            success_message=(
                f"macOS Self Service branding configuration {id} successfully deleted."
            ),
        )

    """
    self-service-branding-preview
    """

    def create_self_service_branding(self, filepath: str) -> dict:
        """
        Uploads a self service branding image by ID and filepath

        :param filepath: Literal path to file to upload
        :param id: Self Service branding ID
        """
        filename = basename(filepath)
        content_type = guess_type(filename.lower())[0]
        file = {"file": (filename, open(filepath, "rb"), content_type)}
        endpoint = "/api/self-service/branding/images"

        return self._post(endpoint, file=file)

    """
    sites
    """

    def get_sites(self) -> dict:
        """
        Returns all sites
        """
        endpoint = "/api/v1/sites"

        return self._get(endpoint)

    """
    sites-preview
    """

    # All endpoints deprecated

    """
    smart-computer-groups-preview
    """

    def create_smart_computer_group_recalculate_computer(
        self, id: Union[int, str]
    ) -> dict:
        """
        Recalculates smart groups of the specified computer then returns the
        count of smart groups the computer falls into by ID

        :param id: Computer ID
        """
        endpoint = f"/api/v1/computers/{id}/recalculate-smart-groups"

        return self._post(endpoint)

    def create_smart_computer_group_recalculate_group(
        self, id: Union[int, str]
    ) -> dict:
        """
        Recalculates the smart group for the given ID and then returns the
        count of the computers in the smart group

        :param id: Smart computer group ID
        """
        endpoint = f"/api/v1/smart-computer-groups/{id}/recalculate"

        return self._post(endpoint)

    """
    smart-mobile-device-groups-preview
    """

    def create_smart_mobile_device_group_recalculate_device(
        self, id: Union[int, str]
    ) -> dict:
        """
        Recalculates smart groups of the specified mobile device then returns
        the count of smart groups the device falls into by ID

        :param id: Mobile device ID
        """
        endpoint = f"/api/v1/mobile-devices/{id}/recalculate-smart-groups"

        return self._post(endpoint)

    def create_smart_mobile_device_group_recalculate_group(
        self, id: Union[int, str]
    ) -> dict:
        """
        Recalculates the smart group for the given ID and then returns the
        count of the mobile devices in the smart group

        :param id: Smart mobile device group ID
        """
        endpoint = f"/api/v1/smart-mobile-device-groups/{id}/recalculate"

        return self._post(endpoint)

    """
    smart-user-groups-preview
    """

    def create_smart_user_group_recalculate_user(self, id: Union[int, str]) -> dict:
        """
        Recalculates smart groups of the specified user then returns the count
        of smart groups the user falls into by ID

        :param id: User ID
        """
        endpoint = f"/api/v1/users/{id}/recalculate-smart-groups"

        return self._post(endpoint)

    def create_smart_user_group_recalculate_group(self, id: Union[int, str]) -> dict:
        """
        Recalculates the smart group for the given ID and then returns the
        count of the users in the smart group

        :param id: Smart user group ID
        """
        endpoint = f"/api/v1/smart-user-groups/{id}/recalculate"

        return self._post(endpoint)

    """
    sso-certificate
    """

    def get_sso_certificate(self) -> dict:
        """
        Returns the certificate currently configured for use with SSO
        """
        endpoint = "/api/v2/sso/cert"

        return self._get(endpoint)

    def get_sso_certificate_file(self) -> dict:
        """
        Downloads the certificate currently configured for use with Jamf Pro's
        SSO configuration
        """
        endpoint = "/api/v2/sso/cert/download"

        return self._download(endpoint)

    def create_sso_certificate(self) -> dict:
        """
        Generates a new certificate and use it to sign SSO requests to the
        identity provider
        """
        endpoint = "/api/v2/sso/cert"

        return self._post(endpoint)

    def create_sso_certificate_parse(self, data: dict) -> dict:
        """
        Parses the certificate to get details about certificate type and keys
        needed to upload certificate file with JSON

        :param data: JSON data to parse certificate with
        """
        endpoint = "/api/v2/sso/cert/parse"

        return self._post(endpoint, data)

    def update_sso_certificate(self, data: dict) -> dict:
        """
        Updates the certificate used by Jamf Pro to sign SSO requests to the
        identify provider with JSON

        :param data: JSON data to update SSO certificate with
        """
        endpoint = "/api/v2/sso/cert"

        return self._put(endpoint, data)

    def delete_sso_certificate(self) -> str:
        """
        Deletes the currently configured certificate used by SSO
        """
        endpoint = "/api/v2/sso/cert"

        return self._delete(
            endpoint, success_message="SSO certificate successfully deleted."
        )

    """
    sso-certificate-preview
    """

    # sso-certificate is a more up to date version of this collection

    """
    sso-settings
    """

    def get_sso_settings(self) -> dict:
        """
        Returns the current SSO configuration settings
        """
        endpoint = "/api/v1/sso"

        return self._get(endpoint)

    def get_sso_settings_enrollment_customizations(self) -> dict:
        """
        Returns the list of enrollment customizations using SSO
        """
        endpoint = "/api/v1/sso/dependencies"

        return self._get(endpoint)

    def get_sso_settings_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns paged and sorted SSO settings history

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
        endpoint = "/api/v1/sso/history"

        return self._get(endpoint, params=params)

    def get_sso_settings_saml_metadata_file(self) -> str:
        """
        Downloads the Jamf Pro SAML metadata file to the current users
        downloads folder
        """
        endpoint = "/api/v1/sso/metadata/download"

        return self._download(endpoint)

    def create_sso_settings_disable(self) -> str:
        """
        Disables SSO for the Jamf Pro Server
        """
        endpoint = "/api/v1/sso/disable"

        return self._post(endpoint, success_message="SSO successfully disabled.")

    def create_sso_settings_history_note(self, data: dict) -> dict:
        """
        Creates SSO history note with JSON

        :param data: JSON data to create SSO history note with
        """
        endpoint = "/api/v1/sso/history"

        return self._post(endpoint, data)

    def create_sso_settings_validate_saml_metadata_url(self, data: dict) -> str:
        """
        Validates content available udner provided metadata URL with JSON

        :param data: JSON data to validate
        """
        endpoint = "/api/v1/sso/validate"

        return self._post(endpoint, data, success_message="Metadata URL is valid.")

    def update_sso_settings(self, data: dict) -> dict:
        """
        Updates the current SSSO configuration settings

        :param data: JSON data to update the SSO settings with
        """
        endpoint = "/api/v1/sso"

        return self._put(endpoint, data)

    """
    startup-status
    """

    def get_startup_status(self) -> dict:
        """
        Returns information about application startup. Current startup
        operation taking place (if any) and overall startup completion
        percentage.
        """
        endpoint = "/api/startup-status"

        return self._get(endpoint)

    """
    static-user-groups-preview
    """

    def get_static_user_groups(self) -> List:
        """
        Returns all static user groups
        """
        endpoint = "/api/v1/static-user-groups"

        return self._get(endpoint)

    def get_static_user_group(self, id: Union[int, str]) -> dict:
        """
        Returns a static user group by ID

        :param id: Static user group ID
        """
        endpoint = f"/api/v1/static-user-groups/{id}"

        return self._get(endpoint)

    """
    supervision-identities-preview
    """

    def get_supervision_identities(
        self, page: int = None, page_size: int = None, sort: List[str] = ["id:asc"]
    ) -> dict:
        """
        Returns sorted and paged supervision identities

        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param sort:
            Sorting criteria in the format: property:asc/desc. Default sort is
            id:asc. Multiple sort criteria are supported and must be separated
            with a comma.

            Example: ["id:desc", "commonName:asc"]
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "sort": sort,
            }
        )
        endpoint = "/api/v1/supervision-identities"

        return self._get(endpoint, params=params)

    def get_supervision_identity(self, id: Union[int, str]) -> dict:
        """
        Returns a supervision identity by ID

        :param id: Supervision identity ID
        """
        endpoint = f"/api/v1/supervision-identities/{id}"

        return self._get(endpoint)

    def get_supervision_identity_file(self, id: Union[int, str]) -> dict:
        """
        Downloads the supervision identity .p12 file by ID

        :param id: Supervision identity ID
        """
        endpoint = f"/api/v1/supervision-identities/{id}/download"

        return self._download(endpoint)

    def create_supervision_identity(self, data: dict) -> dict:
        """
        Creates a supervision identity with JSON

        :param data: JSON data to create supervision identity with
        """
        endpoint = "/api/v1/supervision-identities"

        return self._post(endpoint, data)

    def create_supervision_identity_file(self, data: dict) -> dict:
        """
        Creates the superivision identity .p12 file with JSON

        :param data: JSON data to create supervision identity p12 file with
        """
        endpoint = "/api/v1/supervision-identities/upload"

        return self._post(endpoint, data)

    def update_supervision_identity(self, data: dict, id: Union[int, str]) -> dict:
        """
        Updates a supervision identity by ID with JSON

        :param data: JSON data to update supervision identity with
        :param id: Supervision identity ID
        """
        endpoint = f"/api/v1/supervision-identities/{id}"

        return self._put(endpoint, data)

    def delete_supervision_identity(self, id: Union[int, str]) -> str:
        """
        Deletes a supervision identity by ID

        :param id: Supervision identity ID
        """
        endpoint = f"/api/v1/supervision-identities/{id}"

        return self._delete(
            endpoint, success_message=f"Supervision identity {id} successfully deleted."
        )

    """
    teacher-app
    """

    def get_teacher_app_settings(self):
        """
        Returns the Jamf Teacher settings that the user has access to see
        """
        endpoint = "/api/v1/teacher-app"

        return self._get(endpoint)

    def get_teacher_app_history(
        self,
        page: int = None,
        page_size: int = None,
        sort: List[str] = ["date:desc"],
        filter: str = None,
    ) -> dict:
        """
        Returns Jamf Teacher settings history

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
        endpoint = "/api/v1/teacher-app/history"

        return self._get(endpoint, params=params)

    def create_teacher_app_history_note(self, data: dict) -> dict:
        """
        Creates a Jamf Teacher app settings history note with JSON

        :param data:
            JSON data to create Jamf Teacher app settings history note with
        """
        endpoint = "/api/v1/teacher-app/history"

        return self._post(endpoint, data)

    def update_teacher_app_settings(self, data: dict) -> dict:
        """
        Updates Jamf Teacher app settings with JSON

        :param data: JSON data to update Jamf Teacher app settings with
        """
        endpoint = "/api/v1/teacher-app"

        return self._put(endpoint, data)

    """
    team-viewer-remote-administration
    """

    def get_team_viewer_remote_administration_connection_configuration(
        self, id: Union[int, str]
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.
        
        Returns Team Viewer remote administration connection configuration by
        ID

        :param id: Team Viewer connection configuration ID
        """
        endpoint = f"/api/preview/remote-administration-configurations/team-viewer/{id}"

        return self._get(endpoint)

    def get_team_viewer_remote_administration_sessions(
        self,
        configuration_id: Union[int, str],
        page: int = None,
        page_size: int = None,
        filter: str = None,
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Returns a paginated list of sessions by configuration ID

        :param configuration_id: Team Viewer connection configuration ID
        :param page: Page to return, default page is 0.
        :param page_size: Page size to return Default page-size is 100.
        :param filter:
            Query in the RSQL format, allowing to filter sessions collection.
            Default filter is empty query - returning all results for the
            requested page.

            Fields allowed in the query: deviceId, deviceType, state

            Example: deviceId==1 and deviceType=="COMPUTER" and state=="OPEN"
        """
        params = remove_empty_params(
            {
                "page": page,
                "page-size": page_size,
                "filter": filter,
            }
        )
        endpoint = (
            "/api/preview/remote-administration-configurations/team-viewer/"
            f"{configuration_id}/sessions"
        )

        return self._get(endpoint, params=params)

    def get_team_viewer_remote_administration_session(
        self, configuration_id: Union[int, str], session_id: Union[int, str]
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Returns session details if found by ID

        :param configuration_id: Team Viewer connection configuration ID
        :param session_id: Team Viewer session ID
        """
        endpoint = (
            "/api/preview/remote-administration-configurations/team-viewer/"
            f"{configuration_id}/sessions/{session_id}"
        )

        return self._get(endpoint)

    def get_team_viewer_remote_administration_session_status(
        self, configuration_id: Union[int, str], session_id: Union[int, str]
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Returns session status by ID

        :param configuration_id: Team Viewer connection configuration ID
        :param session_id: Team Viewer session ID
        """
        endpoint = (
            "/api/preview/remote-administration-configurations/team-viewer/"
            f"{configuration_id}/sessions/{session_id}/status"
        )

        return self._get(endpoint)

    def get_team_viewer_remote_administration_connection_status(
        self, id: Union[int, str]
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Returns Team Viewer remote administration connection status by ID

        :param id: Team Viewer connection configuration ID
        """
        endpoint = (
            f"/api/preview/remote-administration-configurations/team-viewer/{id}/status"
        )

        return self._get(endpoint)

    def create_team_viewer_remote_administration_connection_configuration(
        self, data: dict
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Creates Team Viewer remote administration connection configuration with
        JSON

        :param data:
            JSON data to create Team Viewer connection configuration with
        """
        endpoint = "/api/preview/remote-administration-configurations/team-viewer"

        return self._post(endpoint, data)

    def create_team_viewer_remote_administration_session(
        self, data: dict, configuration_id: Union[int, str]
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Creates a new Team Viewer session to be used to establish a remote
        connection

        :param data: JSON data to create Team Viewer session with
        :param configuration_id: Team Viewer connection configuration ID
        """
        endpoint = (
            "/api/preview/remote-administration-configurations/team-viewer/"
            f"{configuration_id}/sessions"
        )

        return self._post(endpoint, data)

    def create_team_viewer_remote_administration_session_notification(
        self, configuration_id: Union[int, str], session_id: Union[int, str]
    ) -> str:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Resends configured notifications (e.g. Self Service push notifications)
        for Team Viewer session by ID

        :param configuration_id: Team Viewer connection configuration ID
        :param session_id: Team Viewer session ID
        """
        endpoint = (
            "/api/preview/remote-administration-configurations/team-viewer/"
            f"{configuration_id}/sessions/{session_id}/resend-notification"
        )

        return self._post(
            endpoint,
            success_message=(
                (
                    f"Team Viewer configuration {configuration_id} session "
                    f"{session_id} notifications successfully resent."
                )
            ),
        )

    def update_team_viewer_remote_administration_connection_configuration(
        self, data: dict, id: Union[int, str]
    ) -> dict:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Updates Team Viewer remote administration connection configuration by
        ID with JSON

        :param data:
            JSON data to update Team Viewer connection configuration with
        :param id: Team Viewer connection configuration ID
        """
        endpoint = f"/api/preview/remote-administration-configurations/team-viewer/{id}"

        return self._put(endpoint, data)

    def delete_team_viewer_remote_administration_connection_configuration(
        self, id: Union[int, str]
    ) -> str:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Deletes Team Viewer remote administration connection configuration by
        ID

        :param id: Team Viewer connection configuration ID
        """
        endpoint = f"/api/preview/remote-administration-configurations/team-viewer/{id}"

        return self._delete(
            endpoint,
            success_message=(
                f"Team Viewer connection configuration {id} successfully deleted."
            ),
        )

    def delete_team_viewer_remote_administration_session(
        self, configuration_id: Union[int, str], session_id: Union[int, str]
    ) -> str:
        """
        PREVIEW: THIS ENDPOINT IS A PREVIEW, IT CAN BE CHANGED OR REMOVED
        ON FUTURE JAMF PRO RELEASES. NOT RECOMMENDED FOR PRODUCTION USE.

        Closes a Team Viewer remote session by ID

        :param configuration_id: Team Viewer connection configuration ID
        :param session_id: Team Viewer session ID
        """
        endpoint = (
            "/api/preview/remote-administration-configurations/team-viewer/"
            f"{configuration_id}/sessions/{session_id}/close"
        )

        return self._post(
            endpoint,
            success_message=(
                (
                    f"Team Viewer configuration {configuration_id} session "
                    f"{session_id} successfully closed."
                )
            ),
        )

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
