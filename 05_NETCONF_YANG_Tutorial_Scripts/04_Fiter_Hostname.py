#! /data/Python_envs/Python3/bin/python3

from ncclient import manager

RTR1_MGR = manager.connect(host='192.168.67.52',
                    port=830,
                    username='admin',
                    password='admin',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

FILTER = """
<filter>
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<hostname></hostname>
	</native>
</filter>
"""

print (RTR1_MGR.get_config('running', FILTER))

RTR1_MGR.close_session()
