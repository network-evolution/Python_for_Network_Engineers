#! /usr/local/Python_envs/Python3/bin/python3
import paramiko
import time
import re

version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_no_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')

lab_csr = {
	'host': 'csr1.test.lab',
	'username': 'admin',
	'password': 'admin'
}
devnet_csr = {
	'host': 'ios-xe-mgmt-latest.cisco.com',
	'username': 'developer',
	'password': 'C1sco12345'
}

def cisco_parse_version(host,username,password):
	try:
		print(f"\n{'#' * 55}\nConnecting to the Device {host}\n{'#' * 55} ")
		SESSION = paramiko.SSHClient()
		SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		SESSION.connect(host, port=22,
						username=username,
						password=password,
						look_for_keys=False,
						allow_agent=False)

		DEVICE_ACCESS = SESSION.invoke_shell()
		DEVICE_ACCESS.send(b'term length 0\n')
		DEVICE_ACCESS.send(b'show ver\n')
		time.sleep(1)
		output = (DEVICE_ACCESS.recv(65000).decode('ascii'))

		version_match = version_pattern.search(output)
		version_result = ('IOS Version'.ljust(18)+': '+version_match.group(1))
		print(version_result)

		model_match = model_pattern.search(output)
		model_result = ('Model '.ljust(18)+': '+model_match.group(1))
		print(model_result)

		serial_no_match = serial_no_pattern.search(output)
		serial_no_result = ('Serial Number '.ljust(18)+': '+serial_no_match.group(1))
		print(serial_no_result)

		uptime_match = uptime_pattern.search(output)
		host_name_result = ('Host Name '.ljust(18)+': '+uptime_match.group(1))
		print(host_name_result)

		up_time_result = ('Device Uptime '.ljust(18)+': '+uptime_match.group(2))
		print(up_time_result)

		print(f"\n{'#' * 55}\nFinished Executing Script\n{'#' * 55} ")
		SESSION.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failed")
	except AttributeError:
		print("Parsing Error, Please check the command")
	except:
		print("Can not connect to Device")
cisco_parse_version(**devnet_csr)