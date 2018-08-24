#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
import dijkstra
import direction

import servo
import gripper

print ("Dijkstra's shortest path")
print("")
frm = raw_input('Podaj poczatek trasy: ')
to = raw_input('Podaj koniec trasy: ')
print("")


list = dijkstra.Dijkstra(frm, to)

servo.SetAngle(35)  #open
sleep(2)
gripper.Gripper_Forward()
servo.SetAngle(0)  # close
gripper. Gripper_Reverse()
sleep(2)
 
direction.Check_Direction(list)

sleep(2)	
gripper.Gripper_Forward()
servo.SetAngle(35)  #open
gripper.Gripper_Reverse()
sleep(2)
servo.SetAngle(0)  #open