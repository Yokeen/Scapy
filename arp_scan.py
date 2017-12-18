#-*- coding:utf-8 -*-
from scapy.all import *
from get_mac import get_mac_address
from get_ip import get_ip_address

def arp_scan(network,ifname='eth0'):
    #只需要传入一个网段的前缀
    localip = get_ip_address(ifname)
    localmac = get_mac_address(ifname)
    ip_list = []
    prefix = network.split('.')
    #产生一个扫描的清单
    for i in range(254):
        ipno = prefix[0] + '.' + prefix[1] + '.' + prefix[2] + '.' + str(i+1)
        ip_list.append(ipno)
    for ip in ip_list:

        result_raw = srp(Ether(src=localmac,dst='FF:FF:FF:FF:FF:FF')/ARP(op=1,hwsrc=localmac,psrc=localip,hwdst='00:00:00:00:00:00',pdst=ip),iface=ifname,timeout=5,verbose=False)
        result = result_raw[0].res
        try:
            print '[+]正在扫描：' + ip
            print 'MAC address: ' + result[0][1][1].fields['hwsrc'] + '-->' + result[0][1][1].fields['psrc']
        except IndexError:
            print '局域网不存在此ip'

if __name__ == '__main__':
    arp_scan('192.168.1')

