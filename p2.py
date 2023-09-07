#Drawing Shapes

import cv2 as cv
import numpy as np

#creating empty image
img=cv.imread('archive/train/cats/cat_10.jpg')
height, width, channels = img.shape
cv.rectangle(img,(100,200),(600,800),(0,255,0),thickness=2)
cv.circle(img,(img.shape[1]//2,img.shape[0]//2),radius=160,color=(0,255,0),thickness=2)
cv.line(img,(100,200),(300,300),(0,0,255),thickness=3)
cv.putText(img,"The king is back",org=(500,500),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=2,color=(0,0,255),thickness=2)
cv.imshow('Blank Image',img)
cv.waitKey(0)


# blank_image=np.zeros((500,500,3),dtype='uint8')

# blank_image[1:50,50:100]=0,100,0
# blank_image[100:150,150:200]=0,50,100
# blank_image[101:121]=50,150,50
# cv.imshow('Blank Image',blank_image)
# cv.waitKey(0)


