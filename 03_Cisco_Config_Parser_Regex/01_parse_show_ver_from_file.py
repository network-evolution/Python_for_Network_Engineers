#! /usr/local/Python_envs/Python3/bin/python3
import re

version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)\n')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_no_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')

with open('01_show_version_output.txt', 'r') as file:
    output = file.read()

    version_match = version_pattern.search(output)
    print('IOS Version'.ljust(18)+': '+version_match.group(1))

    model_match = model_pattern.search(output)
    print('Model '.ljust(18)+': '+model_match.group(1))

    serial_no_match = serial_no_pattern.search(output)
    print('Serial Number '.ljust(18)+': '+serial_no_match.group(1))

    uptime_match = uptime_pattern.search(output)
    print('Host Name '.ljust(18)+': '+uptime_match.group(1))
    print('Device Uptime '.ljust(18)+': '+uptime_match.group(2))
