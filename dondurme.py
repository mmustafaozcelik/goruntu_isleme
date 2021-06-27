import numpy as mp
import imutils
import cv2

image = cv2.imread("image/ev.jpg")
cv2.imshow("original",image)
cv2.waitKey(0)

(h,w)=image.shape[:2]
center=(w//2,h//2)

M= cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("45",rotated)
cv2.waitKey(0)

M= cv2.getRotationMatrix2D(center,-90,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("90",rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image,180)
cv2.imshow("180",rotated)
cv2.waitKey(0)
