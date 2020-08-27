# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

from socket import *
import threading

threads = []
portdict= []

def portscanall():
	ipdata = open("./file/alive.txt","r")
	a = ipdata.readlines()
	for ip in a:
		ip = ip.strip("\n")
		portll(ip)
	ipdata.close()

def portll(ip):
	setdefaulttimeout(1)
	for i in range(65535):
		t = threading.Thread(target=portScanner,args=(ip,i))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()

def portScanner(host,port):
	try:
		port = int(port)
		s = socket(AF_INET,SOCK_STREAM)
		s.settimeout(1)
		result = s.connect((host,port))
		if result:
			pass
		else:
			print("发现端口开放\tip地址为:"+host+"\t端口为:"+str(port))
			portname = host +":"+str(port)
			portdict.append(portname)
		s.close()
	except:
		pass
	#print("发现端口未开放\tip地址为:"+host+"\t端口为:"+str(port))
def portscanalll():
	print("正在目标全部端口进行探测扫描")
	portalive=open("./file/port.txt",'a+')
	portscanall()
	for port in portdict:   
		portalive.write(port)
		portalive.write("\n")
	portalive.close()
	return portdict 