#! /usr/local/Python_envs/Python3/bin/python3
'''
ssh-copy-id evolve@192.168.0.14
ssh-keygen
'''
# ######################################################################
# from getpass import getpass
# import paramiko
# import os
# import time
# ip = '192.168.0.14'
# # username = (input("Enter Username(Default 'admin'): ") or "dev")
# # print(f"Username is {username}")
# # password = (input("Enter Password: ") or "Devan@555")
# # password = (getpass("Enter Password : ") or "Devan@555")
#
# username = 'evolve'
# password = 'evolve@123'
# session = paramiko.SSHClient()
# # session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_system_host_keys()
# # session.set_missing_host_key_policy(paramiko.RejectPolicy())
# # session.set_missing_host_key_policy(paramiko.WarningPolicy())
# # session.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# # session.load_host_keys(filename='/home/dev/.ssh/known_hosts')
#
# session.connect(hostname= ip,
#                 username= username,
#                 password= password,
#                 look_for_keys=False,
#                 allow_agent=False)
#
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

######################################################################
'''with plain privatekey'''
# from getpass import getpass
# import paramiko
# import os
# import time
# ip = '192.168.0.14'
# username = 'evolve'
# password = 'evolve@123'
# key_location = '/home/dev/.ssh/id_rsa1'
# session = paramiko.SSHClient()
# # session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_system_host_keys()
# # session.set_missing_host_key_policy(paramiko.RejectPolicy())
# # session.set_missing_host_key_policy(paramiko.WarningPolicy())
# # session.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# # session.load_host_keys(filename='/home/dev/.ssh/known_hosts')
#
# session.connect(hostname= ip,
#                 username= username,
#                 key_filename=key_location,
#                 # password= password,
#                 # look_for_keys=True,
#                 # allow_agent=False
#                 )
#
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
################################################################

'''with plain privatekey'''
from getpass import getpass
import paramiko
import os
import time
ip = '192.168.0.14'
username = 'evolve'
password = 'evolve@123'

priv_key_pass = getpass("Enter Private Key Password : ")
key_file = '/home/dev/.ssh/id_rsa2'
key_pass = paramiko.RSAKey.from_private_key_file(key_file, priv_key_pass)

session = paramiko.SSHClient()
# session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.load_system_host_keys()
# session.set_missing_host_key_policy(paramiko.RejectPolicy())
# session.set_missing_host_key_policy(paramiko.WarningPolicy())
# session.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# session.load_host_keys(filename='/home/dev/.ssh/known_hosts')

session.connect(hostname= ip,
                username= username,
                # key_filename=key_file,
                pkey = key_pass,
                # password= password,
                look_for_keys=True,
                # allow_agent=False
                )

commands = ['ls', 'pwd','llsdsd','who','hostname']

for command in commands:
    print(f"{'#'*10} Executing the Command : {command} {'#'*10}")
    stdin1, stdout1, stderr1 = session.exec_command(command)
    time.sleep(.5)
    print(stdout1.read().decode())
    err = stderr1.read().decode()
    if err:
        print(err)

session.close()

print(f"{'#'*10} COMMAND EXECUTION FINISHED {'#'*10}")
################################################################
