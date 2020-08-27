# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

from lib import *
import ldap3

def p389(portdic):
	p389list = []
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "389":
			p389list.append(check(ip[0]))	
	return p389list


def check(host):   
	try:
		port = 389   
		server = ldap3.Server(host,port, get_info=ldap3.ALL, connect_timeout=3)
		ldap3.Connection(server, auto_bind=True)
		if len(server.info.naming_contexts) > 0:
			print(str(host)+'\t389端口开放，存在LDAP匿名访问漏洞')
			a = host+":389:存在LDAP匿名访问漏洞"
			return a
		else:
			pass
	except:
		pass