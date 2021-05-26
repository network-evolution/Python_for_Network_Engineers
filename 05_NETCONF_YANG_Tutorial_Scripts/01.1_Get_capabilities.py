#! /data/Python_envs/Python3/bin/python3

from ncclient import manager

RTR1_MGR = manager.connect(host='ios-xe-mgmt.cisco.com',
                    port=10000,
                    username='developer',
                    password='C1sco12345',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

for RTR_Capability in RTR1_MGR.server_capabilities:
    print (RTR_Capability)

RTR1_MGR.close_session()
