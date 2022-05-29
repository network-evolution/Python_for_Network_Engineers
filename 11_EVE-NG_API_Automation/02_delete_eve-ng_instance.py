#! /usr/local/Python_envs/Python3/bin/python3
import requests
import json

def delete_instance(*args):
	login_url = 'http://192.168.0.12/api/auth/login'
	cred = '{"username":"admin","password":"eve","html5":"-1"}'
	headers = {'Accept': 'application/json'}

	login = requests.post(url=login_url, data=cred)
	cookies = login.cookies
	# print(cookies)
	for instance_id in args:
		delete_url = f'http://192.168.0.12/api/labs/Lab_Evolution.unl/nodes/{instance_id}'
		delete_api = requests.delete(url=delete_url,cookies=cookies)
		response = delete_api.json()
		print(response)

instance_ids = (input("Enter Instance Id's to delete:").split(','))

delete_instance(*instance_ids)