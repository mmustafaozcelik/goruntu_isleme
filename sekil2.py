import numpy as np
import cv2
canvas =np.zeros((300,300,3), dtype="uint8")
green=(0,255,0)
cv2.rectangle(canvas,(10,10),(60,60),green,1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
red=(0,0,255)
cv2.rectangle(canvas,(50,200),(200,225),red,5)
cv2.imshow("Canvas-2",canvas)
cv2.waitKey(0)