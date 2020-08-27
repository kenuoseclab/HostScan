# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
import requests
from lib import *

def p8080(portdic):
	p8080list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "8080":
			p8080list.append(iisshort(ip[0]))
	return p8080list

def iisshort(host_list):
	try:
		requests.packages.urllib3.disable_warnings()
		host_list1 = host_list+":8080/*~1*/.aspx"
		host_list2 = host_list+":8080/asdfasfasdf*~1*/.aspx"
		a = requests.get("http://" + host_list1,timeout=5,verify=False)
		b = requests.get("http://" + host_list2,timeout=5,verify=False)
		if a.status_code == 404 and b.status_code != 404:
			print(str(host_list)+'\t存在IIS短文件名漏洞')
			c = host_list+":8080:存在IIS短文件名漏洞"
			return c
	except:
		pass