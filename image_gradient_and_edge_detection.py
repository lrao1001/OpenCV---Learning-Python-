# Goals:
# Find Image gradients, edges etc
# We will see following functions :
# cv.Sobel(), cv.Scharr(), cv.Laplacian() etc

# ____________________________________________________________________

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
laplace = cv2.Laplacian(img, cv2.CV_64F)

titles = ['image']
images = [img]

for i in range(len(titles)):
    plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()