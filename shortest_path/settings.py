#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio



DIR = 8  # Direction GPIO Pin
STEP = 11 # Step GPIO Pin

DIR2 = 9  # Direction GPIO Pin
STEP2 = 10 # Step GPIO Pin

DIR3 = 22  # Direction GPIO Pin
STEP3 = 23 # Step GPIO Pin

#step_count_UpDown= 50 #170
#step_count_LeftRight = 20

# Połączenie się z pigpiod
pi = pigpio.pi()

# Ustawienie pinów jako wyjścia
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

pi.set_mode(DIR2, pigpio.OUTPUT)
pi.set_mode(STEP2, pigpio.OUTPUT)

pi.set_mode(DIR3, pigpio.OUTPUT)
pi.set_mode(STEP3, pigpio.OUTPUT)

'''##########################################'''
MODE = (20, 26, 21)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Full'][i])
	
	
MODE2 = (24, 25, 7)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE2[i], RESOLUTION['Full'][i])	
	

MODE3 = (6, 13, 19)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE3[i], RESOLUTION['Full'][i])	
	
'''##########################################'''
# Set duty cycle and frequency

def setPWM_UpDown():
	pi.set_PWM_dutycycle(STEP, 255*0.5)  # 128 -> PWM 1/2 On 1/2 Off  (50% duty) <=>  255*0.5 -> 50% duty
	pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second
	
	pi.set_PWM_dutycycle(STEP2, 255*0.5)  # PWM 1/2 On 1/2 Off
	pi.set_PWM_frequency(STEP2, 500)  # 500 pulses per second
		
def setPWM_LeftRight():
	pi.set_PWM_dutycycle(STEP3, 255*0.5)  # PWM 1/2 On 1/2 Off
	pi.set_PWM_frequency(STEP3, 500)  # 500 pulses per second
	
def stopPWM_UpDown():
	pi.set_PWM_dutycycle(STEP, 0)
	pi.set_PWM_dutycycle(STEP2, 0)
	
def stopPWM_LeftRight():
	pi.set_PWM_dutycycle(STEP3, 0)


def Up(step_count_UpDown):
    
    for x in range(step_count_UpDown):
        pi.write(DIR, 1)
        pi.write(DIR2, 1)
        sleep(.1)
    

		
def Down(step_count_UpDown):
		
	for x in range(step_count_UpDown):
		pi.write(DIR, 0)
		pi.write(DIR2, 0)
		sleep(.1)
	
	
	
def Right(step_count_LeftRight):

    for x in range(step_count_LeftRight):
        pi.write(DIR3, 1)
        sleep(.1)


		
def Left(step_count_LeftRight):		

    for x in range(step_count_LeftRight):
        pi.write(DIR3, 0)
        sleep(.1)

	
def UpRight(step_count_UpDown, step_count_LeftRight):
	setPWM_LeftRight()
	setPWM_UpDown()
	
	
	
	for x in range(step_count_UpDown):
		pi.write(DIR, 1)
		pi.write(DIR2, 1)	
	
	
	for x in range(step_count_LeftRight-3):	
		pi.write(DIR3, 1)
		sleep(.1)
	stopPWM_LeftRight()	
	stopPWM_UpDown()


