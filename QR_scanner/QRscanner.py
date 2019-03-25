#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time


	
def set_camera():
	global cap
	# Przechwycenie obrazu z kamerki
	cap = cv2.VideoCapture(0, cv2.CAP_V4L)

	#Rozdzielczośćo okna -> 640 x 480
	cap.set(3,640)
	cap.set(4,480)
	time.sleep(2)	
	

def decode(im) : 
    # Poszukuj kodów kreskowych i kodów QR
    decodedObjects = pyzbar.decode(im)   
    return decodedObjects

def convex_hull():
        # If the points do not form a quad, find convex hull
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
         
        # Number of points in the convex hull
        n = len(hull)     
        # Draw the convext hull
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)	
  
def compare_data(data1):
        
        if data1 == b'A':
			print('Wykryto A')
        elif data1 == b'B':
			print('Wykryto B')
        elif data1 == b'C':
			print('Wykryto C')
        elif data1 == b'D':
			print('Wykryto D')
        elif data1 == b'E':
			print('Wykryto E')
				
def ReadQR():	
	global points
	global frame
	global data
	
	data =0
	i = 20

	
	print('WEJSCIE DO FUNKCJI')
	
	font = cv2.FONT_HERSHEY_SIMPLEX

	while(cap.isOpened()):
	
		i -= 1
		# Capture frame-by-frame
		ret, frame = cap.read()
		# Our operations on the frame come here
		im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			 
		decodedObjects = decode(im)

		for decodedObject in decodedObjects: 
			
			points = decodedObject.polygon   
			
			convex_hull()

			x = decodedObject.rect.left
			y = decodedObject.rect.top

			
			data = decodedObject.data
			return data	
			 
			compare_data(data)
			
			barCode = str(decodedObject.data)
			cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
				   
		# Display the resulting frame
		cv2.imshow('frame',frame)
	
		key = cv2.waitKey(1)
		#if key & 0xFF == ord('q'):
		
		# Kiedy wszystko skończione, zatrzymaj przechwytywanie obrazu
		#cap.release()
		#cv2.destroyAllWindows()
		#or i == 0
			
		if (data != 0 ):			
			print('DATA:',data)
			data =0
			i = 5
			break		
	print('DATA:',data)

