#! /usr/local/Python_envs/Python3/bin/python3
import requests
import sys
import os
import schedule,datetime

#Import Logging
import logging,logging.handlers
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

#Define Logger
logger = logging.getLogger("FW Backup")

#Set the Minimum Log Level for logger
logger.setLevel(logging.DEBUG)

#Create Handlers(Filehandler with filename| StramHandler with stdout)
file_handler_debug = logging.FileHandler('Backup.log')
smtp_handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com',587),
											fromaddr= 'networkevolution.in@gmail.com',
											toaddrs= ['networkevolution.in@gmail.com'],
											subject="FW Backup Status",
											credentials=('networkevolution.in@gmail.com',MAIL_PASSWORD),
											secure= ())

#Set Additional log level in Handlers if needed
file_handler_debug.setLevel(logging.DEBUG)
smtp_handler.setLevel(logging.INFO)

#Create Formatter and Associate with Handlers
formatter = logging.Formatter('%(asctime)s - %(name)s -%(message)s- %(levelname)s')
file_handler_debug.setFormatter(formatter)
smtp_handler.setFormatter(formatter)

#Add Handlers to logger
logger.addHandler(file_handler_debug)
logger.addHandler(smtp_handler)
def fortigate_backup():
	tnow = datetime.datetime.now().replace(microsecond=0)
	logger.debug("Initiated Configuration Backup")
	url = "http://192.168.0.21/api/v2/monitor/system/config/backup?destination=file&scope=global"

	headers = {
		'Authorization': 'Bearer tQcmNwHmsbm68skz8xgtkzQ0104gnm',
	}

	response = requests.request("GET", url, headers=headers)
	if response.status_code == 200:
		logger.info(f"Backup Successful")
	else:
		logger.info(f"Backup Failed Code: {response.status_code}")


	with open(f"Backup_{tnow}.conf", 'wb') as f:
		f.write(response.content)
	print(response.status_code)

schedule.every(15).seconds.do(fortigate_backup)

while True:
	schedule.run_pending()