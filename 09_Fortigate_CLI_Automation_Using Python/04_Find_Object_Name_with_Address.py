#! /usr/local/Python_envs/Python3/bin/python3

from netmiko import Netmiko
import re

search =input("Enter IP to Search: ")
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
match = False
for ip_reference in ip_references:
	print(ip_reference.group(1))
	match = True
if not match:
	print("No address Object Found")

# print(output)

