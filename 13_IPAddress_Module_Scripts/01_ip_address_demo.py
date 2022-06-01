#! /usr/local/Python_envs/Python3/bin/python3
import ipaddress

# ip_addr1 = ipaddress.ip_address(input("Enter IP:"))
ip_addr1 = ipaddress.ip_address('127.0.0.1')

print(f"IP Address provided is : {ip_addr1}")
print(type(ip_addr1))
print(dir(ip_addr1))

print(ip_addr1.max_prefixlen)
print(ip_addr1.reverse_pointer)

exp = ip_addr1.exploded
print(type(exp))

print(ip_addr1.is_multicast)
print(ip_addr1.is_private)
print(ip_addr1.is_global)
print(ip_addr1.is_link_local)
print(ip_addr1.is_loopback)

try:
	ip_addr2 = ipaddress.ip_address(input("Enter IP:"))
except ValueError:
	print("Invalid IP")