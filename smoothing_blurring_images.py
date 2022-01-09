import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
einstein = cv2.imread('einstein.jpg')

# setting the kernel
kernel = np.ones((5, 5), np.float32)/25     # this kernel acts as an average
# 2D convolution
dst = cv2.filter2D(img, -1, kernel)

# normal blur (average)
blur = cv2.blur(img, (5, 5))

# gaussian blur // best to remove gaussian noise //
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# median blur // best to remove salt&pepper noise //
einstein_blur = cv2.medianBlur(einstein, 5)

# bilateral blur // best ot remove blur but still keep edges sharp //
einstein_bilateral_blur = cv2.bilateralFilter(einstein, 9, 75, 75)

titles = ['image', '2D Convolution', 'Blur', 'Gaussian Blur']
images = [img, dst, blur, gaussian_blur]

# for i in range(len(titles)):
#     plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()

plt.subplot(2, 2, 1), plt.imshow(einstein, 'gray')
plt.title('Original')
plt.subplot(2, 2, 2), plt.imshow(einstein_blur, 'gray')
plt.title('Median Blur ksize=3')
plt.subplot(2, 2, 3), plt.imshow(einstein_blur, 'gray')
plt.title('Median Blur ksize=5')
plt.subplot(2, 2, 4), plt.imshow(einstein_bilateral_blur, 'gray')
plt.title('Bilateral Blur')

plt.show()