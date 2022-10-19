#! /usr/local/Python_envs/Python3/bin/python3
from pyats.topology import loader
testbed = loader.load('../ios_testbed.yaml')

testbed.devices

ios_1 = testbed.devices['ios-1']
ios_2 = testbed.devices['ios-2']

for link in ios_1.find_links(ios_2):
	# print(repr(link))
	print(link)