#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import pigpio
import gripper


DIR = 22  # Direction GPIO Pin
STEP = 23  # Step GPIO Pin


# Połączenie się z pigpiod
pi = pigpio.pi()

# Ustawienie pinów jako wyjścia
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)


MODE = (19, 20, 21)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Half'][i])

# Set duty cycle and frequency

def setPWM():
	pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
	pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second
	
def stopPWM():
	pi.set_PWM_dutycycle(STEP, 0)


def Forward():
    for x in range(40):
        pi.write(DIR, 1)
        sleep(.1)

def Reverse():		
    for x in range(40):
        pi.write(DIR, 0)
        sleep(.1)



try:
	setPWM()
	Forward()
	stopPWM()
	sleep(1)
	gripper.Gripper()
	setPWM()
	Reverse()

        
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    stopPWM() # PWM stop
    pi.stop()