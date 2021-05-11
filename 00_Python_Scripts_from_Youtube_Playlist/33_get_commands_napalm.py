import json
from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.67.47', 'admin', 'admin')
device.open()

print ('#######\nGET FACTS\n#######')
facts = device.get_facts()
print (json.dumps(facts,sort_keys=True,  indent=4))

print ('#######\nGET ARP\n#######')
arptable = device.get_arp_table()
print (json.dumps(arptable,sort_keys=True,  indent=4))

print ('#######\nGET CONFIG\n#######')
config = device.get_config()
print (json.dumps(config,sort_keys=True,  indent=4))

print ('#######\nGET ENVIRONMENT\n#######')
environment = device.get_environment()
print (json.dumps(environment,sort_keys=True,  indent=4))

print ('#######\nGET INTERFACES\n#######')
interfaces = device.get_interfaces()
print (json.dumps(interfaces,sort_keys=True,  indent=4))

print ('#######\nGET INTERFACE COUNTERS\n#######')
interfacecounter = device.get_interfaces_counters()
print (json.dumps(interfacecounter,sort_keys=True,  indent=4))

print ('#######\nPING\n#######')
pingtest = device.ping('192.168.67.254')
print (json.dumps(pingtest,sort_keys=True,  indent=4))

print ('#######\nTRACEROUTE\n#######')
pingtest = device.traceroute('10.10.102.89')
print (json.dumps(pingtest,sort_keys=True,  indent=4))

device.close()

