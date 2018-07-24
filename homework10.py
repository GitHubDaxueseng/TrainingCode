# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:18:35 2018

@author: Google
"""
#P1  Get school id
original = open('C:/Users/Google/Documents/Tencent Files/1273391194/FileRecv/all_school.txt','r',encoding = 'utf-8')
url = original.readlines()
for i in range(len(url)):
	splitedUrl = url[i].split('ie-')[1].split('.')[0]
	print(splitedUrl)
	
#P2  Get city id
import re
original1 = open('C:/Users/Google/Documents/Tencent Files/1273391194/FileRecv/XML高考派城市.txt','r')
xmlList = original1.readlines()
#regex
for i in range(len(xmlList)):
	cityId = re.findall(r', (.*?)\)',xmlList[i])
	if len(cityId) > 0:
		print(cityId[0])
