#! /usr/local/Python_envs/Python3/bin/python3

import paramiko

session = paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname= '127.0.0.1',
                username='dev',
                password='Devan@555',
                look_for_keys=False,
                allow_agent=False)
device_access = session.invoke_shell()
device_access.send(b'ls\n')
time.sleep(.5)
output = device_access.recv(65000)
print(output.decode())
