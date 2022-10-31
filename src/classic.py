from request_builder import RequestBuilder
from typing import Union
from utils import identification_type, valid_subsets


class Classic(RequestBuilder):
    def __init__(self, base_url, username, password):
        super().__init__(base_url, username, password)

    """
    /mobiledevices
    """

    def get_mobile_devices(self, match: str = None, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all mobile devices from a JPS instance in either json or xml.

        :param match:
            String to search mobile devices
        :param data_type:
            json or xml
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
        json or xml. You can specify the return of a subset of the data by
        defining subset as a list of the subsets that you want. Need to supply
        at least one identifier.

        :param data_type: json or xml
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

        :raises UnrecognizedSubset:
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
        Creates a mobile device with the given id and information defined in
        XML data.

        :param data: XML data to update/create the mobile device
        :param id: Mobile device id, set to 0 for next available
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