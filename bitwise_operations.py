"""
Program: Bitwise operations on images
Author: Lakshya Rao
Date: 03 August 2021
Note: Operations only work on B&W images
"""

import cv2
import numpy as np



# img1 = np.zeros((250, 500, 3), np.uint8)
# img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
# img2 = np.full((250, 500, 3), 255, dtype=np.uint8)
# img2 = cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)

# initializing images
img1 = cv2.imread('lena.jpg')
img1 = cv2.resize(img1, (200, 200))
img2 = cv2.imread('messi5.jpg')
img2 = cv2.resize(img2, (200, 200))

# AND operation
bitAnd = cv2.bitwise_and(img2, img1)
# OR operation
bitOR = cv2.bitwise_or(img2, img1)
# XOR operation
bitXOR = cv2.bitwise_xor(img2, img1)

cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow('bit = XOR', bitXOR)
# cv2.imshow('bit = OR', bitOR)
# cv2.imshow('bit = And', bitAnd)




cv2.waitKey(0)
cv2.destroyAllWindows()