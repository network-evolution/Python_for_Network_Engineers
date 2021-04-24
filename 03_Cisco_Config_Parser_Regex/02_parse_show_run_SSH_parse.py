#! /usr/local/Python_envs/Python3/bin/python3
import paramiko
import time
from getpass import getpass
import re
from pprint import pprint

hostname_pattern = re.compile(r'hostname (\S+)')
domainname_pattern = re.compile(r'ip domain name (.+)')
pid_pattern = re.compile(r'license udi pid (\w+) sn (\S+)')
netconf_pattern = re.compile(r"netconf-yang\r\n")
username_pattern = re.compile(r'username (\S+) privilege (\d{2})')
interface_pattern = re.compile(r'interface (\S+[.]?\d*)\r\n.+?\r?\n?\s?ip address ([\d\.]+) ([\d\.]+)')
interface_prop_pattern = re.compile(r'interface (?P<name>\S+[.]?\d*)\r\n\s?.+?\r?\n?\s?ip address (?P<ip_aadress>[\d\.]+) (?P<mask>[\d\.]+)')
default_route_pattern = re.compile(r'ip route 0.0.0.0 0.0.0.0.+?([\d.]+)\r\n')
static_route_pattern = re.compile(r'ip route (?P<dst_subnet>[^0][\d\.]+) (?P<mask>[^0][\d\.]+) (?P<next_hop>[\d\.]+)')

lab_csr = {
	'host': '192.168.0.50',
	'username': 'admin',
	'password': 'admin'
}
devnet_csr = {
	'host': 'ios-xe-mgmt-latest.cisco.com',
	'username': 'developer',
	'password': 'C1sco12345'
}

def cisco_parse_conf(host,username,password):
	try:
		print(f"\n{'#' * 55}\nConnecting to the Device {host}\n{'#' * 55} ")
		SESSION = paramiko.SSHClient()
		SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		SESSION.connect(host, port=22,
						username=username,
						password=password,
						look_for_keys=False,
						allow_agent=False)

		DEVICE_ACCESS = SESSION.invoke_shell()
		DEVICE_ACCESS.send(b'term length 0\n')
		DEVICE_ACCESS.send(b'show run\n')
		time.sleep(2)
		output = (DEVICE_ACCESS.recv(65000).decode('ascii'))

		hostname_match = hostname_pattern.search(output)
		print('Hostname'.ljust(18) + ': ' + str(hostname_match.group(1)))

		domainname_match = domainname_pattern.search(output)
		print('Domain Name'.ljust(18) + ': ' + str(domainname_match.group(1)))

		pid_match = pid_pattern.search(output)
		print('PID'.ljust(18) + ': ' + str(pid_match.group(1)))
		print('SN'.ljust(18) + ': ' + str(pid_match.group(2)))

		netconf_match = netconf_pattern.search(output)
		if netconf_match:
			print('Netconf Enabled'.ljust(18) + ': Yes')
		else:
			print('Netconf Enabled'.ljust(18) + ': No')

		username_iter = username_pattern.finditer(output)
		user_list = []
		for user in username_iter:
			user_list.append(user.group(1))
		print('List of Users'.ljust(18) + ': ' + str(user_list))

		default_route_match = default_route_pattern.search(output)
		if default_route_match:
			print('\n'+'Default Gateway'.ljust(18) + ': ' + default_route_match.group(1))
		else:
			print('\n'+'Default Gateway'.ljust(18) + ': Not available')

		static_route_iter = static_route_pattern.finditer(output)
		static_route_list = []
		for static_route in static_route_iter:
			static_route_list.append(static_route.groupdict())
		print('Static  Routes'.ljust(18) + ': ' + str(static_route_list))

		interface_iter = interface_pattern.finditer(output)

		interface_list = []
		for interface in interface_iter:
			interface_list.append(interface.group(1))

		print('\nInterfaces with IP'.ljust(18) + ': ' + str(interface_list))

		interface_prop = interface_prop_pattern.finditer(output)
		interface_prop_list = []
		for interface_conf in interface_prop:
			interface_prop_list.append(interface_conf.groupdict())

		print('Int Conf Details'.ljust(18) + ': ' )
		pprint(interface_prop_list,indent=10)
		SESSION.close()
	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failed")
	except AttributeError:
		print('Parsing Error, Check the command')
	except:
		print('Can not connect to the Device')

cisco_parse_conf(**devnet_csr)