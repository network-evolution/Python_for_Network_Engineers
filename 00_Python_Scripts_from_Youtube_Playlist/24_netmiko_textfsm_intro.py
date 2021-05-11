

from netmiko import ConnectHandler
from getpass import getpass 
from operator import itemgetter
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

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
#    print(output)
    print (output[3])
    l = len(output)
    print ('Total number of interfaces are ' + str(l))

    name = output[2]['intf']
    status = output[2]['status']
    print ('\n Interface ' + name + ' status is ' + status)

    interface0 = output[1]
    getintf = itemgetter('intf')
    getstatus = itemgetter('status')
    name = getintf(interface0)
    status = getstatus(interface0)

    print ('\n Interface ' + name + ' status is ' + status)

