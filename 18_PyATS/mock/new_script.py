from genie.testbed import load
tb = load('mock.yaml')
dev = tb.devices['nx-osv-1']
dev.connect()
p1 = dev.parse('show inventory')
print('My serial for slot1 is: ' + p1['name']['Slot 1']['serial_number'])
