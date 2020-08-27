# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

from lib import *
import sys
import requests


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:49.0) Gecko/20100101 Firefox/49.0"}

def islive(ur,port):
	url='http://' + str(ur)+':'+str(port)+'/uddiexplorer/'
	url1='https://' + str(ur)+':'+str(port)+'/uddiexplorer/'
	error=['404','Not Found','找不到','安全狗','无权访问','403']
	try:
		requests.packages.urllib3.disable_warnings()
		r = requests.get(url, headers=headers,verify=False)
		for e in error:
			if r.status_code==200 and e not in r.text:
				u='http://' + str(url)+':'+str(port)+'/uddiexplorer/'
				print(str(url) + ':'+str(port)+'\t检测存在weblogic存在SSRF漏洞(CVE-2014-4210)')
				a = ur +":7001:检测存在weblogic存在SSRF漏洞(CVE-2014-4210) "
				return a
			else:
				pass
	except:
		requests.packages.urllib3.disable_warnings()
		r = requests.get(url1, headers=headers,verify=False)
		for e in error:
			if r.status_code==200 and e not in r.text:
				u='http://' + str(url)+':'+str(port)+'/uddiexplorer/'
				print(str(url) + ':'+str(port)+'\t检测存在weblogic存在SSRF漏洞(CVE-2014-4210)')
				a = ur +":7001:检测存在weblogic存在SSRF漏洞(CVE-2014-4210) "
				return a
			else:
				pass

def run(url,port):
	try:
		return islive(url,port)
	except:
		pass