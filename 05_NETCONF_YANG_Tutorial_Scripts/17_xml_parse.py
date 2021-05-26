#! /data/Python_envs/Python3/bin/python3

from ncclient import manager
import xml.etree.ElementTree as ET

RTR1_MGR = manager.connect(host='csr1.test.lab',
                    port=830,
                    username='admin',
                    password='admin',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

FILTER = """
<filter>
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<interface></interface>
	</native>
</filter>"""

OUTPUT = RTR1_MGR.get_config('running', FILTER)
#print (OUTPUT)
root = ET.fromstring(str(OUTPUT))
n = int(input("Enter Interface Number: "))
n = n-1 ;

int_number = list(root)[0][0][0][n][0].text
int_ip =     list(root)[0][0][0][n][1][0][0][0].text

print("Gigabiethernet " +int_number+ " - IP Address : " + int_ip)

RTR1_MGR.close_session()
