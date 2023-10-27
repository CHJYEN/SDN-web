#!/usr/bin/python
import json
import urllib.request
from requests.auth import HTTPBasicAuth
import requests

def set_vlan():
	url = 'http://127.0.0.1:8080/stats/flowentry/add'
	headers = {'Content-Type': 'application/json'}
	flow1 = {
        "dpid": 1,
        "priority": 1,
        "match":{
            "in_port": 1
        },
        "actions":[
            {
                "type": "PUSH_VLAN",    
                "ethertype": 33024      
            },
            {
                "type": "SET_FIELD",
                "field": "vlan_vid",    
                "value": 4096           
            },
            {
                "type": "OUTPUT",
                "port": 3
            }
        ]
    }
	flow2 = {
        "dpid": 1,
        "priority": 1,
        "match":{
            "in_port": 2
        },
        "actions":[
            {
                "type": "PUSH_VLAN",     
                "ethertype": 33024      
            },
            {
                "type": "SET_FIELD",
                "field": "vlan_vid",     
                "value": 4097           
            },
            {
                "type": "OUTPUT",
                "port": 3
            }
        ]
    }
	flow3 = {
        "dpid": 1,
        "priority": 1,
        "match":{
            "vlan_vid": 0
        },
        "actions":[
            {
                "type": "POP_VLAN",    
                "ethertype": 33024     
            },
            {
                "type": "OUTPUT",
                "port": 1
            }
        ]
    }
	flow4 = {
        "dpid": 1,
        "priority": 1,
        "match": {
            "vlan_vid": 1
        },
        "actions": [
            {
                "type": "POP_VLAN", 
                "ethertype": 33024  
            },
            {
                "type": "OUTPUT",
                "port": 2
            }
        ]
    }
	flow5 = {
        "dpid": 2,
        "priority": 1,
        "match": {
            "in_port": 1
        },
        "actions": [
            {
                "type": "PUSH_VLAN", 
                "ethertype": 33024 
            },
            {
                "type": "SET_FIELD",
                "field": "vlan_vid", 
                "value": 4096  
            },
            {
                "type": "OUTPUT",
                "port": 3
            }
        ]
    }
	flow6 = {
        "dpid": 2,
        "priority": 1,
        "match": {
            "in_port": 2
        },
        "actions": [
            {
                "type": "PUSH_VLAN",  
                "ethertype": 33024  
            },
            {
                "type": "SET_FIELD",
                "field": "vlan_vid",  
                "value": 4097 
            },
            {
                "type": "OUTPUT",
                "port": 3
            }
        ]
    }
	flow7 = {
        "dpid": 2,
        "priority": 1,
        "match": {
            "vlan_vid": 0
        },
        "actions": [
            {
                "type": "POP_VLAN", 
                "ethertype": 33024  
            },
            {
                "type": "OUTPUT",
                "port": 1
            }
        ]
    }
	flow8 = {
        "dpid": 2,
        "priority": 1,
        "match": {
            "vlan_vid": 1
        },
        "actions": [
            {
                "type": "POP_VLAN", 
                "ethertype": 33024  
            },
            {
                "type": "OUTPUT",
                "port": 2
            }
        ]
    }
	res1 = requests.post(url, json.dumps(flow1), headers=headers)
	res2 = requests.post(url, json.dumps(flow2), headers=headers)
	res3 = requests.post(url, json.dumps(flow3), headers=headers)
	res4 = requests.post(url, json.dumps(flow4), headers=headers)
	res5 = requests.post(url, json.dumps(flow5), headers=headers)
	res6 = requests.post(url, json.dumps(flow6), headers=headers)
	res7 = requests.post(url, json.dumps(flow7), headers=headers)
	res8 = requests.post(url, json.dumps(flow8), headers=headers)


def get_links():
    url = "http://127.0.0.1:8080/v1.0/topology/links"
    req = urllib.request.Request(url)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    res = json.loads(res)
    print("\n555:")
    print(res)


def main(x):
	url_topo = "http://localhost:8080/v1.0/topology/links"
	url_switch = "http://localhost:8080/stats/switches"
	url_flow = "http://localhost:8080/stats/flow/"
	headers = {'Content-Type': 'application/json'}
	
	s = []
	
	if x == 1:
		print("0000")
		set_vlan()
	elif x == 2:
		resp = requests.get(url_topo, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		print(resp.text)
		print(222)
	elif x == 3:
		resp = requests.get(url_switch, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		s = resp.text
		print(resp.text)
		print(333)
	elif x == 5:
		# resp = requests.get(url_topo, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		# print(resp.text)
		get_links()
		# print(555)
	elif x == 6:
		for i in s:
			if i < '1' or i > '6':
				continue
			print("\nswitch " + i + "'s flow table is : \n")
			resp = requests.get(url_flow + str(i), headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
			print(resp.text, '\n')
		# print(333)

if __name__ == "__main__":
	main(1)
