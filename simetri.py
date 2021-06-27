import cv2

image = cv2.imread("image/ev.jpg")
cv2.imshow("original",image)
flipped=cv2.flip(image,1)
cv2.imshow("flip",flipped)

flipped=cv2.flip(image,0)
cv2.imshow("flip2",flipped)

flipped=cv2.flip(image,-1)
cv2.imshow("flip3",flipped)

cv2.waitKey(0)
