# Python for Network Engineers
This repo contains Scripts which are explained in the YouTube Channel [NetworkEvolution](https://www.youtube.com/c/NetworkEvolution?sub_confirmation=1)

## List of Directories in this Repository:
- [**00_Python_Scripts_from_Youtube_Playlist** ](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/00_Python_Scripts_from_Youtube_Playlist)
- 
# Summary of each Directory
## Directory : 00_Python_Scripts_from_Youtube_Playlist
This directory contains all the Scripts explained in the below YouTube playlist which has more than 70 Videos.


Training starts from a very beginner level like:
How to initiate SSH Connection to the Device using Paramiko
To Intermediate level of Using NETCONF/YANG, RESTCONF etc

[Click here for Complete Videos Playlist In YouTube :Python Learning for Network Engineers](https://www.youtube.com/watch?v=sG_RiytUA38&list=PLOocymQm7YWakdZkBfCRIC06fv7xQE85N)



```
For the Complete Scripts and Video maps please access the folder "`00_Python_Scripts_from_Youtube_Playlist`" in this Repository
```

These Python scripts Contains Tutorials on:
  - Paramiko
  - Netmiko
  - Nornir
  - NAPALM
  - Ansible
  - NETCONF/YANG
  - RESTCONF
  - Regex For Parsing
  - CSV for Bulk Configuration
  - How to use text file for Configuration
 

This script targets the [IOS XE DevNet Always On Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology) that leverages a CSR1000v as a target.  

To execute this script against a different device, create a new device dictionary in `device_info.py` for your device.  Then import this new dictionary instead of `ios_xe1` in the scripts.

* Clone the Python Examples and change into the directory.  

    ```bash
    git clone https://github.com/CiscoDevNet/python_code_samples_network.git
    cd python_code_samples_network
    cd netmiko-interface-example
    ```
