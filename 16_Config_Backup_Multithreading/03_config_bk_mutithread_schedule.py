#! /usr/local/Python_envs/Python3/bin/python3
import sys
import time

from netmiko import Netmiko
import datetime
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import SSHException
import threading
import schedule

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

device_list = [lab_csr, devnet_csr,lab_ios1,lab_ios2]
def cisco_backup(device):
	now = datetime.datetime.now()
	print(f"Connecting to the device: {device['host']} at {now}")
	try:
		my_router = Netmiko(**device)
		print(f"Connected successfully to the device {device['host']}")
		print(f"{device['host']} prompt is:  {my_router.find_prompt()}")
		print(f"Executing show run in {device['host']}")

		show_run = my_router.send_command('show run')

		now = datetime.datetime.now().replace(microsecond=0)
		current_conf_file = f"{now}_{device['host']}.txt"
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

def bkp_thread():
	bkp_thread_list = list()
	for device in device_list:
		bkp_thread = threading.Thread(target=cisco_backup, args=(device,))
		bkp_thread.start()
		bkp_thread_list.append(bkp_thread)
	for thread in bkp_thread_list:
		thread.join()
	print("#### Finished execution of the script ####")

schedule.every(15).seconds.do(bkp_thread)

while True:
	schedule.run_pending()
	time.sleep(1)


