import cv2
import numpy as np

img = cv2.imread('sudoku.png')
grey = cv2.COLOR_BGR2GRAY
img1 = cv2.cvtColor(img, grey)

# normal thresholding
_, th1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
# adaptive thresholding
th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, 11)

cv2.imshow('Original Image', img1)
# cv2.imshow('Image', th1)
cv2.imshow('Adaptive', th2)
cv2.waitKey(0)
cv2.destroyAllWindows()