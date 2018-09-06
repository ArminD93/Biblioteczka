#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty, ListProperty

from time import sleep
import dijkstra

frm = '1A'


class StatusBar(BoxLayout):

	def label1B(self):
			to = '1B'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  =" Trasa do 1B: " + " ->".join(list)				
	def label1C(self):
			to = '1C'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 1C: " + " ->".join(list)
	def label1D(self):
			to = '1D'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 1D: " + " ->".join(list)
	def label1E(self):
			to = '1E'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 1E: " + " ->".join(list)
# #############################################
	def label2A(self):
			to = '2A'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 2A: " + " ->".join(list)
	def label2B(self):
			to = '2B'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 2B: " + " ->".join(list)
	def label2C(self):
			to = '2C'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 2C: " + " ->".join(list)
	def label2D(self):
			to = '2D'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 2D: " + " ->".join(list)
	def label2E(self):
			to = '2E'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 2E: " + " ->".join(list)
# #############################################
	def label3A(self):
			to = '3A'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 3A: " + " ->".join(list)
	def label3B(self):
			to = '3B'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 3B: " + " ->".join(list)
	def label3C(self):
			to = '3C'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 3C: " + " ->".join(list)
	def label3D(self):
			to = '3D'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 3D: " + " ->".join(list)
	def label3E(self):
			to = '3E'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 3E: " + " ->".join(list)
# #############################################
	def label4A(self):
			to = '4A'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 4A: " + " ->".join(list)
	def label4B(self):
			to = '4B'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 4B: " + " ->".join(list)
	def label4C(self):
			to = '4C'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 4C: " + " ->".join(list)
	def label4D(self):
			to = '4D'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 4D: " + " ->".join(list)
	def label4E(self):
			to = '4E'
			list = dijkstra.Dijkstra(frm, to)
			self.lbl.text  = " Trasa do 4E: " + " ->".join(list)