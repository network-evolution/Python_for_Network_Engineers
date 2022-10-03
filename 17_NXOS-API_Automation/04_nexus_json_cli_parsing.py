#! /usr/local/Python_envs/Python3/bin/python3
import requests
import json
from pprint import pprint

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

switchuser='admin'
switchpassword='admin'

url='https://192.168.0.201/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show version ; show hardware ; show ip interface brief",
    "output_format": "json"
  }
}

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()
pprint(response)

print(response["ins_api"]["outputs"]["output"][0]['body']['chassis_id'])
print(response["ins_api"]["outputs"]["output"][0]['body']['proc_board_id'])
print(response["ins_api"]["outputs"]["output"][1]['body']['manufacturer'])
print(response["ins_api"]["outputs"]["output"][2]['body']['TABLE_intf']['ROW_intf']['intf-name'])
print(response["ins_api"]["outputs"]["output"][2]['body']['TABLE_intf']['ROW_intf']['prefix'])





