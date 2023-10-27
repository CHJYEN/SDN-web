#!/usr/bin/python
import requests
import json
from requests.auth import HTTPBasicAuth

def main(op):
	url_del = "http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/"
	url_put = "http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1"
	url_get = "http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/opendaylight-flow-table-statistics:flow-table-statistics"
	url_cnt = "http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/table/0/"
	url_topo = "http://127.0.0.1:8080/restconf/operational/network-topology:network-topology/"
	headers = {'Content-Type': 'application/json'}
	with open('flowtable.json') as f:
		jstr = f.read()
		
	if op == 1:
		resp = requests.delete(url_del, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		return resp
	elif op == 2:
		resp = requests.put(url_put, jstr, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		return resp
	elif op == 3:
		resp = requests.get(url_cnt, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		res = json.loads(resp.text)
		# print(resp.text)
		if len(res) != 0:
			cnt = len(res['flow-node-inventory:table'][0]['flow'])
		# print(res['flow-node-inventory:table'][0]['flow'])
		else:
			cnt = 0
		print("\nflow-num = ", cnt)
		return cnt
	elif op == 4:
		resp = requests.get(url_get, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		# res = json.loads(resp.text)
		print(resp.text)
		# cnt = res['opendaylight-flow-table-statistics:flow-table-statistics']['active-flows']
		# print("\nflow-num = ", cnt)
	elif op == 5:
		resp = requests.get(url_topo, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
		print(resp.text)
		return resp.text

if __name__ == "__main__":
	main(1)
