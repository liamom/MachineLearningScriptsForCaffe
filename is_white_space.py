#!/usr/bin/env python
import numpy as np
import cv2
import glob
import os
import sys
from numpy import array
from PIL import Image

def isWhite(maskImg, x, y):
	
	im = Image.open(maskImg)
	
	pix = im.load()
	if pix[x, y] == (255, 255, 255):
		return 1
	else:
		return 0
		
	
