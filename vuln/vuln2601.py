# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *
import requests

def p2601(portdic):
	p2601list = []
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "2601":
			p2601list.append(zebra(ip[0]))
		if ip[-1] == "2604":
			p2601list.append(zebra1(ip[0]))
	return p2601list

def zebra(host_list):
	try:
		url = "https://"+host_list+":2601/login"
		requests.packages.urllib3.disable_warnings()
		a = requests.get(url,timeout=5,verify=False)
		if a.status_code == 200:
			print(str(host_list)+'\t识别到Zebra路由，请检测默认口令zebra:zebra')
			ff = host_list + ":2601:识别到Zebra路由，请检测默认口令zebra:zebra"
			return ff
		else:
			pass
	except:
		pass


def zebra1(host_list):
	try:
		url = "https://"+host_list+":2604/login"
		requests.packages.urllib3.disable_warnings()
		a = requests.get(url,timeout=5,verify=False)
		if a.status_code == 200:
			print(str(host_list)+'\t识别到Zebra路由，请检测默认口令zebra:zebra')
			ff = host_list + ":2604:Zebra端口开放，识别到Zebra路由，请检测默认口令zebra:zebra"
			return ff
		else:
			pass
	except:
		pass