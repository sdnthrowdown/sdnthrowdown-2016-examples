'''
Created on Feb 21, 2016

@author: azaringh
'''

import requests
requests.packages.urllib3.disable_warnings()
import json
import math

# Source: http://www.johndcook.com/blog/python_longitude_latitude/
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc

routers = [ 
           { 'name': 'chicago', 'router_id': '10.210.10.124', 'latitude':'', 'longitude':''},
           { 'name': 'san francisco', 'router_id': '10.210.10.100', 'latitude':'', 'longitude':''},
           { 'name': 'dallas', 'router_id': '10.210.10.106', 'latitude':'', 'longitude':''},
           { 'name': 'miami', 'router_id': '10.210.10.112', 'latitude':'', 'longitude':''},
           { 'name': 'new york', 'router_id': '10.210.10.118', 'latitude':'', 'longitude':''},
           { 'name': 'los angeles', 'router_id': '10.210.10.113', 'latitude':'', 'longitude':''},
           { 'name': 'houston', 'router_id': '10.210.10.114', 'latitude':'', 'longitude':''},
           { 'name': 'tampa', 'router_id': '10.210.10.115', 'latitude':'', 'longitude':''}
           ]

url = "https://10.10.2.25:8443/oauth2/token"

payload = {'grant_type': 'password', 'username': 'some_name', 'some_password': 'northstar123'}
response = requests.post (url, data=payload, auth=('some_name','some_password'), verify=False)
json_data = json.loads(response.text)
authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

r = requests.get('https://10.10.2.25:8443/NorthStar/API/v1/tenant/1/topology/1/nodes/', headers=authHeader, verify=False)

p = json.dumps(r.json())
nodes = json.loads(p)

for node in nodes:
    for rtr in routers:
        if node['name'] == rtr['router_id']:
            rtr['latitude'] = node['topology']['coordinates']['coordinates'][0]
            rtr['longitude'] = node['topology']['coordinates']['coordinates'][1]
            print rtr['name'], ':'
            print '\t latitude: ', rtr['latitude']
            print '\t longitude: ', rtr['longitude']
            break
        
i = j = 0
rn = len(routers)

for i in range(rn):
    for j in range(i+1, rn):
        d = 3960 * distance_on_unit_sphere(routers[i]['latitude'], routers[i]['longitude'], routers[j]['latitude'], routers[j]['longitude'])
        print 'Distance between ' + routers[i]['name'] + ' and ' + routers[j]['name'] + ': ', int(d)
