from typing import List, Union

from request_builder import RequestBuilder
from utils import (
    check_conflicting_params,
    identification_type,
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
        query_string = [f"criteria={criteria}", f"site={site}", f"contains={contains}"]

        return self._get(endpoint, query_string=query_string)

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
            if isinstance(id, str) or isinstance(id, int):
                endpoint = f"/api/v1/advanced-mobile-device-searches/{id}"
                return self._delete(
                    endpoint,
                    success_message=(
                        f"Advanced mobile device search {id} successfully deleted."
                    ),
                )
            else:
                raise TypeError("id must be a single number")
        # I have a ticket in with Jamf about this one not working
        if ids:
            if isinstance(ids, List):
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
            else:
                raise TypeError("ids must be a List of ids")

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
