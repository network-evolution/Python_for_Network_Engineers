#! /usr/local/Python_envs/Python3/bin/python3
from netmiko import Netmiko

fw_01 = {'host': '192.168.0.21',
		 'username':'admin',
		 'password':'Password@123',
		 'device_type': 'fortinet'
	}
print(f"{'#'*20} Connecting to the Device {'#'*20}")
net_connect = Netmiko(**fw_01)
print(f"{'#'*20} Connected {'#'*20}")
# print(net_connect.find_prompt())

# command = 'show full-configuration'
# full_config = net_connect.send_command(command)
# print(full_config)

config = ['config firewall address',
		  'edit IP_101',
		  'set type ipmask',
		  'set subnet 192.168.0.101/32',
		  'end'
]
send_config = net_connect.send_config_set(config)

print(send_config)




