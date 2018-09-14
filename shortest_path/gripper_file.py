#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.append('./gripper')

import RPi.GPIO as GPIO
from time import sleep
import pigpio


		
GPIO.setwarnings(False)

servo = 17
		
delay = 0.0055 #0.0055  #0.005 / 32 
steps = 20*3 #20 * 32 * 8  

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

pi = pigpio.pi()
pwm = GPIO.PWM(servo, 50) # GPIO 12 for PWM with 50Hz

coil_A_1_pin = 18
coil_A_2_pin = 4
coil_B_1_pin = 15
coil_B_2_pin = 14

pi.set_mode(coil_A_1_pin, pigpio.OUTPUT)
pi.set_mode(coil_A_2_pin, pigpio.OUTPUT)
pi.set_mode(coil_B_1_pin, pigpio.OUTPUT)
pi.set_mode(coil_B_2_pin, pigpio.OUTPUT)

	
def setStep(w1, w2, w3, w4):
	
		pi.write(coil_A_1_pin, w1)
		pi.write(coil_A_2_pin, w2)
		pi.write(coil_B_1_pin, w3)
		pi.write(coil_B_2_pin, w4)

def SetAngle(angle):
		
		pwm.start(0) # Initialization
		duty = angle / 18 + 2
		pi.write(servo,1)
		pwm.ChangeDutyCycle(duty)
		sleep(1)
		pi.write(servo,0)
		pwm.ChangeDutyCycle(duty)
									
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


def Gripper_take():
		print("Pobranie klocka")
		SetAngle(35)
		sleep(2)
		Gripper_Forward()
		SetAngle(0)
		Gripper_Reverse()
		sleep(2)
		
def Gripper_give():
		print("Odlozenie klocka")
		sleep(2)
		Gripper_Forward()
		SetAngle(35)
		Gripper_Reverse()
		sleep(2)
		SetAngle(0)	
		
		
GPIO.cleanup()	