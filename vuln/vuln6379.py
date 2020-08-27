# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p6379(portdic):
	p6379list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "6379":
			print(str(ip[0])+'\t请检查是否存在Redis存在弱口令')
			a = ip[0]+":6379:Redis端口开放，请检查是否存在Redis存在弱口令"
			p6379list.append(a)
			p6379list.append(do_nmap(ip[0]))
	return p6379list

def do_nmap(host_list):
	nm = nmap.PortScanner()
	b= nm.scan(hosts=host_list, arguments=' -p6379  --script redis-info.nse ')
	try:
		#a = nm[host_list]["tcp"][6379]["script"]['redis-info']
		if 'redis-info' and "memory" and "Version" in  str(b):
			print(str(host_list)+'\t存在Redis未授权访问漏洞')
			a = host_list+":6379:存在Redis未授权访问漏洞"
			return a
	except:
		pass