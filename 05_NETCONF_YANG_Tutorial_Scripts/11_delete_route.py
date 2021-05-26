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
		<ip>
			<route>
				<ip-route-interface-forwarding-list operation='delete'>
					<prefix>10.10.20.0</prefix>
					<mask>255.255.255.0</mask>
					<fwd-list>
						<fwd>192.168.0.1</fwd>
					</fwd-list>
				</ip-route-interface-forwarding-list>
			</route>
		</ip>
	</native>
</config>"""

DATA = RTR1_MGR.edit_config(CONFIGURATION,  target = 'running')
print (DATA)
RTR1_MGR.close_session()
