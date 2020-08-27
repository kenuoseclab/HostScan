# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p5432(portdic):
	p5432list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "5432":
			print(str(ip[0])+'\t请检查PostgreSQL是否存在弱口令')
			a = ip[0]+":5432:PostgreSQL端口开放，请检查PostgreSQL是否存在弱口令"
			p5432list.append(a)
			pass
			#do_nmap(ip[0])
	return p5432list
	