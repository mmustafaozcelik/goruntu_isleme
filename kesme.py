import cv2

image = cv2.imread("image/ev.jpg")
cv2.imshow("original",image)

cropped=image[20:136,91:176]
cv2.imshow("kesme",cropped)
cv2.waitKey(0)