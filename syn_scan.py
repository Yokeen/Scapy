#!/usr/bin/env python
# -*-coding:utf-8 -*-

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy import *

#传入目的地址，扫描开始的端口lport，扫描结束的端口hport
def syn_scan(hostname,lport,hport):
	raw = sr(IP(dst=hostname)/TCP(dport=(int(lport),int(hport)),flags="S"),verbose = False)
	# 传入的主机可以是一个列表，端口处支持元组，两个端口号，flag是S代表SYN，也可以填2
	# ACK是16，SYN为2，值是18说明是开的，这里的数字你可以去看一个完整的三次握手
	raw_list = raw[0].res
	for i in range(len(raw_list)):
		tcpfields = raw_list[i][1][1].fields   #把每一个接收的数据报的TCP头部产生字典
		if tcpfields['flags'] == 18:
			print('端口号：' + str(tcpfields['sport']) + 'is Open!!!')

if __name__ == '__main__':
	host = raw_input('输入要扫描的主机IP地址：')
	low_port = input('输入要扫描的起始端口：')
	high_port = input('输入要扫描的结束端口：')
	syn_scan(host,low_port,high_port)
