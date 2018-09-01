#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import dijkstra
import direction

import servo
import gripper



frm = '1A'


answ = 0

while answ != 'tak':

	print ("Dijkstra's shortest path")
	print("")
	to = raw_input('Wskaż miejsce przedmiotu: ')
	print("")
	
	list = dijkstra.Dijkstra(frm, to)
	direction.Check_Direction(list)

	servo.SetAngle(35)  #open
	sleep(2)
	gripper.Gripper_Forward()
	servo.SetAngle(0)  # close
	gripper. Gripper_Reverse()
	sleep(2)
 
	list = dijkstra.Dijkstra(to, frm)
	direction.Check_Direction(list)

	sleep(2)	
	gripper.Gripper_Forward()
	servo.SetAngle(35)  #open
	gripper.Gripper_Reverse()
	sleep(2)
	servo.SetAngle(0)  #open
	
	print ("Czy zakończyć? tak/nie")
	answ = raw_input("Odpowiedź: ")