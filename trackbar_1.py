import cv2
import numpy as np


# does nothing
def nothing(x):
    pass


# creating a black image and a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Image')

# creating the trackbar
cv2.createTrackbar('B', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('R', 'Image', 0, 255, nothing)
cv2.createTrackbar('Switch', 'Image', 0, 1, nothing)


while True:
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # getting values of current trackbar
    b = cv2.getTrackbarPos('B', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')
    switch = cv2.getTrackbarPos('Switch', 'Image')

    if switch == 1:
        # setting image colors
        img[:] = [b, g, r]

cv2.destroyAllWindows()

