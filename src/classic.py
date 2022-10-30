from request_builder import RequestBuilder
from utils import identification_type


class Classic(RequestBuilder):
    def __init__(self, base_url, username, password):
        super().__init__(base_url, username, password)

    """
    /mobiledevices
    """

    def get_mobile_devices(self, data_type: str = "json"):
        """
        Returns all mobile devices from a JPS instance.

        :param data_type:
            json or xml
        
        :returns:
            
        """
        endpoint = "/JSSResource/mobiledevices"

        return self.get(endpoint, data_type)

    def get_mobile_device(
        self,
        data_type: str = "json",
        id: str = None,
        name: str = None,
        udid: str = None,
        serialnumber: str = None,
        macaddress: str = None,
    ):
        identification_options = {
            "id": id,
            "name": name,
            "udid": udid,
            "serialnumber": serialnumber,
            "macaddress": macaddress,
        }
        identification = identification_type(identification_options)

        endpoint = (f"/JSSResource/mobiledevices/{identification}"
        f"/{identification_options[identification]}")

        return self.get(endpoint, data_type)
