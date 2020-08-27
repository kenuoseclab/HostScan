# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import sys
from lib import *
import threading
import os
import time

#线程类
class Request(threading.Thread):
	def __init__(self, alive_queue, livecase, *args, **kwargs):
		super(Request, self).__init__(*args, **kwargs)
		self.alive_queue = alive_queue
		self.livecase = livecase

	def run(self):
		while True:
			if self.alive_queue.empty():
				break
			ip = self.alive_queue.get()
			self.alive(ip)
	def alive(self,ip):
		if self.livecase =="1":
			try:
				if os.name == "nt":
					winping(ip)
				else:
					unixping(ip)
			except:
				pass
		elif self.livecase =="2":
			arp_scan(ip)
		else:
			os._exit(0)

#通用处理
def father(iplist):
	print("正在对目标地址进行存活检测")
	ascii_banner = pyfiglet.figlet_format("hostscan")
	print(ascii_banner)
	print("请选择存活探测的方式 ")
	print('''1.Ping探测 (适用于没有禁用Ping)\n2.ARP探测 （适用于禁用Ping探测,不能跨网段)\n\n任意键退出程序''')
	print("\n")
	livecase = input(u"请选择探测存活方式：")
	
	alive_queue = Queue(len(iplist))
	for ip in iplist:
		alive_queue.put(ip)
	thread_list = []
	for u in range(500):
		t = Request(alive_queue,livecase)
		t.start()
		thread_list.append(t)
	for i in thread_list:
		i.join()
	print("存活地址已成功写入/file/alive.txt中")
	print("\n")
	vullist = []
	portdic = []
	alivelist = []
	ipdata = open("./file/alive.txt","r")
	alivedata = ipdata.readlines()
	for i in alivedata:
		alivelist.append(i.strip("\n"))
	ipdata.close()
	ascii_banner = pyfiglet.figlet_format("hostscan")
	print(ascii_banner)
	print("请选择端口扫描的方式 ")
	print('1.仅探测风险端口 (Socket方式,适用于少IP)\n2.仅探测风险端口 (Masscan方式,适用于多IP)\n3.探测常规端口 (Nmap的top1000端口)\n4.探测全端口 (Socket方式,适用于少IP)\n5.探测全端口 (Masscan方式,适用于多IP)\n\n任意键退出程序,并生成报告')
	print("\n")
	scancase = input(u"请填写扫描方式：")
	if scancase == "1":
		portdic = portscan()
	elif scancase == "2":
		threadd = input(u"请填写进程配置(默认2000)：")
		if threadd == "":
			threadd ="2000"
		portdic = portmasscan_vul(threadd)
	elif scancase == "3":
		portdic = nmapscan()
	elif scancase == "4":
		portdic = portscanalll()
	elif scancase == "5":
		threadd = input(u"请填写进程配置(默认2000)：")
		if threadd == "":
			threadd ="2000"
		portdic = portmasscan_all(threadd)
	else:
		resultreport(iplist,alivelist,portdic,vullist)
		exit()
	print("\n")
	ascii_banner = pyfiglet.figlet_format("hostscan")
	print(ascii_banner)
	print("是否进行风险端口漏洞探测 ")
	print('1.探测风险端口\n\n任意键退出程序，并生成当前进度报告')
	print("\n")
	scancase = input(u"请选择是否进行漏洞探测：")
	if scancase == "1":
		#vullist是存在漏洞的ip地址以及漏洞信息 
		vullist = p21(portdic)+p23(portdic)+p22(portdic)+p80(portdic)+p110(portdic)+p143(portdic)+p443(portdic)+p445(portdic)+p873(portdic)+p1433(portdic)+p3306(portdic)+p6379(portdic)+p8080(portdic)+p9200(portdic)+p11211(portdic)+p27017(portdic)+p1521(portdic)+p2601(portdic)+vulnall(portdic)+p4848(portdic)+p2181(portdic)+p389(portdic)+p5432(portdic)+p3389(portdic)+poolmana(portdic)
		resultreport(iplist,alivelist,portdic,vullist)
	elif scancase == "2":
		resultreport(iplist,alivelist,portdic,vullist)
	else:
		resultreport(iplist,alivelist,portdic,vullist)
		exit()
	#存活数据
	#alivelist = []
	#端口数据
	#portdic
	#漏洞数据
	#vullist   

#报告模块
def resultreport(iplist,alivelist,portdic,vullist):
	vullist = list(filter(None, vullist))
	path = reportfile(iplist,alivelist,portdic,vullist) 
	print('生成报告成功')
	print('报告地址：'+path)
	print('扫描结束')
	if os.path.exists("./file/alive.txt"):
		os.remove("./file/alive.txt")
	if os.path.exists("./file/port.txt"):
		os.remove("./file/port.txt")


#主程序
if __name__ == "__main__":
	if sys.version_info.major < 3:
		sys.stdout.write("请使用Python 3版本运行hostscan脚本\n")
	else:
		import argparse
		import pyfiglet
		from IPy import IP
		import telnetlib
		from script import *
		from  queue  import Queue
		from vuln import *
		import platform

		#重置部分
		if os.path.exists("./file/alive.txt"):
			os.remove("./file/alive.txt")
		if os.path.exists("./file/port.txt"):
			os.remove("./file/port.txt")

		#头部信息部分
		ascii_banner = pyfiglet.figlet_format("HostScan")
		print(ascii_banner)
		print("\n")
		parser = argparse.ArgumentParser()
		#脚本执行帮助部分
		print("请输入 -h 获取命令帮助 " + "\n")
		parser.add_argument("-i", "--ip", help = ' -i 参数，指定的IP范围') 
		parser.add_argument("-f", "--file", help = ' -f 参数，导入IP地址文件')
		args = parser.parse_args()
		params = vars(args)
		#导入文件处理簇
		if args.file:
			iplist = importfile(args.file)
			father(iplist)
		#直接输入范围处理簇
		if args.ip:
			ip =str(args.ip)
			iplist = IPinfo(ip)
			father(iplist)