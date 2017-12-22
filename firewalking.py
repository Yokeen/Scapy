#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import scapy

conf.route.add(net='10.1.1.0/24',gw='202.100.1.10')    #为scapy添加路由，超越linux的路由表
print(conf.route)   #打印scapy的路由表

def Firewalking(dstaddr,ttlno,lport,hport):
	#定义方法，目的地址，TTL值，起始端口，结束端口
	result_raw = sr(IP(dst=dstaddr,ttl=ttlno)/TCP(dport=(lport,hport)),inter=1,timeout=5,verbose=False)
	#目的地址必须真是存在，流量确实被ACL放过，TTL抵达防火墙时为0，测试才能成功。
	result_list = result_raw[0].res
	for i in range(len(result_list)):
		icmp_fields = result_list[i][1]['ICMP'].fields # 提取响应中的ICMP字段，产生字典
		ip_fields = result_list[i][1]['IP'].fields
		scan_fields = result_list[i][0]['TCP'].fields    #提取发送数据包的TCP字段，并产生字典
		if icmp_fields['type'] == 11:  
		#如果ICMP类型为11，TTL超时(ICMP TYPE CODE对应表，11 TTL生存时间为0)，如果超时，这个端口是开的
			print('Firewall is at ' + ip_fields['src'] + ' Port ' + str(scan_fields['dport']) + 'is Open!!')

if __name__ == '__main__':
	Firewalking('x.x.x.x',0,20,40)