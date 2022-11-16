from typing import List, Union

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
