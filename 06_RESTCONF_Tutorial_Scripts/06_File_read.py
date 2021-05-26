#! /usr/local/Python_envs/Python3/bin/python3
import json

with open('output.json') as file:

    interfaces = json.load(file)['ietf-interfaces:interfaces']['interface']

#print (interfaces)

for interface in interfaces:
#    print(interface['enabled'])
    if bool(interface['ietf-ip:ipv4']):
#        print(bool(interface['ietf-ip:ipv4']['address']))
        print (interface['name']+' '+ interface['ietf-ip:ipv4']['address'][0]['ip'])

for interface in interfaces:
#    print(interface1['enabled'])
    if bool(interface['enabled']) :
        print ('Enabled Int is '+ interface['name'])

# for interface in interfaces:
#     print (bool(interface['ietf-ip:ipv4']))
#     if bool(interface['ietf-ip:ipv4']):
#         print ('Interface '+ interface['name'].ljust(20) + \
#         ' IP Address: '+ interface['ietf-ip:ipv4']['address'][0]['ip'])
#     else:
#         print ('Interface '+ interface['name'].ljust(20) + ' No ip configured ')
