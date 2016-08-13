'''
Created on Aug 12, 2016

@author: azaringh
'''
import requests
requests.packages.urllib3.disable_warnings()
import json


url = "https://10.10.2.29:8443/oauth2/token"

payload = {'grant_type': 'password', 'username': 'some_name', 'password': 'some_password'}
response = requests.post (url, data=payload, auth=('some_name','some_password'), verify=False)
json_data = json.loads(response.text)
authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/links/', headers=authHeader, verify=False)
print "r is:", r
print "r.json is:", r.json() # r.json() returns a python dict


for link in r.json():
    if link['name'] == 'L10.210.11.1_10.210.11.2':
        print 'A node:', link['endA']['node']['name']
        print 'Z node:', link['endZ']['node']['name']
