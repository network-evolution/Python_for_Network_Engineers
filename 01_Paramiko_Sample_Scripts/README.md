# Directory : [01_Paramiko_Sample_Scripts](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/01_Paramiko_Sample_Scripts)
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

### List of Scripts in the Directory
```
01_ssh_host_key_policy.py
02.1_ssh_key_cisco_exec_command.py
02.2_ssh_key_cisco_invoke_shell.py
02.3_ssh_key_cisco_invoke_shell_fn.py
```

[Click here for Complete Paramiko Scripts Tutorial Playlist In YouTube :01_Paramiko_Sample_Scripts](https://www.youtube.com/watch?v=A075aWJMAeM&list=PLOocymQm7YWYc73phqzbZ1S3ANrVVpUFN)
