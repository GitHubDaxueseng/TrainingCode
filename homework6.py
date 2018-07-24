# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:35:27 2018
Taobao spider
	1.4 goods in a list
	2.print 36 goods
	3.sorted by price
	4.sorted by seal_account
	5.list posted goods
@author: Google
"""
import urllib.request as r
import json
import csv
page = 100
DATA = []
FreeFEE = []
#DATA.append({'a':1})
goods = []
all_price = []
salesnum = []
keywords = input('Input thing that you want to search:\n')
#url="https://s.taobao.com/search?q="+keywords+"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s="+str((N-1)*44)
url2='https://s.taobao.com/search?q='+keywords+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1ie=utf8&initiative_id=tbindexz_20170306&ajax=true&s={}'.format(str((page-1)*44))
#print(url2)
data_list=r.urlopen(url2).read().decode('utf-8','ignore')
data_list=json.loads(data_list)

#data dic->mods dic->itemlist ->data dic->auction list-> o index dic->title
#title = data['mods']['itemlist']['data']['auction'][0]['title']
#price = data['mods']['itemlist']['data']['auction'][0]['view_price']
#description = data['mods']['itemlist']['data']['auction'][0]['price']

auction = data_list['mods']['itemlist']['data']['auctions']

for i in range(0,4):
	print("Goods" + str(i+1))
	print('Title' + auction[i]['raw_title'])
	print('Price'+ auction[i]['view_price'])
	print('Fee' + auction[i]['view_fee'])
	print('Sales:' + auction[i]['view_sales'])
	print('**********'+'\n')
'''
item = auction[i][2]
print(item)
'''
f = open('taobao.csv','a',encoding = 'gbk')
wf = csv.writer(f)
if page == 1:
	x = 36
else:
	x = 44
for p in range(page):
	for i in range(0,x):
		print("Goods" + str(i+1))
		print('Title:' + auction[i]['raw_title'])
		print('Price:' + auction[i]['view_price'])
		print('Fee:' + auction[i]['view_fee'])
		print('Sales:' + auction[i]['view_sales']+'\n')
		goodsInfo = [
				(str((auction[i]['raw_title']))),
				(str((auction[i]['view_price'])))
				#(data_list['mods']['itemlist']['data']['auctions'][i]['view_fee']),
				#(data_list['mods']['itemlist']['data']['auctions'][i]['view_sales'])
				]
		wf.writerows(goodsInfo)
		'''wf.writerows(
				[(str(data_list['mods']['itemlist']['data']['auctions'][i]['raw_title']),
				str(data_list['mods']['itemlist']['data']['auctions'][i]['view_price']),
				str(data_list['mods']['itemlist']['data']['auctions'][i]['view_fee']),
				str(data_list['mods']['itemlist']['data']['auctions'][i]['view_sales']))]
				)'''
		if i % 4 == 0: print('*'*20)
		temp = {
					'Title' : auction[i]['raw_title'],
					'Price' : auction[i]['view_price'],
					'Fee' : auction[i]['view_fee'],
					'Sales' : auction[i]['view_sales']
				}	
		#DATA.append(temp)
f.close()


for i in range(0,36):
	all_price.append(float(DATA[i]['Price']))
print(all_price)

for i in range(0,36):
	salesnum.append(int(str(DATA[i]['Sales'][:-3])))
print('Best_sales:'+str(max(salesnum))+'\nAll_Sales:')
print(salesnum)

def getMax(allprice):
	maxPrice = max(allprice)
	print('Max_Price:'+str(maxPrice))
	print('Sort:')
	print(sorted(all_price))
getMax(all_price)	

def getMin(allprice):
	minPrice = min(allprice)
	print('Min_Price:'+str(minPrice))
getMin(all_price)	

print(DATA[2]['Fee'])

def isFree():
	for i in range(0,36):
		if DATA[i]['Fee'] == '0.00':

			print("Goods" + str(i+1)+'  is exemption from postage')
			print('Title:' + auction[i]['raw_title'])
			print('Price:' + auction[i]['view_price'])
			print('Fee:' + auction[i]['view_fee'])
			print('Sales:' + auction[i]['view_sales']+'\n')

			if i % 4 == 0: print('*'*20)
			temp = {
						'Title' : auction[i]['raw_title'],
						'Price' : auction[i]['view_price'],
						'Fee' : auction[i]['view_fee'],
						'Sales' : auction[i]['view_sales']
					}	
			FreeFEE.append(temp)
print(DATA)
print(DATA[0]['Price'])


