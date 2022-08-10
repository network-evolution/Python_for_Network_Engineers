#! /usr/local/Python_envs/Python3/bin/python3
import sys
from netmiko import Netmiko
import datetime
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import SSHException
import threading
import re
from tabulate import tabulate
import ipaddress
int_pattern = re.compile(r"(\S+)\s+(([\d\\.]+)|unassigned)\s+\S+\s+\S+\s+(up|administratively down)\s+(\S+)")
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
ip_net_input = ipaddress.ip_network(input("Enter subnet/mask to match with:"))
def cisco_int_parser(device):
	now = datetime.datetime.now()
	print(f"Connecting to the device: {device['host']} at {now}")
	try:
		my_router = Netmiko(**device)
		print(f"Connected successfully to the device {device['host']}")
		print(f"{device['host']} prompt is:  {my_router.find_prompt()}")
		print(f"Executing show ip int brief in {device['host']}")

		show_ip_interface = my_router.send_command('show ip interface brief')
		# print(show_ip_interface)
		int_iter = int_pattern.finditer(show_ip_interface)
		int_list = list()
		for intr in int_iter:
			int_dict = dict()
			# print(intr.group(1), intr.group(2), intr.group(4))
			int_dict['int'], int_dict['ip'], int_dict['status'] = intr.group(1), intr.group(2), intr.group(4)
			# print(int_dict)
			int_list.append(int_dict)
		# print(int_list)
		print(f"\n\n {'#'*10} {device['host']} Interface Details {'#'*10}")
		print(tabulate(int_list, headers='keys', tablefmt="fancy_grid"))
		print(f"\n\n {'#' * 10} {device['host']} : Interface belongs to subnet {ip_net_input} are {'#' * 10}")
		for intr in int_list:
			try:
				ip = ipaddress.ip_network(intr['ip'])
				if ip_net_input.overlaps(ip):
					print(intr['int'], intr['ip'])
			except:
				continue
	except NetmikoAuthenticationException:
		print(f"Authentication Failed on {device['host']}")

	except NetmikoTimeoutException:
		print(sys.exc_info()[0])
		print(f"Connection Failure : {device['host']}")

	except SSHException:
		print(f"SSH Exception: {device['host']}")
	except:
		print(sys.exc_info()[0])
		print(f"Exception Occurred : {device['host']}")

def bkp_thread():
	bkp_thread_list = list()
	for device in device_list:
		bkp_thread = threading.Thread(target=cisco_int_parser, args=(device,))
		bkp_thread.start()
		bkp_thread_list.append(bkp_thread)
	for thread in bkp_thread_list:
		thread.join()
	print("#### Finished execution of the script ####")

bkp_thread()
# cisco_int_parser(lab_csr)


