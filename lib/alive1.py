# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

from scapy.all import *

def arp_scan(ip):
	try:
		arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
		res = srp1(arpPkt, timeout=1, verbose=0)
		ipalive=open("./file/alive.txt",'a+')
		if res:
			ip = res.psrc
			print(" 测试范围中:\t"+ip+"\t存活")
			ipalive.write(ip)
			ipalive.write("\n")
		else:
			pass
		ipalive.close()
	except:
		pass

