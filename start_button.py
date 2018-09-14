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



def find_path(frm, to, FLG=False):
	global DS
		
	if FLG == True:
		list = dijkstra.Dijkstra(frm, to)
		direction.Check_Direction(list)
		gripper_file.Gripper_take()		
		
		list = dijkstra.Dijkstra(to, frm)
		direction.Check_Direction(list)
		gripper_file.Gripper_give()
		
	else:
		list = dijkstra.Dijkstra(frm, to)
		list = dijkstra.Dijkstra(to, frm)		
	
	#print ( "liczba ruchow: " , len(list)-1)
	DS += (len(list)-1 ) *2
	
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
	

def Cell_target(target, FLG=False):
			global DS
			DS = 0
			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == True:
			
				find_path(target, library.toA, FLG)									
				
			if any([library.FLG_2B, library.FLG_3B, library.FLG_4B]) == True:
			
				find_path(target, library.toB, FLG)																			
				
			if any([library.FLG_2C, library.FLG_3C, library.FLG_4C]) == True:
				
				find_path(target, library.toC, FLG)													
						
			if any([library.FLG_2D, library.FLG_3D, library.FLG_4D]) == True:
			
				find_path(target, library.toD, FLG)											
					
			if any([library.FLG_2E, library.FLG_3E, library.FLG_4E]) == True:
				
				find_path(target, library.toE, FLG)	
				
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
				FLG = True
				Cell_target(Cell, FLG)	
				
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
	




