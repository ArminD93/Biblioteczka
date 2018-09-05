from time import sleep
import sys
sys.path.append('./gripper')
import servo
import stepper_z


def forward():
	servo.SetAngle(35)  #open
	sleep(2)
	stepper_z.Gripper_Forward()
	servo.SetAngle(0)  # close
	stepper_z. Gripper_Reverse()
	sleep(2)
 

def reverse():
	sleep(2)	
	stepper_z.Gripper_Forward()
	servo.SetAngle(35)  #open
	stepper_z.Gripper_Reverse()
	sleep(2)
	servo.SetAngle(0)  #open