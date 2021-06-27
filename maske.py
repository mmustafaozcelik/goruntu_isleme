import numpy as np
import cv2
image = cv2.imread("image/ev.jpg")
cv2.imshow("orji",image)

mask = np.zeros(image.shape[:2],dtype=np.uint8)
(cX,cY) = (image.shape[1]//5,image.shape[0]//2)
cv2.rectangle(mask,(cX-75,cY-75),(cX+75,cY+75),225,-1)
cv2.imshow("mask",mask)

masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("maske",masked)
cv2.waitKey(0)

mask=np.zeros(image.shape[:2],dtype=np.uint8)
cv2.circle(mask,(cX,cY),100,255,-1)
masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("maskeli",mask)
cv2.imshow("maske2",masked)
cv2.waitKey(0)
