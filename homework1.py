# -*- coding: utf-8 -*-
"""
Work1:
	Define a weather list and print each day's weather info
	If Wednesday is this day, print Wednesday
Created on Tue Jul 17 15:04:36 2018

@author: Google
"""

weather = [25,12,36,23,40,33,32]
print(weather[0])
print(weather[1])
print("WED  "+str(weather[2])+'бу')
print(weather[3])
print(weather[4])
print(weather[5])
print(weather[6])

print('\n\n')

weather1 = {
		'SUN':['25','Cloudy'],
		'MON':['26','Cloudy'],
		'TUE':['27','Cloudy'],
		'WED':['28','Cloudy'],
		'THU':['29','Cloudy'],
		'FRI':['30','Cloudy'],
		'SAT':['31','Cloudy']
		}

print('TUE: '+weather1['TUE'][0]+' '+weather1['TUE'][1])