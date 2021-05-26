#! /usr/local/Python_envs/Python3/bin/python3
import requests
import json
#device = input("Enter Device Name/IP :" or "ios-xe-mgmt-latest.cisco.com")

restconf_headers = {"Accept": "application/yang-data+json"}
url = 'https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/ietf-interfaces:interfaces'

r = requests.get(url,
        headers = restconf_headers,
        auth=("developer", "C1sco12345"),
        verify=False)

# Print returned data
print("GET DATA:")
print(r.text)
