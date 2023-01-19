from jps_api_wrapper.classic import Classic
from jps_api_wrapper.pro import Pro
from os import environ
from pprint import pprint

JPS_URL = "https://cvtcprod.jamfcloud.com/"
JPS_USERNAME = "bweber26"
JPS_PASSWORD = environ["JPS_PASSWORD"]
with Classic(JPS_URL, JPS_USERNAME, JPS_PASSWORD) as classic:
    pprint(classic.get_computer_history(146, subsets=["Audits"]))
