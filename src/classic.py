from request_builder import RequestBuilder
from typing import Union
from utils import identification_type, valid_subsets


class Classic(RequestBuilder):
    def __init__(self, base_url, username, password):
        super().__init__(base_url, username, password)

    """
    /accounts
    """

    def get_accounts(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all accounts and account groups.

        :param data_type: JSON or XML
        """
        endpoint = "/JSSResource/accounts"

        return self._get(endpoint, data_type)

    def get_account_group(
        self, data_type: str = "json", id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Returns an account group by either ID or name in json or xml. Need to
        supply at least one identifier.

        :param data_type: JSON or XML
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
        self, data_type: str = "json", id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Returns an account by either ID or name in json or xml. Need to
        supply at least one identifier.

        :param data_type: JSON or XML
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

        :param data_type: JSON or XML
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

        :param data_type: JSON or XML
        """
        endpoint = "/JSSResource/advancedcomputersearches"

        return self._get(endpoint, data_type)

    def get_advanced_computer_search(
        self, data_type: str = "json", id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Returns data on a specific advanced computer search by either ID or
        name.

        :param data_type: JSON or XML
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
        Deletes an advanced computer search by either ID or name. Need to supply
        at least one identifier.

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

        :param data_type: JSON or XML
        """
        endpoint = "/JSSResource/advancedmobiledevicesearches"

        return self._get(endpoint, data_type)

    def get_advanced_mobile_device_search(
        self, data_type: str = "json", id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Returns data on a specific advanced mobile device search by either ID or
        name.

        :param data_type: JSON or XML
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

        return self._get(endpoint, data_type)

    def create_advanced_mobile_device_search(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
        """
        Creates an advanced mobile device search with the given XML data. Use ID 0
        to use the next available ID.

        :param data: XML data to create the advanced mobile device search with
        :param id:
            ID of the new advanced mobile device search, use 0 for next available ID
        """
        endpoint = f"/JSSResource/advancedmobiledevicesearches/id/{id}"

        return self._post(endpoint, data, data_type="xml")

    def update_advanced_mobile_device_search(
        self, data: str, id: Union[int, str] = None, name: str = None
    ) -> str:
        """
        Updates and advanced mobile device search with the given XML data. Need to
        supply at least one identifier.

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
        Deletes an advanced mobile device search by either ID or name. Need to supply
        at least one identifier.

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

    def get_advanced_user_searches(
        self, data_type: str = "json"
    ) -> Union[dict, str]:
        """
        Returns all advanced user searches in either JSON or XML.

        :param data_type: JSON or XML
        """
        endpoint = "/JSSResource/advancedusersearches"

        return self._get(endpoint, data_type)

    def get_advanced_user_search(
        self, data_type: str = "json", id: Union[int, str] = None, name: str = None
    ) -> Union[dict, str]:
        """
        Returns data on a specific advanced user search by either ID or
        name.

        :param data_type: JSON or XML
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

        return self._get(endpoint, data_type)

    def create_advanced_user_search(
        self, data: str, id: Union[int, str] = 0
    ) -> str:
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

    """
    /buildings
    """

    """
    /byoprofiles
    """

    """
    /categories
    """

    """
    /classes
    """

    """
    /commandflush
    """

    """
    /computerapplications
    """

    """
    /computerapplicationusage
    """

    """
    /computercheckin
    """

    """
    /computercommands
    """

    """
    /computerextensionattributes
    """

    """
    /computergroups
    """

    """
    /computerhardwaresoftwarereports
    """

    """
    /computerhistory
    """

    """
    /computerinventorycollection
    """

    """
    /computerinvitations
    """

    """
    /computermanagement
    """

    """
    /computerreports
    """

    """
    /computers
    """

    """
    /departments
    """

    """
    /directorybindings
    """

    """
    /diskencryptionconfigurations
    """

    """
    /distributionpoints
    """

    """
    /dockitems
    """

    """
    /ebooks
    """

    """
    /fileuploads
    """

    """
    /gsxconnection
    """

    """
    /healthcaraelistener
    """

    """
    /healthcarelistenerrule
    """

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

        :param match:
            String to search mobile devices
        :param data_type:
            JSON or XML
        """

        if match:
            endpoint = f"/JSSResource/mobiledevices/match/{match}"
        else:
            endpoint = "/JSSResource/mobiledevices"

        return self._get(endpoint, data_type)

    def get_mobile_device(
        self,
        data_type: str = "json",
        subsets: list = None,
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
    ):
        """
        Returns information on a mobile device with given identifier in either
        JSON or XML. You can specify the return of a subset of the data by
        defining subset as a list of the subsets that you want. Need to supply
        at least one identifier.

        :param data_type: JSON or XML
        :param subsets:
            Subset(s) of data from the mobile device
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
