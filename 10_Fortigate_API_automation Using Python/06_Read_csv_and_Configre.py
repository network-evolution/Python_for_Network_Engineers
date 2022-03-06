#! /usr/local/Python_envs/Python3/bin/python3
import time

import requests
import json
from csv import DictReader

url = "http://192.168.0.21/api/v2/cmdb/firewall/address"
###############################################################################
# number = int(input("Enter the Number of IPs Needed: "))
# l1 = list()
# for addr_obj in range(1, number + 1):
# 	addr_dict = dict()
# 	addr_dict['name'] = input(f"\n Enter the Name of Address Object_{addr_obj}: ")
# 	addr_dict['subnet'] = input(f"Enter the IP of Address Object_{addr_obj}: ")
# 	l1.append(addr_dict)
#
# payload = json.dumps(l1)
################################################################################
# with open('01_IP_List.csv', 'r') as csv_file:
# 	ip_details = DictReader(csv_file)
# 	l1 = list()
# 	for ip in ip_details:
# 		ip_dict = dict()
# 		ip_dict['name'] = ip['Name']
# 		ip_dict['subnet'] = ip['IP']
# 		l1.append(ip_dict)
# payload = json.dumps(l1)
######################## Send each Object ###############
with open('01_IP_List.csv', 'r') as csv_file:
	ip_details = DictReader(csv_file)

	for ip in ip_details:
		time.sleep(.5)
		print(f"Configuring {ip['Name']} {ip['IP']}")
		ip_dict = dict()
		ip_dict['name'] = ip['Name']
		ip_dict['subnet'] = ip['IP']

		print(ip_dict)

		payload = json.dumps(ip_dict)

		headers = {'Authorization': 'Bearer tQcmNwHmsbm68skz8xgtkzQ0104gnm', }

		response = requests.request("POST", url, headers=headers, data=payload)

		print(response.status_code)
		print(response.ok)
		# print(response.content)
		output = response.json()

		if 'cli_error' in output:
			print(f"CLI Error: {output['cli_error']}")





