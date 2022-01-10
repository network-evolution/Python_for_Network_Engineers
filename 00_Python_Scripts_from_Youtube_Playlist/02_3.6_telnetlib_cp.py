#! /data/Python_envs/Python3/bin/python3
from telnetlib import Telnet
cmd = input('Enter the Command to execute :')
tn = Telnet('192.168.0.12', 32777)
# tn.write(b'admin\n')
# tn.write(b'admin\n')
tn.write(b'term length 0\n')
tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'exit\n')
print (tn.read_all().decode('ascii'))
