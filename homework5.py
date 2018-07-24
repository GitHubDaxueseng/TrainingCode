# -*- coding: utf-8 -*-
"""
Get weather informations from weather API
Created on Wed Jul 18 09:58:38 2018

@author: Google
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:31:16 2018
@author: Google
"""
#Loading weather app
#!/usr/bin/env python
import urllib.request as r
from matplotlib import pyplot
import json

addr=input('Plsease input your address\n')
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+addr+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
data=json.loads(data)

day = ['1','2','3','4','5']
a = [1,2,3,4,5]
b = [2,10,18,26,34]
dtemp = []
description = []
temp_min = []
temp_max = []
pressure = []


def tips(description):
	if(description == 'Clear'): return 'It\'s clear today,Why not come out to play?'
	elif(description == 'Clouds'): return 'Cloudy weather doesn\'t look good'
	elif(description == 'Rain'): return 'You better bring an umbrella before going out.'

def weatherInfo():
	for i in a:
		print(i)
		#print(b[i-1])
		dtemp.append(data['list'][b[i-1]]['main']['temp'])
		description.append(data['list'][b[i-1]]['weather'][0]['main'])
		temp_min.append(data['list'][b[i-1]]['main']['temp_min'])
		temp_max.append(data['list'][b[i-1]]['main']['temp_max'])
		pressure.append(data['list'][b[i-1]]['main']['pressure'])

weatherInfo()
def weatherInfoPrint():
	for i in a:
		print('Day'+str(i)+':\n'+
		  'Temp:'+str(dtemp[i-1])+'\n'
		  'Description:'+description[i-1]+'\n'
		  'Temp_min:'+str(temp_min[i-1])+'\n'
		  'Temp_max:'+str(temp_max[i-1])+'\n'
		  'Pressure:'+str(pressure[i-1])+'\n'
		  'Tips:'+tips(description[i-1])+'\n'
		  )
	
def chart():
	print('\n'+'Temp Chart:')
	for i in a:
		tmp = int(dtemp[i-1])
		print('\t'+str(i)+'-'*tmp)

if __name__ == '__main__':
	
	weatherInfoPrint()
	chart()
	#生成图表
	pyplot.plot(day, dtemp)	
	pyplot.xlabel('Day')
	pyplot.ylabel('Temp')
	pyplot.title('Temp Charts')
	#pyplot.fill_between(day, dtemp, 5, color = 'green')
	#显示图表
	tmp2 = sorted(dtemp)
	print('Sorted temp:'+'\n\t')
	print(tmp2)