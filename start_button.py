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
import gripper



DS = 0


def find_path(frm, to):
	global DS
	
	
	list = dijkstra.Dijkstra(frm, to)
	
	#print ( "liczba ruchow: " , len(list)-1)
	DS += len(list)-1

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
				to = target
				find_path(library.toA, to)				
				
			if any([library.FLG_2B, library.FLG_3B, library.FLG_4B]) == True:
			
				find_path(target, library.toB)	
				to = target
				find_path(library.toB, to)										
						
				
			if any([library.FLG_2C, library.FLG_3C, library.FLG_4C]) == True:
				
				find_path(target, library.toC)	
				to = target
				find_path(library.toC, to)									
						
			if any([library.FLG_2D, library.FLG_3D, library.FLG_4D]) == True:
			
				find_path(target, library.toD)	
				to = target
				find_path(library.toD, to)								
					
			if any([library.FLG_2E, library.FLG_3E, library.FLG_4E]) == True:
				
				find_path(target, library.toE)	
				to = target
				find_path(library.toE, to)
				
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
					
			Flg_False()
			

			
			
			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == False:
				if any([library.FLG_2B, library.FLG_3B, library.FLG_4B]) == False:
					if any([library.FLG_2C, library.FLG_3C, library.FLG_4C]) == False:
						if any([library.FLG_2D, library.FLG_3D, library.FLG_4D]) == False:
							if any([library.FLG_2E, library.FLG_3E, library.FLG_4E]) == False:
								print("")
								print('Wybierz pole od 1B do 4E')
			
								print ("Calkowita droga: ", DSs )
								print("")
	




