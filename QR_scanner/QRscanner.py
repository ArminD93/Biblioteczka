#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time


	
def set_camera(): # Ustawienie obrazu z kamery.
	global cap
	# Przechwycenie obrazu z kamerki
	cap = cv2.VideoCapture(0, cv2.CAP_V4L) # Przechwycenie obrazu z kamerki
	
	#Rozdzielczosc okna -> 640 x 480
	cap.set(3,640)
	cap.set(4,480)
	time.sleep(2)	
	

def decode(im) : # Funkcja dekodująca kod QR.
    # Poszukuj kodow kreskowych i kodow QR
    decodedObjects = pyzbar.decode(im)   
    return decodedObjects

def convex_hull(): # Określenie granic kodu QR
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
 
				
def ReadQR(): # Funkcja odczytująca Kod QR.		
	global points
	global frame
	global data
	
	data =0
	i = 20

	print('URUCHOMIENIE KAMERKI')
	
	font = cv2.FONT_HERSHEY_SIMPLEX

	while(cap.isOpened()): # Wykonuj poniższe instrukcje dopóki kamera nie skończy przechwytywać obraz.
	
		i -= 1
		
		ret, frame = cap.read() # Przechwycony obraz zapisz do zmiennych.
		
		im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Określnie koloru obrazu w postaci odcieni szarości i zapisanie do zmiennej im (image).
			 
		decodedObjects = decode(im) # Funkcja decode dekoduje obraz.

		for decodedObject in decodedObjects: 
			
			points = decodedObject.polygon   
			
			convex_hull() # Realizacja funkcji określającej granice kodu QR.

			x = decodedObject.rect.left
			y = decodedObject.rect.top
		
			data = decodedObject.data
			return data	
			
			barCode = str(decodedObject.data)
			cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
	
		cv2.imshow('frame',frame) # Wyświetl obraz z wynikiem.
		
		key = cv2.waitKey(1)
		#if key & 0xFF == ord('q'):  # Jeśli zostanie wciśnięty na klawiaturze przycisk q, zakończ przechwytywanie obrazu.	

def Release_camera(): # Kiedy wszystko skończone, zatrzymaj przechwytywanie obrazu.
		# Kiedy wszystko skonczione, zatrzymaj przechwytywanie obrazu
		print('WYLACZENIE KAMERKI')
		cap.release() # Funkcja zatrzymująca przechwytywanie obrazu.
		cv2.destroyAllWindows()	# Zamknięcie okna podglądu z kamerki.
