# Python for Network Engineers
This repo contains Scripts which are explained in the YouTube Channel [NetworkEvolution](https://www.youtube.com/c/NetworkEvolution?sub_confirmation=1)

## List of Directories in this Repository:
- [**00_Python_Scripts_from_Youtube_Playlist** ](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/00_Python_Scripts_from_Youtube_Playlist)
- [**01_Paramiko_Sample_Scripts** ](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/01_Paramiko_Sample_Scripts)

# Summary of each Directory
***
## Directory : [00_Python_Scripts_from_Youtube_Playlist](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/00_Python_Scripts_from_Youtube_Playlist)
This directory contains all the Scripts explained in the below YouTube playlist which has more than 70 Videos.


Training starts from a very beginner level like:
How to initiate SSH Connection to the Device using Paramiko
To Intermediate level of Using NETCONF/YANG, RESTCONF etc
> List of all the Scripts

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

***
## Directory : [01_Paramiko_Sample_Scripts](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/01_Paramiko_Sample_Scripts)
This directory contains Scripts which explains how to use Paramiko Library for communicating with Cisco Devices.

* Demonstrates the use of SSH Hostkey policy. Different ways to use hostkey policies :
```
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.load_host_keys('/home/evolve/.ssh/known_hosts')
session.set_missing_host_key_policy(paramiko.WarningPolicy())
```

* SSH Keybased Authentication Using Paramiko:
* Paramiko SSH exec_command Example
* Paramiko invoke_shell example
* SSH Password Based Authentication

### List of Scripts
```
01_ssh_host_key_policy.py
02.1_ssh_key_cisco_exec_command.py
02.2_ssh_key_cisco_invoke_shell.py
02.3_ssh_key_cisco_invoke_shell_fn.py
```

[Click here for Complete Paramiko Scripts Tutorial Playlist In YouTube :01_Paramiko_Sample_Scripts](https://www.youtube.com/watch?v=A075aWJMAeM&list=PLOocymQm7YWYc73phqzbZ1S3ANrVVpUFN)

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
