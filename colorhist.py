from __future__ import print_function
from matplotlib import pyplot as plt
import cv2

image = cv2.imread("image/ev.jpg")
cv2.imshow("orji",image)

chans=cv2.split(image)
colors=("b","g","r")
plt.figure()
plt.title("aa")
plt.xlabel("as")
plt.ylabel("ass")

for (chan,color) in zip(chans,colors):
    hist=cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])

fig = plt.figure()

ax = fig.add_subplot(131)
hist=cv2.calcHist([chans[1],chans[0]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("g and b")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist=cv2.calcHist([chans[1],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("g and r")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist=cv2.calcHist([chans[0],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("r and b")
plt.colorbar(p)
