

import json
from napalm import get_network_driver

cisco = ['192.168.67.47', '192.168.67.43']
arista = ['192.168.67.30']

def getfacts(ips,vendor,mode ):
    for ip in ips:
        print ('Connecting to'+ vendor +'device ' + str(ip))
        driver = get_network_driver(mode)
        device = driver(ip, 'admin', 'admin')
        device.open()
        facts = device.get_facts()
        print (json.dumps(facts,sort_keys=True,  indent=4))
        print (vendor +'Device ' + str(ip) + ' software version is ' + facts['os_version'])
        device.close()

getfacts(cisco,' cisco ' ,'ios')
getfacts(arista,' arista ' , 'eos')



