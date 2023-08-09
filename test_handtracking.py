# aprogram to detect hands using mediapipe and opencv and display the video from webcam

import cv2
import mediapipe as mp
import time

#global variables
cap = cv2.VideoCapture(1)

#mediapipe variables
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#fps variables
pTime = 0
cTime = 0

while True:
    ret, frame = cap.read()
    #convert frame to RGB
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #process the image
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    #if there are hands in the frame
    if results.multi_hand_landmarks:
        #for each hand in the frame
        for handLms in results.multi_hand_landmarks:
            #draw the hand landmarks
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    #calculate fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    #display fps
    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    #display the frame
    cv2.imshow('frame', frame)
    #press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



