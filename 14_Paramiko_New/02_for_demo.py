#! /usr/local/Python_envs/Python3/bin/python3

# ######################################################################
'''
With plain privatekey
'''
# import paramiko
# import time
# ip = 'ubuntu2.test.lab'
# username = 'user1'
# key_file = paramiko.RSAKey.from_private_key_file("/home/evolve/.ssh/03_id")
# session = paramiko.SSHClient()
# session.load_system_host_keys()
#
# session.connect(hostname= ip,
#                 username= username,
#                 # password= password,
# 				pkey=key_file,
#                 look_for_keys=False,
# 				allow_agent=False
# 				)
# #
# commands = ['ls', 'pwd','llsdsd','who','hostname']
#
# for command in commands:
#     print(f"{'#'*10} Executing the Command : {command} {'#'*10}")
#     stdin1, stdout1, stderr1 = session.exec_command(command)
#     time.sleep(.5)
#     print(stdout1.read().decode())
#     err = stderr1.read().decode()
#     if err:
#         print(err)
#
# session.close()
# ################################################################
'''
With enc privatekey
'''

# import paramiko
# import time
# from getpass import getpass
# ip = 'ubuntu2.test.lab'
# username = 'user1'
#
# priv_key_pass = getpass("Enter Private Key Password : ")
# key_file = '/home/evolve/.ssh/01_id'
# key_pass = paramiko.RSAKey.from_private_key_file(key_file, priv_key_pass)
#
# session = paramiko.SSHClient()
# session.load_system_host_keys()
#
# session.connect(hostname= ip,
# 				username= username,
# 				# password= password,
# 				# pkey = key_pass,
# 				look_for_keys=False,
# 				)
# #
# commands = ['ls', 'pwd','llsdsd','who','hostname']
#
# for command in commands:
# 	print(f"{'#'*10} Executing the Command : {command} {'#'*10}")
# 	stdin1, stdout1, stderr1 = session.exec_command(command)
# 	time.sleep(.5)
# 	print(stdout1.read().decode())
# 	err = stderr1.read().decode()
# 	if err:
# 		print(err)
#
# session.close()
# # ################################################################
'''
Cisco
ip ssh pubkey-chain
username admin1
key-string

fold -b -w 64 file
ssh-keygen -f file -l
ssh-keygen -E md5 -lf id_rsa.pub
'''
#Cisco
############################################################
import paramiko
import time
ip = 'csr1.test.lab'
username = 'admin'
password = 'admin'
# key_file = paramiko.RSAKey.from_private_key_file("/home/evolve/.ssh/03_id")
session = paramiko.SSHClient()
session.load_system_host_keys()

session.connect(hostname= ip,
				username= username,
				password= password,
				# pkey=key_file,
				look_for_keys=False,
				)
#
commands = ['show ip route']

for command in commands:
	print(f"{'#'*10} Executing the Command : {command} {'#'*10}")
	stdin1, stdout1, stderr1 = session.exec_command(command)
	time.sleep(.5)
	print(stdout1.read().decode())
	err = stderr1.read().decode()
	if err:
		print(err)

session.close()
##########################################################################