import numpy as np
import cv2
import glob
import os
import sys

## main program
#path = "test/images/"
####SPECIFY YOUR OWN PATHS BEFORE COMPILING####
folder = "train/Seq01"
imagesPath = folder+"/imagesjpg/"
masksPath = folder+"/masks/"
resultsPath = folder + "/results/"#where each image folder of 10800 will go
resizeRatio = 0.25
subimgSize = 32
outputText = ""
masksFileExt = ".png"
imagesFileExt = ".jpg"
resultsFileExt = ".png"

count = 0
i=0
for filename in glob.glob(imagesPath + "/*" + imagesFileExt):#specify your own path
    if (i == 1):
        break
    else:
        i += 1
    
    print filename
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(0,0),fx=resizeRatio,fy=resizeRatio)
    borderImg= cv2.copyMakeBorder(img,subimgSize/2,subimgSize/2,subimgSize/2,subimgSize/2,cv2.BORDER_CONSTANT,value=[0,0,0])

    filename = filename.split('/')[-1]#look for "/" until there are no more
    #print filename
    maskName = filename.split('.')[0] + "_1"
    maskFilename = masksPath + maskName + masksFileExt
    #print maskFilename
    mask = cv2.imread(maskFilename,cv2.IMREAD_GRAYSCALE)
    mask = mask[0:360, 0:480]
    mask = cv2.resize(mask,(0,0),fx=resizeRatio,fy=resizeRatio)
    mask = cv2.copyMakeBorder(mask,subimgSize/2,subimgSize/2,subimgSize/2,subimgSize/2,cv2.BORDER_CONSTANT,value=[0,0,0])

    height = int(360*resizeRatio + subimgSize)
    width = int(480*resizeRatio + subimgSize)
    print height
    print width

	
    if not os.path.exists(resultsPath + maskName):
        os.makedirs(resultsPath + maskName)#01_000n_1/1_w
    print resultsPath + maskName
    #for each win32 center pixel, write each image(10800 total) to a dir "01_000n_1"
    #which will contain image files in format "01_000n_1_win32ID" where ID is 1 to 10800
    for x in range(width - subimgSize):#1 to 120
        #x = i * (width/subSets)
        
        for y in range(height - subimgSize):#1 to 90
            #y = j * (height/subSets)
            count += x*y
	    
            cropimg = mask[y:y+subimgSize, x:x+subimgSize]
            #outfilepath = folder+"/out/" + str(x) + "-" + str(y) + "-" + filename
            hasHead = ( "w" if mask[y + subimgSize/2, x + subimgSize/2] == (255, 255, 255)[0] else "b" )
            #outputText += outfilepath + " " + hasHead + "\n"
	    resultsFileName = resultsPath + maskName + "/" + str(count) + "_" + hasHead + resultsFileExt
            cv2.imwrite(resultsFileName, cropimg)
	    
	    



