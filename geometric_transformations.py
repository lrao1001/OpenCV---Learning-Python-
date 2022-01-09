import cv2
import numpy as np

# TRANSLATION ______________________________________________________________
# img = cv2.imread('messi5.jpg')
# rows, cols, channel = img.shape
#
# M = np.float32([[1, 0, 100], [0, 1, 50]])   # translating by 100 right and 50 down
# dst = cv2.warpAffine(img, M, (cols, rows))
#
# cv2.imshow('image', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# AFFINE _________________________________________________________________

img = cv2.imread('messi5.jpg')
rows, cols, channels = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Warped', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

