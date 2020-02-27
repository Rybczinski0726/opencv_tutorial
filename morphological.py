import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

titles = ['Image', 'Mask', 'Dilation', 'Erosion', 'Opening', 'Closing', 'MG', 'TH']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks(([])), plt.yticks([])

plt.show()