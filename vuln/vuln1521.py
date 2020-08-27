# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p1521(portdic):
	p1521list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "1521":
			print(str(ip[0])+'\t请检查ORACLE是否存在弱口令')
			a = ip[0]+":1521:Oracle端口开放，请检查Oracle是否存在弱口令"
			p1521list.append(a)
			pass
			#do_nmap(ip[0])
	return p1521list   