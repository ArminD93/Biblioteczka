#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper
import settings
import servo

#step_count_LeftRight=15
#step_count_UpDown = 69 #23

try:
	#while True:
	for step_count_UpDown in range(69, -23, -23):
		print (step_count_UpDown)
		for step_count_LeftRight in range(20, 10, -5):

				settings.setPWM_LeftRight()	
				settings.Right(step_count_LeftRight)
				settings.stopPWM_LeftRight()


				settings.setPWM_UpDown()
				settings.Up(step_count_UpDown)
				settings.stopPWM_UpDown() # PWM stop



				servo.SetAngle(35)  #open
				sleep(2)
				gripper.Gripper_Forward()
				servo.SetAngle(0)  # close
				gripper. Gripper_Reverse()
				sleep(2)


				settings.setPWM_LeftRight()
				settings.Left(step_count_LeftRight)
				settings.stopPWM_LeftRight()



				settings.setPWM_UpDown()
				settings.Down(step_count_UpDown)
				settings.stopPWM_UpDown()      

				sleep(2)	
				gripper.Gripper_Forward()

				servo.SetAngle(35)  #open

				gripper.Gripper_Reverse()
				sleep(2)
				servo.SetAngle(0)  #open
		
				print (step_count_LeftRight)

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:	
	settings.pi.stop()