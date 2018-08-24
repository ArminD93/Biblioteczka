#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio

import settings


step_count_UpDown = 69 #23

try:
	#while True:
		settings.setPWM_UpDown()
		settings.Up(step_count_UpDown)
		settings.stopPWM_UpDown()
		sleep(1)
		settings.setPWM_UpDown()
		settings.Down(step_count_UpDown)

        
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    settings.stopPWM_UpDown() # PWM stop
    settings.pi.stop()