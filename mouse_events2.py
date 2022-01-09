import cv2
import numpy as np


def mouse_click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:

        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        my_color_image = np.zeros((200, 200, 3), np.uint8)
        my_color_image[:] = [blue, green, red]

        # cv2.circle(img, (x, y), 3.5, (0, 0, 255), -1)
        # points.append((x, y))
        # if len(points) >= 2:
        #     cv2.line(img, points[-1], points[-2], (255, 0, 0), 2)

        cv2.imshow('Color', my_color_image)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)

points = []
cv2.setMouseCallback('Image', mouse_click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()