#! /data/Python_envs/Python3/bin/python3

from ncclient import manager

RTR1_MGR = manager.connect(host='172.17.0.51',
                    port=830,
                    username='admin',
                    password='admin',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

for RTR_Capability in RTR1_MGR.server_capabilities:
    print (RTR_Capability)

RTR1_MGR.close_session()
