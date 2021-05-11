
from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.67.43', 'admin', 'admin')
device.open()

device.load_merge_candidate(filename='29_cisco_route')
print (device.compare_config())

if len(device.compare_config()) > 0:
    choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()
    else:
        print('Discarding ...')
        device.discard_config()

else:
    print ('No difference')

# close the session with the device.
device.close()
print('Done.')

