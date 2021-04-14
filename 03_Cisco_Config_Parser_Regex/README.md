# Directory : [03_Cisco_Config_Parser_Regex](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/03_Cisco_Config_Parser_Regex)
This directory contains Scripts which explains how to parse configuration lines from Cisco Devices Using Regex in Python

### Sample Parsed Output :

*Show Version Parser 

![Show_Version](https://user-images.githubusercontent.com/70020386/114664645-9dac7380-9d19-11eb-9e8f-864eae0bc6b0.png)

*Show Running Config Parser Output:

![Show_run_parsing](https://user-images.githubusercontent.com/70020386/114667044-9f2b6b00-9d1c-11eb-8fe4-9f2d38bf8b2d.png)

* Regex Patterns Used for Show Version Parser:
```
version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_no_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')

```
* Regex Patterns Used for Show running Parser:
```
hostname_pattern = re.compile(r'hostname (\S+)')
domainname_pattern = re.compile(r'ip domain name (.+)')
pid_pattern = re.compile(r'license udi pid (\w+) sn (\S+)')
netconf_pattern = re.compile(r"netconf-yang\r\n")
username_pattern = re.compile(r'username (\S+) privilege (\d{2})')
interface_pattern = re.compile(r'interface (\S+[.]?\d*)\r\n.+?\r?\n?\s?ip address ([\d\.]+) ([\d\.]+)')
interface_prop_pattern = re.compile(r'interface (?P<name>\S+[.]?\d*)\r\n\s?.+?\r?\n?\s?ip address (?P<ip_aadress>[\d\.]+) (?P<mask>[\d\.]+)')
default_route_pattern = re.compile(r'ip route 0.0.0.0 0.0.0.0.+?([\d.]+)\r\n')
static_route_pattern = re.compile(r'ip route (?P<dst_subnet>[^0][\d\.]+) (?P<mask>[^0][\d\.]+) (?P<next_hop>[\d\.]+)')

```

* 

### List of Scripts in the Directory
- **01_parse_Show_ver_SSH.py** : Parse Show Version Output over SSH : [Script Demonstration Videos](https://www.youtube.com/watch?v=PbP9tyV0Zao&list=PLOocymQm7YWY8Eksax8mjRSWbUijb7W93)
- **01_parse_show_ver_from_file.py** : Parse Show Version Output from Text file : [Script Demonstration Videos](https://www.youtube.com/watch?v=PbP9tyV0Zao&list=PLOocymQm7YWY8Eksax8mjRSWbUijb7W93)
- **02_parse_show_run_from_file.py** : Parse Show Run Output from Text file :[Script Demonstration Videos](https://www.youtube.com/watch?v=PbP9tyV0Zao&list=PLOocymQm7YWY8Eksax8mjRSWbUijb7W93)
- **02_parse_show_run_from_SSH.py** : HParse Show Run Output from SSH : [Script Demonstration Videos](https://www.youtube.com/watch?v=PbP9tyV0Zao&list=PLOocymQm7YWY8Eksax8mjRSWbUijb7W93)
- **command_output_to_txt.py** : Save Multiple Show Commands to text file :[Script Demonstration Videos](https://www.youtube.com/watch?v=PbP9tyV0Zao&list=PLOocymQm7YWY8Eksax8mjRSWbUijb7W93)

[Click here for Complete Cisco Configuration Parsing Videos Playlist In YouTube](https://www.youtube.com/watch?v=PbP9tyV0Zao&list=PLOocymQm7YWY8Eksax8mjRSWbUijb7W93)
