import cv2
import numpy as np

# print(img.shape)    # returns tuple (rows, columns, no. of channels)
# print(img.size)     # returns number of pixels
# print(img.dtype)    # returns image data type

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# resizing images
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# adding the two images
dst1 = cv2.add(img, img2)
# adding the two images (weighted)
dst2 = cv2.addWeighted(img, 0.2, img2, 0.9, 0)

cv2.imshow('Image', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()