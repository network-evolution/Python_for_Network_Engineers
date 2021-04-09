#! /data/05_Atom_Demo/Atom_P3.6/bin/python3.6
from telnetlib import Telnet
cmd = input('Enter the Command to execute :')
tn = Telnet('172.18.1.1')
tn.write(b'admin\n')
tn.write(b'admin\n')
tn.write(b'term length 0\n')
tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'exit\n')
print (tn.read_all().decode('ascii'))
