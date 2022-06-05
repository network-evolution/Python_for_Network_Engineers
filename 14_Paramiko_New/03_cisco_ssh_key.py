#! /usr/local/Python_envs/Python3/bin/python3

import paramiko
from getpass import getpass
import time

host = "csr1.test.lab"
username = 'admin1'
# password = 'admin'
# password = getpass("Enter password :")

session = paramiko.SSHClient()

# session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_host_keys('/home/evolve/.ssh/known_hosts')
# session.set_missing_host_key_policy(paramiko.WarningPolicy())
session.load_system_host_keys()

key_pass = getpass("Enter Private Key Password:")
key_file = paramiko.RSAKey.from_private_key_file("/home/evolve/.ssh/id_01", key_pass)

# key_file = paramiko.RSAKey.from_private_key_file("/home/evolve/.ssh/id_rsa")

session.connect(hostname=host,
				username=username,
				# password=password,
				pkey=key_file,
				allow_agent=False,
				look_for_keys=False
				)

commands =['show ver']

for command in commands:
	print(f"{'#'*10} Executing the Command : {command} {'#'*10} ")
	stdin, stdout, stderr = session.exec_command(command)
	time.sleep(.5)
	print(stdout.read().decode())
	err = stderr.read().decode()
	if err:
		print(err)
session.close()


