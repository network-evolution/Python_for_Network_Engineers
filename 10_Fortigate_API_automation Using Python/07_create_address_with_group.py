#! /usr/local/Python_envs/Python3/bin/python3
import time

import requests
import json
from csv import DictReader

url = "http://192.168.0.21/api/v2/cmdb/firewall/address"

with open('01_IP_List_group.csv', 'r') as csv_file:
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

		group_dict = dict()
		group_dict["name"] = ip["Name"]
		group_payload = json.dumps(group_dict)
		print(f"Group Dictionary : {group_dict}")

		group_url = f"http://192.168.0.21/api/v2/cmdb/firewall/addrgrp/{ip['Group']}/member"

		group_response = requests.request("POST",group_url, data=group_payload, headers=headers)

		print(group_response.status_code)
		print(group_response.ok)
		# print(response.content)
		output = group_response.json()







