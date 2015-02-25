import numpy as np
import cv2
import glob
import os
import sys

mystr = ""

for filename in glob.glob("train/Seq01/masks/*.png"):#specify your own path
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    mystr = ""
    
    for i in range(480):
        a = img [i]
        for b in a:
            if(b != 0):
                b = 1
                
            mystr += str(b) + ","
            
    break
f = open("testFile.txt", 'w')
f.write(mystr)
f.close()