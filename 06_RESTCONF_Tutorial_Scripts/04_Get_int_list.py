#! /usr/local/Python_envs/Python3/bin/python3
import requests
import getpass

username = input('Enter Username :' )
password = getpass.getpass('Enter Password :' )
ip = "ios-xe-mgmt-latest.cisco.com"
port = "9443"

headers = {"Accept" : "application/yang-data+json"}

get_interface_url = "https://"+ip+":"+port+"/restconf/data/ietf-interfaces:interfaces"

requests.packages.urllib3.disable_warnings()
response = requests.get(get_interface_url, headers=headers, auth=(username, password), verify=False)
print(response.text)
#print (response)
interfaces = response.json()['ietf-interfaces:interfaces']['interface']
#print(interfaces)

for interface in interfaces:
    if bool(interface['ietf-ip:ipv4']): #check if IP address is available
#      print(f"{interface['name']} -- {interface['description']} -- {interface['ietf-ip:ipv4']['address'][0]['ip']}")
#        print(f"{interface['name']}  {interface['ietf-ip:ipv4']['address'][0]['ip']}")
#        print(f"{interface['name']} {interface['ietf-ip:ipv4']['address'][0]['ip']}")
        print ('Interface '+ interface['name'].ljust(20) + \
        ' IP Address: '+ interface['ietf-ip:ipv4']['address'][0]['ip'])
    else:
        print ('Interface '+ interface['name'].ljust(20) + ' No ip configured ')
#https://blog.wimwauters.com/networkprogrammability/2020-04-04_restconf_python/
