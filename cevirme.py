import numpy as np
import cv2

image = cv2.imread("image/ev.jpg")
cv2.imshow("image", image)

M = np.float32([[1,0,25],[0,1,50]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("shifted down and right",shifted)
cv2.waitKey(0)

M = np.float32([[1,0,-50],[0,1,-90]])
shifted2 = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("shifted up and left",shifted2)
cv2.waitKey(0)
