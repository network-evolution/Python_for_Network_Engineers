#! /data/Python_envs/Python3/bin/python3

import xml.etree.ElementTree as ET
tree = ET.parse('all_int.xml')
root = tree.getroot()

#print(root[0][0][0][0][0].tag)
n = int(input("Enter Interface Number: "))
n = n-1 ;

int_number = list(root)[0][0][0][n][0].text
int_ip =     list(root)[0][0][0][n][1][0][0][0].text
#print(int_number)
#print(int_ip)

print("Gigabiethernet " +int_number+ " - IP Address : " + int_ip)
