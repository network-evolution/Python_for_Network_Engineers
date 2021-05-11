

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

    name = output[1]['intf']
    status = output[1]['status']
    print ('\n Interface ' + name + ' status is ' + status)

    if status == 'up':
        print ('Finishing the script')
    else:
        print ('Making backup interface UP')
        config_commands = [ 'int fa1/0',
                            'no shut' ]
        output = net_connect.send_config_set(config_commands)
        print(output)

