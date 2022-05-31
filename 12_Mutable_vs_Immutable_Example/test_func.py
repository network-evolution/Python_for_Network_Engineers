#! /usr/local/Python_envs/Python3/bin/python3

import string
import random

########################################################
def password_generator():
	password = ''.join(random.choices(string.ascii_uppercase +
							 string.digits + string.ascii_lowercase, k=8))
	return(password)

########################################################
def password_dict_generator(user):
	password = ''.join(random.choices(string.ascii_uppercase +
									  string.digits + string.ascii_lowercase, k=8))
	return({'username':user, 'pwd':password})
########################################################






#https://docs.python.org/3/glossary.html#term-immutable
#https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types


