from  matplotlib import pyplot as plt
import numpy as np
import cv2

def plor_histogram(image,title,mask=None):
    chans=cv2.split(image)
    colors=("b","g","r")
    plt.figure()
    plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("pix")

    for (chanicolor) in zip(chans,colors):
        hist=cv2.calcHist([chan],[0],mask,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])


image=cv2.imread("image/ev.jpg")
cv2.imshow("orgi",image),ü
plot_histogram(image,"hisr")


mask = np.zeros(image.shape[:2],dtype="uint8")
cv2.rectangle(mask,(15,15),(130,100),255,-1)
cv2.imshow("mask",mask)

masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("maske ap",masked)

plot_histogram(image,"mask image",mask=mask)

plt.show()
cv2.waitKey(0)
