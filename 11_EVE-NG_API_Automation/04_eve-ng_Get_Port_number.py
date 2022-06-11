#! /usr/local/Python_envs/Python3/bin/python3
import re
import time

import requests
import json
from telnetlib import Telnet


def create_instance(instance_name):
	login_url = 'http://192.168.0.12/api/auth/login'
	cred = '{"username":"admin","password":"eve","html5":"-1"}'
	headers = {'Accept': 'application/json'}

	login = requests.post(url=login_url, data=cred)
	cookies = login.cookies
	print(cookies)


	ios_data = {"template": "vios", "type": "qemu", "count": "1", "image": "vios-Rtr-15", "name": f"{instance_name}",
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

		######### Get telnet Port
	url = f"http://192.168.0.12/api/labs/Lab_Evolution.unl/nodes"
	nodes = requests.get(url=url, headers=headers,cookies=cookies)
	data = nodes.json()
	node_dict = data['data']
	port_details = node_dict[f"{device_id}"]['url']
	# print(port_details)
	port_pattern = re.compile(r'telnet.+:(\d+)')
	port_output = int((port_pattern.search(port_details).group(1)))
	return port_output

def telnet_initial(telnet_port):
	TELNET_TIMEOUT =10
	tn = Telnet(host='192.168.0.12',port=telnet_port,timeout=TELNET_TIMEOUT)
	tn.write(b"\n")
	tn.write(b"\n")
	tn.write(b"\n")
	tn.write(b"no\n")
	time.sleep(10)
	tn.write(b"\n")

def device_config(device_name,telnet_port):
	TELNET_TIMEOUT = 10
	tn = Telnet(host='192.168.0.12', port=telnet_port, timeout=TELNET_TIMEOUT)
	with open(f"{device_name}.conf", 'r') as cmd_file:
		for cmd in cmd_file.readlines():
			cmd = cmd.strip('\r\n')
			tn.write(cmd.encode()+ b'\r')
			time.sleep(1)

def provision(device_name):
	telnet_port = create_instance(device_name)
	print(f"Telnet Port of the Node is: {telnet_port}")
	print("Initiating sleep for 100s")
	time.sleep(100)
	print("Finished sleep for 100s")
	telnet_initial(telnet_port)
	print("Finished Initial Configuration")
	time.sleep(15)
	device_config(device_name,telnet_port)
	print("Finished Setting up the device")

# provision('vIOS_91')
provision('vIOS_62')