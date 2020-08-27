# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p3306(portdic):
	p3306list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "3306":
			#do_nmap(ip[0])
			print(str(ip[0])+'\t请检查是否存在MYSQL存在弱口令')
			a = ip[0]+":3306:MYSQL端口开放，请检查是否存在MYSQL存在弱口令"
			p3306list.append(a)
			p3306list.append(do_nmap1(ip[0]))
	return p3306list

def do_nmap(host_list):
	nm = nmap.PortScanner()
	nm.scan(hosts=host_list, arguments='-Pn -sC -p 3306 -max-hostgroup 3 -open -script mysql-brute.nse -v')
	for host in nm.all_hosts():
		print(str(host)+'\t mysql root弱口令简单爆破，存在弱口令')

def do_nmap1(host_list):
	nm = nmap.PortScanner()
	b = nm.scan(hosts=host_list, arguments='-p 3306  -script mysql-vuln-cve2012-2122.nse ')
	try:
		#a = nm[host_list]["tcp"][3306]["script"]['mysql-vuln-cve2012-2122']
		if "mysql-vuln-cve2012-2122" and "VULNERABLE" in str(b) :
			print(str(host_list)+'\t存在Mysql身份认证漏洞')
			a = host_list+":3306:存在CVE-2012-2122-Mysql身份认证漏洞"
			return a
	except:
		pass