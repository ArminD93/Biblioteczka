#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper
import settings

step_count_LeftRight=20


try:
	#while True:
		settings.setPWM_LeftRight()
		
		settings.Right(step_count_LeftRight)
		
		settings.stopPWM_LeftRight()
		sleep(1)
		
	
		
		settings.setPWM_LeftRight()
		
		settings.Left(step_count_LeftRight)

        
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    settings.stopPWM_LeftRight() # PWM stop
    settings.pi.stop()