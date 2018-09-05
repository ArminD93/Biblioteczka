#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio

import settings


step_count_UpDown = 23
step_count_LeftRight = 5


# #####################################################
def Check_Direction(list):


	
	i = 0        
	for pole in list:
		if i < len(list)-1:
			if list[i][0] < list[i+1][0] : 
				print "W gore"	
				settings.setPWM_UpDown()
				settings.Up(step_count_UpDown)
				settings.stopPWM_UpDown()
				
			elif list[i][0] > list[i+1][0] : 
				print "W dol"
				settings.setPWM_UpDown()		
				settings.Down(step_count_UpDown)
				settings.stopPWM_UpDown()	
					
			elif list[i][1] < list[i+1][1] : 
				print "W prawo"
				settings.setPWM_LeftRight()
				settings.Right(step_count_LeftRight)
				settings.stopPWM_LeftRight()
				
			elif list[i][1] > list[i+1][1] : 
				print "W lewo"	
				settings.setPWM_LeftRight()
				settings.Left(step_count_LeftRight)
				settings.stopPWM_LeftRight()
			i +=1
		else: break
            
# #####################################################      