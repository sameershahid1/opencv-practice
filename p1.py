import cv2 as cv

#Reading images
img=cv.imread('archive/train/cats/cat_10.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)


#Reading Videos
capture=cv.VideoCapture('Videos/C1.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow('Cat Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# Rescale function: Can be applied on videos, Live Videos and image
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# Changing the dimension: Will works only Live Video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


capture=cv.VideoCapture('Videos/C1.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resize=rescaleFrame(frame,0.20)
    cv.imshow('Cat Video',frame_resize)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()



