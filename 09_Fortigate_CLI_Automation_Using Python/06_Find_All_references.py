#! /usr/local/Python_envs/Python3/bin/python3

from netmiko import Netmiko
import re

search =input("Enter Object Name: ")

fw_01 = {'host': '192.168.0.21',
		 'username':'admin',
		 'password':'Password@123',
		 'device_type': 'fortinet'
		 }
print(f"{'#'*20} Connecting to the Device {'#'*20}")
net_connect = Netmiko(**fw_01)
print(f"{'#'*20} Connected {'#'*20}")


command = f'diagnose sys cmdb refcnt show firewall.address:name {search}'
output = net_connect.send_command(command)

match = False
if output:
	match = True
	print(output)
else:
	print("Not Reference found")


