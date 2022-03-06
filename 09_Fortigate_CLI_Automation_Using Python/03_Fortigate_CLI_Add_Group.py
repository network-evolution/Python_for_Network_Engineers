#! /usr/local/Python_envs/Python3/bin/python3

from csv import DictReader
import time
from netmiko import Netmiko

fw_01 = {'host': '192.168.0.21',
		 'username':'admin',
		 'password':'Password@123',
		 'device_type': 'fortinet'
		 }
print(f"{'#'*20} Connecting to the Device {'#'*20}")
net_connect = Netmiko(**fw_01)
print(f"{'#'*20} Connected {'#'*20}")



with open('01_IP_List_group.csv') as csv_file:
	ip_details = DictReader(csv_file)
	# print(ip_details)
	for ip in ip_details:
		time.sleep(2)
		print(f"{'#'*20} Configuring Object {ip['Name']} {'#'*20}")
		config = ['config firewall address',
				  f'edit {ip["Name"]}',
				  'set type ipmask',
				  f'set subnet {ip["IP"]}',
				  'end',
				  'config firewall addrgrp',
				  f'edit {ip["Group"]}',
				  f'append member {ip["Name"]}',
				  'end'
				  ]
		send_config = net_connect.send_config_set(config)
		print(send_config)