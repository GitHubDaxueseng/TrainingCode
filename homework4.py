# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:31:16 2018
@author: Google
"""
#Loading weather app
#!/usr/bin/env python
import urllib.request as r
addr=input('Plsease input your address:\n')
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+addr+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
import json
data=json.loads(data)

from matplotlib import pyplot

def tips(description):
	if(description == 'Clear'): return 'It\'s clear today,Why not come out to play?'
	elif(description == 'Clouds'): return 'Cloudy weather doesn\'t look good'
	elif(description == 'Rain'): return 'You better bring an umbrella before going out.'

#def chart():
	
	
d1temp = data['list'][2]['main']['temp']
d1description = data['list'][2]['weather'][0]['main']
d1temp_min = data['list'][2]['main']['temp_min']
d1temp_max = data['list'][2]['main']['temp_max']
d1pressure = data['list'][2]['main']['pressure']

d2temp = data['list'][10]['main']['temp']
d2description = data['list'][10]['weather'][0]['main']
d2temp_min = data['list'][10]['main']['temp_min']
d2temp_max = data['list'][10]['main']['temp_max']
d2pressure = data['list'][10]['main']['pressure']

d3temp = data['list'][18]['main']['temp']
d3description = data['list'][18]['weather'][0]['main']
d3temp_min = data['list'][18]['main']['temp_min']
d3temp_max = data['list'][18]['main']['temp_max']
d3pressure = data['list'][18]['main']['pressure']

d4temp = data['list'][26]['main']['temp']
d4description = data['list'][26]['weather'][0]['main']
d4temp_min = data['list'][26]['main']['temp_min']
d4temp_max = data['list'][26]['main']['temp_max']
d4pressure = data['list'][26]['main']['pressure']

d5temp = data['list'][34]['main']['temp']
d5description = data['list'][34]['weather'][0]['main']
d5temp_min = data['list'][34]['main']['temp_min']
d5temp_max = data['list'][34]['main']['temp_max']
d5pressure = data['list'][34]['main']['pressure']

if __name__ == '__main__':
	print('\n\n')
	print('City:'+addr)
	
	print('Day1:\n'+
		  'Temp:'+str(d1temp)+'\n'
		  'Description:'+d1description+'\n'
		  'Temp_min:'+str(d1temp_min)+'\n'
		  'Temp_max:'+str(d1temp_max)+'\n'
		  'Pressure:'+str(d1pressure)+'\n'
		  'Tips:'+tips(d1description)+'\n')
	
	print('Day2:\n'+
		  'Temp:'+str(d2temp)+'\n'
		  'Description:'+d2description+'\n'
		  'Temp_min:'+str(d2temp_min)+'\n'
		  'Temp_max:'+str(d2temp_max)+'\n'
		  'Pressure:'+str(d2pressure)+'\n'
		  'Tips:'+tips(d2description)+'\n'
		  )
	
	print('Day3:\n'+
		  'Temp:'+str(d3temp)+'\n'
		  'Description:'+d3description+'\n'
		  'Temp_min:'+str(d3temp_min)+'\n'
		  'Temp_max:'+str(d3temp_max)+'\n'
		  'Pressure:'+str(d3pressure)+'\n'
		  'Tips:'+tips(d3description)+'\n'
		  )
	
	print('Day4:\n'+
		  'Temp:'+str(d4temp)+'\n'
		  'Description:'+d4description+'\n'
		  'Temp_min:'+str(d4temp_min)+'\n'
		  'Temp_max:'+str(d4temp_max)+'\n'
		  'Pressure:'+str(d4pressure)+'\n'
		  'Tips:'+tips(d4description)+'\n'
		  )
	
	print('Day5:\n'+
		  'Temp:'+str(d5temp)+'\n'
		  'Description:'+d5description+'\n'
		  'Temp_min:'+str(d5temp_min)+'\n'
		  'Temp_max:'+str(d5temp_max)+'\n'
		  'Pressure:'+str(d5pressure)+'\n'
		  'Tips:'+tips(d5description)+'\n'
		  )
	
	print('\n'+'Temp Chart:')
	print('\t'+'1'+'-'*int(d1temp))
	print('\t'+'2'+'-'*int(d2temp))
	print('\t'+'3'+'-'*int(d3temp))
	print('\t'+'4'+'-'*int(d4temp))
	print('\t'+'5'+'-'*int(d5temp))
	
	
	tmp = [d1temp,d2temp,d3temp,d4temp,d5temp]
	
	day = [1,2,3,4,5]
	#生成图表
	pyplot.plot(day, tmp)
	pyplot.xlabel('Day')
	pyplot.ylabel('Temp')
	pyplot.title('Temp Charts')
	pyplot.fill_between(day, tmp, 10, color = 'green')
	#显示图表
	tmp2 = sorted(tmp)
	print('Sorted temp:'+'\n\t')
	print(tmp2)
