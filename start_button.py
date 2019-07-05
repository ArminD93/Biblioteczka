#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.append('./shortest_path')
sys.path.append('./QR_scanner')

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
suma = []

def find_path(frm, to, FLG=False):
	import QRscanner
	global DS
	global zero_pos
	global schowek
	
	

	if FLG == True:	
		list = dijkstra.Dijkstra(zero_pos, to)
		print('TRASA: ',list)
		direction.Check_Direction(list, suma)

		QRscanner.set_camera()
		QRscanner.ReadQR()
		print("Sprawdzenie, czy obiekt jest na miejscu")
		print('Wykryto:',QRscanner.data)
		QRscanner.Release_camera()  		
		if QRscanner.data == to[1]:		
			gripper_file.Gripper_take()				
			zero_pos = frm			
			list = dijkstra.Dijkstra(to, frm)
			direction.Check_Direction(list, suma)
		if QRscanner.data == to[1]:
			gripper_file.Gripper_give()	
		else:
			print("Brak klocka na regale")
			print('frm: ', frm)
			print('to: ', to)
			zero_pos = frm	
			print('zero_pos: ', zero_pos)
			list = dijkstra.Dijkstra(to, frm)
			print('TRASA POWROTNA: ',list)
			direction.Check_Direction(list, suma)			
		print("Suma wszystkich krokow: ",sum(suma))
	else:
		#Szukanie najmniejszej liczby ruchów
		list = dijkstra.Dijkstra(frm, to)
		#print('LISTA_1: ', list)
		#list = dijkstra.Dijkstra(to, frm)
		#print('LISTA_2: ', list)		
	
	#print ( "liczba ruchow: " , len(list)-1)
	DS += (len(list)-1 ) *2	
	#print ("Droga: ", DS )
	
	
	
	
def Flg_False():
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

'''
def Cell_target(target, FLG=False):
			global DS
			global zero_pos			
			DS = 0
			zero_pos = '1A' #pozycja startowa, skąd startuje chwytak
			
			literki = ['A', 'B', 'C', 'D', 'E']
			cyfry = ['1','2','3','4']
			LitCyfr = [['A', 'B', 'C', 'D', 'E'], ['1','2','3','4']]
			for item in literki:
				#n = bool(item)
				FLAGA_2 = 'FLG_2' + item
				FLG_2A = FLAGA_2
				print(FLG_2A)
				
				if any([FLG_2A, library.FLG_3A, library.FLG_4A]) == True:		
					find_path(target, library.toA, FLG)												
			
			return DS
'''
def Cell_target(target, FLG=False):
			global DS
			global zero_pos			
			DS = 0
			zero_pos = '1A' #pozycja startowa, skąd startuje chwytak
			#print (zero_pos)				
			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == True:
				#print('szukanie dla A')
				find_path(target, library.toA, FLG)									
				
			if any([library.FLG_2B, library.FLG_3B, library.FLG_4B]) == True:
				#print('szukanie dla B')
				find_path(target, library.toB, FLG)	
		
			if any([library.FLG_2C, library.FLG_3C, library.FLG_4C]) == True:
				#print('szukanie dla C')
				find_path(target, library.toC, FLG)													
						
			if any([library.FLG_2D, library.FLG_3D, library.FLG_4D]) == True:
				#print('szukanie dla D')
				find_path(target, library.toD, FLG)											
					
			if any([library.FLG_2E, library.FLG_3E, library.FLG_4E]) == True:
				#print('szukanie dla E')
				find_path(target, library.toE, FLG)	
				
			#print("Droga do" ,target, ": " ,DS)
			
			return DS

			
class START(GridLayout):	

	def buttonStart(self, event):		
			DSs = []
			targets = ['1A', '1B', '1C', '1D', '1E']
			#targets = ['1D']
			for item in targets:		
				target = item
				Cell_target(target)		
				
				DSs.append(DS)			
			
			DSmin = min(DSs)
			DSindex = DSs.index(min(DSs))
			Cell = targets[DSindex]
			
			if Cell in targets:
				#print (Cell, "Jest na liscie")
			
				FLG = True							
				Cell_target(Cell, FLG)			
				zero_pos = '1A'
				list = dijkstra.Dijkstra(Cell, zero_pos)

				direction.Check_Direction(list, suma)
							
				self.status_bar1.label_delete1()
				self.status_bar2.label_delete2()
				self.status_bar3.label_delete3()
			Flg_False()
			

			if any([library.FLG_2A, library.FLG_3A, library.FLG_4A]) == False:
				if any([library.FLG_2B, library.FLG_3B, library.FLG_4B]) == False:
					if any([library.FLG_2C, library.FLG_3C, library.FLG_4C]) == False:
						if any([library.FLG_2D, library.FLG_3D, library.FLG_4D]) == False:
							if any([library.FLG_2E, library.FLG_3E, library.FLG_4E]) == False:
								'''print("")
								print('Wybierz pole od 1B do 4E')
								print("")
								print ("Dostepne cele: ", targets )
								print ("Calkowite drogi do kazdego z celow: ", DSs )
								print ("Najkrotsza droga: ", DSmin )
								print ("Pozycja na liscie: ", DSindex )
								print ("Najkrotsza droga jest do komorki: ", Cell )
								print("")
	'''




