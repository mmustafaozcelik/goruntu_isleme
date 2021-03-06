import numpy as np
import cv2
canvas =np.zeros((300,300,3), dtype="uint8")
(centerX,centerY)=(canvas.shape[1]//2,canvas.shape[0]//2)

white = (255,255,255)
for r in range(0,175,25):
    cv2.circle(canvas,(centerX,centerY),r,white,3)
cv2.imshow("Circle",canvas)
cv2.waitKey(0)
for i in range(0,25):
    radius = np.random.randint(5,high=200)
    color = np.random.randint(0,high=256, size=(3)).tolist()
    pt= np.random.randint(0,high=300,size=(2,))

    cv2.circle(canvas,tuple(pt),radius,color,-1)

cv2.imshow("canvas-5",canvas)
cv2.waitKey(0)