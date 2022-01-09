import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('gradient.png')
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)        # binary threshold
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)    # inverse binary threshold
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# ^ until threshold (127), pixel values are normal, after 127, they stay at 127.
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# ^ when pixel value is out of boundaries, it is turned to 0 (black)

titles = ['Original Image', 'BINARY', 'BINARY-INV', 'TRUNC', 'TO-ZERO']
images = [img, th1, th2, th3, th4]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()