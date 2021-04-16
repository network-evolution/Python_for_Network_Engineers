
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import time
import datetime

TNOW = datetime.datetime.now().replace(microsecond=0)
IP_LIST = open('20_devices')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin1',
        'use_keys': True,
        'key_file': '/data/05_PYTHON_DEMO/SSH_KEY/admin1',
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

    print('\n Initiating config backup \n')
    output = net_connect.send_command('show run')
    SAVE_FILE = open('ROUTER_' + IP + str(TNOW), 'w')
    SAVE_FILE.write(output)
    SAVE_FILE.close()
    print('\n Finished config backup \n')
