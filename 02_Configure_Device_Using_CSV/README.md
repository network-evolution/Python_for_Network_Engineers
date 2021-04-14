# Directory : [02_Configure_Device_Using_CSV](https://github.com/network-evolution/Python_for_Network_Engineers/tree/main/02_Configure_Device_Using_CSV)
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
- **01_config_in_row.csv** : How to read Content from CSV file in row format : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- **01_csv_reader_row.py** : How to read Content from CSV file Using Reader format : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- **02_config_in_column.csv** : How to read Content from CSV file in Column format :[Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- **02_csv_reader_column.py** : How to read Content from CSV file in Column format using Reader : [Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
- **03_csv_DictReader_column.py** : How to read Content from CSV file in Column format using DictReader :[Script Demonstration Videos](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)

[Click here for Complete CSV Videos Playlist In YouTube :02_Configure_Device_Using_CSV](https://www.youtube.com/watch?v=3XoVPJkHMFU&list=PLOocymQm7YWYpP_Qkju89vN8BykhvWO5U)
