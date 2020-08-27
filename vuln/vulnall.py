# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def vulnall(portdic):
	pvulnall=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "5900":
			print(str(ip[0])+'\t请检查VNC是否存在弱口令')
			a = ip[0]+":5900:VNC端口开放，请检查VNC是否存在弱口令"
			pvulnall.append(a)
		if ip[-1] == "5984":
			print(str(ip[0])+'\t请检查CouchDB是否存在CVE-2017-12636命令执行漏洞')
			b = ip[0]+":5984:CouchDB端口开放，检查CouchDB是否存在CVE-2017-12636命令执行漏洞"
			pvulnall.append(b)
		if ip[-1] == "2049":
			print(str(ip[0])+'\t请检查是否存在NFS未授权访问漏洞')
			c = ip[0]+":2049:NFS端口开放，请检查是否存在NFS未授权访问漏洞"
			pvulnall.append(c)  
		if ip[-1] == "50030":
			print(str(ip[0])+'\t请检查是否存在Hadoop未授权访问漏洞')
			d = ip[0]+":50030:Hadoop端口开放，请检查是否存在Hadoop未授权访问漏洞"
			pvulnall.append(d)	 
		if ip[-1] == "50070":
			print(str(ip[0])+'\t请检查是否存在Hadoop未授权访问漏洞')
			e = ip[0]+":50070:Hadoop端口开放，请检查是否存在Hadoop未授权访问漏洞"
			pvulnall.append(e) 
	return pvulnall