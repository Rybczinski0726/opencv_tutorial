import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5,))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Image', '2D Convolution', 'Blur', 'Gaussian', 'Bilateral']
images = [img, dst, blur, gblur, bilateral]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
