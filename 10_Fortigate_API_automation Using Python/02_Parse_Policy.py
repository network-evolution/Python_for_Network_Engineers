#! /usr/local/Python_envs/Python3/bin/python3
import requests

url = "http://192.168.0.21/api/v2/cmdb/firewall/policy"

payload={}
headers = {
	'Authorization': 'Bearer tQcmNwHmsbm68skz8xgtkzQ0104gnm'
}

response = requests.request("GET", url, headers=headers, data=payload)

results = response.json()['results']
print(results)
total = len(results)

for i in range(0,total):
	print(f"\n\n{'Policy Name'.ljust(18)}:{results[i]['name']}")
	print(f"{'Source Int.'.ljust(18)}:{results[i]['srcintf'][0]['name']}")
	print(f"{'Destination Int.'.ljust(18)}:{results[i]['dstintf'][0]['name']}")


