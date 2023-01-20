from mimetypes import guess_type
from os.path import basename
from typing import List, Union

from jps_api_wrapper.request_builder import RequestBuilder
from jps_api_wrapper.utils import (
    InvalidParameterOptions,
    check_conflicting_params,
    enforce_params,
    identification_type,
    param_or_data,
    valid_param_options,
    valid_subsets,
    validate_date,
)


class Classic(RequestBuilder):
    def __init__(self, base_url, username, password):
        super().__init__(base_url, username, password)  # pragma: no cover

    """
    /accounts
    """

    def get_accounts(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all accounts and account groups.

        :param data_type: json or xml

        :returns: All accounts in either JSON or XML
        """
        endpoint = "/JSSResource/accounts"

        return self._get(endpoint, data_type)

    def get_account(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns an account by either ID or name in JSON or XML. Need to supply
        at least one identifier.

        :param id: Account ID
        :param name: Account name
        :param data_type: json or xml

        :returns: Account information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/accounts/user{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def get_account_group(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns an account group by either ID or name in JSON or XML. Need to
        supply at least one identifier.

        :param id: Account group ID
        :param name: Account group name
        :param data_type: json or xml

        :returns: Account group information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/accounts/group{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_account(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates an account with the given XML data. Use ID 0 to use the
        next available ID.

        :param data:
            XML data to create the account with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createaccountbyid>`__
        :param id: ID of the new account, use 0 for next available ID

        :returns: New account information in XML
        """
        endpoint = f"/JSSResource/accounts/userid/{id}"

        return self._post(endpoint, data, data_type="xml")

    def create_account_group(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates an account group with the given XML data. Use ID 0 to use the
        next available ID.

        :param data:
            XML data to create the account group with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/creategroupbyid>`__
        :param id: ID of the new account group, set to 0 for next available ID

        :returns: New account group information in XML
        """
        endpoint = f"/JSSResource/accounts/groupid/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_account(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates an account with the given XML data by either ID or name.
        Need to supply at least one identifier.

        :param data:
            XML data to update the account with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateaccountbyid>`__
        :param id: Account ID
        :param name: Account name

        :returns: Updated account information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/accounts/user{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def update_account_group(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates an account group with the given XML data by either ID or name.
        Need to supply at least one identifier.

        :param data:
            XML data to update the account group with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updategroupbyid>`__
        :param id: Account group ID
        :param name: Account group name

        :returns: Updated account group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/accounts/group{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_account(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes an account by ID or name. Need to supply at leas one
        identifier.

        :param id: Account ID
        :param name: Account name

        :returns: Deleted account information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/accounts/user{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    def delete_account_group(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes an account group by ID or name. Need to supply at leas one
        identifier.

        :param id: Account group ID
        :param name: Account group name

        :returns: Deleted account group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/accounts/group{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /activationcode
    """

    def get_activation_code(self, data_type: str = "json") -> str:
        """
        Returns the activation code of the JPS server.

        :param data_type: json or xml

        :returns: Activation code information in JSON or XML
        """
        endpoint = "/JSSResource/activationcode"

        return self._get(endpoint, data_type)

    def update_activation_code(self, data: str) -> str:
        """
        Updates the activation code of the JPS server.

        :param data:
            XML data to update the activation code with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateactivationcode>`__

        :returns: Updated activation code information in XML
        """
        endpoint = "/JSSResource/activationcode"

        return self._put(endpoint, data, data_type="xml")

    """
    /advancedcomputersearches
    """

    def get_advanced_computer_searches(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all advanced computer searches in either JSON or XML.

        :param data_type: json or xml

        :returns: All advanced computer searches in JSON or XML
        """
        endpoint = "/JSSResource/advancedcomputersearches"

        return self._get(endpoint, data_type)

    def get_advanced_computer_search(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific advanced computer search by either ID or
        name.

        :param id: Advanced computer search ID
        :param name: Advanced computer search name
        :param data_type: json or xml

        :returns: Advanced computer search information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedcomputersearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_advanced_computer_search(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates an advanced computer search with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the advanced computer search with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createadvancedcomputersearchgbyid>`__
        :param id:
            ID of the new advanced computer search, use 0 for next available ID

        :returns: New advanced computer search information in XML
        """
        endpoint = f"/JSSResource/advancedcomputersearches/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_advanced_computer_search(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates and advanced computer search with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the advanced computer search with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateadvancedcomputersearchbyid>`__
        :param id: Advanced computer search ID
        :param name: Advanced computer search name

        :returns: Updated advanced computer search information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedcomputersearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_advanced_computer_search(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes an advanced computer search by either ID or name. Need to
        supply at least one identifier.

        :param id: Advanced computer search ID
        :param name: Advanced computer search name

        :returns:
            Deleted advanced computer search information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedcomputersearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /advancedmobiledevicesearches
    """

    def get_advanced_mobile_device_searches(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all advanced mobile device searches in either JSON or XML.

        :param data_type: json or xml

        :returns: All advanced mobile device searches in JSON or XML
        """
        endpoint = "/JSSResource/advancedmobiledevicesearches"

        return self._get(endpoint, data_type)

    def get_advanced_mobile_device_search(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific advanced mobile device search by either ID
        or name.

        :param id: Advanced mobile device search ID
        :param name: Advanced mobile device search name
        :param data_type: json or xml

        :returns: Advanced mobile device search information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedmobiledevicesearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_advanced_mobile_device_search(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates an advanced mobile device search with the given XML data. Use
        ID 0 to use the next available ID.

        :param data:
            XML data to create the advanced mobile device search with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createadvancedmobiledevicesearchbyid>`__
        :param id:
            ID of the new advanced mobile device search, use 0 for next
            available ID

        :returns: New advanced mobile device search information in XML
        """
        endpoint = f"/JSSResource/advancedmobiledevicesearches/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_advanced_mobile_device_search(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates and advanced mobile device search with the given XML data. Need
        to supply at least one identifier.

        :param data:
            XML data to update the advanced mobile device search with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateadvancedmobiledevicesearchbyid>`__
        :param id: Advanced mobile device search ID
        :param name: Advanced mobile device search name

        :returns: Updated advanced mobile device search information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedmobiledevicesearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_advanced_mobile_device_search(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes an advanced mobile device search by either ID or name. Need
        to supply at least one identifier.

        :param id: Advanced mobile device search ID
        :param name: Advanced mobile device search name

        :returns:
            Deleted advanced mobile device search information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedmobiledevicesearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /advancedusersearches
    """

    def get_advanced_user_searches(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all advanced user searches in either JSON or XML.

        :param data_type: json or xml

        :returns: All advanced user searches in JSON or XML
        """
        endpoint = "/JSSResource/advancedusersearches"

        return self._get(endpoint, data_type)

    def get_advanced_user_search(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific advanced user search by either ID or
        name.

        :param id: Advanced user search ID
        :param name: Advanced user search name
        :param data_type: json or xml

        :returns: Advanced user search information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedusersearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_advanced_user_search(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates an advanced user search with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the advanced user search with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createadvancedusersearchgbyid>`__
        :param id:
            ID of the new advanced user search, use 0 for next available ID

        :returns: New advanced user search information in XML
        """
        endpoint = f"/JSSResource/advancedusersearches/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_advanced_user_search(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates and advanced user search with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the advanced user search with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateadvancedusersearchbyid>`__
        :param id: Advanced user search ID
        :param name: Advanced user search name

        :returns: Updated advanced user search information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedusersearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_advanced_user_search(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes an advanced user search by either ID or name. Need to supply
        at least one identifier.

        :param id: Advanced user search ID
        :param name: Advanced user search name

        :returns:
            Deleted advanced used search information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/advancedusersearches/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /allowedfileextensions
    """

    def get_allowed_file_extensions(self, data_type="json") -> Union[dict, str]:
        """
        Returns all allowed file extensions in either JSON or XML

        :param data_type: json or xml

        :returns: All allowed file extensions in JSON or XML
        """
        endpoint = "/JSSResource/allowedfileextensions"

        return self._get(endpoint, data_type)

    def get_allowed_file_extension(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on one allowed file extension by ID or name in either
        JSON or XML

        :param id: Allowed file extension ID
        :param name: Allowed file extension name
        :param data_type: json or xml

        :returns: Allowed file extension information in JSON or XML
        """
        identification_options = {"id": id, "name": name}
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/allowedfileextensions/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_allowed_file_extension(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates an allowed file extension with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the allowed file extension. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createallowedfileextensionbyid>`__
        :param id: Allowed file extension id

        :returns: New allowed file extension information in XML
        """
        endpoint = f"/JSSResource/allowedfileextensions/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def delete_allowed_file_extension(self, id: Union[int, str]) -> str:
        """
        Deletes an allowed file extension with the given ID.

        :param id: Allowed file extension ID

        :returns:
            Deleted allowed file extension information in XML
        """
        endpoint = f"/JSSResource/allowedfileextensions/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /buildings
    """

    def get_buildings(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all buildings in either JSON or XML.

        :param data_type: json or xml

        :returns: All buildings in JSON or XML
        """
        endpoint = "/JSSResource/buildings"

        return self._get(endpoint, data_type)

    def get_building(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific building by either ID or
        name.

        :param id: building ID
        :param name: building name
        :param data_type: json or xml

        :returns: Building information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/buildings/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_building(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a building with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the building with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createbuildingbyid>`__
        :param id:
            ID of the new building, use 0 for next available ID

        :returns: New building information in XML
        """
        endpoint = f"/JSSResource/buildings/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_building(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a building with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the building with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatebuildingbyid>`__
        :param id: building ID
        :param name: building name

        :returns: Updated building information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/buildings/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_building(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a building by either ID or name. Need to supply
        at least one identifier.

        :param id: building ID
        :param name: building name

        :returns: Deleted building information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/buildings/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /byoprofiles
    """

    def get_byo_profiles(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all BYO profiles in either JSON or XML.

        :param data_type: json or xml

        :returns: All BYO profiles in JSON or XML
        """
        endpoint = "/JSSResource/byoprofiles"

        return self._get(endpoint, data_type)

    def get_byo_profile(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific BYO profile by either ID or
        name.

        :param id: BYO profile ID
        :param name: BYO profile name
        :param data_type: json or xml

        :returns: BYO profile information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/byoprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_byo_profile(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a BYO profile with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the byo profile with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createbyoprofilesbyid>`__
        :param id:
            ID of the new BYO profile, use 0 for next available ID

        :returns: New BYO profile information in XML
        """
        endpoint = f"/JSSResource/byoprofiles/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_byo_profile(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a BYO profile with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the BYO profile with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatebyoprofilesbyid>`__
        :param id: BYO profile ID
        :param name: BYO profile name

        :returns: Updated BYO profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/byoprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_byo_profile(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a byo profile by either ID or name. Need to supply
        at least one identifier.

        :param id: byo profile ID
        :param name: byo profile name

        :returns: Deleted BYO profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/byoprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /categories
    """

    def get_categories(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all categories in either JSON or XML.

        :param data_type: json or xml

        :returns: All categories in JSON or XML
        """
        endpoint = "/JSSResource/categories"

        return self._get(endpoint, data_type)

    def get_category(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific category by either ID or
        name.

        :param id: category ID
        :param name: category name
        :param data_type: json or xml

        :returns: Category information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/categories/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_category(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a category with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the category with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createcategorybyid>`__
        :param id:
            ID of the new category, use 0 for next available ID

        :returns: New category information in XML
        """
        endpoint = f"/JSSResource/categories/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_category(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a category with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the category with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatecategorybyid>`__
        :param id: category ID
        :param name: category name

        :returns: Updated category information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/categories/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_category(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a category by either ID or name. Need to supply
        at least one identifier.

        :param id: category ID
        :param name: category name

        :returns: Deleted category information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/categories/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /classes
    """

    def get_classes(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all classes in either JSON or XML.

        :param data_type: json or xml

        :returns: All classes in JSON or XML
        """
        endpoint = "/JSSResource/classes"

        return self._get(endpoint, data_type)

    def get_class(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific class by either ID or
        name.

        :param id: class ID
        :param name: class name
        :param data_type: json or xml

        :returns: Class information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/classes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_class(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a class with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the class with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createclassbyid>`__
        :param id:
            ID of the new class, use 0 for next available ID

        :returns: New class information in XML
        """
        endpoint = f"/JSSResource/classes/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_class(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a class with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the class with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateclassbyid>`__
        :param id: class ID
        :param name: class name

        :returns: Updated class information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/classes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_class(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a class by either ID or name. Need to supply
        at least one identifier.

        :param id: class ID
        :param name: class name

        :returns: Deleted class information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/classes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /commandflush
    """

    def create_command_flush(
        self,
        idtype: str = None,
        id: Union[int, str] = None,
        status: str = None,
        data: str = None,
    ) -> str:
        """
        Flushes commands to a specified selection of computers or devices. Can
        choose to flush either pending, failed, or both. Use either the idtype,
        id, and status parameters or data.

        :param idtype: Type of device to be flushed

        Options:
        - computers
        - computergroups
        - mobiledevices
        - mobiledevicegroups

        :param id: ID of device to be flushed
        :param status: Command status to be flushed

        Options:
        - Pending
        - Failed
        - Pending+Failed

        :param data:
            XML data to define command flushing. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/commandflush-1>`__

        :returns: Command flush results in XML
        """
        params = {"idtype": idtype, "id": id, "status": status}
        param_type = param_or_data(params, data)
        if param_type == "params":
            idtype_options = [
                "computers",
                "computergroups",
                "mobiledevices",
                "mobiledevicegroups",
            ]
            status_options = ["Pending", "Failed", "Pending+Failed"]
            enforce_params(params)
            valid_param_options(idtype, idtype_options)
            valid_param_options(status, status_options)

            endpoint = f"/JSSResource/commandflush/{idtype}/id/{id}/status/{status}"
        if param_type == "data":
            endpoint = "/JSSResource/commandflush"

        return self._delete(endpoint, data, data_type="xml")

    """
    /computerapplications
    """

    def get_computer_application(
        self,
        application: str,
        version: Union[int, float, str] = None,
        inventory: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns computer applications based on name. You can also filter by
        version and return additional inventory data.

        :param application: Application name, must include extension (.app)
        :param version: Application version
        :param inventory:
            Display fields seperated by commas without spaces
            e.g. Platform,Bar Code,HostName

        :returns: Computer application information in JSON or XML
        """
        if not version and not inventory:
            endpoint = f"/JSSResource/computerapplications/application/{application}"
        if version and not inventory:
            endpoint = (
                f"/JSSResource/computerapplications/application/{application}"
                f"/version/{version}"
            )
        if not version and inventory:
            endpoint = (
                f"/JSSResource/computerapplications/application/{application}"
                f"/inventory/{inventory}"
            )
        if version and inventory:
            endpoint = (
                f"/JSSResource/computerapplications/application/{application}"
                f"/version/{version}/inventory/{inventory}"
            )

        return self._get(endpoint, data_type)

    """
    /computerapplicationusage
    """

    def get_computer_application_usage(
        self,
        start_date: str,
        end_date: str,
        id: Union[int, str] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns computer application usage data in a date range specified by
        start_date and end_date and one identifier.

        :param start_date: Start date (e.g. yyyy-mm-dd)
        :param end_date: End date (e.g. yyyy-mm-dd)
        :param id: Computer ID
        :param name: Computer name
        :param udid: Computer UDID
        :param serialnumber: Computer serial number
        :param macaddress: Computer MAC address,
        :param data_type: json or xml

        :returns: Computer application usage information in JSON or XML
        """
        validate_date(start_date)
        validate_date(end_date)
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerapplicationusage/{identification}"
            f"/{identification_options[identification]}"
            f"/{start_date}_{end_date}"
        )

        return self._get(endpoint, data_type)

    """
    /computercheckin
    """

    def get_computer_check_in(self, data_type: str = "json"):
        """
        Returns all computer check in information

        :param data_type: json or xml

        :returns: All computer check in information in JSON or XML
        """
        endpoint = "/JSSResource/computercheckin"

        return self._get(endpoint, data_type)

    def update_computer_check_in(self, data: str) -> str:
        """
        Updates computer check in information based on XML data

        :param data:
            XML data to update computer check in with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatecomputercheckin>`__

        :returns: Updated computer check in information in XML
        """
        endpoint = "/JSSResource/computercheckin"

        return self._put(endpoint, data, data_type="xml")

    """
    /computercommands
    """

    def get_computer_commands(
        self, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on all computer commands, can optionally filter by name

        :param name: Computer command name
        :param data_type: json or xml

        :returns: All computer commands in JSON or XML
        """
        if name:
            endpoint = endpoint = f"/JSSResource/computercommands/name/{name}"
        else:
            endpoint = "/JSSResource/computercommands"

        return self._get(endpoint, data_type)

    def get_computer_command(
        self, uuid: str, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific computer command by uuid

        :param uuid: Computer command UUID
        :param data_type: json or xml

        :returns: Computer command in JSON or XML
        """
        endpoint = f"/JSSResource/computercommands/uuid/{uuid}"

        return self._get(endpoint, data_type)

    def get_computer_command_status(
        self, uuid: str, data_type="json"
    ) -> Union[dict, str]:
        """
        Returns the status of a specific computer command by uuid

        :param uuid: Computer command UUID
        :param data_type: json or xml

        :returns: Computer command status in JSON or XML
        """
        endpoint = f"/JSSResource/computercommands/status/{uuid}"

        return self._get(endpoint, data_type)

    def create_computer_command(
        self,
        command: str,
        ids: List[Union[int, str]] = None,
        action: str = None,
        passcode: str = None,
        data: str = None,
    ) -> str:
        """
        Creates a new computer command

        :param command: Computer command name

        Options:
        - BlankPush
        - DeleteUser
        - DeviceLock
        - DisableRemoteDesktop
        - EnableRemoteDesktop
        - EraseDevice
        - ScheduleOSUpdate
        - SettingsDisableBluetooth
        - SettingsEnableBluetooth
        - UnlockUserAccount
        - UnmanageDevice

        :param ids: Comma seperated list of IDs without spaces (e.g. 8,10,55)
        :param action:
            Options:
            - download (just downloads)
            - install (download and installs)

            Supported Commands:
            - ScheduleOSUpdate

        :param passcode:
            Passcode to apply to device, must be 6 characters. Required for
            DeviceLock and EraseDevice commands.
        :param data:
            XML data for creating computer command. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createcomputercommandbycommandandid>`__

        :returns: New computer command information in XML
        """
        command_options = [
            "BlankPush",
            "DeleteUser",
            "DeviceLock",
            "DisableRemoteDesktop",
            "EnableRemoteDesktop",
            "EraseDevice",
            "ScheduleOSUpdate",
            "SettingsDisableBluetooth",
            "SettingsEnableBluetooth",
            "UnlockUserAccount",
            "UnmanageDevice",
        ]
        valid_param_options(command, command_options)
        params = {"ids": ids}
        param_type = param_or_data(params, data)
        if param_type == "data":
            endpoint = f"/JSSResource/computercommands/command/{command}"
        if param_type == "params":
            check_conflicting_params({"action": action, "passcode": passcode})
            ids = ",".join([str(id) for id in ids])
            if (
                not action
                and not passcode
                and command not in ["DeviceLock", "EraseDevice"]
            ):
                endpoint = f"/JSSResource/computercommands/command/{command}/id/{ids}"
            if action and command in ["ScheduleOSUpdate"]:
                valid_param_options(action, ["download", "install"])
                endpoint = (
                    f"/JSSResource/computercommands/command/{command}"
                    f"/action/{action}/id/{ids}"
                )
            if passcode and command in ["DeviceLock", "EraseDevice"]:
                endpoint = (
                    f"/JSSResource/computercommands/command/{command}"
                    f"/passcode/{passcode}/id/{ids}"
                )
            if not passcode and command in ["DeviceLock", "EraseDevice"]:
                raise ValueError(
                    f"The {command} command requires the passcode parameter."
                )

        return self._post(endpoint, data, data_type="xml")

    """
    /computerextensionattributes
    """

    def get_computer_extension_attributes(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all computer extension attributes in either JSON or XML.

        :param data_type: json or xml

        :returns: All computer extension attributes in JSON or XML
        """
        endpoint = "/JSSResource/computerextensionattributes"

        return self._get(endpoint, data_type)

    def get_computer_extension_attribute(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific computer extension attribute by either ID or
        name.

        :param id: computer extension attribute ID
        :param name: computer extension attribute name
        :param data_type: json or xml

        :returns: Computer extension attribute information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_computer_extension_attribute(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a computer extension attribute with the given XML data. Use
        ID 0 to use the next available ID.

        :param data:
            XML data to create the computer extension attribute with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createcomputerextensionattributebyid>`__
        :param id:
            ID of the new computer extension attribute, use 0 for next
            available ID

        :returns: New computer extension attribute information in XML
        """
        endpoint = f"/JSSResource/computerextensionattributes/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_computer_extension_attribute(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a computer extension attribute with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the computer extension attribute with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatecomputerextensionattributebyid>`__
        :param id: computer extension attribute ID
        :param name: computer extension attribute name

        :returns: Updated computer extension attribute information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_computer_extension_attribute(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a computer extension attribute by either ID or name. Need to
        supply at least one identifier.

        :param id: computer extension attribute ID
        :param name: computer extension attribute name

        :returns:
            Deleted computer extension attribute information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /computergroups
    """

    def get_computer_groups(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all computer groups in either JSON or XML.

        :param data_type: json or xml

        :returns: All computer groups in JSON or XML
        """
        endpoint = "/JSSResource/computergroups"

        return self._get(endpoint, data_type)

    def get_computer_group(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific computer group by either ID or
        name.

        :param id: computer group ID
        :param name: computer group name
        :param data_type: json or xml

        :returns: Computer group information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computergroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_computer_group(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a computer group with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the computer group with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createcomputergroupbyid>`__
        :param id:
            ID of the new computer group, use 0 for next
            available ID

        :returns: New computer group information in XML
        """
        endpoint = f"/JSSResource/computergroups/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_computer_group(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a computer group with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the computer group with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatecomputergroupbyid>`__
        :param id: computer group ID
        :param name: computer group name

        :returns: Updated computer group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computergroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_computer_group(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a computer group by either ID or name. Need to supply
        at least one identifier.

        :param id: computer group ID
        :param name: computer group name

        :returns: Deleted computer group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computergroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /computerhardwaresoftwarereports
    """

    def get_computer_hardware_software_reports(
        self,
        start_date: str,
        end_date: str,
        id: Union[int, str] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns computer hardware and software reports data in a date range
        specified by start_date and end_date and one identifier and optional
        subsets.

        :param start_date: Start date (e.g. yyyy-mm-dd)
        :param end_date: End date (e.g. yyyy-mm-dd)
        :param id: Computer ID
        :param name: Computer name
        :param udid: Computer UDID
        :param serialnumber: Computer serial number
        :param macaddress: Computer MAC address,
        :param subsets:
            Subset(s) of data from the computer hardware software report in a
            list of strings

            Options:
            - Software
            - Hardware
            - Fonts
            - Plugins

        :param data_type: json or xml

        :returns:
            Computer hardware and software reports information in JSON or XML
        """
        validate_date(start_date)
        validate_date(end_date)
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        subset_options = ["Software", "Hardware", "Fonts", "Plugins"]
        identification = identification_type(identification_options)
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/computerhardwaresoftwarereports/{identification}"
                f"/{identification_options[identification]}"
                f"/{start_date}_{end_date}/subset/{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/computerhardwaresoftwarereports/{identification}"
                f"/{identification_options[identification]}"
                f"/{start_date}_{end_date}"
            )

        return self._get(endpoint, data_type)

    """
    /computerhistory
    """

    def get_computer_history(
        self,
        id: Union[int, str] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns computer history data with the given identifier and optional
        subsets. Need to supply at least one identifier.

        :param id: Computer ID
        :param name: Computer name
        :param udid: Computer UDID
        :param serialnumber: Computer serial number
        :param macaddress: Computer MAC address,
        :param subsets:
            Subset(s) of data from the computer history in a list of strings
            Options:
            - General
            - ComputerUsageLogs
            - Audits
            - PolicyLogs
            - CasperRemoteLogs
            - ScreenSharingLogs
            - CasperImagingLogs
            - Commands
            - UserLocation
            - MacAppStoreApplications

        :param data_type: json or xml

        :returns: Computer history information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        subset_options = [
            "General",
            "ComputerUsageLogs",
            "Audits",
            "PolicyLogs",
            "CasperRemoteLogs",
            "ScreenSharingLogs",
            "CasperImagingLogs",
            "Commands",
            "UserLocation",
            "MacAppStoreApplications",
        ]
        identification = identification_type(identification_options)
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/computerhistory/{identification}"
                f"/{identification_options[identification]}"
                f"/subset/{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/computerhistory/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    """
    /computerinventorycollection
    """

    def get_computer_inventory_collection(self, data_type="json") -> Union[dict, list]:
        """
        Returns computer inventory collection settings on the JPS server in
        either JSON or XML.

        :param data_type: json or xml

        :returns: Computer inventory collection in JSON or XML
        """
        endpoint = "/JSSResource/computerinventorycollection"

        return self._get(endpoint, data_type)

    def update_computer_inventory_collection(self, data: str) -> str:
        """
        Updates computer inventory collection settings on the JPS server with
        the given XML data. Need to supply at least one identifier.

        :param data:
            XML data to update the computer inventory collection. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatecomputerinventorycollection>`__

        :returns: Updated computer inventory collection information in XML
        """
        endpoint = "/JSSResource/computerinventorycollection"

        return self._put(endpoint, data, data_type="xml")

    """
    /computerinvitations
    """

    def get_computer_invitations(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all computer invitation data in either JSON or XML.

        :param data_type: json or xml

        :returns: All computer invitations in JSON or XML
        """
        endpoint = "/JSSResource/computerinvitations"

        return self._get(endpoint, data_type)

    def get_computer_invitation(
        self,
        id: Union[int, str] = None,
        invitation: Union[int, str] = None,
        data_type: str = "json",
    ):
        """
        Returns information on a single computer invitation defined by either
        ID or invitation. Need to supply at least one identifier.

        :param id: Computer invitation ID
        :param invitation:
            Computer invitation invitation identifier (name)
            Typically a long int
        :param data_type: json or xml

        :returns: Computer invitation information in JSON or XML
        """
        identification_options = {
            "id": id,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerinvitations/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_computer_invitation(
        self, data: str, id: Union[int, str] = None, invitation: Union[int, str] = None
    ) -> str:
        """
        Creates a computer invitation defined by the XML data and either ID
        or invitation.

        :param data:
            XML data to create computer invitation with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createcomputerinvitationsbyid>`__
        :param id: Computer invitation ID, use 0 for next available
        :param invitation:
            Computer invitation invitation identifier, use 0 for next available

        :returns: New computer invitation information in XML
        """
        identification_options = {
            "id": id,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerinvitations/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._post(endpoint, data, data_type="xml")

    def delete_computer_invitation(
        self, id: Union[int, str] = None, invitation: Union[int, str] = None
    ) -> str:
        """
        Deletes a computer invitation by either ID or invitation identifiers.
        Need to supply at least one identifier.

        :param id: Computer invitation ID
        :param invitation:
            Computer invitation invitation identifier (name)
            Typically a long int

        :returns: Deleted computer invitation information in XML
        """
        identification_options = {
            "id": id,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerinvitations/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /computermanagement
    """

    def get_computer_management(
        self,
        id: Union[int, str] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
        username: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns computer management data in a date range specified by
        start_date and end_date and one identifier and optional subsets.
        Need to supply at least one identifier.

        :param id: Computer ID
        :param name: Computer name
        :param udid: Computer UDID
        :param serialnumber: Computer serial number
        :param macaddress: Computer MAC address
        :param username: User to filter by
        :param subsets:
            Subset(s) of data from the computer management in a list of strings
            Options:
            - General
            - Policies
            - Ebooks
            - MacAppStoreApps
            - OSXConfigurationProfiles
            - ManagedPreferenceProfiles
            - RestrictedSoftware
            - SmartGroups
            - StaticGroups
            - PatchReportingSoftwareTitles

        :param data_type: json or xml

        :returns: Computer management information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        subset_options = [
            "General",
            "Policies",
            "Ebooks",
            "MacAppStoreApps",
            "OSXConfigurationProfiles",
            "ManagedPreferenceProfiles",
            "RestrictedSoftware",
            "SmartGroups",
            "StaticGroups",
            "PatchReportingSoftwareTitles",
        ]
        identification = identification_type(identification_options)
        if valid_subsets(subsets, subset_options) and username:
            endpoint = (
                f"/JSSResource/computermanagement/{identification}"
                f"/{identification_options[identification]}"
                f"/username/{username}"
                f"/subset/{'&'.join(subsets)}"
            )
        elif valid_subsets(subsets, subset_options) and not username:
            endpoint = (
                f"/JSSResource/computermanagement/{identification}"
                f"/{identification_options[identification]}"
                f"/subset/{'&'.join(subsets)}"
            )
        elif not subsets and username:
            endpoint = (
                f"/JSSResource/computermanagement/{identification}"
                f"/{identification_options[identification]}"
                f"/username/{username}"
            )
        else:
            endpoint = (
                f"/JSSResource/computermanagement/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    """
    /computerreports
    """

    def get_computer_reports(self, data_type="json") -> Union[dict, str]:
        """
        Returns all computer reports in a JPS server

        :param data_type: json or xml

        :returns: All computer reports in JSON or XML
        """
        endpoint = "/JSSResource/computerreports"

        return self._get(endpoint, data_type)

    def get_computer_report(
        self, id: Union[int, str] = None, name: str = None, data_type="json"
    ) -> Union[dict, str]:
        """
        Returns data on one computer report by either ID or name. Need to
        supply at least one identifier.

        :param id: Computer report ID
        :param name: Computer report name
        :param data_type: json or xml

        :returns: Computer report information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/computerreports/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    """
    /computers
    """

    def get_computers(
        self, match: str = None, basic: bool = False, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all computers with optional filters match and matchname and the
        option to only return basic information by setting basic to True.

        :param match:
            Name, mac address, etc. to filter by. Match uses the same format
            as the general search in Jamf Pro. For instance, admin* can be
            used to match computer names that begin with admin
        :param basic: Only return basic info
        :param data_type: json or xml

        :returns: All computers in JSON or XML
        """
        check_conflicting_params({"match": match, "basic": basic})
        if match:
            endpoint = f"/JSSResource/computers/match/{match}"
        else:
            if basic:
                endpoint = "/JSSResource/computers/subset/basic"
            else:
                endpoint = "/JSSResource/computers"

        return self._get(endpoint, data_type)

    def get_computer(
        self,
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ):
        """
        Returns information on a computer with given identifier in either
        JSON or XML. You can specify the return of a subset of the data by
        defining subset as a list of the subsets that you want. Need to supply
        at least one identifier.

        :param id: Computer ID
        :param name: Computer name
        :param udid: Computer UDID
        :param serialnumber: Computer serial number
        :param macaddress: Computer MAC address
        :param subsets:
            Subset(s) of data from the computer in a list of strings
            Options:
            - General
            - Location
            - Purchasing
            - Peripherals
            - Hardware
            - Certificates
            - Software
            - ExtensionAttributes
            - GroupsAccounts
            - iphones
            - ConfigurationProfiles

        :param data_type: json or xml

        :returns: Computer information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        subset_options = [
            "General",
            "Location",
            "Purchasing",
            "Peripherals",
            "Hardware",
            "Certificates",
            "Software",
            "ExtensionAttributes",
            "GroupsAccounts",
            "iphones",
            "ConfigurationProfiles",
        ]
        identification = identification_type(identification_options)

        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/computers/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/computers/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_computer(self, data: str, id: Union[str, int] = 0) -> str:
        """
        Creates a computer with the given ID and information defined in
        XML data.

        :param data:
            XML data to create computer record with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createcomputerbyid>`__
        :param id: Computer ID, set to 0 for next available ID

        :returns: New computer information in XML
        """
        endpoint = f"/JSSResource/computers/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_computer(
        self,
        data: str,
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
    ) -> str:
        """
        Updates information on a computer with given identifier. Need to
        supply at least one identifier.

        :param data:
            XML string to update the computer with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatecomputerbyid>`__
        :param id: Computer ID
        :param name: Computer name
        :param udid: Computer UDID
        :param serialnumber: Computer serial number
        :param macaddress: Computer MAC address

        :returns: Updated computer information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        identification = identification_type(identification_options)

        endpoint = (
            f"/JSSResource/computers/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_computer(
        self,
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
    ) -> str:
        """
        Deletes a computer with given identifier. Need to supply at least
        one identifier.

        :param id: computer ID
        :param name: computer name
        :param udid: computer UDID
        :param serialnumber: computer serial number
        :param macaddress: computer MAC address

        :returns:
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        identification = identification_type(identification_options)

        endpoint = (
            f"/JSSResource/computers/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    def delete_computers_extension_attribute_data(self, id: Union[int, str]) -> str:
        """
        Deletes data collected by an extension attribute by ID

        :param id: ID of the computer extension attribute data to be deleted

        :returns: Deleted computers extension attribute data information in XML
        """
        endpoint = f"/JSSResource/computers/extensionattributedataflush/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /departments
    """

    def get_departments(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all departments in either JSON or XML.

        :param data_type: json or xml

        :returns: All departments in JSON or XML
        """
        endpoint = "/JSSResource/departments"

        return self._get(endpoint, data_type)

    def get_department(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific department by either ID or
        name.

        :param id: Department ID
        :param name: Department name
        :param data_type: json or xml

        :returns: Department information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/departments/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_department(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a department with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the department with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createdepartmentbyid>`__
        :param id:
            ID of the new department, use 0 for next
            available ID

        :returns: New department information in XML
        """
        endpoint = f"/JSSResource/departments/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_department(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a department with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the department with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatedepartmentbyid>`__
        :param id: Department ID
        :param name: Department name

        :returns: Updated department information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/departments/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_department(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a department by either ID or name. Need to supply
        at least one identifier.

        :param id: Department ID
        :param name: Department name

        :returns: Deleted department information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/departments/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /directorybindings
    """

    def get_directory_bindings(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all directory bindings in either JSON or XML.

        :param data_type: json or xml

        :returns: All directory bindings in JSON or XML
        """
        endpoint = "/JSSResource/directorybindings"

        return self._get(endpoint, data_type)

    def get_directory_binding(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific directory binding by either ID or
        name.

        :param id: Directory binding ID
        :param name: Directory binding name
        :param data_type: json or xml

        :returns: Directory binding information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/directorybindings/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_directory_binding(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a directory binding with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the directory binding with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createdirectorybindingbyid>`__
        :param id:
            ID of the new directory binding, use 0 for next
            available ID

        :returns: New directory binding information in XML
        """
        endpoint = f"/JSSResource/directorybindings/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_directory_binding(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a directory binding with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the directory binding with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatedirectorybindingbyid>`__
        :param id: Directory binding ID
        :param name: Directory binding name

        :returns: Updated directory binding information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/directorybindings/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_directory_binding(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a directory binding by either ID or name. Need to supply
        at least one identifier.

        :param id: Directory binding ID
        :param name: Directory binding name

        :returns: Deleted directory binding information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/directorybindings/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /diskencryptionconfigurations
    """

    def get_disk_encryption_configurations(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all disk encryption configurations in either JSON or XML.

        :param data_type: json or xml

        :returns: All disk encryption configuration information in JSON or XML
        """
        endpoint = "/JSSResource/diskencryptionconfigurations"

        return self._get(endpoint, data_type)

    def get_disk_encryption_configuration(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific disk encryption configuration by either ID
        or name.

        :param id: disk encryption configuration ID
        :param name: disk encryption configuration name
        :param data_type: json or xml

        :returns: Disk encryption cnofiguration information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/diskencryptionconfigurations/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_disk_encryption_configuration(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a disk encryption configuration with the given XML data. Use
        ID 0 to use the next available ID.

        :param data:
            XML data to create the disk encryption configuration with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/creatediskencryptionconfigurationbyid>`__
        :param id:
            ID of the new disk encryption configuration, use 0 for next
            available ID

        :returns: New disk encryption configuration information in XML
        """
        endpoint = f"/JSSResource/diskencryptionconfigurations/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_disk_encryption_configuration(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a disk encryption configuration with the given XML data. Need
        to supply at least one identifier.

        :param data:
            XML data to update the disk encryption configuration with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatediskencryptionconfigurationbyid>`__
        :param id: disk encryption configuration ID
        :param name: disk encryption configuration name

        :returns: Updated disk encryption configuration information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/diskencryptionconfigurations/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_disk_encryption_configuration(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a disk encryption configuration by either ID or name. Need to
        supply at least one identifier.

        :param id: disk encryption configuration ID
        :param name: disk encryption configuration name

        :returns: Deleted disk encryption configuration information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/diskencryptionconfigurations/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /distributionpoints
    """

    def get_distribution_points(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all distribution points in either JSON or XML.

        :param data_type: json or xml

        :returns: All disribution points in JSON or XML
        """
        endpoint = "/JSSResource/distributionpoints"

        return self._get(endpoint, data_type)

    def get_distribution_point(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific distribution point by either ID or
        name.

        :param id: Distribution point ID
        :param name: Distribution point name
        :param data_type: json or xml

        :returns: Distribution point information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/distributionpoints/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_distribution_point(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a distribution point with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the distribution point with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createdistributionpointbyid>`__
        :param id:
            ID of the new distribution point, use 0 for next
            available ID

        :returns: New distribution point information in XML
        """
        endpoint = f"/JSSResource/distributionpoints/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_distribution_point(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a distribution point with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the distribution point with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatedistributionpointbyid>`__
        :param id: Distribution point ID
        :param name: Distribution point name

        :returns: Updated distribution point information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/distributionpoints/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_distribution_point(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a distribution point by either ID or name. Need to supply
        at least one identifier.

        :param id: Distribution point ID
        :param name: Distribution point name

        :returns: Deleted distribution point information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/distributionpoints/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /dockitems
    """

    def get_dock_items(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all dock items in either JSON or XML.

        :param data_type: json or xml

        :returns: All dock items in JSON or XML
        """
        endpoint = "/JSSResource/dockitems"

        return self._get(endpoint, data_type)

    def get_dock_item(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific dock item by either ID or name.

        :param id: Dock item ID
        :param name: Dock item name
        :param data_type: json or xml

        :returns: Dock item information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/dockitems/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_dock_item(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a dock item with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the dock item with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createdockitembyid>`__
        :param id:
            ID of the new dock item, use 0 for next
            available ID

        :returns: New dock item information in XML
        """
        endpoint = f"/JSSResource/dockitems/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_dock_item(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a dock item with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the dock item with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatedockitembyid>`__
        :param id: Dock item ID
        :param name: Dock item name

        :returns: Updated dock item information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/dockitems/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_dock_item(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a dock item by either ID or name. Need to supply
        at least one identifier.

        :param id: Dock item ID
        :param name: Dock item name

        :returns: Deleted dock item information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/dockitems/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /ebooks
    """

    def get_ebooks(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all ebooks in either JSON or XML.

        :param data_type: json or xml

        :returns: All ebooks in JSON or XML
        """
        endpoint = "/JSSResource/ebooks"

        return self._get(endpoint, data_type)

    def get_ebook(
        self,
        id: Union[int, str] = None,
        name: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific ebook by either ID or name.

        :param id: eBook ID
        :param name: eBook name
        :param subsets:
            Subset(s) of data from the eBook in a list of strings

            Options:
            - General
            - Scope
            - SelfService

        :param data_type: json or xml

        :returns: Ebook information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        subset_options = [
            "General",
            "Scope",
            "SelfService",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/ebooks/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/ebooks/{identification}/"
                f"{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_ebook(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates an ebook with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the ebook with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createebookbyid>`__
        :param id:
            ID of the new ebook, use 0 for next
            available ID

        :returns: New ebook information in XML
        """
        endpoint = f"/JSSResource/ebooks/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_ebook(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates an ebook with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the ebook with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateebookbyid>`__
        :param id: eBook ID
        :param name: eBook name

        :returns: Updated ebook information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ebooks/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_ebook(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a ebook by either ID or name. Need to supply
        at least one identifier.

        :param id: eBook ID
        :param name: eBook name

        :returns: Deleted ebook information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ebooks/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /fileuploads
    """

    # enrollmentprofiles and printers resources do not work
    # peripherals work but are no longer supported by Jamf so I didn't add them

    def create_file_upload(
        self,
        resource: str,
        filepath: str,
        id: Union[int, str] = None,
        name: str = None,
        force_ipa_upload: bool = False,
    ) -> str:
        """
        Uploads a file attachment to the specified resource by either ID or
        name. On the mobiledeviceapplicationsipa resource you can set
        force_ipa_upload to True to enforce .ipa files. The printers and
        enrollmentprofiles resources listed in the documentation do not
        actually work as documented under Classic Privilege Requirements
        here https://developer.jamf.com/jamf-pro/docs. Need to supply at least
        one identifier.

        :param resource:
            Resource to attach the file to

            Options:
            computers, mobiledevices, policies, ebooks,
            mobiledeviceapplicationsicon, mobiledeviceapplicationsipa,
            diskencryptionconfigurations

        :param filepath: Filepath to file to upload
        :param id: Resource ID
        :param name:
            Resource name, not usable with resource options peripherals
        :param force_ipa_upload:
            True of False, enforces ipa file type. Only usable with
            mobiledeviceapplicationsipa resource

        :returns: Success message stating that the file was uploaded

        :raises FileNotFoundError:
            Could not find file at file path
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        if force_ipa_upload and resource != "mobiledeviceapplicationsipa":
            raise ValueError(
                "force_ipa_upload can only be used with the "
                "mobiledeviceapplicationsipa resource"
            )
        if identification == "name" and resource == "peripherals":
            raise ValueError(
                "Name is not a usable identifier for the peripherals "
                "resource, use id instead."
            )
        if not filepath.lower().endswith(
            (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
        ) and resource in ("policies", "ebooks", "mobiledeviceapplicationicon"):
            raise ValueError(
                "Uploaded icon files to the policies, ebooks, or "
                "mobiledeviceapplicationsicon resources must be in a valid "
                "image format."
            )
        if (
            not filepath.lower().endswith((".p12", ".cer", ".pem"))
            and resource == "diskencryptionconfigurations"
        ):
            raise ValueError(
                "Uploaded recovery key files to the diskencryptionconfigurations "
                "resource must be in .p12, .cer, or .pem format."
            )
        resource_options = [
            "computers",
            "mobiledevices",
            "peripherals",
            "policies",
            "ebooks",
            "mobiledeviceapplicationsicon",
            "mobiledeviceapplicationsipa",
            "diskencryptionconfigurations",
        ]
        valid_param_options(resource, resource_options)
        try:
            with open(filepath, "rb") as f:
                filename = basename(filepath)
                content_type = guess_type(filename.lower())[0]
                if not content_type and filename.endswith(".ipa"):
                    content_type = "application/octet-stream"
                if not content_type and filename.endswith(".pem"):
                    content_type = "application/x-pem-file"
                if not content_type:
                    raise ValueError(f"Unable to detect MIME type of file {filename}")
                file = {"name": (filename, f, content_type)}
                if force_ipa_upload:
                    params = {"FORCE_IPA_UPLOAD": "true"}
                else:
                    params = None
                endpoint = (
                    f"/JSSResource/fileuploads/{resource}/{identification}"
                    f"/{identification_options[identification]}"
                )

                return self._post(
                    endpoint,
                    file=file,
                    data_type=None,
                    params=params,
                    success_message="File uploaded successfully.",
                )
        except FileNotFoundError:
            raise FileNotFoundError(f"{filepath} could not be opened.")

    """
    /gsxconnection
    """

    def get_gsx_connection(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns the Jamf Pro GSX connection information in either JSON or XML.

        :param data_type: json or xml

        :returns: GSX connection information in JSON or XML
        """
        endpoint = "/JSSResource/gsxconnection"

        return self._get(endpoint, data_type)

    def update_gsx_connection(self, data: str):
        """
        Updates the Jamf Pro GSX connection information with XML data.

        :param data:
            XML data to update with. For syntax information view `Jamf's
            documentation.
            <https://developer.jamf.com/jamf-pro/reference/updategsxconnection>`__

        :returns: Updated GSX connection information in XML
        """
        endpoint = "/JSSResource/gsxconnection"

        return self._put(endpoint, data, data_type="xml")

    """
    /healthcarelistener
    """

    def get_healthcare_listeners(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all healthcare listeners in JSON or XML

        :param data_type: json or dict

        :returns: All healthcare listeners in JSON or XML
        """
        endpoint = "/JSSResource/healthcarelistener"

        return self._get(endpoint, data_type)

    def get_healthcare_listener(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Return a healthcare listener by ID in either JSON or XML

        :param id: Healthcare listener ID
        :param data_type: json or xml

        :returns: Healthcare listener information in JSON or XML
        """
        endpoint = f"/JSSResource/healthcarelistener/id/{id}"

        return self._get(endpoint, data_type)

    def update_healthcare_listener(self, data: str, id: Union[int, str]) -> str:
        """
        Updates an existing healthcare listener by ID with XML data

        :param data:
            XML data to update healthcare listener with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatehealthcarelistenerbyid>`__
        :param id: Healthcare listener ID

        :returns: Updated healthcare listener information in XML
        """
        endpoint = f"/JSSResource/healthcarelistener/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    """
    /healthcarelistenerrule
    """

    def get_healthcare_listener_rules(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all healthcare listener rules in JSON or XML

        :param data_type: json or dict

        :returns: All healthcare listener rules in JSON or XML
        """
        endpoint = "/JSSResource/healthcarelistenerrule"

        return self._get(endpoint, data_type)

    def get_healthcare_listener_rule(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Return a healthcare listener rule by ID in either JSON or XML

        :param id: healthcare listener rule ID
        :param data_type: json or xml

        :returns: Healthcare listener rule information in JSON or XML
        """
        endpoint = f"/JSSResource/healthcarelistenerrule/id/{id}"

        return self._get(endpoint, data_type)

    def create_healthcare_listener_rule(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a healthcare listener rule by ID with XML data

        :param data:
            XML data to update healthcare listener rule with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createhealthcarelistenerrulebyid>`__
        :param id: Healthcare listener rule ID, use 0 for next available ID

        :returns: New healthcare listener rule information in XML
        """
        endpoint = f"/JSSResource/healthcarelistenerrule/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_healthcare_listener_rule(self, data: str, id: Union[int, str]) -> str:
        """
        Updates an existing healthcare listener rule by ID with XML data

        :param data:
            XML data to update healthcare listener rule with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatehealthcarelistenerrulebyid>`__
        :param id: healthcare listener rule ID

        :returns: Updated healthcare listener rule information in XML
        """
        endpoint = f"/JSSResource/healthcarelistenerrule/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    """
    /ibeacons
    """

    def get_ibeacon_regions(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all iBeacon regions in either JSON or XML.

        :param data_type: json or xml

        :returns: All iBeacon regions in JSON or XML
        """
        endpoint = "/JSSResource/ibeacons"

        return self._get(endpoint, data_type)

    def get_ibeacon_region(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific iBeacon region by either ID or name.

        :param id: iBeacon region ID
        :param name: iBeacon region name
        :param data_type: json or xml

        :returns: iBeacon region information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ibeacons/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_ibeacon_region(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a iBeacon region with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the iBeacon region with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createibeaconbyid>`__
        :param id:
            ID of the new iBeacon region, use 0 for next
            available ID

        :returns: New iBeacon region information in XML
        """
        endpoint = f"/JSSResource/ibeacons/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_ibeacon_region(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a iBeacon region with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the iBeacon region with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateibeaconbyid>`__
        :param id: iBeacon region ID
        :param name: iBeacon region name

        :returns: Updated iBeacon region information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ibeacons/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_ibeacon_region(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a iBeacon region by either ID or name. Need to supply
        at least one identifier.

        :param id: iBeacon region ID
        :param name: iBeacon region name

        :returns: Deleted iBeacon region information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ibeacons/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /infrastructuremanager
    """

    def get_infrastructure_managers(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all infrastructure managers in JSON or XML

        :param data_type: json or dict

        :returns: All infrastructure managers in JSON or XML
        """
        endpoint = "/JSSResource/infrastructuremanager"

        return self._get(endpoint, data_type)

    def get_infrastructure_manager(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Return a infrastructure manager by ID in either JSON or XML

        :param id: Infrastructure manager ID
        :param data_type: json or xml

        :returns: Infrastructure manager information in JSON or XML
        """
        endpoint = f"/JSSResource/infrastructuremanager/id/{id}"

        return self._get(endpoint, data_type)

    def update_infrastructure_manager(self, data: str, id: Union[int, str]) -> str:
        """
        Updates an existing infrastructure manager by ID with XML data

        :param data:
            XML data to update infrastructure manager with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateinfrastructuremanagerbyid>`__
        :param id: Infrastructure manager ID

        :returns: Updated infrastructure manager information in XML
        """
        endpoint = f"/JSSResource/infrastructuremanager/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    """
    /jssuser
    """

    # This endpoint no longer works

    """
    /jsonwebtokenconfigurations
    """

    def get_json_web_token_configurations(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all JSON web token configurations in JSON or XML

        :param data_type: json or dict

        :returns: All JSON web token configurations in JSON or XML
        """
        endpoint = "/JSSResource/jsonwebtokenconfigurations"

        return self._get(endpoint, data_type)

    def get_json_web_token_configuration(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Return a JSON web token configuration by ID in either JSON or XML

        :param id: JSON web token configuration ID
        :param data_type: json or xml

        :returns: JSON web token configuration in JSON or XML
        """
        endpoint = f"/JSSResource/jsonwebtokenconfigurations/id/{id}"

        return self._get(endpoint, data_type)

    def create_json_web_token_configuration(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a JSON web token configuration by ID with XML data

        :param data:
            XML data to update JSON web token configuration with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createjsonwebtokenconfigurationbyid>`__
        :param id: JSON web token configuration ID, use 0 for next available ID

        :returns: New JSON web token configuration information in XML
        """
        endpoint = f"/JSSResource/jsonwebtokenconfigurations/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_json_web_token_configuration(
        self, data: str, id: Union[int, str]
    ) -> str:
        """
        Updates an existing JSON web token configuration by ID with XML data

        :param data:
            XML data to update JSON web token configuration with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatejsonwebtokenconfigurationbyid>`__
        :param id: JSON web token configuration ID

        :returns: Updated JSON web token configuration information in XML
        """
        endpoint = f"/JSSResource/jsonwebtokenconfigurations/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_json_web_token_configuration(self, id: Union[int, str]) -> str:
        """
        Deletes a JSON web token configuration by ID with XML data

        :param id: Json web token configuration ID

        :returns: Deleted JSON web token configuration information in XML
        """
        endpoint = f"/JSSResource/jsonwebtokenconfigurations/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /ldapservers
    """

    def get_ldap_servers(self, data_type="json") -> Union[dict, str]:
        """
        Returns all LDAP servers in JSON or XML

        :param data_type: json or xml

        :returns: All LDAP servers in JSON or XML
        """
        endpoint = "/JSSResource/ldapservers"

        return self._get(endpoint, data_type)

    def get_ldap_server(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on one LDAP server by ID or name in JSON or XML

        :param id: LDAP server ID
        :param name: LDAP server name

        :returns: LDAP server information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ldapservers/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def get_ldap_server_user(
        self,
        user: str,
        id: Union[int, str] = None,
        name: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns information for matching users for an LDAP server by ID or name
        in JSON or XML

        :param user: LDAP server user
        :param id: LDAP server ID
        :param name: LDAP server name
        :param data_type: json or xml

        :returns: LDAP server user information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ldapservers/{identification}"
            f"/{identification_options[identification]}/user/{user}"
        )

        return self._get(endpoint, data_type)

    def get_ldap_server_group(
        self,
        group: str,
        id: Union[int, str] = None,
        name: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns information for matching groups for an LDAP server by ID or
        name in JSON or XML

        :param group: LDAP server group
        :param id: LDAP server ID
        :param name: LDAP server name
        :param data_type: json or xml

        :returns: LDAP server group information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ldapservers/{identification}"
            f"/{identification_options[identification]}/group/{group}"
        )

        return self._get(endpoint, data_type)

    def get_ldap_server_group_user(
        self,
        group: str,
        users: List[str],
        id: Union[int, str] = None,
        name: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns information about user membership in a group for an LDAP server
        by ID or name in JSON or XML

        :param group: LDAP server group
        :param users:
            Users to search for in the group, in a list of strings
            (e.g. ["nameone", "nametwo"])
        :param id: LDAP server ID
        :param name: LDAP server name
        :param data_type: json or xml

        :returns: LDAP server group user information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ldapservers/{identification}"
            f"/{identification_options[identification]}"
            f"/group/{group}/user/{','.join(users)}"
        )

        return self._get(endpoint, data_type)

    def create_ldap_server(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a new LDAP server by ID or name with XML data

        :param data:
            XML data to create LDAP server with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createldapserverbyid>`__
        :param id: LDAP server ID, set to 0 for next available ID

        :returns: New LDAP server information in XML
        """
        endpoint = f"/JSSResource/ldapservers/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_ldap_server(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates an existing LDAP server by ID or name with XML data

        :param data:
            XML data to update LDAP server with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateldapserverbyid>`__
        :param id: LDAP server ID
        :param name: LDAP server name

        :returns: Updated LDAP server information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ldapservers/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_ldap_server(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes an LDAP server by ID or name

        :param id: LDAP server ID
        :param name: LDAP server name

        :returns: Deleted LDAP server information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/ldapservers/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /licensedsoftware
    """

    def get_licensed_software_all(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all licensed software in either JSON or XML.

        :param data_type: json or xml

        :returns: All licensed software in JSON or XML
        """
        endpoint = "/JSSResource/licensedsoftware"

        return self._get(endpoint, data_type)

    def get_licensed_software(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific licensed software by either ID or name in
        JSON or XML.

        :param id: Licensed software ID
        :param name: Licensed software name
        :param data_type: json or xml

        :returns: Licensed software information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/licensedsoftware/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_licensed_software(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a licensed software with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the licensed software with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createlicensedsoftwarebyid>`__
        :param id:
            ID of the new licensed software, use 0 for next
            available ID

        :returns: New licensed software information in XML
        """
        endpoint = f"/JSSResource/licensedsoftware/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_licensed_software(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a licensed software with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the licensed software with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatelicensedsoftwarebyid>`__
        :param id: Licensed software ID
        :param name: Licensed software name

        :returns: Updated licensed software information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/licensedsoftware/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_licensed_software(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a licensed software by either ID or name. Need to supply
        at least one identifier.

        :param id: Licensed software ID
        :param name: Licensed software name

        :returns: Deleted licensed software information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/licensedsoftware/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /logflush
    """
    # The commands complete but nothing changes in the JPS instance
    def create_log_flush(self, data: str) -> str:
        """
        Deletes policy or computer logs based on XML data

        :param data:
            XML data that defines which logs to flush. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/logflush-1>`__

        :returns: Flushed log information in XML
        """
        endpoint = "/JSSResource/logflush"

        return self._delete(endpoint, data, data_type="xml")

    def create_log_flush_interval(
        self, interval: str, id: Union[int, str] = None
    ) -> str:
        """
        Deletes policy logs based on an interval and optionally only a single
        log defined by ID.

        :param interval:
            Supported values are a combination of [Zero, One, Two, Three, Six]
            and [Days, Weeks, Months, Years]. The values must be joined with
            a "+", e.g. One+Weeks or Six+Months.
        :param id: Policy ID

        :returns: Flushed log information in XML

        :raises ValueError: No + in interval string
        """
        if "+" not in interval:
            raise ValueError(
                "Interval values must be joined by a '+', e.g. One+Weeks or Six+Months"
            )
        if id:
            endpoint = f"/JSSResource/logflush/policy/id/{id}/interval/{interval}"
        else:
            endpoint = f"/JSSResource/logflush/policy/interval/{interval}"

        return self._delete(endpoint, data_type="xml")

    """
    /macapplications
    """

    def get_mac_applications(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all Mac applications in either JSON or XML.

        :param data_type: json or xml

        :returns: All Mac applications in JSON or XML
        """
        endpoint = "/JSSResource/macapplications"

        return self._get(endpoint, data_type)

    def get_mac_application(
        self,
        id: Union[int, str] = None,
        name: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific Mac application by either ID or name.

        :param id: Mac application ID
        :param name: Mac application name
        :param subsets:
            Subset(s) of data from the Mac application in a list of strings

            Options:
            - General
            - Scope
            - SelfService
            - VPPCodes
            - VPP

        :param data_type: json or xml

        :returns: Mac application information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        subset_options = [
            "General",
            "Scope",
            "SelfService",
            "VPPCodes",
            "VPP",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/macapplications/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/macapplications/{identification}/"
                f"{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_mac_application(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a Mac application with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the Mac application with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmacappbyid>`__
        :param id:
            ID of the new Mac application, use 0 for next
            available ID

        :returns: New Mac application information in XML
        """
        endpoint = f"/JSSResource/macapplications/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_mac_application(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a Mac application with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the Mac application with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemacappbyid>`__
        :param id: Mac application ID
        :param name: Mac application name

        :returns: Updated Mac application information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/macapplications/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_mac_application(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a Mac application by either ID or name. Need to supply
        at least one identifier.

        :param id: Mac application ID
        :param name: Mac application name

        :returns: Deleted Mac application information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/macapplications/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /managedpreferenceprofiles
    """

    """
    Managed preference profiles have been deprecated by Apple and Jamf.
    I added the ability to get, update, and delete them as you can no do these
    through the GUI but omitted creation as they should not be used.
    """

    def get_managed_preference_profiles(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all managed preference profiles in either JSON or XML.

        :param data_type: json or xml

        :returns: All managed preference profiles in JSON or XML
        """
        endpoint = "/JSSResource/managedpreferenceprofiles"

        return self._get(endpoint, data_type)

    def get_managed_preference_profile(
        self,
        id: Union[int, str] = None,
        name: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific managed preference profile by either ID or
        name.

        :param id: Managed preference profile ID
        :param name: Managed preference profile name
        :param subsets:
            Subset(s) of data from the managed preference profile in a list
            of strings

            Options:
            - General
            - Scope
            - Settings

        :param data_type: json or xml

        :returns: Managed preference profile information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        subset_options = [
            "General",
            "Scope",
            "Settings",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/managedpreferenceprofiles/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/managedpreferenceprofiles/{identification}/"
                f"{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def update_managed_preference_profile(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a managed preference profile with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the managed preference profile with. For syntax
            information view `Jamf's documentation.
            https://developer.jamf.com/jamf-pro/reference/updatemanagedpreferenceprofilesbyid>`__
        :param id: Managed preference profile ID
        :param name: Managed preference profile name

        :returns: Updated managed preference profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/managedpreferenceprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_managed_preference_profile(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a managed preference profile by either ID or name. Need to
        supply at least one identifier.

        :param id: Managed preference profile ID
        :param name: Managed preference profile name

        :returns: Deleted managed preference profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/managedpreferenceprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledeviceapplications
    """

    def get_mobile_device_applications(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile device applications in either JSON or XML

        :param data_type: json or xml

        :returns: All mobile device applications in JSON or XML
        """
        endpoint = "/JSSResource/mobiledeviceapplications"

        return self._get(endpoint, data_type)

    def get_mobile_device_application(
        self,
        id: Union[int, str] = None,
        name: str = None,
        bundleid: str = None,
        version: str = None,
        subsets: List[str] = None,
        data_type="json",
    ):
        """
        Returns data on one mobile device application by ID, name, or bundle
        ID. When using bundle ID as the identifier you can also optionally
        filter by version. When using ID or name as an identifier you can
        filter the data by subsets. Need to supply at least one identifier.

        :param id: Mobile device ID
        :param name: Mobile device name
        :param bundleid: Mobile device bundle ID
        :param version: Mobile device version
        :param subsets:
            Subset(s) of data from the mobile device application in a list
            of strings

            Options:
            - General
            - Scope
            - SelfService
            - VPPCodes
            - VPP
            - AppConfiguration

        :param data_type: json or xml

        :returns: Mobile device application information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "bundleid": bundleid,
        }
        identification = identification_type(identification_options)
        if identification == "bundleid" and subsets:
            raise ValueError(
                "Can not return a subset of data with bundleid as the identifier."
            )
        if identification != "bundleid" and version:
            raise ValueError(
                "Can not filter by version using ID or name as an identifier. "
                "Use bundleid as the identifier to filter by version."
            )
        if version:
            endpoint = (
                f"/JSSResource/mobiledeviceapplications/bundleid/{bundleid}"
                f"/version/{version}"
            )
        subset_options = [
            "General",
            "Scope",
            "SelfService",
            "VPPCodes",
            "VPP",
            "AppConfiguration",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/mobiledeviceapplications/{identification}"
                f"/{identification_options[identification]}"
                f"/subset/{'&'.join(subsets)}"
            )
        if not version and not subsets:
            endpoint = (
                f"/JSSResource/mobiledeviceapplications/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_mobile_device_application(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a mobile device application with XML data.

        :param data:
            XML data to create mobile device application with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledeviceapplicationbyid>`__
        :param id: Mobile device ID, set to 0 for next available ID

        :returns: New mobile device application information in XML
        """
        endpoint = f"/JSSResource/mobiledeviceapplications/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_mobile_device_application(
        self,
        data: str,
        id: Union[int, str] = None,
        name: str = None,
        bundleid: str = None,
        version: str = None,
    ) -> str:
        """
        Updates an existing mobile device application by ID, name, or bundleid.
        Bundleid can additionaly be defined by version. Need to supply at
        least one identifier.

        :param data:
            XML data to update mobile device application with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemobiledeviceapplicationbyid>`__
        :param id: Mobile device ID
        :param name: Mobile device name
        :param bundleid: Mobile device bundle ID
        :param version: Mobile device version

        :returns: Updated mobile device application information in XML
        """
        identification_options = {"id": id, "name": name, "bundleid": bundleid}
        identification = identification_type(identification_options)
        if identification != "bundleid" and version:
            raise ValueError(
                "Can not filter by version using ID or name as an identifier. "
                "Use bundleid as the identifier to filter by version."
            )
        if identification == "bundleid" and version:
            endpoint = (
                f"/JSSResource/mobiledeviceapplications/{identification}"
                f"/{identification_options[identification]}/version/{version}"
            )
        else:
            endpoint = (
                f"/JSSResource/mobiledeviceapplications/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._put(endpoint, data, data_type="xml")

    def delete_mobile_device_application(
        self,
        id: Union[int, str] = None,
        name: str = None,
        bundleid: str = None,
        version: str = None,
    ) -> str:
        """
        Deletes an mobile device application by ID, name, or bundleid.
        Bundleid can additionaly be defined by version. Need to supply at
        least one identifier.

        :param id: Mobile device ID
        :param name: Mobile device name
        :param bundleid: Mobile device bundle ID
        :param version: Mobile device version

        :returns: Deleted mobile device application information in XML
        """
        identification_options = {"id": id, "name": name, "bundleid": bundleid}
        identification = identification_type(identification_options)
        if identification != "bundleid" and version:
            raise ValueError(
                "Can not filter by version using ID or name as an identifier. "
                "Use bundleid as the identifier to filter by version."
            )
        if identification == "bundleid" and version:
            endpoint = (
                f"/JSSResource/mobiledeviceapplications/{identification}"
                f"/{identification_options[identification]}/version/{version}"
            )
        else:
            endpoint = (
                f"/JSSResource/mobiledeviceapplications/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledevicecommands
    """

    # command option is omitted since it is the same as name
    def get_mobile_device_commands(
        self, name: str = None, data_type="json"
    ) -> Union[dict, str]:
        """
        Returns all mobile device commands in JSON or XML. Can optionally
        filter by name as well.

        :param name: Mobile device command name e.g. UpdateInventory
        :param data_type: json or xml

        :returns: All mobile device commands in JSON or XML
        """
        if name:
            endpoint = f"/JSSResource/mobiledevicecommands/name/{name}"
        else:
            endpoint = "/JSSResource/mobiledevicecommands"

        return self._get(endpoint, data_type)

    def get_mobile_device_command(
        self, uuid: str, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on one mobile device command by UUID in JSON or XML

        :param uuid: Mobile device command UUID
        :param data_type: json or xml

        :returns: Mobile device command information in JSON or XML
        """
        endpoint = f"/JSSResource/mobiledevicecommands/uuid/{uuid}"

        return self._get(endpoint, data_type)

    def create_mobile_device_command(
        self,
        command: str = None,
        ids: List[Union[int, str]] = None,
        device_name: str = None,
        lock_message: str = None,
        install_action: Union[int, str] = None,
        product_version: str = None,
        data: str = None,
    ):
        """
        Creates a mobile device command with either XML data or parameters

        :param command:
            Mobile device command to send to device

            Options and requirements:
            - BlankPush
            - ClearPasscode
            - ClearRestrictionsPassword
            - DeviceLocation  Supervised and in lost mode
            - DeviceLock
            - DeviceName
            - DisableLostMode
            - EnableLostMode  Supervised device
            - EraseDevice
            - PasscodeLockGracePeriod  Shared iPad
            - PlayLostMostSound  Supervised and in lost mode
            - RestartDevice  Supervised device
            - ScheduleOSUpdate
            - Settings
            - SettingsDisableAppAnalytics
            - SettingsDisableBluetooth  iOS 11.3+ and Supervised
            - SettingsEnablePersonalHotspot
            - SettingsDisablePersonalHotspot
            - SettingsDisableDataRoaming
            - SettingsDisableDiagnosticSubmission
            - SettingsEnableAppAnalytics
            - SettingsEnableBluetooth  iOS 11.3+ and Supervised
            - SettingsEnableDataRoaming
            - SettingsEnableDiagnosticSubmission
            - SettingsEnableVoiceRoaming
            - ShutDownDevice  Supervised device
            - UnmanageDevice
            - UpdateInventory

        :param ids: List of mobile device IDs
        :param device_name:
            Device name to set for the DeviceName command
        :param lock_message:
            Lock message for the DeviceLock command
        :param install_action:
            Specify the behavior of the install.

            Possible integer values are:
            1. (Download the update for users to install)
            2. (Download and install the update, and restart devices after
            installation)

        :param product_version:
            Specify the OS version of the update. Updating to a specific iOS
            version requires devices with iOS 11.3 or later. Updating to a
            specific tvOS version requires devices with tvOS 12.2 or later.
            install_action required by the ScheduleOSUpdate command if
            product_version is specified.
        :param data:
            XML data to create a mobile device command with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledevicecommand>`__

        :returns: New mobile device command information in XML

        :raises InvalidParameterOptions:
            Raised if a parameter is set to an unrecognized value

        """
        params = {"command": command, "ids": ids}
        param_type = param_or_data(params, data)
        if param_type == "data":
            endpoint = "/JSSResource/mobiledevicecommands/command"
        if param_type == "params":
            enforce_params(params)
            if command in ["EnableLostMode", "EraseDevice", "PasscodeLockGracePeriod"]:
                raise InvalidParameterOptions(
                    f"{command} requires additonal parameters that need to be passed. "
                    "Please use the XML data option to use this command instead."
                )
            command_options = [
                "BlankPush",
                "ClearPasscode",
                "ClearRestrictionsPassword",
                "DeviceLocation",
                "DeviceLock",
                "DeviceName",
                "DisableLostMode",
                "PlayLostModeSound",
                "RestartDevice",
                "ScheduleOSUpdate",
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
            valid_param_options(command, command_options)
            ids = ",".join([str(id) for id in ids])
            if command == "DeviceName":
                enforce_params({"command": command, "device_name": device_name})
                endpoint = (
                    f"/JSSResource/mobiledevicecommands/command/{command}"
                    f"/{device_name}/id/{ids}"
                )
            elif command == "DeviceLock":
                enforce_params({"command": command, "lock_message": lock_message})
                endpoint = (
                    f"/JSSResource/mobiledevicecommands/command/{command}"
                    f"/{lock_message}/id/{ids}"
                )
            elif command == "ScheduleOSUpdate":
                enforce_params({"command": command, "install_action": install_action})
                if str(install_action) not in ["1", "2"]:
                    raise InvalidParameterOptions(
                        "install_action must be set to 1 or 2, view docstring "
                        "for more info on these options."
                    )
                if product_version:
                    endpoint = (
                        f"/JSSResource/mobiledevicecommands/command/{command}"
                        f"/{install_action}/{product_version}/id/{ids}"
                    )
                else:
                    endpoint = (
                        f"/JSSResource/mobiledevicecommands/command/{command}"
                        f"/{install_action}/id/{ids}"
                    )
            else:
                endpoint = (
                    f"/JSSResource/mobiledevicecommands/command/{command}/id/{ids}"
                )

        return self._post(endpoint, data, data_type="xml")

    """
    /mobiledeviceconfigurationprofiles
    """

    def get_mobile_device_configuration_profiles(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile device configuration profiles in either JSON or XML.

        :param data_type: json or xml

        :returns: All mobile device configuration profiles in JSON or XML
        """
        endpoint = "/JSSResource/mobiledeviceconfigurationprofiles"

        return self._get(endpoint, data_type)

    def get_mobile_device_configuration_profile(
        self,
        id: Union[int, str] = None,
        name: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific mobile device configuration profile by
        either ID or name.

        :param id: Mobile device configuration profile ID
        :param name: Mobile device configuration profile name
        :param subsets:
            Subset(s) of data from the mobile device configuration profile in
            a list of strings

            Options:
            - General
            - Scope
            - SelfService

        :param data_type: json or xml

        :returns:
            Mobile device configuration profile information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        subset_options = [
            "General",
            "Scope",
            "SelfService",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/mobiledeviceconfigurationprofiles/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/mobiledeviceconfigurationprofiles/{identification}/"
                f"{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_mobile_device_configuration_profile(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a mobile device configuration profile with the given XML data.
        Use ID 0 to use the next available ID. Payload of XML must be encoded
        to differentiate between the uploaded XML and the XML of the request
        body.

        :param data:
            XML data to create the mobile device configuration profile with.
            For syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledeviceconfigurationprofilebyid>`__
        :param id:
            ID of the new mobile device configuration profile, use 0 for next
            available ID

        :returns: New mobile device configuration profile information in XML
        """
        endpoint = f"/JSSResource/mobiledeviceconfigurationprofiles/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_mobile_device_configuration_profile(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a mobile device configuration profile with the given XML data.
        Need to supply at least one identifier. Payload of XML data must be
        encoded to differentiate between the uploaded XML and the XML of the
        request body.

        :param data:
            XML data to update the mobile device configuration profile with.
            For syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemobiledeviceconfigurationprofilebyid>`__
        :param id: Mobile device configuration profile ID
        :param name: Mobile device configuration profile name

        :returns:
            Updated mobile device configuration profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceconfigurationprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_mobile_device_configuration_profile(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a mobile device configuration profile by either ID or name.
        Need to supply at least one identifier.

        :param id: Mobile device configuration profile ID
        :param name: Mobile device configuration profile name

        :returns:
            Deleted mobile device configuration profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceconfigurationprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledeviceenrollmentprofiles
    """

    def get_mobile_device_enrollment_profiles(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile device enrollment profiles in either JSON or XML.

        :param data_type: json or xml

        :returns: All mobile device enrollment profiles in JSON or XML
        """
        endpoint = "/JSSResource/mobiledeviceenrollmentprofiles"

        return self._get(endpoint, data_type)

    def get_mobile_device_enrollment_profile(
        self,
        id: Union[int, str] = None,
        name: str = None,
        invitation: Union[int, str] = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific mobile device enrollment profile by either
        ID or name.

        :param id: Mobile device enrollment profile ID
        :param name: Mobile device enrollment profile name
        :param invitation: Mobile device enrollment profile invitation
        :param subsets:
            Subset(s) of data from the mobile device enrollment profile in a
            list of strings

            Options:
            - General
            - Location
            - Purchasing
            - Attachments

        :param data_type: json or xml

        :returns: Mobile device enrollment profile information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        subset_options = [
            "General",
            "Location",
            "Purchasing",
            "Attachments",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/mobiledeviceenrollmentprofiles/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/mobiledeviceenrollmentprofiles/{identification}/"
                f"{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_mobile_device_enrollment_profile(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a mobile device enrollment profile with the given XML data.
        Use ID 0 to use the next available ID.

        :param data:
            XML data to create the mobile device enrollment profile with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledeviceenrollmentprofilesbyid>`__
        :param id:
            ID of the new mobile device enrollment profile, use 0 for next
            available ID

        :returns: New mobile device enrollment profile information in XML
        """
        endpoint = f"/JSSResource/mobiledeviceenrollmentprofiles/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_mobile_device_enrollment_profile(
        self,
        data: str,
        id: Union[int, str] = None,
        name: str = None,
        invitation: Union[int, str] = None,
    ) -> str:
        """
        Updates a mobile device enrollment profile with the given XML data.
        Need to supply at least one identifier.

        :param data:
            XML data to update the mobile device enrollment profile with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemobiledeviceenrollmentprofilebyid>`__
        :param id: Mobile device enrollment profile ID
        :param name: Mobile device enrollment profile name
        :param invitation: Mobile device enrollment profile invitation

        :returns: Updated mobile device enrollment profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceenrollmentprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_mobile_device_enrollment_profile(
        self,
        id: Union[int, str] = None,
        name: str = None,
        invitation: Union[int, str] = None,
    ) -> str:
        """
        Deletes a mobile device enrollment profile by either ID or name.
        Need to supply at least one identifier.

        :param id: Mobile device enrollment profile ID
        :param name: Mobile device enrollment profile name
        :param invitation: Mobile device enrollment profile invitation

        :returns: Deleted mobile device enrollment profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceenrollmentprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledeviceextensionattributes
    """

    def get_mobile_device_extension_attributes(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile device extension attributes in either JSON or XML.

        :param data_type: json or xml

        :returns: All mobile device extension attributes in JSON or XML
        """
        endpoint = "/JSSResource/mobiledeviceextensionattributes"

        return self._get(endpoint, data_type)

    def get_mobile_device_extension_attribute(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific mobile device extension attribute by either
        ID or name in JSON or XML.

        :param id: Mobile device extension attribute ID
        :param name: Mobile device extension attribute name
        :param data_type: json or xml

        :returns: Mobile device extension attribute information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_mobile_device_extension_attribute(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a mobile device extension attribute with the given XML data.
        Use ID 0 to use the next available ID.

        :param data:
            XML data to create the mobile device extension attribute with. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledeviceextensionattributebyid>`__
        :param id:
            ID of the new mobile device extension attribute, use 0 for next
            available ID

        :returns: New mobile device extension attribute information in XML
        """
        endpoint = f"/JSSResource/mobiledeviceextensionattributes/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_mobile_device_extension_attribute(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a mobile device extension attribute with the given XML data.
        Need to supply at least one identifier.

        :param data:
            XML data to update the mobile device extension attribute with.
            For syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemobiledeviceextensionattributebyid>`__
        :param id: Mobile device extension attribute ID
        :param name: Mobile device extension attribute name

        :returns: Updated mobile device extension attribute information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_mobile_device_extension_attribute(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a mobile device extension attribute by either ID or name. Need
        to supply at least one identifier.

        :param id: Mobile device extension attribute ID
        :param name: Mobile device extension attribute name

        :returns: Deleted mobile device extension attribute information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledevicegroups
    """

    def get_mobile_device_groups(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all mobile device groups in either JSON or XML.

        :param data_type: json or xml

        :returns: All mobile device groups in JSON or XML
        """
        endpoint = "/JSSResource/mobiledevicegroups"

        return self._get(endpoint, data_type)

    def get_mobile_device_group(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific mobile device group by either ID or name in
        JSON or XML.

        :param id: Mobile device group ID
        :param name: Mobile device group name
        :param data_type: json or xml

        :returns: Mobile device group information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledevicegroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_mobile_device_group(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a mobile device group with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the mobile device group with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledevicegroupbyid>`__
        :param id:
            ID of the new mobile device group, use 0 for next
            available ID

        :returns: New mobile device group information in XML
        """
        endpoint = f"/JSSResource/mobiledevicegroups/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_mobile_device_group(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a mobile device group with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the mobile device group with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemobiledevicegroupbyid>`__
        :param id: Mobile device group ID
        :param name: Mobile device group name

        :returns: Updated mobile device group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledevicegroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_mobile_device_group(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a mobile device group by either ID or name. Need to supply
        at least one identifier.

        :param id: Mobile device group ID
        :param name: Mobile device group name

        :returns: Deleted mobile device group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledevicegroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledevicehistory
    """

    def get_mobile_device_history(
        self,
        id: Union[int, str] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns mobile device history data with the given identifier and
        optional subsets. Need to supply at least one identifier.

        :param id: Mobile device ID
        :param name: Mobile device name
        :param udid: Mobile device UDID
        :param serialnumber: Mobile device serial number
        :param macaddress: Mobile device MAC address,
        :param subsets:
            Subset(s) of data from the mobile device history in a list
            of strings

            Options:
            - General
            - ManagementCommands
            - UserLocation
            - Audits
            - Applications
            - Ebooks

        :param data_type: json or xml

        :returns: Mobile device history information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        subset_options = [
            "General",
            "ManagementCommands",
            "UserLocation",
            "Audits",
            "Applications",
            "Ebooks",
        ]
        identification = identification_type(identification_options)
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/mobiledevicehistory/{identification}"
                f"/{identification_options[identification]}"
                f"/subset/{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/mobiledevicehistory/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    """
    /mobiledeviceinvitations
    """

    def get_mobile_device_invitations(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile device invitation data in either JSON or XML.

        :param data_type: json or xml

        :returns: All mobile device invitations in JSON or XML
        """
        endpoint = "/JSSResource/mobiledeviceinvitations"

        return self._get(endpoint, data_type)

    def get_mobile_device_invitation(
        self,
        id: Union[int, str] = None,
        invitation: Union[int, str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns information on a single mobile device invitation defined by
        either ID or invitation. Need to supply at least one identifier.

        :param id: Mobile device invitation ID
        :param invitation:
            Mobile device invitation invitation identifier (name)
            Typically a long int
        :param data_type: json or xml

        :returns: Mobile device invitation information in JSON or XML
        """
        identification_options = {
            "id": id,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceinvitations/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_mobile_device_invitation(
        self, data: str, id: Union[int, str] = None, invitation: Union[int, str] = None
    ) -> str:
        """
        Creates a mobile device invitation defined by the XML data and either
        ID or invitation.

        :param data: XML data
        :param id:
            Mobile device invitation ID, use 0 for next available. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledeviceinvitationsbyid>`__
        :param invitation:
            Mobile device invitation invitation identifier, use 0 for next
            available

        :returns: New mobile device invitation information in XML
        """
        identification_options = {
            "id": id,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceinvitations/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._post(endpoint, data, data_type="xml")

    def delete_mobile_device_invitation(
        self, id: Union[int, str] = None, invitation: Union[int, str] = None
    ) -> str:
        """
        Deletes a mobile device invitation by either ID or invitation
        identifiers. Need to supply at least one identifier.

        :param id: Mobile device invitation ID
        :param invitation:
            Mobile device invitation invitation identifier (name)
            Typically a long int

        :returns: Deleted mobile device invitation information in XML
        """
        identification_options = {
            "id": id,
            "invitation": invitation,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceinvitations/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledeviceprovisioningprofiles
    """

    def get_mobile_device_provisioning_profiles(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile device provisioning profiles in JSON or XML

        :param data_type: json or xml

        :returns: All mobile device provisioning profiles in JSON or XML
        """
        endpoint = "/JSSResource/mobiledeviceprovisioningprofiles"

        return self._get(endpoint, data_type)

    def get_mobile_device_provisioning_profile(
        self,
        id: Union[int, str] = None,
        name: str = None,
        uuid: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on one mobile device provisioning profile in JSON or XML
        by ID, name, or UUID. Need to supply at least one identifier.

        :param id: Mobile device provisioning profile ID
        :param name: Mobile device provisioning profile name
        :param uuid: Mobile device provisioning profile UUID
        :param data_type: json or xml

        :returns: Mobile device provisioning profile information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "uuid": uuid,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceprovisioningprofiles/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_mobile_device_provisioning_profile(
        self, data: str, id: Union[int, str] = None, name: str = None, uuid: str = None
    ) -> str:
        """
        Creates a mobile device provisioning profile with XML data by ID,
        name, or UUID. Need to supply at least one identifier.

        :param data:
            XML data configuration for mobile device provisioning profile. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledeviceprovisioningprofilesbyid>`__
        :param id:
            Mobile device provisioning profile ID, set to 0 for next available
        :param name: Mobile device provisioning profile name
        :param uuid: Mobile device provisioning profile UUID

        :returns: New mobile deivce provisioning profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "uuid": uuid,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceprovisioningprofiles/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._post(endpoint, data, data_type="xml")

    def update_mobile_device_provisioning_profile(
        self, data: str, id: Union[int, str] = None, name: str = None, uuid: str = None
    ) -> str:
        """
        Updates a mobile device provisioning profile with XML data by ID,
        name, or UUID. Need to supply at least one identifier.

        :param data:
            XML data configuration for mobile device provisioning profile. For
            syntax information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemobiledeviceprovisioningprofilesbyid>`__
        :param id:
            Mobile device provisioning profile ID, set to 0 for next available
        :param name: Mobile device provisioning profile name
        :param uuid: Mobile device provisioning profile UUID

        :returns: Updated mobile device provisioning profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "uuid": uuid,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceprovisioningprofiles/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_mobile_device_provisioning_profile(
        self,
        id: Union[int, str] = None,
        name: str = None,
        uuid: str = None,
    ) -> Union[dict, str]:
        """
        Deletes a mobile device provisioning profile by ID, name, or UUID.
        Need to supply at least one identifier.

        :param id: Mobile device provisioning profile ID
        :param name: Mobile device provisioning profile name
        :param uuid: Mobile device provisioning profile UUID
        :param data_type: json or xml

        :returns: Deleted mobile device provisioning profile information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "uuid": uuid,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/mobiledeviceprovisioningprofiles/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /mobiledevices
    """

    def get_mobile_devices(
        self, match: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile devices from a JPS instance in either JSON or XML.
        You can pass the match param to get all mobile devices that match
        your search critera.

        :param match: String to search mobile devices
        :param data_type: json or xml

        :returns: All mobile devices in JSON or XML
        """

        if match:
            endpoint = f"/JSSResource/mobiledevices/match/{match}"
        else:
            endpoint = "/JSSResource/mobiledevices"

        return self._get(endpoint, data_type)

    def get_mobile_device(
        self,
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ):
        """
        Returns information on a mobile device with given identifier in either
        JSON or XML. You can specify the return of a subset of the data by
        defining subset as a list of the subsets that you want. Need to supply
        at least one identifier.

        :param id: Mobile device ID
        :param name: Mobile device name
        :param udid: Mobile device UDID
        :param serialnumber: Mobile device serial number
        :param macaddress: Mobile device MAC address
        :param subsets:
            Subset(s) of data from the mobile device in a list of strings

            Options:
            - General
            - Location
            - Purchasing
            - Applications
            - Security
            - Network
            - Certifications
            - ConfigurationProfiles
            - ProvisioningProfiles
            - MobileDeviceGroups
            - ExtensionAttributes

        :param data_type: json or xml

        :returns: Mobile device information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        subset_options = [
            "General",
            "Location",
            "Purchasing",
            "Applications",
            "Security",
            "Network",
            "Certificates",
            "ConfigurationProfiles",
            "ProvisioningProfiles",
            "MobileDeviceGroups",
            "ExtensionAttributes",
        ]
        identification = identification_type(identification_options)

        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/mobiledevices/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/mobiledevices/{identification}"
                f"/{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_mobile_device(self, data: str, id: Union[str, int] = 0) -> str:
        """
        Creates a mobile device with the given ID and information defined in
        XML data.

        :param data:
            XML data to create the mobile device. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createmobiledevicebyid>`__
        :param id: Mobile device ID, set to 0 for next available ID

        :returns: New mobile device information in XML
        """
        endpoint = f"/JSSResource/mobiledevices/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_mobile_device(
        self,
        data: str,
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
    ) -> str:
        """
        Updates information on a mobile device with given identifier. Need to
        supply at least one identifier.

        :param data:
            XML string to update the Mobile device with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatemobiledevicebyid>`__
        :param id: Mobile device ID
        :param name: Mobile device name
        :param udid: Mobile device UDID
        :param serialnumber: Mobile device serial number
        :param macaddress: Mobile device MAC address

        :returns: Updated mobile device information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        identification = identification_type(identification_options)

        endpoint = (
            f"/JSSResource/mobiledevices/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_mobile_device(
        self,
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
    ) -> str:
        """
        Deletes a mobile device with given identifier. Need to supply at least
        one identifier.

        :param id: Mobile device ID
        :param name: Mobile device name
        :param udid: Mobile device UDID
        :param serialnumber: Mobile device serial number
        :param macaddress: Mobile device MAC address

        :returns: Deleted mobile device information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        identification = identification_type(identification_options)

        endpoint = (
            f"/JSSResource/mobiledevices/{identification}"
            f"/{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /networksegments
    """

    def get_network_segments(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all network segments in either JSON or XML.

        :param data_type: json or xml

        :returns: All network segments in JSON or XML
        """
        endpoint = "/JSSResource/networksegments"

        return self._get(endpoint, data_type)

    def get_network_segment(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific network segment by either ID or name in
        JSON or XML.

        :param id: network segment ID
        :param name: network segment name
        :param data_type: json or xml

        :returns: Network segment information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/networksegments/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_network_segment(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a network segment with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the network segment with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createnetworksegmentbyid>`__
        :param id:
            ID of the new network segment, use 0 for next
            available ID

        :returns: New network segment information in XML
        """
        endpoint = f"/JSSResource/networksegments/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_network_segment(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a network segment with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the network segment with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatenetworksegmentbyid>`__
        :param id: network segment ID
        :param name: network segment name

        :returns: Updated network segment information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/networksegments/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_network_segment(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a network segment by either ID or name. Need to supply
        at least one identifier.

        :param id: network segment ID
        :param name: network segment name

        :returns: Deleted network segment information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/networksegments/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /osxconfigurationprofiles
    """

    def get_osx_configuration_profiles(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all OSX configuration profiles in either JSON or XML.

        :param data_type: json or xml

        :returns: All OSX configuratiion profiles in JSON or XML
        """
        endpoint = "/JSSResource/osxconfigurationprofiles"

        return self._get(endpoint, data_type)

    def get_osx_configuration_profile(
        self,
        id: Union[int, str] = None,
        name: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific OSX configuration profile by either ID or
        name.

        :param id: OSX configuration profile ID
        :param name: OSX configuration profile name
        :param subsets:
            Subset(s) of data from the OSX configuration profile in a list of
            strings

            Options:
            - General
            - Scope
            - SelfService

        :param data_type: json or xml

        :returns: OSX configuration profile information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        subset_options = [
            "General",
            "Scope",
            "SelfService",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/osxconfigurationprofiles/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/osxconfigurationprofiles/{identification}/"
                f"{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_osx_configuration_profile(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a OSX configuration profile with the given XML data.
        Use ID 0 to use the next available ID. Payload of XML must be encoded
        to differentiate between the uploaded XML and the XML of the request
        body

        :param data:
            XML data to create the OSX configuration profile with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createosxconfigurationprofilebyid>`__
        :param id:
            ID of the new OSX configuration profile, use 0 for next
            available ID

        :returns: New OSX configuration profile in XML
        """
        endpoint = f"/JSSResource/osxconfigurationprofiles/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_osx_configuration_profile(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a OSX configuration profile with the given XML data.
        Need to supply at least one identifier. Payload of XML data must be
        encoded to differentiate between the uploaded XML and the XML of the
        request body

        :param data:
            XML data to update the OSX configuration profile with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateosxconfigurationprofilebyid>`__
        :param id: OSX configuration profile ID
        :param name: OSX configuration profile name

        :returns: Updated OSX configuration profile in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/osxconfigurationprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_osx_configuration_profile(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a OSX configuration profile by either ID or name.
        Need to supply at least one identifier.

        :param id: OSX configuration profile ID
        :param name: OSX configuration profile name

        :returns: Deleted OSX configuration profile in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/osxconfigurationprofiles/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /packages
    """

    def get_packages(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all packages in either JSON or XML.

        :param data_type: json or xml

        :returns: All packages in JSON or XML
        """
        endpoint = "/JSSResource/packages"

        return self._get(endpoint, data_type)

    def get_package(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific package by either ID or name in
        JSON or XML.

        :param id: Package ID
        :param name: Package name
        :param data_type: json or xml

        :returns: Package information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/packages/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_package(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a package with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the package with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createpackagebyid>`__
        :param id:
            ID of the new package, use 0 for next
            available ID

        :returns: New package information in XML
        """
        endpoint = f"/JSSResource/packages/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_package(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a package with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the package with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatepackagebyid>`__
        :param id: Package ID
        :param name: Package name

        :returns: Updated package information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/packages/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_package(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a package by either ID or name. Need to supply
        at least one identifier.

        :param id: Package ID
        :param name: Package name

        :returns: Deleted package information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/packages/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /patchavailabletitles
    """

    def get_patch_available_titles(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all available patch titles from a source by ID in JSON or XML

        :param id: External or internal patch source ID
        :param data_type: json or xml

        :returns: All available patch titles in JSON or XML
        """
        endpoint = f"/JSSResource/patchavailabletitles/sourceid/{id}"

        return self._get(endpoint, data_type)

    """
    /patches
    """

    # Deprecated - use patchsoftwaretitles and patchreports

    """
    /patchexternalsources
    """

    def get_patch_external_sources(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all external patch sources in either JSON or XML.

        :param data_type: json or xml

        :returns: All external patch sources in JSON or XML
        """
        endpoint = "/JSSResource/patchexternalsources"

        return self._get(endpoint, data_type)

    def get_patch_external_source(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific external patch source by either ID or name
        in JSON or XML.

        :param id: External patch source ID
        :param name: External patch source name
        :param data_type: json or xml

        :returns: External patch source information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/patchexternalsources/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_patch_external_source(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Creates an external patch source with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the external patch source with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createpatchexternalsourcesbyid>`__
        :param id:
            ID of the new external patch source, use 0 for next
            available ID
        :param name: External patch source name

        :returns: New external patch source information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/patchexternalsources/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._post(endpoint, data, data_type="xml")

    def update_patch_external_source(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a external patch source with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the external patch source with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatepatchexternalsourcesbyid>`__
        :param id: External patch source ID
        :param name: External patch source name

        :returns: Updated external patch source information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/patchexternalsources/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_patch_external_source(self, id: Union[int, str]) -> str:
        """
        Deletes an external patch source by ID.

        :param id: External patch source ID

        :returns: Deleted external patch sourcen information in XML
        """
        endpoint = f"/JSSResource/patchexternalsources/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /patchinternalsources
    """

    def get_patch_internal_sources(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all internal patch sources in either JSON or XML.

        :param data_type: json or xml

        :returns: All internal patch sources in JSON or XML
        """
        endpoint = "/JSSResource/patchinternalsources"

        return self._get(endpoint, data_type)

    def get_patch_internal_source(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific internal patch source by either ID or name
        in JSON or XML.

        :param id: Internal patch source ID
        :param name: Internal patch source name
        :param data_type: json or xml

        :returns: Internal patch source information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/patchinternalsources/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    """
    /patchpolicies
    """

    def get_patch_policies(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all patch policies in JSON or XML

        :param data_type: json or xml

        :returns: All patch policies in JSON or XML
        """
        endpoint = "/JSSResource/patchpolicies"

        return self._get(endpoint, data_type)

    def get_patch_policy(
        self,
        id: Union[int, str] = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on one patch policy by ID or software title config ID
        in JSON or XML

        :param id: Software title config ID
        :param subsets:
            Subset(s) of data from the patch policy in a list of strings

            Options:
            - General
            - Scope
            - UserInteraction

        :param data_type: json or xml

        :returns: Patch policy information in JSON or XML
        """
        subset_options = [
            "General",
            "Scope",
            "UserInteraction",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/patchpolicies/softwaretitleconfig/id/{id}"
                f"/subset/{'&'.join(subsets)}"
            )
        else:
            endpoint = f"/JSSResource/patchpolicies/softwaretitleconfig/id/{id}"

        return self._get(endpoint, data_type)

    def create_patch_policy(self, data: str, id: Union[str, int] = 0) -> str:
        """
        Creates a patch policy by ID with XML data

        :param data:
            XML data to create patch policy with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createpatchpolicybysoftwaretitleconfigid>`__
        :param id: Patch policy ID, set to 0 for next available

        :returns: New patch policy information in XML
        """
        endpoint = f"/JSSResource/patchpolicies/softwaretitleconfig/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_patch_policy(self, data: str, id: Union[str, int] = 0) -> str:
        """
        Updates a patch policy by ID with XML data

        :param data:
            XML data to update patch policy with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatepatchpolicybyid>`__
        :param id: Patch policy ID, set to 0 for next available

        :returns: Updated patch policy information in XML
        """
        endpoint = f"/JSSResource/patchpolicies/softwaretitleconfig/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_patch_policy(self, id: Union[int, str]) -> str:
        """
        Deletes a patch policy by ID.

        :param id: Patch policy ID

        :returns: Deleted patch policy information in XML
        """
        endpoint = f"/JSSResource/patchpolicies/softwaretitleconfig/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /patchreports
    """

    def get_patch_report(
        self, id: Union[int, str], version: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data one a patch report filtered by ID and optionally version
        in JSON or XML

        :param id: Patch software title ID to filter by
        :param version: Version number to filter by
        :param data_type: json or xml

        :returns: Patch report information in JSON or XML
        """
        if version:
            endpoint = (
                f"/JSSResource/patchreports/patchsoftwaretitleid/{id}/version/{version}"
            )
        else:
            endpoint = f"/JSSResource/patchreports/patchsoftwaretitleid/{id}"

        return self._get(endpoint, data_type)

    """
    /patchsoftwaretitles
    """

    def get_patch_software_titles(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all patch software titles in JSON or XML

        :param data_type: json or xml

        :returns: All patch software titles in JSON or XML
        """
        endpoint = "/JSSResource/patchsoftwaretitles"

        return self._get(endpoint, data_type)

    def get_patch_software_title(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on one patch software title in JSON or XML

        :param id: Patch software title ID
        :param data_type: json or xml

        :returns: Patch software title information in JSON or XML
        """
        endpoint = f"/JSSResource/patchsoftwaretitles/id/{id}"

        return self._get(endpoint, data_type)

    def create_patch_software_title(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a patch software title by ID with XML data

        :param data:
            XML data to create the patch software title with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/patchsoftwaretitlesidbyidpost>`__
        :param id: Patch software title ID, set to 0 for next available ID

        :returns: New patch software title information in XML
        """
        endpoint = f"/JSSResource/patchsoftwaretitles/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_patch_software_title(self, data: str, id: Union[int, str]) -> str:
        """
        Updates a patch software title by ID with XML data

        :param data:
            XML data to udpate the patch software title with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/patchsoftwaretitlesidbyidput>`__
        :param id: Patch software title ID

        :returns: Updated patch software title information in XML
        """
        endpoint = f"/JSSResource/patchsoftwaretitles/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_patch_software_title(self, id: Union[int, str]) -> str:
        """
        Deletes a patch software title by ID

        :param id: Patch software title ID

        :returns: Deleted patch software title information in XML
        """
        endpoint = f"/JSSResource/patchsoftwaretitles/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /peripherals
    """

    """
    Peripherals were deprecated by Jamf so I've omitted the creation
    endpoint, you can still get, update, and delete so that you can change or
    delete them.
    """

    def get_peripherals(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all peripherals in JSON or XML

        :param data_type: json or xml

        :returns: All peripherals in JSON or XML
        """
        endpoint = "/JSSResource/peripherals"

        return self._get(endpoint, data_type)

    def get_peripheral(
        self,
        id: Union[int, str] = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on one Peripheral by ID in JSON or XML

        :param id: Peripheral ID
        :param subsets:
            Subset(s) of data from the peripheral in a list of strings

            Options:
            - General
            - Location
            - Purchasing
            - Attachments
        :param data_type: json or xml

        :returns: Peripheral information in JSON or XML
        """
        subset_options = [
            "General",
            "Location",
            "Purchasing",
            "Attachments",
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/peripherals/id/{id}" f"/subset/{'&'.join(subsets)}"
            )
        else:
            endpoint = f"/JSSResource/peripherals/id/{id}"

        return self._get(endpoint, data_type)

    def update_peripheral(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Updates a peripheral by ID with XML data

        :param data:
            XML data to update peripheral with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateperipheralbyid>`__
        :param id: Peripheral ID, set to 0 for next available

        :returns: Updated peripheral information in XML
        """
        endpoint = f"/JSSResource/peripherals/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_peripheral(self, id: Union[int, str]) -> str:
        """
        Deletes a peripheral by ID.

        :param id: Peripheral ID

        :returns: Deleted peripheral information in XML
        """
        endpoint = f"/JSSResource/peripherals/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /peripheraltypes
    """

    """
    Peripherals were deprecated by Jamf so I've omitted the creation
    endpoint, you can still get, update, and delete are still available
    so that you can change or delete them.
    """

    def get_peripheral_types(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all peripheral types in JSON or XML

        :param data_type: json or xml

        :returns: All peripheral types in JSON or XML
        """
        endpoint = "/JSSResource/peripheraltypes"

        return self._get(endpoint, data_type)

    def get_peripheral_type(
        self,
        id: Union[int, str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on one peripheral type by ID or peripheral type ID
        in JSON or XML

        :param id: Peripheral type ID
        :param data_type: json or xml

        :returns: Peripheral type information in JSON or XML
        """
        endpoint = f"/JSSResource/peripheraltypes/id/{id}"

        return self._get(endpoint, data_type)

    def update_peripheral_type(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Updates a peripheral type by ID with XML data

        :param data:
            XML data to update peripheral type with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateperipheraltypebyid>`__
        :param id: Peripheral type ID, set to 0 for next available

        :returns: Updated peripheral type information in XML
        """
        endpoint = f"/JSSResource/peripheraltypes/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_peripheral_type(self, id: Union[int, str]) -> str:
        """
        Deletes a peripheral type by ID.

        :param id: Peripheral type ID

        :returns: Deleted peripheral type information in XML
        """
        endpoint = f"/JSSResource/peripheraltypes/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /policies
    """

    def get_policies(
        self, category: str = None, createdby: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all policies in either JSON or XML.

        :param category:
            Category may be specified by id or name, or 'None' for policies
            with no category
        :param createdby:
            The value 'casper' refers to Casper Remote. The value 'jss'
            refers to policies created in the GUI or via the API.
        :param data_type: json or xml

        :returns: All policies in JSON or XML
        """
        if createdby and createdby not in ["jss", "casper"]:
            raise ValueError("createdby only supports the values jss and casper")
        if category:
            endpoint = f"/JSSResource/policies/category/{category}"
        elif createdby:
            endpoint = f"/JSSResource/policies/createdBy/{createdby}"
        else:
            endpoint = "/JSSResource/policies"

        return self._get(endpoint, data_type)

    def get_policy(
        self,
        id: Union[int, str] = None,
        name: str = None,
        subsets: List[str] = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific policy by either ID or name.

        :param id: Policy ID
        :param name: Policy name
        :param subsets:
            Subset(s) of data from the policy in a list of strings

            Options:
            - General
            - Scope
            - SelfService
            - PackageConfiguration
            - Scripts
            - Printers
            - DockItems
            - AccountMaintenance
            - Reboot
            - Maintenance
            - FilesProcesses
            - UserInteraction
            - DiskEncryption

        :param data_type: json or xml

        :returns: Policy information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        subset_options = [
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
        ]
        if valid_subsets(subsets, subset_options):
            endpoint = (
                f"/JSSResource/policies/{identification}"
                f"/{identification_options[identification]}/subset/"
                f"{'&'.join(subsets)}"
            )
        else:
            endpoint = (
                f"/JSSResource/policies/{identification}/"
                f"{identification_options[identification]}"
            )

        return self._get(endpoint, data_type)

    def create_policy(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a policy with the given XML data. Use ID 0 to use the next
        available ID.

        :param data:
            XML data to create the policy with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createpolicybyid>`__
        :param id:
            ID of the new policy, use 0 for next
            available ID

        :returns: New policy information in XML
        """
        endpoint = f"/JSSResource/policies/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_policy(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a policy with the given XML data. Need to supply at least one
        identifier.

        :param data:
            XML data to update the policy with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatepolicybyid>`__
        :param id: Policy ID
        :param name: Policy name

        :returns: Updated policy information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/policies/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_policy(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a policy by either ID or name. Need to supply at least one
        identifier.

        :param id: Policy ID
        :param name: Policy name

        :returns: Deleted policy information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/policies/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /printers
    """

    def get_printers(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all printers in either JSON or XML.

        :param data_type: json or xml

        :returns: All printers in JSON or XML
        """
        endpoint = "/JSSResource/printers"

        return self._get(endpoint, data_type)

    def get_printer(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific printer by either ID or name in JSON or
        XML.

        :param id: Printer ID
        :param name: Printer name
        :param data_type: json or xml

        :returns: Printer information information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/printers/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_printer(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a printer with the given XML data. Use ID 0 to use the next
        available ID.

        :param data:
            XML data to create the printer with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createprinterbyid>`__
        :param id:
            ID of the new printer, use 0 for next
            available ID

        :returns: New printer information in XML
        """
        endpoint = f"/JSSResource/printers/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_printer(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a printer with the given XML data. Need to supply at least
        one identifier.

        :param data:
            XML data to update the printer with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateprinterbyid>`__
        :param id: Printer ID
        :param name: Printer name

        :returns: Updated printer information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/printers/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_printer(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a printer by either ID or name. Need to supply at least one
        identifier.

        :param id: Printer ID
        :param name: Printer name

        :returns: Deleted printer information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/printers/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /removablemacaddresses
    """

    def get_removable_mac_addresses(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all removable MAC addresses in either JSON or XML.

        :param data_type: json or xml

        :returns: All removable MAC addresses in JSON or XML
        """
        endpoint = "/JSSResource/removablemacaddresses"

        return self._get(endpoint, data_type)

    def get_removable_mac_address(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific removable MAC address by either ID or name
        in JSON or XML.

        :param id: removable MAC address ID
        :param name: removable MAC address name
        :param data_type: json or xml

        :returns: Removable MAC address information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/removablemacaddresses/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_removable_mac_address(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a removable MAC address with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the removable MAC address with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createremovablemacaddressbyid>`__
        :param id:
            ID of the new removable MAC address, use 0 for next
            available ID

        :returns: New removable MAC address information in XML
        """
        endpoint = f"/JSSResource/removablemacaddresses/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_removable_mac_address(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a removable MAC address with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the removable MAC address with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateremovablemacaddressbyid>`__
        :param id: removable MAC address ID
        :param name: removable MAC address name

        :returns: Updated removable MAC address information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/removablemacaddresses/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_removable_mac_address(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a removable MAC address by either ID or name. Need to supply
        at least one identifier.

        :param id: removable MAC address ID
        :param name: removable MAC address name

        :returns: Deleted removable MAC address in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/removablemacaddresses/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /restrictedsoftware
    """

    def get_restricted_software_all(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all restricted software in either JSON or XML.

        :param data_type: json or xml

        :returns: All restricted software in JSON or XML
        """
        endpoint = "/JSSResource/restrictedsoftware"

        return self._get(endpoint, data_type)

    def get_restricted_software(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific restricted software by either ID or name in
        JSON or XML.

        :param id: Restricted software ID
        :param name: Restricted software name
        :param data_type: json or xml

        :returns: Restricted software information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/restrictedsoftware/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_restricted_software(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a restricted software with the given XML data. Use ID 0 to
        use the next available ID.

        :param data:
            XML data to create the restricted software with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createrestrictedsoftwarebyid>`__
        :param id:
            ID of the new restricted software, use 0 for next
            available ID

        :returns: New restricted software information in XML
        """
        endpoint = f"/JSSResource/restrictedsoftware/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_restricted_software(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a restricted software with the given XML data. Need to supply
        at least one identifier.

        :param data:
            XML data to update the restricted software with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updaterestrictedsoftwarebyid>`__
        :param id: Restricted software ID
        :param name: Restricted software name

        :returns: Updated restricted software information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/restrictedsoftware/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_restricted_software(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a restricted software by either ID or name. Need to supply
        at least one identifier.

        :param id: Restricted software ID
        :param name: Restricted software name

        :returns: Deleted restricted software information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/restrictedsoftware/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /savedsearches
    """

    """
    Deprecated - use advancedcomputersearches, advancedmobiledevicesearches,
    and advancedusersearches instead.
    """

    """
    /scripts
    """

    def get_scripts(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all scripts in either JSON or XML.

        :param data_type: json or xml

        :returns: All scripts in JSON or XML
        """
        endpoint = "/JSSResource/scripts"

        return self._get(endpoint, data_type)

    def get_script(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific script by either ID or name in JSON or XML.

        :param id: Script ID
        :param name: Script name
        :param data_type: json or xml

        :returns: Script information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/scripts/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_script(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a script with the given XML data. Use ID 0 to use the next
        available ID.

        :param data:
            XML data to create the script with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createscriptbyid>`__
        :param id:
            ID of the new script, use 0 for next
            available ID

        :returns: New script information in XML
        """
        endpoint = f"/JSSResource/scripts/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_script(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a script with the given XML data. Need to supply at least one
        identifier.

        :param data:
            XML data to update the script with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatescriptbyid>`__
        :param id: Script ID
        :param name: Script name

        :returns: Updated script information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/scripts/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_script(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a script by either ID or name. Need to supply at least one
        identifier.

        :param id: Script ID
        :param name: Script name

        :returns: Deleted script information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/scripts/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /sites
    """

    def get_sites(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all sites in either JSON or XML.

        :param data_type: json or xml

        :returns: All sites in JSON or XML
        """
        endpoint = "/JSSResource/sites"

        return self._get(endpoint, data_type)

    def get_site(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific site by either ID or name in JSON or XML.

        :param id: Site ID
        :param name: Site name
        :param data_type: json or xml

        :returns: Site information information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/sites/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_site(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a site with the given XML data. Use ID 0 to use the next
        available ID.

        :param data:
            XML data to create the site with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createsitebyid>`__
        :param id:
            ID of the new site, use 0 for next
            available ID

        :returns: New site information in XML
        """
        endpoint = f"/JSSResource/sites/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_site(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a site with the given XML data. Need to supply at least one
        identifier.

        :param data:
            XML data to update the site with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatesitebyid>`__
        :param id: Site ID
        :param name: Site name

        :returns: Updated site information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/sites/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_site(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a site by either ID or name. Need to supply at least one
        identifier.

        :param id: Site ID
        :param name: Site name

        :returns: Deleted site information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/sites/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /smtpserver
    """

    def get_smtp_server(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns information on the SMTP server for the JPS server

        :param data_type: json or xml

        :returns: SMTP server information in JSON or XML
        """
        endpoint = "/JSSResource/smtpserver"

        return self._get(endpoint, data_type)

    def update_smtp_server(self, data: str) -> str:
        """
        Updates the SMTP server info on the JPS server with XML data.

        :param data:
            XML data to update the smtp server with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatesmtpserver>`__

        :returns: Updated SMTP server information in XML
        """
        endpoint = "/JSSResource/smtpserver"

        return self._put(endpoint, data, data_type="xml")

    """
    /softwareupdateservers
    """

    def get_software_update_servers(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all software update servers in either JSON or XML.

        :param data_type: json or xml

        :returns: All software update server in JSON or XML
        """
        endpoint = "/JSSResource/softwareupdateservers"

        return self._get(endpoint, data_type)

    def get_software_update_server(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific software update server by either ID or name
        in JSON or XML.

        :param id: Software update server ID
        :param name: Software update server name
        :param data_type: json or xml

        :returns: Software update server information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/softwareupdateservers/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_software_update_server(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a software update server with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the software update server with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createsoftwareupdateserverbyid>`__
        :param id:
            ID of the new software update server, use 0 for next
            available ID

        :returns: New software update server information in XML
        """
        endpoint = f"/JSSResource/softwareupdateservers/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_software_update_server(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a software update server with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the software update server with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatesoftwareupdateserverbyid>`__
        :param id: Software update server ID
        :param name: Software update server name

        :returns: Updated software update server information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/softwareupdateservers/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_software_update_server(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a software update server by either ID or name. Need to supply
        at least one identifier.

        :param id: Software update server ID
        :param name: Software update server name

        :returns: Deleted software update server information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/softwareupdateservers/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /userextensionattributes
    """

    def get_user_extension_attributes(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all user extension attributes in either JSON or XML.

        :param data_type: json or xml

        :returns: All user extension attributes in JSON or XML
        """
        endpoint = "/JSSResource/userextensionattributes"

        return self._get(endpoint, data_type)

    def get_user_extension_attribute(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific user extension attribute by either ID or
        name in JSON or XML.

        :param id: User extension attribute ID
        :param name: User extension attribute name
        :param data_type: json or xml

        :returns: User extension attribute information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/userextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_user_extension_attribute(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a user extension attribute with the given XML data. Use ID 0
        to use the next available ID.

        :param data:
            XML data to create the user extension attribute with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createuserextensionattributebyid>`__
        :param id:
            ID of the new user extension attribute, use 0 for next
            available ID

        :returns: New user extension attribute information in XML
        """
        endpoint = f"/JSSResource/userextensionattributes/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_user_extension_attribute(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a user extension attribute with the given XML data. Need to
        supply at least one identifier.

        :param data:
            XML data to update the user extension attribute with. For syntax
            information view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateuserextensionattributebyid>`__
        :param id: User extension attribute ID
        :param name: User extension attribute name

        :returns: Updated user extension attribute information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/userextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_user_extension_attribute(
        self, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Deletes a user extension attribute by either ID or name. Need to supply
        at least one identifier.

        :param id: User extension attribute ID
        :param name: User extension attribute name

        :returns: Deleted user extension attribute information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/userextensionattributes/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /usergroups
    """

    def get_user_groups(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all user groups in either JSON or XML.

        :param data_type: json or xml

        :returns: All user groups in JSON or XML
        """
        endpoint = "/JSSResource/usergroups"

        return self._get(endpoint, data_type)

    def get_user_group(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific user group by either ID or name in JSON
        or XML.

        :param id: User group ID
        :param name: User group name
        :param data_type: json or xml

        :returns: User group information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/usergroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_user_group(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a user group with the given XML data. Use ID 0 to use the next
        available ID.

        :param data:
            XML data to create the user group with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createusergroupsbyid>`__
        :param id:
            ID of the new user group, use 0 for next
            available ID

        :returns: New user group information in XML
        """
        endpoint = f"/JSSResource/usergroups/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_user_group(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a user group with the given XML data. Need to supply at least
        one identifier.

        :param data:
            XML data to update the user group with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateusergroupsbyid>`__
        :param id: User group ID
        :param name: User group name

        :returns: Update user group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/usergroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_user_group(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a user group by either ID or name. Need to supply at least one
        identifier.

        :param id: User group ID
        :param name: User group name

        :returns: Deleted user group information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/usergroups/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /users
    """

    def get_users(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all users in either JSON or XML.

        :param data_type: json or xml

        :returns: All users in JSON or XML
        """
        endpoint = "/JSSResource/users"

        return self._get(endpoint, data_type)

    def get_user(
        self,
        id: Union[int, str] = None,
        name: str = None,
        email: str = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific user by either ID or name in JSON or XML.

        :param id: User ID
        :param name: User name
        :param email: User email
        :param data_type: json or xml

        :returns: User information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "email": email,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/users/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_user(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a user with the given XML data. Use ID 0 to use the next
        available ID.

        :param data:
            XML data to create the user with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createuserbyid>`__
        :param id:
            ID of the new user, use 0 for next
            available ID

        :returns: New user information in XML
        """
        endpoint = f"/JSSResource/users/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_user(
        self, data: str, id: Union[int, str] = None, name: str = None, email: str = None
    ) -> str:
        """
        Updates a user with the given XML data. Need to supply at least
        one identifier.

        :param data:
            XML data to update the user with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateuserbyid>`__
        :param id: User ID
        :param name: User name
        :param email: User email

        :returns: Updated user information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "email": email,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/users/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_user(
        self, id: Union[int, str] = None, name: str = None, email: str = None
    ) -> str:
        """
        Deletes a user by either ID or name. Need to supply at least one
        identifier.

        :param id: User ID
        :param name: User name
        :param email: User email

        :returns: Deleted user information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
            "email": email,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/users/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")

    """
    /vppaccounts
    """

    def get_vpp_accounts(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all VPP accounts in JSON or XML

        :param data_type: json or xml

        :returns: All VPP accounts in JSON or XML
        """
        endpoint = "/JSSResource/vppaccounts"

        return self._get(endpoint, data_type)

    def get_vpp_account(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on one VPP account in JSON or XML

        :param id: VPP account ID
        :param data_type: json or xml

        :returns: VPP account information in JSON or XML
        """
        endpoint = f"/JSSResource/vppaccounts/id/{id}"

        return self._get(endpoint, data_type)

    def create_vpp_account(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a VPP account by ID with XML data

        :param data:
            XML data to create the VPP account with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createvppadminaccountbyid>`__
        :param id: VPP account ID, set to 0 for next available ID

        :returns: New VPP account information in XML
        """
        endpoint = f"/JSSResource/vppaccounts/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_vpp_account(self, data: str, id: Union[int, str]) -> str:
        """
        Updates a VPP account by ID with XML data

        :param data:
            XML data to udpate the VPP account with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatevppadminaccountbyid>`__
        :param id: VPP account ID

        :returns: Updated VPP account information in XML
        """
        endpoint = f"/JSSResource/vppaccounts/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_vpp_account(self, id: Union[int, str]) -> str:
        """
        Deletes a VPP account by ID

        :param id: VPP account ID

        :returns: Deleted VPP account information in XML
        """
        endpoint = f"/JSSResource/vppaccounts/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /vppassignments
    """

    def get_vpp_assignments(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all VPP assignments in JSON or XML

        :param data_type: json or xml

        :returns: All VPP assignments in JSON or XML
        """
        endpoint = "/JSSResource/vppassignments"

        return self._get(endpoint, data_type)

    def get_vpp_assignment(
        self, id: Union[int, str], data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on one VPP assignment in JSON or XML

        :param id: VPP assignment ID
        :param data_type: json or xml

        :returns: VPP assignment information in JSON or XML
        """
        endpoint = f"/JSSResource/vppassignments/id/{id}"

        return self._get(endpoint, data_type)

    def create_vpp_assignment(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a VPP assignment by ID with XML data

        :param data:
            XML data to create the VPP assignment with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createassignmentbyid>`__
        :param id: VPP assignment ID, set to 0 for next available ID

        :returns: New VPP assignment in XML
        """
        endpoint = f"/JSSResource/vppassignments/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_vpp_assignment(self, data: str, id: Union[int, str]) -> str:
        """
        Updates a VPP assignment by ID with XML data

        :param data:
            XML data to udpate the VPP assignment with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateassignmentbyid>`__
        :param id: VPP assignment ID

        :returns: Updated VPP assignment information in XML
        """
        endpoint = f"/JSSResource/vppassignments/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_vpp_assignment(self, id: Union[int, str]) -> str:
        """
        Deletes a VPP assignment by ID

        :param id: VPP assignment ID

        :returns: Deleted VPP assignment information in XML
        """
        endpoint = f"/JSSResource/vppassignments/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /vppinvitations
    """

    def get_vpp_invitations(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all VPP invitations in JSON or XML

        :param data_type: json or xml

        :returns: All VPP invitations in JSON or XML
        """
        endpoint = "/JSSResource/vppinvitations"

        return self._get(endpoint, data_type)

    def get_vpp_invitation(
        self, id: Union[int, str], subsets: List[str] = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on one VPP invitation in JSON or XML

        :param id: VPP invitation ID
        :param subsets:
            Subset(s) of data from the VPP invitation in a list of strings

            Options:
            - General
            - Scope
            - InvitationUsages

        :param data_type: json or xml

        :returns: VPP invitation information in JSON or XML
        """
        subset_options = ["General", "Scope", "InvitationUsages"]
        if valid_subsets(subsets, subset_options):
            endpoint = f"/JSSResource/vppinvitations/id/{id}/subset/{'&'.join(subsets)}"
        else:
            endpoint = f"/JSSResource/vppinvitations/id/{id}"

        return self._get(endpoint, data_type)

    def create_vpp_invitation(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a VPP invitation by ID with XML data

        :param data:
            XML data to create the VPP invitation with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createinvitationbyid>`__
        :param id: VPP invitation ID, set to 0 for next available ID

        :returns: New VPP invitation information in XML
        """
        endpoint = f"/JSSResource/vppinvitations/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_vpp_invitation(self, data: str, id: Union[int, str]) -> str:
        """
        Updates a VPP invitation by ID with XML data

        :param data:
            XML data to udpate the VPP invitation with. For syntax information
            view `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updateinvitationbyid>`__
        :param id: VPP invitation ID

        :returns: Updated VPP invitation information in XML
        """
        endpoint = f"/JSSResource/vppinvitations/id/{id}"

        return self._put(endpoint, data, data_type="xml")

    def delete_vpp_invitation(self, id: Union[int, str]) -> str:
        """
        Deletes a VPP invitation by ID

        :param id: VPP invitation ID

        :returns: Deleted VPP invitation information in XML
        """
        endpoint = f"/JSSResource/vppinvitations/id/{id}"

        return self._delete(endpoint, data_type="xml")

    """
    /webhooks
    """

    def get_webhooks(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all webhooks in either JSON or XML.

        :param data_type: json or xml

        :returns: All webhooks in JSON or XML
        """
        endpoint = "/JSSResource/webhooks"

        return self._get(endpoint, data_type)

    def get_webhook(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific webhook by either ID or name  in JSON
        or XML.

        :param id: Webhook ID
        :param name: Webhook name
        :param data_type: json or xml

        :returns: Webhook information in JSON or XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/webhooks/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._get(endpoint, data_type)

    def create_webhook(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates a webhook with the given XML data. Use ID 0 to use the next
        available ID.

        :param data:
            XML data to create the webhook with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/createwebhookbyid>`__
        :param id: ID of the new webhook, use 0 for next available ID.

        :returns: New webhook information in XML
        """
        endpoint = f"/JSSResource/webhooks/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_webhook(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a webhook with the given XML data. Need to supply at least
        one identifier.

        :param data:
            XML data to update the webhook with. For syntax information view
            `Jamf's documentation.
            <https://developer.jamf.com/jamf-pro/reference/updatewebhookbyid>`__
        :param id: Webhook ID
        :param name: Webhook name

        :returns: Updated information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/webhooks/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._put(endpoint, data, data_type="xml")

    def delete_webhook(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes a webhook by either ID or name. Need to supply at least one
        identifier.

        :param id: Webhook ID
        :param name: Webhook name

        :returns: Deleted webhook information in XML
        """
        identification_options = {
            "id": id,
            "name": name,
        }
        identification = identification_type(identification_options)
        endpoint = (
            f"/JSSResource/webhooks/{identification}/"
            f"{identification_options[identification]}"
        )

        return self._delete(endpoint, data_type="xml")
