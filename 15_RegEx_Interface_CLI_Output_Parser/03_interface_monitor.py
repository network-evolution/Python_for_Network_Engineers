#! /usr/local/Python_envs/Python3/bin/python3
import sys
import time

from netmiko import Netmiko
import datetime
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import SSHException
import re
from tabulate import tabulate
import schedule
############ Logging ###################
# Logging Levels #
################
#  CRITICAL 50
#  ERROR    40
#  WARNING  30
#  INFO     20
#  DEBUG    10
###############
#Import Logging
import os
import logging,logging.handlers
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

#Define Logger
logger = logging.getLogger("Interface_Parser")

#Set the Minimum Log Level for logger
logger.setLevel(logging.DEBUG)

#Create Handlers(Filehandler with filename| StramHandler with stdout)
file_handler_info = logging.FileHandler('show_int_info.log')
file_handler_debug = logging.FileHandler('show_int_debug.log')
stream_handler = logging.StreamHandler(sys.stdout)

smtp_handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com',587),
											fromaddr= 'networkevolution.in@gmail.com',
											toaddrs= ['networkevolution.in@gmail.com'],
											subject="Interface Log Alert from Python",
											credentials=('networkevolution.in@gmail.com',MAIL_PASSWORD),
											secure= ())

#Set Additional log level in Handlers if needed
file_handler_info.setLevel(logging.INFO)
file_handler_debug.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.INFO)
smtp_handler.setLevel(logging.CRITICAL)

#Create Formatter and Associate with Handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler_info.setFormatter(formatter)
file_handler_debug.setFormatter(formatter)
stream_handler.setFormatter(formatter)
smtp_handler.setFormatter(formatter)

#Add Handlers to logger
logger.addHandler(file_handler_info)
logger.addHandler(file_handler_debug)
logger.addHandler(stream_handler)
logger.addHandler(smtp_handler)


########################################
int_pattern = re.compile(r"(\S+)\s+(([\d\\.]+)|unassigned)\s+\S+\s+\S+\s+(up|administratively down)\s+(\S+)")
lab_csr = {'host': '192.168.0.63',
		   'username': 'admin',
		   'password': 'admin',
		   'device_type': 'cisco_ios'}

def cisco_int_parser(device):
	now = datetime.datetime.now()
	logger.info(f"Connecting to the device: {device['host']} at {now}")
	try:
		my_router = Netmiko(**device)
		logger.info(f"Connected successfully to the device {device['host']}")
		logger.debug(f"{device['host']} prompt is:  {my_router.find_prompt()}")
		logger.info(f"Executing show ip int brief in {device['host']}")

		show_ip_interface = my_router.send_command('show ip interface brief')
		# print(show_ip_interface)
		int_iter = int_pattern.finditer(show_ip_interface)
		int_list = list()
		for intr in int_iter:
			int_dict = dict()
			# print(intr.group(1), intr.group(2), intr.group(4))
			int_dict['int'], int_dict['ip'], int_dict['status'] = intr.group(1), intr.group(2), intr.group(4)
			logger.debug(int_dict)
			if int_dict['int'] == 'GigabitEthernet2' and int_dict['status'] == 'administratively down':
				print("GigabitEthernet2 is down")
				logger.critical("GigabitEthernet2 is down")
			int_list.append(int_dict)

		logger.debug(int_list)
		print(f"\n\n {'#'*10} {device['host']} Interface Details {'#'*10}")
		print(tabulate(int_list, headers='keys', tablefmt="fancy_grid"))
	except NetmikoAuthenticationException:
		logger.warning(f"Authentication Failed on {device['host']}")

	except NetmikoTimeoutException:
		print(sys.exc_info()[0])
		logger.warning(f"Connection Failure : {device['host']}")

	except SSHException:
		logger.error(f"SSH Exception: {device['host']}")
	except:
		print(sys.exc_info()[0])
		logger.error(f"Exception Occurred : {device['host']}")

# cisco_int_parser(lab_csr)
schedule.every(15).seconds.do(cisco_int_parser, lab_csr)
while True:
	schedule.run_pending()
	time.sleep(1)

