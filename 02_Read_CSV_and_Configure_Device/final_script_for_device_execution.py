#! /usr/local/Python_envs/Python3/bin/python3

from csv import DictReader
from pprint import pprint
import paramiko
import time

conf_dict = {}
with open ('02_config_in_column.csv','r') as csv_file:
	csv_content = DictReader(csv_file)
	column_names = csv_content.fieldnames
	# print(column_names)
	for row in csv_content:
		for column_name in column_names:
			if not column_name:
				continue
			if not row[column_name]:
				continue
			if column_name not in conf_dict.keys():
				conf_dict[column_name]= []
			conf_dict[column_name].append(row[column_name])

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


