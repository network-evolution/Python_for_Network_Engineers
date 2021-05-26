#! /usr/local/Python_envs/Python3/bin/python3
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)

print(r.headers['content-type'])
r.encoding
r.text
r.json()
