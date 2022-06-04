#! /usr/local/Python_envs/Python3/bin/python3
import ipaddress
from colorama import Fore,Style
ip_list = []
while True:
	try:
		# ip_input = ipaddress.ip_address(input(f"\n\n{'~'*50}\nEnter IP Address: "))
		ip_input = input(f"\n\n{'~'*50}\nEnter IP Address/list/exit: ")
		if ip_input == 'exit':
			print("Exiting the Script")
			exit()
		if ip_input == 'list':
			print(f"Current Assigned List is:{sorted(ip_list)}")
			continue
		else:
			ip_input= ipaddress.ip_address(ip_input)
		lan_subnet = ipaddress.ip_network("192.168.0.0/24")
		if ip_input not in ip_list:
			if ip_input in lan_subnet:
				ip_list.append(ip_input)
				print(f"{Fore.GREEN}{Style.BRIGHT}Value Accepted:  IP {ip_input}{Style.RESET_ALL} is added to the list ")
			else:
				print(f"{Fore.YELLOW}{Style.BRIGHT}Subnet mismatch.{Style.NORMAL} Enter IP in {Fore.CYAN}192.168.0.0/24 {Fore.YELLOW}Range{Style.RESET_ALL}")
		else:
			print("IP already exist")

	except ValueError:
		print(f"{Fore.RED}{Style.BRIGHT}Invalid IP{Style.RESET_ALL}")
