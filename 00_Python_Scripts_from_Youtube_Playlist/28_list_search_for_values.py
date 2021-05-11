

from netmiko import ConnectHandler
from getpass import getpass 
from operator import itemgetter
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

ip = input ('Enter the IP :')
IP_LIST = open('15_devices')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin',
        'password': 'admin',
    }

    print ('\n #### Connecting to the device ' + IP.strip() + '#### \n')
    try:
        net_connect = ConnectHandler(**RTR)
    except NetMikoTimeoutException:
        print ('Device not reachable' )
        continue

    except NetMikoAuthenticationException:
        print ('Authentication Failure' )
        continue

    except SSHException:
        print ('Make sure SSH is enabled' )
        continue
    output = net_connect.send_command('show ip int brief',use_textfsm=True)

    print('\nSEARCH RESULT \n####################################')

    ipsearch =[i['intf'] for i in output if i['ipaddr'] == ip]
    for ipoutput in ipsearch:
        print ('IP Address ' + ip + ' belongs to the interface ' + ipoutput)













