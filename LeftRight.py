#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper
import settings



try:
	#while True:
		settings.setPWM_LeftRight()
		
		settings.Right()
		
		settings.stopPWM_LeftRight()
		sleep(1)
		
		gripper.Gripper()
		
		settings.setPWM_LeftRight()
		
		settings.Left()

        
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    settings.stopPWM_LeftRight() # PWM stop
    settings.pi.stop()