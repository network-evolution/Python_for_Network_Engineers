import getpass
import telnetlib

HOST = "10.10.10.10"
user = str("admin")
pwd = getpass.getpass()
cmd = raw_input("Enter the command: ")

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if pwd:
    tn.read_until("Password: ")
    tn.write(pwd + "\n")

tn.write("term length 0\n")
tn.write(cmd + "\n")
tn.write("exit\n")

print tn.read_all()
