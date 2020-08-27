# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import http.client
from lib import *


def p4848(portdic):
	p4848list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "4848":
			p4848list.append(check(ip[0]))
	return p4848list

def check(ip):  
	try:

		selector = "/jdbc/jdbcConnectionPoolProperty.jsf?name=DerbyPool"
		port = 4848
		url = 'http://%s:%s%s' % (ip, port, selector)
		headers = { 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0;Windows NT 5.1; Trident/4.0)',
					'Host': '%s:%s' % (ip, port),
					'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'Accept-Language': 'en-us,en;q=0.5',
					'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
					'Accept-Encoding': 'gzip,deflate',
					'Connection': 'close',
					'Referer': url}
		conn = http.client.HTTPConnection(ip,port)
		conn.request(method="TRACE", url=url, headers=headers)
		response = conn.getresponse()
		conn.close()
		a = response.read()
		if "jdbc:"in a :
			print(str(ip)+'\t存在GlassFish未授权访问漏洞')
			a = ip+":4848:存在GlassFish未授权访问漏洞"
			return a
	except:
		pass