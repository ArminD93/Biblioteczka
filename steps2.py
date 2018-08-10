#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper


DIR = 8  # Direction GPIO Pin
STEP = 11 # Step GPIO Pin

DIR2 = 9  # Direction GPIO Pin
STEP2 = 10 # Step GPIO Pin

step_count= 170


# Połączenie się z pigpiod
pi = pigpio.pi()

# Ustawienie pinów jako wyjścia
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

pi.set_mode(DIR2, pigpio.OUTPUT)
pi.set_mode(STEP2, pigpio.OUTPUT)


MODE = (20, 26, 21)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Half'][i])
	
	
MODE2 = (24, 25, 7)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE2[i], RESOLUTION['Half'][i])	
	

# Set duty cycle and frequency

def setPWM():
	pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
	pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second
	
	pi.set_PWM_dutycycle(STEP2, 128)  # PWM 1/2 On 1/2 Off
	pi.set_PWM_frequency(STEP2, 500)  # 500 pulses per second
	
def stopPWM():
	pi.set_PWM_dutycycle(STEP, 0)
	pi.set_PWM_dutycycle(STEP2, 0)


def Up():
    for x in range(step_count):
        pi.write(DIR, 1)
        pi.write(DIR2, 1)
        sleep(.1)

		
def Down():		
    for x in range(step_count):
        pi.write(DIR, 0)
        pi.write(DIR2, 0)
        sleep(.1)



try:
	#while True:
		setPWM()
		Up()
		stopPWM()
		sleep(1)
		setPWM()
		Down()

        
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    stopPWM() # PWM stop
    pi.stop()