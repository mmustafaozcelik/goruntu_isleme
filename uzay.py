import cv2

image = cv2.imread("image/ev.jpg")
cv2.imshow("orji",image)

gray=cv2.cvtColor(image,cv2.COLOR_BAYER_BG2GRAY)
cv2.imshow("gray",gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BAYER_BGR2HSV)
cv2.imshow("hsv",hsv)

lab = cv2.cvtColor(image,cv2.COLOR_BAYER_BGR2LAB)
cv2.imshow("gray",lab)

cv2.waitKey(0)

