#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper
import settings




try:
	#while True:
		settings.setPWM_UpDown()
		settings.Up()
		settings.stopPWM_UpDown()
		sleep(1)
		settings.setPWM_UpDown()
		settings.Down()

        
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    settings.stopPWM_UpDown() # PWM stop
    settings.pi.stop()