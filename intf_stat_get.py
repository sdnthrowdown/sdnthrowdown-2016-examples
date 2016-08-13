'''
Created on Aug 11, 2016

@author: azaringh
'''
import redis
import json
import pprint

# print last input pps for ge-1/0/5 on Chicago

r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
chi_ge_105 = r.lrange('chicago:ge-1/0/1:traffic statistics', 0, -1)[0]
print chi_ge_105 # json-formatted string
print isinstance (chi_ge_105, str)
data = json.loads(chi_ge_105) # decode json; convert json string to python dictionary
print data
print data['stats'][0]['input-bps'][0]['data']