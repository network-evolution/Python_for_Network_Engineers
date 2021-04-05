#! /usr/local/Python_envs/Python3/bin/python3
import re
from pprint import pprint

hostname_pattern = re.compile(r'hostname (\S+)')
domainname_pattern = re.compile(r'ip domain name (.+)')
pid_pattern = re.compile(r'license udi pid (\w+) sn (\S+)')
netconf_pattern = re.compile(r"netconf-yang\n")
username_pattern = re.compile(r'username (\S+) privilege (\d{1,2})')
interface_pattern = re.compile(r'interface (\S+)\n.+?\n?\s?ip address ([\d\.]+) ([\d\.]+)')
interface_prop_pattern = re.compile(r'interface (?P<name>\S+)\n.+?\n?\s?ip address (?P<ip_address>[\d\.]+) (?P<mask>[\d\.]+)')
default_route_pattern = re.compile(r'ip route 0.0.0.0 0.0.0.0.+?([\d.]+)\n')
static_route_pattern = re.compile(r'ip route (?P<dst_subnet>[^0][\d\.]+) (?P<mask>[^0][\d\.]+) (?P<next_hop>[\d\.]+)')

with open('02_show_run_output.txt','r') as file:
	output = file.read()

	hostname_match = hostname_pattern.search(output)
	print('Hostname'.ljust(18)+': '+str(hostname_match.group(1)))

	domainname_match = domainname_pattern.search(output)
	print('Domain Name'.ljust(18)+': '+str(domainname_match.group(1)))

	pid_match = pid_pattern.search(output)
	print('PID'.ljust(18)+': '+str(pid_match.group(1)))
	print('SN'.ljust(18)+': '+str(pid_match.group(2)))

	netconf_match = netconf_pattern.search(output)
	if netconf_match:
		print('Netconf Enabled'.ljust(18)+': Yes')
	else :
		print('Netconf Enabled'.ljust(18)+': No')

	username_iter = username_pattern.finditer(output)
	user_list =[]
	for user in username_iter:
		user_list.append(user.group(1))
	print('List of Users'.ljust(18)+': '+ str(user_list))


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

