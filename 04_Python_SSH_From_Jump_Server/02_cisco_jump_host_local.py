#! /usr/local/Python_envs/Python3/bin/python3

from netmiko import Netmiko
from netmiko import redispatch,ssh_exception
import time

cisco_jump_host_ip = '192.168.0.49'
cisco_jump_host_user = 'admin'
cisco_jump_host_password = 'admin'

router_ip = '192.168.0.50'
router_user = 'admin'
router_password = 'admin'

print(f"\n{'#'*50}\n1. Connecting to the Cisco Jump host\n{'#'*50}")
try:
	net_connect = Netmiko(device_type='cisco_ios',
								 host = cisco_jump_host_ip,
								 username = cisco_jump_host_user,
								 password = cisco_jump_host_password)

	print(net_connect.find_prompt())
	print(f"\n{'*'*10}Connected to the Jump host{'*'*10}")
	print(f"\n{'~'*50}\n2. Connecting to the Dest Router\n{'~'*50}")
	print(net_connect.find_prompt(),end='')
	net_connect.write_channel(f'ssh -l {router_user} {router_ip}\n')
	time.sleep(2)
	output = net_connect.read_channel()
	print(output)
	if 'Password' in output:
		print("**Received Password Prompt, Entering password**")
		net_connect.write_channel(router_password+'\n')
		time.sleep(2)

		print(f"\n{'~'*50}\nDestination Device Prompt\n{'~'*50}\n")
		print(net_connect.find_prompt())
		cmds = ['show ip int brie','show ip route','show users']

		redispatch(net_connect,device_type='cisco_ios')
		for cmd in cmds:
			print(f"\n{'~'*50}\nIn {net_connect.find_prompt()} Executing the Command: {cmd}\n{'~'*50}")
			router_output = net_connect.send_command(cmd)
			print(router_output)
	else:
		print("Unable to get output from the End Device")

except ssh_exception.AuthenticationException:
	print("Jump host Auth failed")
except ssh_exception.NetmikoTimeoutException:
	print("Jump Host not reachable")

print(f"\n{'#'*50}\nFinished Executing Script\n{'#'*50}")