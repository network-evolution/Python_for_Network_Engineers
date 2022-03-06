#! /usr/local/Python_envs/Python3/bin/python3
import requests

url = "http://192.168.0.21/api/v2/monitor/system/config/backup?destination=file&scope=global"

payload={}
headers = {
	'Authorization': 'Bearer tQcmNwHmsbm68skz8xgtkzQ0104gnm',
	'Cookie': 'FILE_DOWNLOADING_10658316494359874758="1"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

with open("Backup02.conf", 'wb') as f:
	f.write(response.content)