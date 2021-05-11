

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
    print('\nOUTPUT FROM DEVICE \n')
    output = net_connect.send_command('show ip int brief',use_textfsm=True)
    print(output)

    print('\nOUTPUT USING FOR LOOP AND IF \n')
    devlist =[]
    for i in output:
        if i['status'] == 'up':
            devlist.append(i['intf'])
    print (devlist)

    print('\nOUTPUT USING LIST COMPREHENSION \n')

    print ([i['intf'] for i in output if i['status'] == 'up'])

    print('\nLIST OF INTERFACES WHICH ARE UP \n####################################')

    statusup =[i['intf'] for i in output if i['status'] == 'up']
    for ifaceup in statusup:
        print (ifaceup)

    print('\nLIST OF INTERFACES WHICH ARE DOWN \n####################################')

    statusdown =[i['intf'] for i in output if i['status'] != 'up']
    for ifacedown in statusdown:
        print (ifacedown)















