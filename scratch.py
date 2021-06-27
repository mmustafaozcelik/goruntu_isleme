
import cv2 as cv

image = cv.imread("image/ev.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))

cv.namedWindow("output",cv.WINDOW_NORMAL)

(b, g, r)=image[0,0]
print("Pixel at(0,0)-Red: {} ,Green: {},Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
print("Pixel at(0,0)-Red: {} ,Green: {},Blue: {}".format(r, g, b))
cv.imshow("output",image)
cv.waitKey(0)
cv.destroyWindow()