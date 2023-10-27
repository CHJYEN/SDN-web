from mininet.net import Mininet  
from mininet.node import Controller, OVSKernelSwitch  
from mininet.link import TCLink
import os
import threading

def create_topo():
    # 创建网络  
    print("Start create topo......\n")
    # os.system("~/102101441/distribution-karaf-0.4.4-Beryllium-SR4/bin/karaf")
    # os.system("gnome-terminal -e 'bash -c \"~/102101441/distribution-karaf-0.4.4-Beryllium-SR4/bin/karaf; exec bash\"'")
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch, link=TCLink)  
    
    # 添加一台交换机  
    switch = net.addSwitch('s1')  
    
    # 添加三台主机  
    h1 = net.addHost('h1')  
    h2 = net.addHost('h2')  
    h3 = net.addHost('h3')  
    
    # 连接主机到交换机  
    net.addLink(h1, switch)
    net.addLink(h2, switch)
    net.addLink(h3, switch)
    
    # 启动网络  
    net.start()

    net.interact()

def ctrl_start():
    print("Start ctrl......\n")
    os.system("/home/chen/112101429/distribution-karaf-0.4.4-Beryllium-SR4/bin/karaf")

def ryu_topo():
	os.system("sudo mn --custom /home/chen/112101429/mininet/custom/lab2_topo.py --topo mytopo --controller remote --switch ovsk,protocols=OpenFlow13")

def new_topo():
	os.system("sudo mn --topo=single,3 --mac --controller=remote,ip=127.0.0.1,port=6633 --switch ovsk,protocols=OpenFlow10")

if __name__ == "__main__":
    new_topo()
    """
    threads = []
    threads.append(
        threading.Thread(target=create_topo)
    )
    threads.append(
        threading.Thread(target=ctrl_start)
    )
    for thread in threads:
        thread.start()
    """
