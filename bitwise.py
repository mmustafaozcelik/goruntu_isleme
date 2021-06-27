import cv2
import numpy as np
rectangle = np.zeros((300,300),dtype=np.uint8)
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("rec",rectangle)
cv2.waitKey(0)

circle=np.zeros((300,300),dtype=np.uint8)
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("circ",circle)
cv2.waitKey(0)

bitwiseand =cv2.bitwise_and(rectangle,circle)
cv2.imshow("and",bitwiseand)
cv2.waitKey(0)

bitwiseor =cv2.bitwise_or(rectangle,circle)
cv2.imshow("and",bitwiseor)
cv2.waitKey(0)

bitwiseXor =cv2.bitwise_xor(rectangle,circle)
cv2.imshow("Xor",bitwiseXor)
cv2.waitKey(0)

bitwiseNot =cv2.bitwise_not(rectangle,circle)
cv2.imshow("bot",bitwiseNot)
cv2.waitKey(0)