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
<interfaces
	xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
	<interface>
		<name>GigabitEthernet2</name>
		<type
			xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd

		</type>
		<enabled>true</enabled>
		<ipv4
			xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
			<address>
				<ip>22.22.22.2</ip>
				<netmask>255.255.255.0</netmask>
			</address>
		</ipv4>
		<ipv6
			xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
		</ipv6>
	</interface>
</interfaces>
</config>"""

DATA = RTR1_MGR.edit_config(CONFIGURATION,  target = 'running')
print (DATA)
RTR1_MGR.close_session()
