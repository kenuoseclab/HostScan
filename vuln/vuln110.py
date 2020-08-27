# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p110(portdic):
	p110list = []
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "110":
			print(str(ip[0])+'\t请检查是否存在POP存在弱口令')
			a = ip[0]+":110:110端口开放，请检测是否存在POP存在弱口令"
			p110list.append(a)
			pass
		if ip[-1] == "995":
			print(str(ip[0])+'\t请检查是否存在POP存在弱口令')
			b = ip[0]+":995:995端口开放，请检测是否存在POP存在弱口令"
			p110list.append(b)
			pass
			#do_nmap(ip[0])
	return  p110list

def do_nmap(host_list):
	nm = nmap.PortScanner()
	nm.scan(hosts=host_list, arguments='-Pn -sC -p 110 -max-hostgroup 3 -open -script pop3-brute.nse -v')
	for host in nm.all_hosts():
		print(str(host)+'\tpop简单弱口令爆破，存在弱口令')