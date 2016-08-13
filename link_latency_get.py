'''
Created on Aug 11, 2016

@author: azaringh
'''
import redis
import json

# print last input pps for ge-1/0/5 on Chicago

r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
latency_str = r.lrange('dallas:houston:latency', 0, -1)[0]
print latency_str
latency_dict = json.loads(latency_str) # decode json; convert json string to python dictionary
print latency_dict
print latency_dict['timestamp'], latency_dict['rtt-average(ms)']