import flow
import vlan
import ctrl
import create_topo
import threading
import time
import os
import sys
from flask import Flask, request
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)
flag = 0


@app.route('/put')
def flow_put():
    print("recv put yes!\n")
    # dif = request.args.get('difficulty')
    flow.main(2)
    return jsonify(1)

@app.route('/pall')
def ping_all():
    print("recv ryu_topo yes!\n")
    # os.system("gnome-terminal")
    os.system("gnome-terminal -e 'ryu-manager /home/chen/112101429/ryu/ryu/app/gui_topology/gui_topology.py --observe-links'")
    time.sleep(5)
    # create_topo.ryu_topo()
    os.system("gnome-terminal -e 'sudo mn --custom /home/chen/112101429/mininet/custom/t2.py --topo mytopo --controller remote --switch ovsk,protocols=OpenFlow13'")
    return jsonify(1)

@app.route('/del')
def flow_del():
    print("recv del yes!\n")
    # dif = request.args.get('difficulty')
    flow.main(1)
    return jsonify(1)

@app.route('/cnt')
def flow_cnt():
    print("recv cnt yes!\n")
    # dif = request.args.get('difficulty')
    return jsonify(flow.main(3))

@app.route('/vlan')
def set_vlan():
	global flag
	print("recv vlan yes!\n")
	print("flag = ", flag, "\n")
	if flag == 0:
		flag = 1
		# dif = request.args.get('difficulty')
		return jsonify(vlan.main(1))
	else:
		return jsonify(1)

@app.route('/create_topo')
def topo_create():
    print("recv ODL_topo yes!\n")
    os.system("gnome-terminal -- '/home/chen/112101429/distribution-karaf-0.4.4-Beryllium-SR4/bin/karaf'")
    # myth = threading.Thread(target=ctrl.st_ctrl)
    # myth.start()
    time.sleep(3)
    create_topo.new_topo()
    # os.system("start powershell.exe cmd /k '~/102101441/distribution-karaf-0.4.4-Beryllium-SR4/bin/karaf'")
    # os.system("sudo mn --custom ~/102101441/mininet/custom/lab2_topo.py --topo mytopo --controller remote --switch ovsk,protocols=OpenFlow13")
    # os.system("sudo mn --topo=single,3 --mac --controller=remote,ip=127.0.0.1,port=6633 --switch ovsk,protocols=OpenFlow10")
    # os.system("qj030504")
    
    return jsonify(1)

@app.route('/ctrl')
def run_ctrl():
    print("recv ctrl yes!\n")
    os.system("/home/chen/112101429/distribution-karaf-0.4.4-Beryllium-SR4/bin/karaf")
    return jsonify(1)


if __name__ == '__main__':
	app.run()
