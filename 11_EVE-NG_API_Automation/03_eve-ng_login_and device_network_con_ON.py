#! /usr/local/Python_envs/Python3/bin/python3

import requests
import json

def create_instance(total):
	login_url = 'http://192.168.0.12/api/auth/login'
	cred = '{"username":"admin","password":"eve","html5":"-1"}'
	headers = {'Accept': 'application/json'}

	login = requests.post(url=login_url, data=cred)
	cookies = login.cookies
	print(cookies)
	for i in range(1,total+1):

		ios_data = {"template": "vios", "type": "qemu", "count": "1", "image": "vios-Rtr-15", "name": f"vIOS_{i}",
					"icon": "Router.png", "uuid": "", "cpulimit": "undefined", "cpu": "1", "ram": "1024", "ethernet": "4",
					"qemu_version": "", "qemu_arch": "", "qemu_nic": "",
					"qemu_options": "-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
					"ro_qemu_options": "-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
					"config": "0", "delay": "0", "console": "telnet", "left": "1005", "top": "130", "postfix": 0}

		ios_data = json.dumps(ios_data)
		create_url = 'http://192.168.0.12/api/labs/Lab_Evolution.unl/nodes'

		create_api = requests.post(url=create_url,data=ios_data,cookies=cookies,headers=headers)
		response =create_api.json()
		print(response)
		device_id = response['data']['id']
		print(f"Created Instance ID is: {device_id}")

		###### Interface connection
		print("Connecting the Interface")
		add_int_url = f'http://192.168.0.12/api/labs/Lab_Evolution.unl/nodes/{device_id}/interfaces'
		int_map = '{"0":"1"}'
		connect_int = requests.put(url=add_int_url,data=int_map,headers=headers,cookies=cookies)
		print(connect_int.json())

		####### Start Instance
		print("Starting the Device")
		url = f"http://192.168.0.12/api/labs/Lab_Evolution.unl/nodes/{device_id}/start"
		start_api = requests.request("GET", url, headers=headers, cookies=cookies)
		print(start_api.json())

total_instance = int(input("Enter total number of Instances Required:"))
create_instance(total_instance)
