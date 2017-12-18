# -*- coding:utf-8 -*-
#利用os和正则表达式获取本地指定网卡的IP
import os, re

def get_ip_address(iface):
    data = os.popen('ifconfig '+ iface).read()
    words = data.split()
    ip_found = 0  #是否找到ip地址
    network_found = 0 #是否找到网络地址
    broadcast_found = 0 #是否找到广播地址
    location = 0  #用来记录位置
    ip_index = 0  #Ip的位置
    network_index = 0
    broadcast_index = 0
    for x in words:
        if re.findall('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})',x):
            result = re.findall('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})',x)
            if result[0][3] == '0': #最后一个字段为0，即网络地址
                network_found = 1
                network_index = location
                location += 1
                # print '网络地址为:'+ words[network_index]
            elif result[0][3] == '255':
                broadcast_found = 1
                broadcast_index = location
                location += 1
                # print '广播地址为:'+ words[broadcast_index]
            else:
                ip_found = 1
                ip_index = location
                location += 1
        else:
            location += 1

    if ip_found == 1:
        ip = words[ip_index]

    else:
        ip = None
    return ip
