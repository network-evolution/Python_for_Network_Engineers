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
      "cmd": "show hardware",
      "version": 1
    },
    "id": 10
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()

pprint(response)
print(response['result']['body']['kickstart_ver_str'])
print(response['result']['body']['kick_file_name'])


