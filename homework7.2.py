# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:37:56 2018

@author: Google
"""
import urllib.request as r
#import json
MAX = 100
url_list = []
json_list = []
for i in range(MAX):
	try:
		url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&ie=utf8&loc=%E5%98%89%E5%85%B4&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48&ajax=true&s='+(str((i)*44))
		data = r.urlopen(url).read().decode('utf-8','ignore')
		print(str(i))
	except Exception as err:
		print('err')
	f = open('taobao_json.txt','a',encoding='utf-8')
	f.write(data+'\n')
f.close()
