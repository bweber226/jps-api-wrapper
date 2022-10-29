from request_builder import RequestBuilder

class Classic(RequestBuilder):

    def __init__(self, base_url, username, password):
        super().__init__(base_url, username, password)
    
    # /mobiledevices
    def get_mobile_devices(self, data_type: str = "json"):
        endpoint = "/JSSResource/mobiledevices"
    
        return self.get(endpoint, data_type)

    def get_mobile_device(self, id, data_type: str = "json"):
        endpoint = f"/JSSResource/mobiledevices/id/{id}"

        return self.get(endpoint, data_type)