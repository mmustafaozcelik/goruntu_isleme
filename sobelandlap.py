import numpy as np
import cv2
image = cv2.imread("image/coin.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("orgi",image)

lap = cv2.Laplacian(image,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("lap",lap)
cv2.waitKey(0)

sobelX=cv2.Sobel(image,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(image,cv2.CV_64F,0,1)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("sobelx",sobelX)
cv2.imshow("sobely",sobelY)
cv2.imshow("sobelc",sobelCombined)
cv2.waitKey(0)