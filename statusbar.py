#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import kivy
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty, ObjectProperty, ListProperty


class StatusBar1(AnchorLayout):


	def label4A(self):
			self.lbl.text  =" Wybrano 4A"
	def label4B(self):
			self.lbl.text  =" Wybrano 4B"
	def label4C(self):
			self.lbl.text  =" Wybrano 4C"
	def label4D(self):
			self.lbl.text  =" Wybrano 4D"
	def label4E(self):
			self.lbl.text  =" Wybrano 4E"		
	def label_delete1(self):
			self.lbl.text  =" "
			
class StatusBar2(AnchorLayout):

	def label3A(self):
			self.lbl2.text  =" Wybrano 3A"
	def label3B(self):
			self.lbl2.text  =" Wybrano 3B"
	def label3C(self):
			self.lbl2.text  =" Wybrano 3C"
	def label3D(self):
			self.lbl2.text  =" Wybrano 3D"
	def label3E(self):
			self.lbl2.text  =" Wybrano 3E"
	def label_delete2(self):
			self.lbl2.text  =" "
			
class StatusBar3(AnchorLayout):

	def label2A(self):
			self.lbl3.text  =" Wybrano 2A"
	def label2B(self):
			self.lbl3.text  =" Wybrano 2B"
	def label2C(self):
			self.lbl3.text  =" Wybrano 2C"
	def label2D(self):
			self.lbl3.text  =" Wybrano 2D"
	def label2E(self):
			self.lbl3.text  =" Wybrano 2E"
	def label_delete3(self):
			self.lbl3.text  =" "