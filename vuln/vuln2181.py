# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

from lib import *
import socket

def p2181(portdic):
	p2181list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "2181":
			p2181list.append(check(ip[0]))
	return p2181list

def check(ip):
	try:
		socket.setdefaulttimeout(3)
		s = socket.socket()
		s.connect((ip, 2181))
		flag = b"envi"
		s.send(flag)
		data = s.recv(1024)
		s.close()
		if b'Environment' in data:
			print(str(ip)+'\t存在zookeeper未授权访问漏洞')
			a = ip+":2181:存在zookeeper未授权访问漏洞"
			return a
	except:
		pass