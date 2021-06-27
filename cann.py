import cv2
import numpy as np

image=cv2.imread("image/coin.png")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(11,11),0)
cv2.imshow("image",blurred)

edged= cv2.Canny(blurred,30,50)
cv2.imshow("edg",edged)

(_,cnts,_) = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("demir={}".format(len(cnts)))

coins =image.copy()
cv2.drawContours(coins,cnts,-1,(0,255,0),2)
cv2.imshow("coin",coins)
cv2.waitKey(0)
for (i,c) in enumerate(cnts):
    (x,y,w,h)=cv2.boundingRect(c)

    print("coin #{}",format(i+1))
    coin=image[yy+h,x:x+w]
    cv2.imshow("coin",coin)

    mask=np.zeros(image.shape[:2],dtype=np.uint8)
    ((centerX,centerY),radius)=cv2.minEnclosingCircle(c)
    cv2.circle(mask,(int(centerX),int(centerY)),int(radius),255,-1)
    mask =mask[y:y+h,x:x+w]
    cv2.imshow("mask",cv2.bitwise_and(coin,coin,mask=mask))
    cv2.waitKey(0)