#! /usr/local/Python_envs/Python3/bin/python3
import paramiko
import time

host = 'csr1.test.lab'
username = 'admin'
password = 'admin'

n = 0
while True:

    show_command = input("Enter Show command to execute: ")
    if show_command in ['','exit']:
        print("Exiting the Code")
        break

    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(host, port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'term length 0\n')
    DEVICE_ACCESS.send(f'{show_command}\n')
    time.sleep(1)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))
    SESSION.close()
    n = n+1
    with open (f"{n:02d}_{show_command.replace(' ','_')}_output.txt", 'w') as f:
        f.write(output.decode('ascii'))

    print (f"\n{'#' * 50}\nConfiguration Saved Successfully \n{'#' * 50}\n")

