#! /usr/local/Python_envs/Python3/bin/python3
import requests
import json
from pprint import pprint

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
"""
Modify these please
"""

switchuser='admin'
switchpassword='admin'

url='https://192.168.0.201/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "interface e1/2",
      "version": 1
    },
    "id": 1,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "description from-jsonrpc",
      "version": 1
    },
    "id": 2,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "aaa",
      "version": 1
    },
    "id": 3,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "no switchport",
      "version": 1
    },
    "id": 4,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "ip add 1.1.1.1 255.255.255.0",
      "version": 1
    },
    "id": 5,
    "rollback": "rollback-on-error"
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False)
print(response.status_code)
output = response.json()
pprint(output)
# print(response['result']['msg'])




