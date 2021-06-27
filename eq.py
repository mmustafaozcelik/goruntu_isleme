import numpy as np
import cv2

image=cv2.imread("image/ev.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("or",image)
eq=cv2.equalizeHist(image)

cv2.imshow("hist",np.hstack([image,eq]))
cv2.waitKey(0)
