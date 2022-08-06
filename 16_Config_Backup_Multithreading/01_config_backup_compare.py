#! /usr/local/Python_envs/Python3/bin/python3
import sys

from netmiko import Netmiko
import datetime
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import SSHException
import threading

lab_csr = {'host': '192.168.0.63',
		   'username': 'admin',
		   'password': 'admin',
		   'device_type': 'cisco_ios'}

devnet_csr = {'host': 'ios-xe-mgmt-latest.cisco.com',
		   'username': 'developer',
		   'password': 'C1sco12345',
		   'device_type': 'cisco_ios'}

lab_ios1 = {'host': '192.168.0.61',
		   'username': 'admin',
		   'password': 'admin',
		   'device_type': 'cisco_ios'}

lab_ios2 = {'host': '192.168.0.62',
		   'username': 'admin',
		   'password': 'admin',
		   'device_type': 'cisco_ios'}


try:
	my_router = Netmiko(**lab_csr)
	print(f"Connected successfully to the device {lab_csr['host']}")
	print(f"{lab_csr['host']} prompt is:  {my_router.find_prompt()}")
	print(f"Executing show run in {lab_csr['host']}")

	show_run = my_router.send_command('show run')

	now = datetime.datetime.now().replace(microsecond=0)
	current_conf_file = f"{now}_{lab_csr['host']}.txt"
	print(f"Saving the output to file: {current_conf_file}")
	with open(current_conf_file, 'w') as my_data:
		my_data.write(show_run)

except NetmikoAuthenticationException:
	print("Authentication Failed")

except NetmikoTimeoutException:
	print(sys.exc_info()[0])
	print("Connection Failure")

except SSHException:
	print("SSH Exception")
except:
	print(sys.exc_info()[0])
	print("Exception Occurred")


