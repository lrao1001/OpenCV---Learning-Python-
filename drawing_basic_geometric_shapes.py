import numpy as np
import cv2

# reading an image using open-cv
# img = cv2.imread('lena.jpg', 1)

# reading an image using numpy zeros
img = np.zeros([512, 512, 3], np.uint8)

# draw a line
img = cv2.line(img, (0, 0), (255, 255), (0, 255, 179), 10)

# draw a rectangle
img = cv2.rectangle(img, (200, 200), (390, 140), (0, 255, 0), -1)

# write text
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'Lena', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
