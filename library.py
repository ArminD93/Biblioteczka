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

frm = '1A'

def find_path(to):
	list = dijkstra.Dijkstra(frm, to)
	direction.Check_Direction(list)
			
	gripper.forward()
			
	list = dijkstra.Dijkstra(to, frm)
	direction.Check_Direction(list)		
	
	gripper.reverse()	

class Library(GridLayout):	
		
	def button1B(self, instance, value):
		if value == 'down':
				self.status_bar.label1B()
				to = '1B'
				find_path(to)
						
				
 	def button1C(self, instance, value):
		if value == 'down':
				print("1C")
				self.status_bar.label1C()
				to = '1C'
				find_path(to)				
		else:
				print("Wylaczono")
				
	def button1D(self, instance, value):
		if value == 'down':
				print("1D")
				self.status_bar.label1D()
				to = '1D'
				find_path(to)				
		else:
				print("Wylaczono")				
	def button1E(self, instance, value):
		if value == 'down':
				print("1E")
				self.status_bar.label1E()
				to = '1E'
				find_path(to)				
		else:
				print("Wylaczono")
				
# ###################################################
	def button2A(self, instance, value):
		if value == 'down':
				print("2A")
				self.status_bar.label2A()
				to = '2A'
				find_path(to)				
		else:
				print("Wylaczono")
				
 	def button2B(self, instance, value):
		if value == 'down':
				print("2B")
				self.status_bar.label2B()
				to = '2B'
				find_path(to)				
		else:
				print("Wylaczono")
				
	def button2C(self, instance, value):
		if value == 'down':
				print("2C")
				self.status_bar.label2C()
				to = '2C'
				find_path(to)				
		else:
				print("Wylaczono")				
	def button2D(self, instance, value):
		if value == 'down':
				print("2D")
				self.status_bar.label2D()
				to = '2D'
				find_path(to)				
		else:
				print("Wylaczono")
				
	def button2E(self, instance, value):
		if value == 'down':
				print("2E")
				self.status_bar.label2E()
				to = '2E'
				find_path(to)				
		else:
				print("Wylaczono")	
# ############################################
	def button3A(self, instance, value):
		if value == 'down':
				print("3A")
				self.status_bar.label3A()
				to = '3A'
				find_path(to)				
		else:
				print("Wylaczono")
				
 	def button3B(self, instance, value):
		if value == 'down':
				print("3B")
				self.status_bar.label3B()
				to = '3B'
				find_path(to)				
		else:
				print("Wylaczono")
				
	def button3C(self, instance, value):
		if value == 'down':
				print("3C")
				self.status_bar.label3C()
				to = '3C'
				find_path(to)				
		else:
				print("Wylaczono")				
	def button3D(self, instance, value):
		if value == 'down':
				print("3D")
				self.status_bar.label3D()
				to = '3D'
				find_path(to)				
		else:
				print("Wylaczono")
				
	def button3E(self, instance, value):
		if value == 'down':
				print("3E")
				self.status_bar.label3E()
				to = '3E'
				find_path(to)				
		else:
				print("Wylaczono")	
# #############################################
	def button4A(self, instance, value):
		if value == 'down':
				print("4A")
				self.status_bar.label4A()
				to = '4A'
				find_path(to)				
				
		else:
				print("Wylaczono")
				
 	def button4B(self, instance, value):
		if value == 'down':
				print("4B")
				self.status_bar.label4B()
				to = '4B'
				find_path(to)			
		else:
				print("Wylaczono")
				
	def button4C(self, instance, value):
		if value == 'down':
				print("4C")
				self.status_bar.label4C()
				to = '4C'
				find_path(to)				
		else:
				print("Wylaczono")				
	def button4D(self, instance, value):
		if value == 'down':
				print("4D")
				self.status_bar.label4D()
				to = '4D'
				find_path(to)			
		else:
				print("Wylaczono")
				
	def button4E(self, instance, value):
		if value == 'down':
				print("4E")
				self.status_bar.label4E()
				to = '4E'
				find_path(to)				
		else:
				print("Wylaczono")	
# #######################