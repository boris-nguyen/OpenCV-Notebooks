import cv2
import numpy as np

###################################
## FUNCTION
###################################
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(255,0,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,255,0),-1)

cv2.namedWindow(winname='Drawing')

cv2.setMouseCallback('Drawing', draw_circle) 

###################################
## SHOWING IMAGE WITH OPENCV
###################################
img = np.zeros((512,512,3),dtype=np.int8)

while True:
    cv2.imshow('Drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
