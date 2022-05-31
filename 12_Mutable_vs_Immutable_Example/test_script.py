#! /usr/local/Python_envs/Python3/bin/python3
from test_func import password_generator,password_dict_generator

users = ['user1', 'user2','user3']
# print(password_generator())
# print(password_generator())
## Mutables : List, Dictionaries, Sets
## Immutables : Str, Int, bool, tuples etc.

##################################################
####         Dictionaries are Mutable     ########
##################################################
final_users_list = []
user_dict = {}
for user in users:
	user_dict['username']= user
	user_dict['pwd']= password_generator()
	# user_dict ={'username':user, 'pwd':password_generator()}
	final_users_list.append(user_dict)
print(final_users_list)

##################################################
####         Strings are Immutable        ########
##################################################
# final_users_list = []
# user_str = ''
# for user in users:
# 	user_str = user
# 	final_users_list.append(user_str)
#
# print(final_users_list)

##################################################

##################################################
####         Lists are Mutable            ########
##################################################
# final_users_list = []
#
# for user in users:
#     user_list = []
#     user_list.append(user)
#     user_list.append(password_generator())
#     final_users_list.append(user_list)
# print(final_users_list)

##################################################
#### With Dictionary as Input In Function ########
##################################################
# new_list = []
#
# for user in users:
# 	new_list.append(password_dict_generator(user))
#
# print(new_list)
###################################################
# s = 'sh'
# print(id(s))
# s = s+'ibi'
# print(id(s))
# k = 'sg'
# print(id(k))
# j = k
# print(id(j))
# t1 = (1,2)
# print(id(t1))
# t1 = t1+(3,4)
# print(id(t1))
t2 = (1,2)
print(id(t2))
'''
string pool implementation
'''

t3 = ([2,3],[4,5])
print(t3)
id(t3)
t3[0].append(4)
print(t3)
id(t3)




