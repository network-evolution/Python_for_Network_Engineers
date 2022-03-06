#! /usr/local/Python_envs/Python3/bin/python3

from netmiko import Netmiko
import re

search =input("Enter IP to search: ")
ip_objects = []
ip_pattern = re.compile(r"edit (.+)")

fw_01 = {'host': '192.168.0.21',
		 'username':'admin',
		 'password':'Password@123',
		 'device_type': 'fortinet'
		 }
print(f"{'#'*20} Connecting to the Device {'#'*20}")
net_connect = Netmiko(**fw_01)
print(f"{'#'*20} Connected {'#'*20}")


command = f'show firewall address | grep -f {search}'
output = net_connect.send_command(command)

ip_references = ip_pattern.finditer(output)

for ip_reference in ip_references:
	ip_objects.append(ip_reference.group(1))
print(f"{'#'*20} Address Objects are{'#'*20}")
print(ip_objects)

for ip_object in ip_objects:
	print(f"{'~'*20} Reference for {ip_object}{'~'*20}")
	command = f'diagnose sys cmdb refcnt show firewall.address:name {ip_object}'
	output = net_connect.send_command(command)
	print(output)




