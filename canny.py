import cv2
import numpy as np
from matplotlib import pyplot as plt


def change_threshold(x):
    th1 = cv2.getTrackbarPos('th1', 'Image')
    th2 = cv2.getTrackbarPos('th2', 'Image')

    print(th1)
    print(th2)

    img2 = cv2.Canny(origin, th1, th2)
    cv2.imshow('Image', img2)


origin = cv2.imread('data/lena.jpg', 0)


img = cv2.Canny(origin, 100, 200)
cv2.imshow('Image', img)
cv2.createTrackbar('th1', 'Image', 100, 255, change_threshold)
cv2.createTrackbar('th2', 'Image', 200, 255, change_threshold)

cv2.waitKey(0)

cv2.destroyAllWindows()

# canny = cv2.Canny(img, 100, 200)
#
# titles = ['Image', 'Canny']
# images = [img, canny]
#
# for i in range(len(images)):
#     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()