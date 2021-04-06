#! /usr/local/Python_envs/Python3/bin/python3

from csv import reader
from pprint import pprint
import paramiko
import time

conf_dict = {}
with open("01_config_in_row.csv", "r") as csv_file:
	csv_content = reader(csv_file)
	for device in csv_content:
		if not device[0]:
			continue
		if device[0] not in conf_dict.keys():
			conf_dict[device[0]] = []
		n = len(device)
		for conf in range(1,n):
			if not device[conf]:
				continue
			conf_dict[device[0]].append(device[conf])

session = paramiko.SSHClient()
session.load_system_host_keys()

key_file = paramiko.RSAKey.from_private_key_file("/home/evolve/.ssh/id_rsa")
for ip in conf_dict.keys():
	try:
		print(f"\n{'#' * 50}\nConnecting to the Device {ip}\n{'#' * 50} ")
		session.connect(hostname=ip,
						username='admin1',
						# password='admin',
						pkey=key_file,
						)
		DEVICE_ACCESS = session.invoke_shell()
		print(f"\nExecuting Commands are\n{'~'*22}\n{conf_dict[ip]}")
		for conf in conf_dict[ip]:
			DEVICE_ACCESS.send(conf+'\n')
			time.sleep(1)
			output = DEVICE_ACCESS.recv(65000)
			print (output.decode('ascii'),end='')
			time.sleep(.5)
		session.close()
	except :
		print('Can not connect to the device')

print (f"\n{'#' * 50}\nCOMMAND EXECUTION COMPLETED\n{'#' * 50}\n")
