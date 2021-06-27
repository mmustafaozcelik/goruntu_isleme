from __future__ import print_function
import mahotas
import cv2

image=cv2.imread("image/coin.png")
cv2.imshow("or",image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blur",image)

T=mahotas.thresholding.otsu(blurred)
print("otsu:{}".format(T))

thresh =image.copy()
thresh[thresh>T]=255
thresh[thresh<T]=0
thresh=cv2.bitwise_not(thresh)
cv2.imshow("otsu",thresh)

T=mahotas.thresholding.rc(blurred)
print("rc:{}".format(T))
thresh =image.copy()
thresh[thresh>T]=255
thresh[thresh<T]=0
thresh=cv2.bitwise_not(thresh)
cv2.imshow("otsu",thresh)
cv2.waitKey(0)
