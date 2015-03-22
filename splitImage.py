import numpy as np
import cv2
import glob
import os
import sys

## main program
#path = "test/images/"
folder = "test"#test or validation
path = folder+"/imagesjpg/"
resizeRatio = 0.25
subimgSize = 32
outputText = ""

i=0
for filename in glob.glob(path + "/*.jpg"):#specify your own path
    if (i == 20):
        break
    else:
        i += 1
        
    print filename
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(0,0),fx=resizeRatio,fy=resizeRatio)
    borderImg= cv2.copyMakeBorder(img,subimgSize/2,subimgSize/2,subimgSize/2,subimgSize/2,cv2.BORDER_CONSTANT,value=[0,0,0])

    filename = filename.split('/')[-1]
    maskname = folder+"/masks/" + filename.split('.')[0] + "_1.png"
    mask = cv2.imread(maskname,cv2.IMREAD_GRAYSCALE)
    mask = mask[0:360,0:480]
    mask = cv2.resize(mask,(0,0),fx=resizeRatio,fy=resizeRatio)
    mask = cv2.copyMakeBorder(mask,subimgSize/2,subimgSize/2,subimgSize/2,subimgSize/2,cv2.BORDER_CONSTANT,value=[0,0,0])

    height = int(360*resizeRatio + subimgSize)
    width = int(480*resizeRatio + subimgSize)
    print height
    print width

    for x in range(width - subimgSize):
        #x = i * (width/subSets)
        
        for y in range(height - subimgSize):
            #y = j * (height/subSets)
            
            cropimg = borderImg[y:y+subimgSize, x:x+subimgSize]
            outFile = folder+"/out/" + str(x) + "-" + str(y) + "-" + filename
            hasHead = str( 1 if mask[y + subimgSize/2, x + subimgSize/2] == (255, 255, 255)[0] else 0 )
            outputText += outFile + " " + hasHead + "\n"
            cv2.imwrite( outFile, cropimg )


#write text.txt
if(folder == "test"):
    file = open("test.txt","w")
else:
    file = open("val.txt","w")

file.write(outputText)
file.close()
