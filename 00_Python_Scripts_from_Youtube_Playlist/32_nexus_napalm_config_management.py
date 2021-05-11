
from napalm import get_network_driver
driver = get_network_driver('nxos')
import urllib3
urllib3.disable_warnings()
device = driver('192.168.67.21', 'admin', 'admin')
device.open()

device.load_merge_candidate(filename='32_nexus_route')
#device.load_replace_candidate(filename='31_arista_backup')
print (device.compare_config())

if len(device.compare_config()) > 0:
    choice = input("\nWould you like to Replace the configuration? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()
        choice = input("\nWould you like to Rollback to previous config? [yN]: ")
        if choice == 'y':
            print('Committing ...')
            device.rollback()

    else:
        print('Discarding ...')
        device.discard_config()

else:
    print ('No difference')

# close the session with the device.
device.close()
print('Done.')

