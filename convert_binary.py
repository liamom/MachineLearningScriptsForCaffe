import numpy as np
import cv2
import glob
import os
import sys

for filename in glob.glob("train/Seq01/imagesjpg/*.jpg"):#specify your own path
	img = cv2.imread(filename)
	img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
	cv2.imwrite( filename, img )


