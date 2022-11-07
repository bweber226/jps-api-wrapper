from mimetypes import guess_type
from os.path import basename
from typing import Union

from request_builder import RequestBuilder
from utils import (
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
        """
        endpoint = "/JSSResource/accounts"

        return self._get(endpoint, data_type)

    def get_account_group(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns an account group by either ID or name in json or xml. Need to
        supply at least one identifier.

        :param id: Account group ID
        :param name: Account group name
        :param data_type: json or xml
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

    def create_account_group(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates an account group with the given XML data. Use ID 0 to use the
        next available ID.

        :param data: XML data to create the account group with
        :param id: ID of the new account group, use 0 for next available ID
        """
        endpoint = f"/JSSResource/accounts/groupid/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_account_group(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates an account group with the given XML data by either ID or name.
        Need to supply at least one identifier.

        :param data: XML data to update the account group with
        :param id: Account group ID
        :param name: Account group name
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

    def delete_account_group(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes an account group by ID or name. Need to supply at leas one
        identifier.

        :param id: Account group ID
        :param name: Account group name
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

    def get_account(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns an account by either ID or name in json or xml. Need to
        supply at least one identifier.

        :param id: Account ID
        :param name: Account name
        :param data_type: json or xml
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

    def create_account(self, data: str, id: Union[int, str] = 0) -> str:
        """
        Creates an account with the given XML data. Use ID 0 to use the
        next available ID.

        :param data: XML data to create the account with
        :param id: ID of the new account, use 0 for next available ID
        """
        endpoint = f"/JSSResource/accounts/userid/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_account(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates an account with the given XML data by either ID or name.
        Need to supply at least one identifier.

        :param data: XML data to update the account with
        :param id: Account ID
        :param name: Account name
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

    def delete_account(self, id: Union[int, str] = None, name: str = None) -> str:
        """
        Deletes an account by ID or name. Need to supply at leas one
        identifier.

        :param id: Account ID
        :param name: Account name
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

    """
    /activationcode
    """

    def get_activation_code(self, data_type: str = "json") -> str:
        """
        Get's the activation code of the JPS server.

        :param data_type: json or xml
        """
        endpoint = "/JSSResource/activationcode"

        return self._get(endpoint, data_type)

    def update_activation_code(self, data: str) -> str:
        """
        Updates the activation code of the JPS server.

        :param data: XML data to update the activation code with
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

        :param data: XML data to create the advanced computer search with
        :param id:
            ID of the new advanced computer search, use 0 for next available ID
        """
        endpoint = f"/JSSResource/advancedcomputersearches/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_advanced_computer_search(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates and advanced computer search with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the advanced computer search with
        :param id: Advanced computer search ID
        :param name: Advanced computer search name
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
    ) -> Union[dict, str]:
        """
        Deletes an advanced computer search by either ID or name. Need to
        supply at least one identifier.

        :param id: Advanced computer search ID
        :param name: Advanced computer search name
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

        :param data: XML data to create the advanced mobile device search with
        :param id:
            ID of the new advanced mobile device search, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/advancedmobiledevicesearches/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_advanced_mobile_device_search(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates and advanced mobile device search with the given XML data. Need
        to supply at least one identifier.

        :param data: XML data to update the advanced mobile device search with
        :param id: Advanced mobile device search ID
        :param name: Advanced mobile device search name
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
    ) -> Union[dict, str]:
        """
        Deletes an advanced mobile device search by either ID or name. Need
        to supply at least one identifier.

        :param id: Advanced mobile device search ID
        :param name: Advanced mobile device search name
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

        :param data: XML data to create the advanced user search with
        :param id:
            ID of the new advanced user search, use 0 for next available ID
        """
        endpoint = f"/JSSResource/advancedusersearches/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_advanced_user_search(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates and advanced user search with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the advanced user search with
        :param id: Advanced user search ID
        :param name: Advanced user search name
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
    ) -> Union[dict, str]:
        """
        Deletes an advanced user search by either ID or name. Need to supply
        at least one identifier.

        :param id: Advanced user search ID
        :param name: Advanced user search name
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

        :param data: XML data to create the allowed file extension
        :param id: Allowed file extension id
        """
        endpoint = f"/JSSResource/allowedfileextensions/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def delete_allowed_file_extension(self, id: Union[int, str]) -> str:
        """
        Deletes an allowed file extension with the given ID.

        :param id: Allowed file extension ID
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

        :param data: XML data to create the building with
        :param id:
            ID of the new building, use 0 for next available ID
        """
        endpoint = f"/JSSResource/buildings/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_building(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a building with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the building with
        :param id: building ID
        :param name: building name
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

    def delete_building(
        self, id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Deletes a building by either ID or name. Need to supply
        at least one identifier.

        :param id: building ID
        :param name: building name
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
        Returns all byo profiles in either JSON or XML.

        :param data_type: json or xml
        """
        endpoint = "/JSSResource/byoprofiles"

        return self._get(endpoint, data_type)

    def get_byo_profile(
        self, id: Union[int, str] = None, name: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns data on a specific byo profile by either ID or
        name.

        :param id: byo profile ID
        :param name: byo profile name
        :param data_type: json or xml
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
        Creates a byo profile with the given XML data. Use ID 0
        to use the next available ID.

        :param data: XML data to create the byo profile with
        :param id:
            ID of the new byo profile, use 0 for next available ID
        """
        endpoint = f"/JSSResource/byoprofiles/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_byo_profile(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a byo profile with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the byo profile with
        :param id: byo profile ID
        :param name: byo profile name
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

    def delete_byo_profile(
        self, id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Deletes a byo profile by either ID or name. Need to supply
        at least one identifier.

        :param id: byo profile ID
        :param name: byo profile name
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

        :param data: XML data to create the category with
        :param id:
            ID of the new category, use 0 for next available ID
        """
        endpoint = f"/JSSResource/categories/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_category(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a category with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the category with
        :param id: category ID
        :param name: category name
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

    def delete_category(
        self, id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Deletes a category by either ID or name. Need to supply
        at least one identifier.

        :param id: category ID
        :param name: category name
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

        :param data: XML data to create the class with
        :param id:
            ID of the new class, use 0 for next available ID
        """
        endpoint = f"/JSSResource/classes/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_class(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a class with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the class with
        :param id: class ID
        :param name: class name
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

    def delete_class(
        self, id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Deletes a class by either ID or name. Need to supply
        at least one identifier.

        :param id: class ID
        :param name: class name
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

    def command_flush(
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

        :param data: XML data to define command flushing
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
        """
        endpoint = "/JSSResource/computercheckin"

        return self._get(endpoint, data_type)

    def update_computer_check_in(self, data: str) -> str:
        """
        Updates computer check in information based on XML data

        :param data: XML data
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
        """
        endpoint = f"/JSSResource/computercommands/status/{uuid}"

        return self._get(endpoint, data_type)

    def create_computer_command(
        self,
        command: str,
        ids: str = None,
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
        :param data: XML data for creating computer command
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

        :param data: XML data to create the computer extension attribute with
        :param id:
            ID of the new computer extension attribute, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/computerextensionattributes/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_computer_extension_attribute(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a computer extension attribute with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the computer extension attribute with
        :param id: computer extension attribute ID
        :param name: computer extension attribute name
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
    ) -> Union[dict, str]:
        """
        Deletes a computer extension attribute by either ID or name. Need to
        supply at least one identifier.

        :param id: computer extension attribute ID
        :param name: computer extension attribute name
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

        :param data: XML data to create the computer group with
        :param id:
            ID of the new computer group, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/computergroups/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_computer_group(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a computer group with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the computer group with
        :param id: computer group ID
        :param name: computer group name
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
    ) -> Union[dict, str]:
        """
        Deletes a computer group by either ID or name. Need to supply
        at least one identifier.

        :param id: computer group ID
        :param name: computer group name
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
        subsets: list = None,
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
        subsets: list = None,
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
        """
        endpoint = "/JSSResource/computerinventorycollection"

        return self._get(endpoint, data_type)

    def update_computer_inventory_collection(self, data: str) -> str:
        """
        Updates computer inventory collection settings on the JPS server with
        the given XML data. Need to supply at least one identifier.

        :param data: XML data to update the computer inventory collection
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

        :param data: XML data
        :param id: Computer invitation ID, use 0 for next available
        :param invitation:
            Computer invitation invitation identifier, use 0 for next available
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
    ) -> Union[int, str]:
        """
        Deletes a computer invitation by either ID or invitation identifiers.
        Need to supply at least one identifier.

        :param id: Computer invitation ID
        :param invitation:
            Computer invitation invitation identifier (name)
            Typically a long int
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
        subsets: list = None,
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

        :param data_type: JSON or XML
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
        subsets: list = None,
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
            XML data to update/create the computer.
        :param id: Computer ID, set to 0 for next available ID
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

        :param data: XML string to update the computer with
        :param id: Computer ID
        :param name: Computer name
        :param udid: Computer UDID
        :param serialnumber: Computer serial number
        :param macaddress: Computer MAC address
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

        :param data: XML data to create the department with
        :param id:
            ID of the new department, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/departments/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_department(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a department with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the department with
        :param id: Department ID
        :param name: Department name
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

    def delete_department(
        self, id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Deletes a department by either ID or name. Need to supply
        at least one identifier.

        :param id: Department ID
        :param name: Department name
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

        :param data: XML data to create the directory binding with
        :param id:
            ID of the new directory binding, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/directorybindings/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_directory_binding(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a directory binding with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the directory binding with
        :param id: Directory binding ID
        :param name: Directory binding name
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
    ) -> Union[dict, str]:
        """
        Deletes a directory binding by either ID or name. Need to supply
        at least one identifier.

        :param id: Directory binding ID
        :param name: Directory binding name
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

        :param data: XML data to create the disk encryption configuration with
        :param id:
            ID of the new disk encryption configuration, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/diskencryptionconfigurations/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_disk_encryption_configuration(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a disk encryption configuration with the given XML data. Need
        to supply at least one identifier.

        :param data: XML data to update the disk encryption configuration with
        :param id: disk encryption configuration ID
        :param name: disk encryption configuration name
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
    ) -> Union[dict, str]:
        """
        Deletes a disk encryption configuration by either ID or name. Need to
        supply at least one identifier.

        :param id: disk encryption configuration ID
        :param name: disk encryption configuration name
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

        :param data: XML data to create the distribution point with
        :param id:
            ID of the new distribution point, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/distributionpoints/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_distribution_point(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a distribution point with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the distribution point with
        :param id: Distribution point ID
        :param name: Distribution point name
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
    ) -> Union[dict, str]:
        """
        Deletes a distribution point by either ID or name. Need to supply
        at least one identifier.

        :param id: Distribution point ID
        :param name: Distribution point name
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

        :param data: XML data to create the dock item with
        :param id:
            ID of the new dock item, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/dockitems/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_dock_item(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a dock item with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the dock item with
        :param id: Dock item ID
        :param name: Dock item name
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

    def delete_dock_item(
        self, id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Deletes a dock item by either ID or name. Need to supply
        at least one identifier.

        :param id: Dock item ID
        :param name: Dock item name
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
        """
        endpoint = "/JSSResource/ebooks"

        return self._get(endpoint, data_type)

    def get_ebook(
        self,
        id: Union[int, str] = None,
        name: str = None,
        subsets: list = None,
        data_type: str = "json",
    ) -> Union[dict, str]:
        """
        Returns data on a specific ebook by either ID or name.

        :param id: eBook ID
        :param name: eBook name
        :param subsets:
            Subset(s) of data from the computer in a list of strings

            Options:
            - General
            - Scope
            - SelfService

        :param data_type: json or xml
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
        Creates a ebook with the given XML data. Use ID 0
        to use the next available ID.

        :param data: XML data to create the ebook with
        :param id:
            ID of the new ebook, use 0 for next
            available ID
        """
        endpoint = f"/JSSResource/ebooks/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_ebook(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates a ebook with the given XML data. Need to
        supply at least one identifier.

        :param data: XML data to update the ebook with
        :param id: eBook ID
        :param name: eBook name
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

    def delete_ebook(
        self, id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Deletes a ebook by either ID or name. Need to supply
        at least one identifier.

        :param id: eBook ID
        :param name: eBook name
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

    def file_upload(
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
        - computers
        - mobiledevices
        - peripherals
        - policies
        - ebooks
        - mobiledeviceapplicationsicon
        - mobiledeviceapplicationsipa
        - diskencryptionconfigurations

        :param filepath: Filepath to file to upload
        :param id: Resource ID
        :param name:
            Resource name, not usable with resource options peripherals
        :param force_ipa_upload:
            True of False, enforces ipa file type. Only usable with
            mobiledeviceapplicationsipa resource

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
                if not content_type:
                    raise ValueError(f"Unable to detect MIME type of file {filename}")
                file = {"name": (filename, f, content_type)}
                if force_ipa_upload:
                    query_string = ["FORCE_IPA_UPLOAD=true"]
                else:
                    query_string = None
                endpoint = (
                    f"/JSSResource/fileuploads/{resource}/{identification}"
                    f"/{identification_options[identification]}"
                )

                return self._post(
                    endpoint, None, file=file, data_type=None, query_string=query_string
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
        """
        endpoint = "/JSSResource/gsxconnection"

        return self._get(endpoint, data_type)

    def update_gsx_connection(self, data: str):
        """
        Updates the Jamf Pro GSX connection information with XML data.

        :param data: XML data to update with
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
        """
        endpoint = f"/JSSResource/healthcarelistener/id/{id}"

        return self._get(endpoint, data_type)

    def update_healthcare_listener(self, data: str, id: Union[int, str]) -> str:
        """
        Updates an existing healthcare listener by ID with XML data

        :param data: XML data to update healthcare listener with
        :param id: Healthcare listener ID
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
        """
        endpoint = f"/JSSResource/healthcarelistenerrule/id/{id}"

        return self._get(endpoint, data_type)

    def create_healthcare_listener_rule(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates a healthcare listener rule by ID with XML data

        :param data: XML data to udpate healthcare listener rule with
        :param id: Healthcare listener rule ID, use 0 for next available ID
        """
        endpoint = f"/JSSResource/healthcarelistenerrule/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_healthcare_listener_rule(self, data: str, id: Union[int, str]) -> str:
        """
        Updates an existing healthcare listener rule by ID with XML data

        :param data: XML data to update healthcare listener rule with
        :param id: healthcare listener rule ID
        """
        endpoint = f"/JSSResource/healthcarelistenerrule/id/{id}"

        return self._put(endpoint, data, data_type="xml")

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

    def get_mobile_devices(
        self, match: str = None, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all mobile devices from a JPS instance in either JSON or XML.
        You can pass the match param to get all mobile devices that match
        your search critera.

        :param match: String to search mobile devices
        :param data_type: json or xml
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
        subsets: list = None,
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
            XML data to update/create the mobile device.
        :param id: Mobile device ID, set to 0 for next available ID
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

        :param data: XML string to update the Mobile device with
        :param id: Mobile device ID
        :param name: Mobile device name
        :param udid: Mobile device UDID
        :param serialnumber: Mobile device serial number
        :param macaddress: Mobile device MAC address
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
