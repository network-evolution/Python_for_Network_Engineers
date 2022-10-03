#! /usr/local/Python_envs/Python3/bin/python3
import re

import requests
import json
from pprint import pprint

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

switchuser='admin'
switchpassword='Admin_1234!'

url='https://sandbox-nxos-1.cisco.com/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show_ascii",
    "chunk": "0",
    "sid": "sid",
    "input": "show version",
    "output_format": "json"
  }
}
my_pattern = re.compile(r"(?P<ProcessorFamily>\S.+) @ (?P<ProcessorSpeed>\S+) with \d+ \S+ of memory.")
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()
# print(response)
cli_ascii_out = response['ins_api']['outputs']['output']['body']
# print(cli_ascii_out)
processor_match = my_pattern.search(cli_ascii_out).groupdict()
print(processor_match)
print(processor_match['ProcessorFamily'])
print(processor_match['ProcessorSpeed'])







