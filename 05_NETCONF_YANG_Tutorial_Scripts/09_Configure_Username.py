#! /data/Python_envs/Python3/bin/python3

from ncclient import manager

RTR1_MGR = manager.connect(host='csr1.test.lab',
                    port=830,
                    username='admin',
                    password='admin',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

CONFIGURATION = """
<config>
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<username>
			<name>netconf_test</name>
			<privilege>15</privilege>
			<secret>
				<encryption>0</encryption>
				<secret>password123</secret>
			</secret>
		</username>
	</native>
</config>"""

DATA = RTR1_MGR.edit_config(CONFIGURATION,  target = 'running')
print (DATA)
RTR1_MGR.close_session()
