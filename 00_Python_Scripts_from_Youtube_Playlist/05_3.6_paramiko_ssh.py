#! /data/05_Atom_Demo/Atom_P3.6/bin/python3.6
import paramiko
import time
from getpass import getpass
ip = '172.18.1.1'
username = 'admin'
password = 'admin'

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'term length 0\n')
DEVICE_ACCESS.send(b'show run\n')
time.sleep(5)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))
SESSION.close()
