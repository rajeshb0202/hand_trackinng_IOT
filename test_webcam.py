#opencv program to read image display a video from webcam

import cv2
import numpy as np

#global variables
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    #print frame width and height
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))



    #press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

