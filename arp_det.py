# -*- coding:utf-8 -*-
from get_ip import get_ip_address
from get_mac import get_mac_address
from scapy.all import *
import sys

def get_arp(ipaddress,ifname = 'eth0'):
    local_ip = get_ip_address(ifname)  # 获得本机ip
    local_mac = get_mac_address(ifname) #获得本机mac

    result_raw = srp(Ether(src=local_mac,dst='FF:FF:FF:FF:FF:FF')/ARP(op=1,hwsrc=local_mac,hwdst='00:00:00:00:00:00',psrc=local_ip,pdst=ipaddress),iface=ifname,verbose=False)
    result_list = result_raw[0].res

    return result_list[0][1][1].fields['hwsrc']




#<Ether  dst=FF:FF:FF:FF:FF:FF src=00:0c:29:72:64:cc type=0x806 |<ARP  op=who-has hwsrc=00:0c:29:72:64:cc psrc=192.168.1.123 hwdst=00:00:00:00:00:00 pdst=192.168.1.117 |>>,
#<Ether  dst=00:0c:29:72:64:cc src=b8:86:87:3b:0d:c7 type=0x806 |<ARP  hwtype=0x1 ptype=0x800 hwlen=6 plen=4 op=is-at hwsrc=b8:86:87:3b:0d:c7 psrc=192.168.1.117 hwdst=00:0c:29:72:64:cc pdst=192.168.1.123 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


if __name__ == '__main__':
    if len(sys.argv)>1:
        ipaddress = sys.argv[1]
        if len(sys.argv) > 2:
            ifname = sys.argv[2]
    if len(sys.argv) > 2:
        print '[+]IP地址：'+ ipaddress + '\n' + '[+]MAC地址：'+get_arp(ipaddress,ifname)
    else:
        print '[+]IP地址：'+ ipaddress + '\n' + '[+]MAC地址：'+get_arp(ipaddress)