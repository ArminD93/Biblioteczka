#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
import servo
from time import sleep
import pigpio
# -*- coding: utf-8 -*-
GPIO.setwarnings(False)



delay = 0.0055 #0.0055  #0.005 / 32 
steps = 20*3 #20 * 32 * 8  

pi = pigpio.pi()




coil_A_1_pin = 18
coil_A_2_pin = 4
coil_B_1_pin = 15
coil_B_2_pin = 14

pi.set_mode(coil_A_1_pin, pigpio.OUTPUT)
pi.set_mode(coil_A_2_pin, pigpio.OUTPUT)
pi.set_mode(coil_B_1_pin, pigpio.OUTPUT)
pi.set_mode(coil_B_2_pin, pigpio.OUTPUT)





def setStep(w1, w2, w3, w4):
#GPIO.output(coil_A_1_pin, w1)
  pi.write(coil_A_1_pin, w1)
  pi.write(coil_A_2_pin, w2)
  pi.write(coil_B_1_pin, w3)
  pi.write(coil_B_2_pin, w4)


#servo.SetAngle(30)  #open
#servo.SetAngle(30)  # close


def  Gripper_Forward():
	
	for i in range(0, steps):
		setStep(0,1,1,0)
		sleep(delay)
		setStep(0,1,0,1)
		sleep(delay)
		setStep(1,0,0,1)
		sleep(delay)
		setStep(1,0,1,0)
		sleep(delay)

def  Gripper_Reverse():

	for i in range(0, steps):
		setStep(1,0,1,0)
		sleep(delay)
		setStep(1,0,0,1)
		sleep(delay)
		setStep(0,1,0,1)
		sleep(delay)
		setStep(0,1,1,0)
		sleep(delay)
	
	



	

GPIO.cleanup()	
	
	
	
