#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
from time import sleep
import pigpio
GPIO.setwarnings(False)

servo = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)


pi = pigpio.pi()
pwm = GPIO.PWM(servo, 50) # GPIO 12 for PWM with 50Hz
pwm.start(0) # Initialization

def SetAngle(angle):
    duty = angle / 18 + 2

    
    pi.write(servo,1)

    pwm.ChangeDutyCycle(duty)
    
    sleep(1)

    pi.write(servo,0)

    pwm.ChangeDutyCycle(duty)
	


