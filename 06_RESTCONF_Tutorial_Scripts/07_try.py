#! /usr/local/Python_envs/Python3/bin/python3
import json

with open('output.json') as file:
    interfaces = json.load(file)['ietf-interfaces:interfaces']['interface']

print (f'total number of interface are {len(interfaces)}\n')
#######################1 ###################################################
# for intnames in interfaces:
#     print (f"{intnames['name']} {intnames['ietf-ip:ipv4']['address']}")
#
# print (interfaces)
######################## 2 ##################################################
for interface in interfaces:
    if interface.get('ietf-ip:ipv4'):
        print(f"{interface['name'].ljust(20)} {interface['ietf-ip:ipv4']['address'][0]['ip']}")
    else:
        print(f"{interface['name'].ljust(20)} No IP Adress")

######################## 2 ##################################################

# for interface in interfaces:
#     print (bool(interface['ietf-ip:ipv4']))
#     if bool(interface['ietf-ip:ipv4']):
#         print ('Interface '+ interface['name'].ljust(20) + \
#         ' IP Address: '+ interface['ietf-ip:ipv4']['address'][0]['ip'])
#     else:
#         print ('Interface '+ interface['name'].ljust(20) + ' No ip configured ')
