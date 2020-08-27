# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import sys
import requests
from lib import *

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:49.0) Gecko/20100101 Firefox/49.0"}

def islive(ur,port):
	url='http://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
	url1='https://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
	error=['404','Not Found','找不到','安全狗','无权访问','403']
	try:
		requests.packages.urllib3.disable_warnings()
		r = requests.get(url, headers=headers,verify=False)
		for e in error:
			if r.status_code ==200 and e not in r.text :
				u='http(s)://' + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
				print(str(url) + ':'+str(port)+'\t请检测weblogic是否存在弱密码')
				a = url +":7001:请检测weblogic是否存在弱密码"
				return a
			else:
				pass
	except:
		requests.packages.urllib3.disable_warnings()
		r = requests.get(url1, headers=headers,verify=False)
		for e in error:
			if r.status_code ==200 and e not in r.text :
				u='http(s)://' + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
				print(str(url) + ':'+str(port)+'\t请检测weblogic是否存在弱密码')
				a = url +":7001:请检测weblogic是否存在弱密码"
				return a
			else:
				pass

def run(url,port):
	try:
		a = islive(url,port)
		return a
	except:
		pass

