

from netmiko import ConnectHandler
from getpass import getpass

IP_LIST = open('15_devices')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin',
        'password': 'admin',
    }

    print ('Connecting to the device ' + IP)
    net_connect = ConnectHandler(**RTR)

    output = net_connect.send_config_from_file(config_file='15_config')
    print(output)

    print('\n Saving the configuration \n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)
