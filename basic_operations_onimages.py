import cv2 as cv
import numpy as np

# ACCESSING AND MODIFYING PIXEL VALUES

img = cv.imread('messi5.jpg')

# accessing all pixels
px = img[100, 100]  # returns [157 166 200]
# accessing just the blue part of pixel
blue_px = img[100, 100, 0]  # returns 157

# ACCESSING IMAGE PROPERTIES

shape = img.shape   # returns tuple (rows, columns, channels). If image is grayscale, no channels are returned
size = img.size     # returns no. of pixels in image

# IMAGE ROI (region of interest)

ball = img[280:240, 330:390]    # getting the ball, the indexing gives the coordinates of top-left and bottom-right
img[273:333, 100:160] = ball    # setting the ball image to a new region in the image



