import cv2
image= cv2.imread("image/coin.png")
cv2.imshow("original",image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blurred",image)

thresh =cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("thresh",thresh)

thresh= cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,3)

cv2.imshow("gthresh",thresh)
cv2.waitKey(0)


