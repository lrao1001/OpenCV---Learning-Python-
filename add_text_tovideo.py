import numpy as np
import cv2
import datetime


cap = cv2.VideoCapture(0)
# cap.set(3, 720)             # '3' refers to width
# cap.set(4, 720)             # '4' refers to height

while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        date_t = str(datetime.datetime.now())

        frame = cv2.putText(frame, date_t, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()