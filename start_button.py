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



frm = '1A'
DS = 0

def find_path(frm, to):
	global DS
	
	print("")
	list = dijkstra.Dijkstra(frm, to)
	
	print ( "liczba ruchow: " , len(list)-1)
	DS += len(list)-1
	print("")
	print ("Droga: ", DS )
	
	
def Flg_False():
	
	print("")
	print ("zerowanie flag")
	
	library.FLG_2A = False
	library.FLG_3A = False
	library.FLG_4A = False
	
	library.FLG_1B = False
	library.FLG_2B = False
	library.FLG_3B = False
	library.FLG_4B = False
	
	library.FLG_1C = False
	library.FLG_2C = False
	library.FLG_3C = False
	library.FLG_4C = False
	
	library.FLG_1D = False
	library.FLG_2D = False
	library.FLG_3D = False
	library.FLG_4D = False
	
	library.FLG_1E = False
	library.FLG_2E= False
	library.FLG_3E = False
	library.FLG_4E = False
	

			

class START(GridLayout):	

	
	def buttonStart(self, event):

			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == True:
			
				find_path(frm, library.toA)	
				to = '1A'
				find_path(library.toA, to)				
				
			if any([library.FLG_1B, library.FLG_2B, library.FLG_3B, library.FLG_4B]) == True:
			
				find_path(frm, library.toB)	
				to = '1A'
				find_path(library.toB, to)										
						
				
			if any([library.FLG_1C, library.FLG_2C, library.FLG_3C, library.FLG_4C]) == True:
				
				find_path(frm, library.toC)	
				to = '1A'
				find_path(library.toC, to)									
						
			if any([library.FLG_1D, library.FLG_2D, library.FLG_3D, library.FLG_4D]) == True:
			
				find_path(frm, library.toD)	
				to = '1A'
				find_path(library.toD, to)								
					
			if any([library.FLG_1E, library.FLG_2E, library.FLG_3E, library.FLG_4E]) == True:
				
				find_path(frm, library.toE)	
				to = '1A'
				find_path(library.toE, to)
								
								
			Flg_False()							
				
														

				
			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == False:
				print("")
				print('Wybierz pole od 1B do 4E')
			
				print ("Calkowita droga: ", DS )
				print("")
	




