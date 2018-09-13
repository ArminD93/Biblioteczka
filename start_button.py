#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.append('./shortest_path')

import kivy
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ObjectProperty
import library
from time import sleep
import dijkstra
import direction
import gripper_file


DS = 0

gripper = gripper_file.Gripper() 

def find_path(frm, to, FLG=False):
	global DS
	
	list = dijkstra.Dijkstra(frm, to)
	if FLG == True:
		direction.Check_Direction(list)	
		gripper.open() # open
		sleep(2)
		gripper.Gripper_Forward()
		gripper.close() # close
		gripper.Gripper_Reverse()
		sleep(2)		
		
	list2 = dijkstra.Dijkstra(to, frm)
	if FLG == True:
		direction.Check_Direction(list2)
		sleep(2)			
		gripper.Gripper_Forward()
		gripper.open() # open
		gripper.Gripper_Reverse()	
		sleep(2)			
		gripper.close() # close
	
	#print ( "liczba ruchow: " , len(list)-1)
	DS += (len(list)-1 )+ (len(list2)-1)
	
	print ("Droga: ", DS )
	
	
	
	
def Flg_False():
	
	print("")
	print ("zerowanie flag")
	
	library.FLG_2A = False
	library.FLG_3A = False
	library.FLG_4A = False
	
	library.FLG_2B = False
	library.FLG_3B = False
	library.FLG_4B = False
	
	library.FLG_2C = False
	library.FLG_3C = False
	library.FLG_4C = False
	
	library.FLG_2D = False
	library.FLG_3D = False
	library.FLG_4D = False
	
	library.FLG_2E= False
	library.FLG_3E = False
	library.FLG_4E = False
	

def Cell_target(target):
			global DS
			DS = 0
			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == True:
			
				find_path(target, library.toA)									
				
			if any([library.FLG_2B, library.FLG_3B, library.FLG_4B]) == True:
			
				find_path(target, library.toB)																			
				
			if any([library.FLG_2C, library.FLG_3C, library.FLG_4C]) == True:
				
				find_path(target, library.toC)													
						
			if any([library.FLG_2D, library.FLG_3D, library.FLG_4D]) == True:
			
				find_path(target, library.toD)											
					
			if any([library.FLG_2E, library.FLG_3E, library.FLG_4E]) == True:
				
				find_path(target, library.toE)	
				
			print("")
			print("Droga do" ,target, ": " ,DS)
			
			return DS

			
class START(GridLayout):	
	
	
	def buttonStart(self, event):
			
			DSs = []
			targets = ['1A', '1B', '1C', '1D', '1E']
			for item in targets:		
				target = item
				Cell_target(target)		
				
				DSs.append(DS)			
					
			
			DSmin = min(DSs)
			DSindex = DSs.index(min(DSs))
			Cell = targets[DSindex]
			
			if Cell in targets:
				print("")
				print (Cell, "Jest na liscie")
				Cell_target(Cell)	
				
			Flg_False()

			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == False:
				if any([library.FLG_2B, library.FLG_3B, library.FLG_4B]) == False:
					if any([library.FLG_2C, library.FLG_3C, library.FLG_4C]) == False:
						if any([library.FLG_2D, library.FLG_3D, library.FLG_4D]) == False:
							if any([library.FLG_2E, library.FLG_3E, library.FLG_4E]) == False:
								print("")
								print('Wybierz pole od 1B do 4E')
								print("")
								print ("Dostepne cele: ", targets )
								print ("Calkowite drogi do kazdego z celow: ", DSs )
								print ("Najkrotsza droga: ", DSmin )
								print ("Pozycja na liscie: ", DSindex )
								print ("Najkrotsza droga jest do komorki: ", Cell )
								print("")
	




