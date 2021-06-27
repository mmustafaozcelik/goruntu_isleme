import cv2
image = cv2.imread("image/coin.png")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blur",image)
canny=cv2.Canny(image,30,50)
cv2.imshow("cann",canny)
cv2.waitKey(0)

