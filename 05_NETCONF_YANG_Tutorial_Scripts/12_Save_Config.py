#! /data/Python_envs/Python3/bin/python3

from ncclient import manager, xml_

RTR1_MGR = manager.connect(host='csr1.test.lab',
                    port=830,
                    username='admin',
                    password='admin',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

SAVE = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""
reply = RTR1_MGR.dispatch(xml_.to_ele(SAVE))
print (reply)

RTR1_MGR.close_session()
