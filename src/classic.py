from request_builder import RequestBuilder
from typing import Union
from utils import identification_type


class Classic(RequestBuilder):
    def __init__(self, base_url, username, password):
        super().__init__(base_url, username, password)

    """
    /mobiledevices
    """

    def get_mobile_devices(self, data_type: str = "json") -> Union[dict, str]:
        """
        Returns all mobile devices from a JPS instance in either json or xml.

        :param data_type:
            json or xml
        """
        endpoint = "/JSSResource/mobiledevices"

        return self._get(endpoint, data_type)

    def get_mobile_device(
        self,
        data_type: str = "json",
        id: Union[str, int] = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
    ):
        """
        Returns information on a mobile device with given identifier in either
        json or xml.

        :param data_type: json or xml
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
        Updates information on a mobile device with given identifier.

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