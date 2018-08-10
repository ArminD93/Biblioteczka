#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper
import settings




try:
	#while True:
		settings.setPWM()
		settings.Up()
		settings.stopPWM()
		sleep(1)
		settings.setPWM()
		settings.Down()

        
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    settings.stopPWM() # PWM stop
    settings.pi.stop()