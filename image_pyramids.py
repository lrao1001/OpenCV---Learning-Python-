import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
lower_res1 = cv.pyrDown(img)
lower_res2 = cv.pyrDown(lower_res1)

cv.imshow('Original', img)
cv.imshow('PyrDown 1', lower_res2)
cv.waitKey(0)
cv.destroyAllWindows()