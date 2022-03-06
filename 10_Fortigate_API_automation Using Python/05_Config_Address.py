#! /usr/local/Python_envs/Python3/bin/python3
import requests
import json

url = "http://192.168.0.21/api/v2/cmdb/firewall/address"
## 01 Pass data as a string ######
# payload = '''
# [{
#     "name": "IP_01",
#     "subnet": "1.1.1.1/32",
#     "color": "0"
#   },
#   {
#     "name": "IP_02",
#     "subnet": "1.1.1.2/32",
#     "color": "0"
#   }
#   ]
#   '''

## Pass as a Python list #########################
# l1 = [{
# 	"name": "IP_01",
# 	"subnet": "1.1.1.1/32",
# 	"color": "0"
# },
# 	{
# 		"name": "IP_02",
# 		"subnet": "1.1.1.2/32",
# 		"color": "0"
# 	}
# ]
# payload = json.dumps(l1)

## 03 Read from Json file ############################
# with open ('address_config.json', 'r') as f:
# 	payload = f.read()
# print(payload)


## 04 User Input #############################
number = int(input("Enter the Number of IPs Needed: "))
l1 = list()
for addr_obj in range(1, number + 1):
	addr_dict = dict()
	addr_dict['name'] = input(f"\n Enter the Name of Address Object_{addr_obj}: ")
	addr_dict['subnet'] = input(f"Enter the IP of Address Object_{addr_obj}: ")
	l1.append(addr_dict)

payload = json.dumps(l1)
headers = {'Authorization': 'Bearer tQcmNwHmsbm68skz8xgtkzQ0104gnm', }

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
