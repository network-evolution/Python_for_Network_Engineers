

from netmiko import ConnectHandler

with open('15_devices') as IP_LIST:
    for IP in IP_LIST:
        RTR = {
            'device_type': 'cisco_ios',
            'ip':   IP,
            'username': 'admin',
            'password': 'admin',
        }

        print ('Connecting to the device ' + IP)
        net_connect = ConnectHandler(**RTR)

        with open('15_config') as CONFIG_LINES:
            CONFIG = CONFIG_LINES.read()
        output = net_connect.send_config_set(CONFIG)
        print(output)

        output = net_connect.send_command('show ip int brief')
        print(output)
