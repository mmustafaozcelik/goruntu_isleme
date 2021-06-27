import cv2
image= cv2.imread("image/coin.png")
cv2.imshow("original",image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blurred",image)

(T,thresh) =cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("tresh",thresh)

(I,threshInv) =cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow("treshI",threshInv)

cv2.imshow("coins",cv2.bitwise_and(image,image,mask=threshInv))
cv2.waitKey(0)


