

from netmiko import ConnectHandler
from getpass import getpass 
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

IP_LIST = open('18_routers')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin',
        'password': 'admin',
    }

    print ('\n #### Connecting to the Router ' + IP.strip() + '#### \n')
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

    output = net_connect.send_config_from_file(config_file='18_router_config')
    print(output)

    print('\n Saving the Router configuration \n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)

##############################
IP_LIST = open('18_switches')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin',
        'password': 'admin',
    }

    print ('\n #### Connecting to the Switch ' + IP.strip() + '#### \n')
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

    output = net_connect.send_config_from_file(config_file='18_switch_config')
    print(output)

    print('\n Saving the Switch configuration \n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show ip route')
    print(output)

