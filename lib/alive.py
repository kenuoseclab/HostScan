# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import subprocess
import os
import sys
import re

def unixping(ip):
	try:
		p = subprocess.Popen(["ping -c 1 -W 20 " +ip],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell = True)
		out = p.stdout.read()
		ipalive=open("./file/alive.txt",'a+')
		if "ttl" in str(out):
			print("测试范围中:\t"+ip+"\t存活")
			ipalive.write(ip)
			ipalive.write("\n")
		else:
			pass
		ipalive.close()
	except:
		ipalive.close()
		exit()

def winping(ip):
	try:
		p = subprocess.Popen(['ping','-n','1','-w','20',ip],
					stdout=subprocess.PIPE,
					stdin = subprocess.PIPE,
					stderr = subprocess.PIPE,
					shell = True)
		output = p.stdout.read().decode("gbk").upper()
		ipalive=open("./file/alive.txt",'a+')
		if "TTL" in output:
			print("测试范围中:\t"+ip+"\t存活")
			ipalive.write(ip)
			ipalive.write("\n")
		else:
			pass
		ipalive.close()
	except:
		ipalive.close()
		exit()
	
	
if __name__ == "__main__":
	ip = sys.argv[1]
	if os.name =="nt":
		winping(ip)
	else:
		unixping(ip)
