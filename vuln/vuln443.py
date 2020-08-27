# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p443(portdic):
	p443list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "443":
			p443list.append(do_nmap(ip[0]))
			p443list.append(phpstudy(ip[0]))
	return p443list

def do_nmap(host_list):
	nm = nmap.PortScanner()
	a= nm.scan(hosts=host_list, arguments='-p 443  -script ssl-heartbleed.nse')
	a = str(a)
	try:
		if "ssl-heartbleed" or "VULNERABLE" in a :
			print(str(host)+'\t存在心脏滴血漏洞')
			return host_list+":443:存在心脏滴血漏洞"
	except:
		pass

def phpstudy(host_list):
	header ={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
				"Accept-Language": "zh-CN",
				"Accept-Encoding": "gzip,deflate",
				"X-Forwarded-For": "8.8.8.8",
				"Connection": "close",
				"Accept-charset": "c3lzdGVtKCdlY2hvIEpFMlNlSnVzdFRydXN0bWUnKSA7",
				"Upgrade-Insecure-Requests": "1"}
	try:
		a = requests.get("https://" + host_list,headers=header,timeout=5)
		if "JE2SeJustTrustme" in a.text:
			print(str(host_list)+'\t存在phpstudy后门')
			ff = host_list + ":443:存在phpstudy后门"
			return ff
		else:
			pass
	except:
		pass