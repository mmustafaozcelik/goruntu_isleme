from matplotlib import pyplot as plt
import cv2

image = cv2.imread("image/ev.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BAYER_BG2GRAY)
cv2.imshow("orji",image)
hist= cv2.calcHist([image],[0],None,[256],[0,256])

plt.figure()
plt.title("sfsd")
plt.xlabel("bins")
plt.ylabel("pixel")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
