# Scapy
> 学习了秦柯老师的Scapy教程之后写的相关Scapy脚本，没做什么改进....
> 学会之后下次需要用的时候再做自己想要的功能

## arp_det.py
探测指定IP的MAC地址
usage：arp_det.py dst_ip

## get_ip/mac.py
获取本地指定网卡名的IP和MAC地址

## arp_spoof.py
实施ARP毒化
usage：arp_spoof.py ip1 ip2
详情见代码

## arp_scan.py
传入一个网段的前缀【网络地址】，例如192.168.1，扫描存在的ip与对应的MAC地址

## syn_scan.py  
syn扫描
输入主机名，起始端口，结束端口进行扫描

## firewalking.py
防火墙开放端口扫描
主机名，ttl值，起始端口，结束端口
