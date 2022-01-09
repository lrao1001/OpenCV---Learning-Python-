import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)  # 2 by 2 square shape which is applied on the black dots on mask
dilation = cv2.dilate(mask, kernel, iterations=5)
erosion = cv2.erode(mask, kernel, iterations=10)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

titles = ['image', 'mask', 'mg']
images = [img, mask, mg]

for i in range(len(titles)):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    # ^ 1 = rows, 1 = columns, i+1 = which element this image is
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()