#! /usr/local/Python_envs/Python3/bin/python3
from genie.testbed import load

tb = load('../my_testbed.yaml')
dev1 = tb.devices['vIOS_61']
dev1.connect()
p1 = dev1.parse('show inventory')
print(p1)
dev2 = tb.devices['vIOS_62']
dev2.connect()
p2 = dev2.parse('show inventory')
print(p2)
dev3 = tb.devices['CSR-17.31']
dev3.connect()
p3 = dev3.parse('show inventory')
print(p3)