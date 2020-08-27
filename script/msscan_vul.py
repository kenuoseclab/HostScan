# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import masscan

portdict = []

def masscanresult(ipstr,thread):
	mas = masscan.PortScanner()
	threads = '--max-rate ' + str(thread)
	mas.scan(ipstr, ports="21,22,23,80,161,389,443,445,512,513,514,873,1025,111,1433,1521,5560,7778,2601,2604,3128,3306,3312,3311,3389,4440,5432,5900,5984,6082,6379,7001,7002,7778,8000,8001,8080,8089,8090,9090,8083,8649,8888,9200,9300,10000,11211,27017,27018,28017,50000,50070,50030", arguments=threads)
	for result in mas.scan_result['scan']: 
		yuanzu =list(mas.scan_result['scan'].values())
		port = list(yuanzu[0]["tcp"].keys())
		for i in port:
			ipdata =result+":"+ str(i)
			print("发现端口开放\tip地址为:"+result+"\t端口为:"+str(i))
			portdict.append(ipdata)
		#for  port in mas.scan_result['scan'].values()["tcp"].keys():
		#	masscanport = result + ":" + port
		#	print(masscanport)

def portscanalll(thread):
	ipdata = open("./file/alive.txt","r")
	ipstr = ipdata.read().replace("\n",",")
	masscanresult(ipstr,thread)
	ipdata.close()

	#print("发现端口未开放\tip地址为:"+host+"\t端口为:"+str(port))
def portmasscan_vul(thread):
	print("正在目标全部端口进行Masscan探测扫描")
	portalive=open("./file/port.txt",'a+')
	portscanalll(thread)
	for port in portdict:   
		portalive.write(port)
		portalive.write("\n")
	portalive.close()
	return portdict 