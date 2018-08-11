#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper
import settings




settings.setPWM_LeftRight()	
settings.Right()
settings.stopPWM_LeftRight()


settings.setPWM_UpDown()
settings.Up()
settings.stopPWM_UpDown() # PWM stop
	


settings.setPWM_LeftRight()
settings.Left()
settings.stopPWM_LeftRight()



settings.setPWM_UpDown()
settings.Down()
settings.stopPWM_UpDown()      
	

	
settings.pi.stop()