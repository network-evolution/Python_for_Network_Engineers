#! /usr/local/Python_envs/Python3/bin/python3
import ipaddress

# ip_subnet = ipaddress.ip_network(input("Enter Subnet:"))
ip_subnet = ipaddress.ip_network('192.168.0.0/24')
print(dir(ip_subnet))

print(ip_subnet.network_address) #192.168.0.0
print(ip_subnet.broadcast_address)#192.168.0.255
print(ip_subnet.netmask)#255.255.255.0
print(ip_subnet.num_addresses)#256
print(ip_subnet.prefixlen)#24

print(ip_subnet.exploded)# str
print(ip_subnet.hostmask)# 0.0.0.255
print(ip_subnet.reverse_pointer)#0/24.0.168.192.in-addr.arpa
print(ip_subnet.with_prefixlen)#192.168.0.0/24
print(ip_subnet.version)#24
print(ip_subnet.max_prefixlen)#32

# k= ip_subnet.hosts()
# for i in k:
# 	print(i)

########################################
#
# print(ip_subnet.overlaps(ipaddress.ip_network('192.168.0.5/32')))# True
#
# server1 = ipaddress.ip_network('192.168.0.10') # True
# print(ip_subnet.overlaps(server1))
#
# #########################################
new_exclude = ipaddress.ip_network('192.168.0.5')
l1 = ip_subnet.address_exclude(new_exclude)
for ip in l1:
	print(ip)

