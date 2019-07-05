#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.append('./shortest_path')


import kivy
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ObjectProperty



from time import sleep
import dijkstra
import direction
import gripper


		

class Library(GridLayout):	

	global FLG_2A
	global FLG_3A
	global FLG_4A	
	
	global FLG_1B
	global FLG_2B
	global FLG_3B
	global FLG_4B	
	
	global FLG_1C
	global FLG_2C
	global FLG_3C
	global FLG_4C

	global FLG_1D
	global FLG_2D
	global FLG_3D
	global FLG_4D
	
	global FLG_1E
	global FLG_2E
	global FLG_3E
	global FLG_4E	

	FLG_2A = False
	FLG_3A = False
	FLG_4A = False
	
	FLG_1B = False
	FLG_2B = False
	FLG_3B = False
	FLG_4B = False
	
	FLG_1C = False
	FLG_2C = False
	FLG_3C = False
	FLG_4C = False
			
	FLG_1D = False
	FLG_2D = False
	FLG_3D = False
	FLG_4D = False
	
	FLG_1E = False
	FLG_2E = False
	FLG_3E = False
	FLG_4E = False
					
# ###################################################
	def button2A(self, instance, val):

		if val == 'down':
			self.status_bar3.label2A()		
			global FLG_2A
			global toA
			FLG_2A = True
			toA = '2A'
			print ("Ustawiono flagę 2A")					

				
 	def button2B(self, instance, val):

		if val == 'down':
			self.status_bar3.label2B()			
			global FLG_2B
			global toB
			FLG_2B = True
			toB = '2B'
			print ("Ustawiono flagę 2B")						
				
	def button2C(self, instance, val):

		if val == 'down':
			self.status_bar3.label2C()			
			global FLG_2C
			global toC
			FLG_2C = True
			toC = '2C'
			print ("Ustawiono flagę 2C")		

				
	def button2D(self, instance, val):

		if val == 'down':
			self.status_bar3.label2D()			
			global FLG_2D
			global toD
			FLG_2D = True
			toD = '2D'
			print ("Ustawiono flagę 2D")	
				
	def button2E(self, instance, val):

		if val == 'down':
			self.status_bar3.label2E()			
			global FLG_2E
			global toE
			FLG_2E = True
			toE = '2E'
			print ("Ustawiono flagę 2E")		
# ############################################
	def button3A(self, instance, val):

		if val == 'down':
			self.status_bar2.label3A()			
			global FLG_3A
			global toA
			FLG_3A = True
			toA = '3A'
			print ("Ustawiono flagę 3A")	
				
 	def button3B(self, instance, val):

		if val == 'down':
			self.status_bar2.label3B()
			global FLG_3B
			global toB
			FLG_3B = True
			toB = '3B'
			print ("Ustawiono flagę 3B")	
				
	def button3C(self, instance, val):
	
		if val == 'down':
			self.status_bar2.label3C()			
			global FLG_3C
			global toC
			FLG_3C = True
			toC = '3C'
			print ("Ustawiono flagę 3C")			
			return FLG_3C	
			
	def button3D(self, instance, val):

		if val == 'down':
			self.status_bar2.label3D()			
			global FLG_3D
			global toD
			FLG_3D = True
			toD = '3D'
			print ("Ustawiono flagę 3D")	
				
	def button3E(self, instance, val):

		if val == 'down':
			self.status_bar2.label3E()			
			global FLG_3E
			global toE
			FLG_3E = True
			toE = '3E'
			print ("Ustawiono flagę 3E")	
# #############################################
	def button4A(self, instance, val):

		if val == 'down':
			self.status_bar1.label4A()			
			global FLG_4A
			global toA
			FLG_4A = True
			toA = '4A'
			print ("Ustawiono flagę 4A")	
			
 	def button4B(self, instance, val):

		if val == 'down':
			self.status_bar1.label4B()		
			global FLG_4B
			global toB
			FLG_4B = True
			toB= '4B'
			print ("Ustawiono flagę 4B")			
				
	def button4C(self, instance, val):
	
		if val == 'down':
			self.status_bar1.label4C()		
			global FLG_4C
			global toC
			FLG_4C = True
			toC = '4C'
			print ("Ustawiono flagę 4C")				
			
	def button4D(self, instance, val):

		if val == 'down':
			self.status_bar1.label4D()		
			global FLG_4D
			global toD
			FLG_4D = True
			toD = '4D'
			print ("Ustawiono flagę 4D")
				
	def button4E(self, instance, val):

		if val == 'down':
			self.status_bar1.label4E()		
			global FLG_4E
			global toE
			FLG_4E = True
			toE = '4E'
			print ("Ustawiono flagę 4E")					
				
# #######################


