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

r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/', headers=authHeader, verify=False)

p = json.dumps(r.json())
lsp_list = json.loads(p)
# Find target LSP to use lspIndex

for lsp in lsp_list:
    if lsp['name'] == 'GROUP_NINE_NY_SF_LSP4':
        break   
print json.dumps(lsp, indent=4, separators=(',', ': '))
print lsp['liveProperties']['rro']
count = 1
for nhop in lsp['liveProperties']['rro']:
    print 'hop' + str(count) + ':', nhop['address']
    count = count + 1
