'''
Created on Feb 21, 2016

@author: azaringh
'''

'''
Retrieve topology of the network
'''

import requests
requests.packages.urllib3.disable_warnings()
import json

url = "https://10.10.2.25:8443/oauth2/token"

payload = {'grant_type': 'password', 'username': 'some_name', 'password': 'some_password'}
response = requests.post (url, data=payload, auth=('some_name','some_password'), verify=False)
json_data = json.loads(response.text)
authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

r = requests.get('https://10.10.2.25:8443/NorthStar/API/v1/tenant/1/topology/1', headers=authHeader, verify=False)
print json.dumps(r.json(), indent=4, separators=(',', ': '))
