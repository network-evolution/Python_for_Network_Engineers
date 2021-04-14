# Python for Network Engineers
This repo contains Scripts which are explained in the YouTube Channel [NetworkEvolution](https://www.youtube.com/c/NetworkEvolution?sub_confirmation=1)

## List of Directories in this Repository:
- [**00_Python_Scripts_from_Youtube_Playlist** ](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/00_Python_Scripts_from_Youtube_Playlist)
- [**01_Paramiko_Sample_Scripts** ](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/01_Paramiko_Sample_Scripts)
- [**02_Configure_Device_Using_CSV** ](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/02_Configure_Device_Using_CSV)
- [**03_Cisco_Config_Parser_Regex** ](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/03_Cisco_Config_Parser_Regex)

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

### List of Scripts in the Directory
```
01_ssh_host_key_policy.py
02.1_ssh_key_cisco_exec_command.py
02.2_ssh_key_cisco_invoke_shell.py
02.3_ssh_key_cisco_invoke_shell_fn.py
```

[Click here for Complete Paramiko Scripts Tutorial Playlist In YouTube :01_Paramiko_Sample_Scripts](https://www.youtube.com/watch?v=A075aWJMAeM&list=PLOocymQm7YWYc73phqzbZ1S3ANrVVpUFN)

```
For the Complete Scripts and Video maps please access the folder "`01_Paramiko_Sample_Scripts`" in this Repository
```
***
## Directory : [02_Configure_Device_Using_CSV](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/02_Configure_Device_Using_CSV)
This directory contains Scripts which explains how to read Device IP Address and configuration lines from CSV file and configure respective devices using Python.

* Sample CSV FIle Used for Configuring the Device :

![CSV1](https://user-images.githubusercontent.com/70020386/114660759-7d79b600-9d13-11eb-8e53-6cd2807341c8.png)


* The above CSV file will create a Dictionary in below format 
```
conf_dict={'192.168.0.50': ['terminal len 0',
                  'config t',
                  'int gi1',
                  'no shut',
                  'exit',
                  'exit',
                  'show ip int brie',
                  'show run int gi1'],
 '192.168.0.51': ['terminal len 0',
                  'config t',
                  'int lo0',
                  'ip add 10.0.0.1 255.255.255.0',
                  'int lo1',
                  'ip add 11.0.0.1 255.255.255.0',
                  'do show run int loopback0',
                  'do show run int loopback1'],
 '192.168.0.53': ['terminal len 0', 'config t', 'int gi3', 'no shut'],
 'csr1.test.lab': ['terminal len 0',
                   'config t',
                   'int gi2',
                   'no shut',
                   'ip address 2.2.2.2 255.255.255.0',
                   'exit',
                   'exit',
                   'show ip int brie',
                   'show run int gi2']}
```

* 

### List of Scripts in the Directory
- <u>01_config_in_row.csv<u> : How to read Content from CSV file in row format : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 01_csv_reader_row.py : How to read Content from CSV file Using Reader format : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 02_config_in_column.csv : How to read Content from CSV file in Column format :[Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 02_csv_reader_column.py : How to read Content from CSV file in Column format using Reader : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 03_csv_DictReader_column.py : How to read Content from CSV file in Column format using DictReader :[Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)

[Click here for Complete CSV Videos Playlist In YouTube :02_Configure_Device_Using_CSV](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)

```
For the Complete Scripts and Video maps please access the folder "`02_Configure_Device_Using_CSV`" in this Repository
```

***
## Directory : [03_Cisco_Config_Parser_Regex](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/03_Cisco_Config_Parser_Regex)
This directory contains Scripts which explains how to parse configuration lines from Cisco Devices Using Regex in Python

* Sample Parsed Output :
** Show Version Parser 

![Show_Version](https://user-images.githubusercontent.com/70020386/114664645-9dac7380-9d19-11eb-9e8f-864eae0bc6b0.png)


* The above CSV file will create a Dictionary in below format 
```
conf_dict={'192.168.0.50': ['terminal len 0',
                  'config t',
                  'int gi1',
                  'no shut',
                  'exit',
                  'exit',
                  'show ip int brie',
                  'show run int gi1'],
 '192.168.0.51': ['terminal len 0',
                  'config t',
                  'int lo0',
                  'ip add 10.0.0.1 255.255.255.0',
                  'int lo1',
                  'ip add 11.0.0.1 255.255.255.0',
                  'do show run int loopback0',
                  'do show run int loopback1'],
 '192.168.0.53': ['terminal len 0', 'config t', 'int gi3', 'no shut'],
 'csr1.test.lab': ['terminal len 0',
                   'config t',
                   'int gi2',
                   'no shut',
                   'ip address 2.2.2.2 255.255.255.0',
                   'exit',
                   'exit',
                   'show ip int brie',
                   'show run int gi2']}
```

* 

### List of Scripts in the Directory
- 01_config_in_row.csv : How to read Content from CSV file in row format : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 01_csv_reader_row.py : How to read Content from CSV file Using Reader format : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 02_config_in_column.csv : How to read Content from CSV file in Column format :[Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 02_csv_reader_column.py : How to read Content from CSV file in Column format using Reader : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- 03_csv_DictReader_column.py : How to read Content from CSV file in Column format using DictReader :[Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)

[Click here for Complete CSV Videos Playlist In YouTube :02_Configure_Device_Using_CSV](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)

```
For the Complete Scripts and Video maps please access the folder "`02_Configure_Device_Using_CSV`" in this Repository
```


