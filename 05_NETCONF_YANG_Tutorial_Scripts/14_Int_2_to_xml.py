#! /data/Python_envs/Python3/bin/python3

from ncclient import manager

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
		<interface><GigabitEthernet><name>2</name></GigabitEthernet></interface>
	</native>
</filter>"""

OUTPUT = RTR1_MGR.get_config('running', FILTER)
print (OUTPUT)

SAVE = open('int_2.xml', 'w')
SAVE.write(str(OUTPUT))
SAVE.close()
RTR1_MGR.close_session()
