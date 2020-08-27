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
	mas.scan(ipstr, ports='1-65535', arguments=threads)
	for result in mas.scan_result['scan']: 
		yuanzu =list(mas.scan_result['scan'].values())
		port = list(yuanzu[0]["tcp"].keys())
		for i in port:
			ipdata =result+":"+ str(i)
			print("发现端口开放\tip地址为:"+result+"\t端口为:"+str(i))
			portdict.append(ipdata)
		# for  port in mas.scan_result['scan'].values()["tcp"].keys():
		#	 masscanport = result + ":" + port
		#	 print(masscanport)

def portscanalll(thread):
	ipdata = open("./file/alive.txt","r")
	ipstr = ipdata.read().replace("\n",",")
	masscanresult(ipstr,thread)
	ipdata.close()

	#print("发现端口未开放\tip地址为:"+host+"\t端口为:"+str(port))
def portmasscan_all(thread):
	print("正在目标全部端口进行Masscan探测扫描")
	portalive=open("./file/port.txt",'a+')
	portscanalll(thread)
	for port in portdict:   
		portalive.write(port)
		portalive.write("\n")
	portalive.close()
	return portdict 