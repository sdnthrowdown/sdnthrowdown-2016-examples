'''
Created on Jan 18, 2016

@author: azaringh
'''
import redis
import json
import csv
import os

stats_name = 'chicago:ge-1/0/5:traffic statistics'

r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
csv_file = os.getenv('HOME') + '/' + stats_name.replace(':', '_').replace('/', '-').replace(' ', '_') + '.csv'
f = open(csv_file, 'w+')   # Read and write
    
def create_csv():
    csvwriter = csv.writer(f)
    stat_list = r.lrange(stats_name, 0 , -1)
    hflag = True
    for stat in reversed(stat_list):
        j = json.loads(stat)
        
        d = { 'time': j['timestamp'], 
              'input-bytes': j['stats'][0]['input-bytes'][0]['data'],
              'input-bps': j['stats'][0]['input-bps'][0]['data'],
              'output-pps': j['stats'][0]['output-pps'][0]['data'],
              'output-bps': j['stats'][0]['output-bps'][0]['data'],
              'output-bytes': j['stats'][0]['output-bytes'][0]['data'],
              'input-pps': j['stats'][0]['input-pps'][0]['data'],
              'input-packets': j['stats'][0]['input-packets'][0]['data'],
              'output-packets': j['stats'][0]['output-packets'][0]['data']
             }
        if hflag == True:
            header = d.keys()
            csvwriter.writerow(header)
            hflag = False
        csvwriter.writerow(d.values())
    return

create_csv()