# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p1433(portdic):
	p1433list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "1433":
			print(str(ip[0])+'\t请检查是否存在MSSQL存在弱口令')
			a = ip[0]+":1433:MSSQL端口开放，请检查是否存在MSSQL存在弱口令"
			p1433list.append(a)
			pass
			#do_nmap(ip[0])
	return p1433list
	
def do_nmap(host_list):
	try:
		nm = nmap.PortScanner()
		nm.scan(hosts=host_list, arguments='-Pn -sC -p 1433 -max-hostgroup 3 -open -script ms-sql-brute.nse  -v')
		for host in nm.all_hosts():
			print(str(host)+'\t mssql sa弱口令爆破')
	except:
		pass