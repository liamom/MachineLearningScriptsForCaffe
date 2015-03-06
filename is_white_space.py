#!/usr/bin/env python
import numpy as np
import cv2
import glob
import os
import sys
from numpy import array
from PIL import Image

def isWhite(img1, img2, pixelNum):
	white = 0
	im = Image.open(img1)
	#arr = array(im) #this is a numpy array
	count = 0
	for pixel in iter(im.getdata()):
		count++
		if count == pixelNum:
			if pixel[pixelNum] == #(255,255,255):
				white = 1
			else:
				white = 0
			break
			

        	
