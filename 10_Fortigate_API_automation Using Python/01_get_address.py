#! /usr/local/Python_envs/Python3/bin/python3
import requests
from pprint import pprint
url = "http://192.168.0.21/api/v2/cmdb/firewall/address"

headers = {'Authorization': 'Bearer tQcmNwHmsbm68skz8xgtkzQ0104gnm'}

response = requests.request("GET", url, headers=headers)

pprint(response.json()['results'])
