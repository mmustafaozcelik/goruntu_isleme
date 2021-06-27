import numpy as np
import cv2

image = cv2.imread("image/ev.jpg")
cv2.imshow("orji",image)
(B,G,R) =cv2.split(image)

cv2.imshow("red",R)
cv2.imshow("green",G)
cv2.imshow("blue",B)
cv2.imshow("orji",image)
cv2.waitKey(0)

merged = cv2.merge([B,G,R])
cv2.imshow("merged",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros=np.zeros(image.shape[:2],dtype=np.uint8)
cv2.imshow("red",cv2.merge([zeros,zeros,R]))
cv2.imshow("green",cv2.merge([zeros,G,zeros]))
cv2.imshow("blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
