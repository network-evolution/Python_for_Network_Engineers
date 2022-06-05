#! /usr/local/Python_envs/Python3/bin/python3

###################################################
# try:
#     k = int(input("Enter Username: "))
#     print(k)
#     print(type(k))
#
# except ValueError as val_ex:
#     print(f"Error Class: {val_ex.__class__}")
#     # raise
#     print(f"Error Message : {val_ex}")
###################################################
'''paramiko Invoke_shell'''
# from getpass import getpass
# import paramiko
# import os
# import time
# ip = '127.0.0.1'
# username = (input("Enter Username(Default 'admin'): ") or "dev")
# print(f"Username is {username}")
# password = (input("Enter Password: ") or "Devan@555")
# # password = (getpass("Enter Password : ") or "Devan@555")
#
# session = paramiko.SSHClient()
# # session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_system_host_keys()
# # session.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# # session.load_host_keys(filename='/home/dev/.ssh/known_hosts')
#
# session.connect(hostname= ip,
#                 username= username,
#                 password= password,
#                 look_for_keys=False,
#                 allow_agent=False)
#
# device_access = session.invoke_shell()
# device_access.send(b'ls\n')
# time.sleep(.5)
# output = device_access.recv(65000)
# print(output.decode())
######################################################################

'''
sudo vi /etc/ssh/ssh_config
vi ~/.ssh/known_hosts
ssh-keygen -H -F 127.0.0.1
'''
from getpass import getpass
import paramiko
import os
import time
host = 'ubuntu2.test.lab'
username = (input("Enter Username(Default 'admin'): ") or "user1")
print(f"Username is {username}")
password = (input("Enter Password: ") or "evolve@123")
# password = (getpass("Enter Password : ") or "Devan@555")

session = paramiko.SSHClient()
# session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.load_system_host_keys()
# session.set_missing_host_key_policy(paramiko.RejectPolicy())
# session.set_missing_host_key_policy(paramiko.WarningPolicy())
# session.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# session.load_host_keys(filename='/home/dev/.ssh/known_hosts')

session.connect(hostname= host,
                username= username,
                password= password,
                look_for_keys=False,
                allow_agent=False)

commands = ['ls /', 'pwd','sdfg','echo $USER','hostname']

for command in commands:
    print(f"{'#'*10} Executing the Command : {command} {'#'*10}")
    stdin1, stdout1, stderr1 = session.exec_command(command)
    time.sleep(.5)
    print(stdout1.read().decode())
    err = stderr1.read().decode()
    if err:
        print(err)

session.close()
################################################################
# =======
# '''paramiko send_command'''

# from getpass import getpass
# import paramiko
# import os
# import time
# ip = '127.0.0.1'
# username = (input("Enter Username(Default 'admin'): ") or "dev")
# print(f"Username is {username}")
# password = (input("Enter Password: ") or "Devan@555")
# # password = (getpass("Enter Password : ") or "Devan@555")
#
# session = paramiko.SSHClient()
# # session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_system_host_keys()
# # session.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# # session.load_host_keys(filename='/home/dev/.ssh/known_hosts')
#
# session.connect(hostname= ip,
#                 username= username,
#                 password= password,
#                 look_for_keys=False,
#                 allow_agent=False)
#
# commands = ['ls', 'pwd','llsdsd']
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

'''paramiko send_command'''
from getpass import getpass
import paramiko
import os
import time
ip = '127.0.0.1'
username = (input("Enter Username(Default 'admin'): ") or "dev")
print(f"Username is {username}")
password = (input("Enter Password: ") or "Devan@555")
# password = (getpass("Enter Password : ") or "Devan@555")

session = paramiko.SSHClient()
# session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.load_system_host_keys()
# session.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# session.load_host_keys(filename='/home/dev/.ssh/known_hosts')

session.connect(hostname= ip,
                username= username,
                password= password,
                look_for_keys=False,
                allow_agent=False)

commands = ['ls', 'pwd','llsdsd']

for command in commands:
    print(f"{'#'*10} Executing the Command : {command} {'#'*10}")
    stdin1, stdout1, stderr1 = session.exec_command(command)
    time.sleep(.5)
    print(stdout1.read().decode())
    err = stderr1.read().decode()
    if err:
        print(err)

session.close()




