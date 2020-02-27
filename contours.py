import numpy as np
import cv2

img = cv2.imread('data/opencv-logo.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
# print(contours[0])
print(hierarchy)

cv2.drawContours(img, contours, 3, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Gray Image', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()