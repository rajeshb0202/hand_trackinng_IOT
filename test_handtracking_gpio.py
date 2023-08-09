#track hands using opencvand mediapipe. And switch on or off the bulb using gpio pins

import cv2
import mediapipe as mp
import time
import RPi.GPIO as GPIO
import math

#gpio set warnings to false
GPIO.setwarnings(False)

#global variables
cap = cv2.VideoCapture(0)

#x and y variables for thumb and index finger
x_thumb = 0
y_thumb = 0
x_index = 0
y_index = 0


#mediapipe variables
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#fps variables
pTime = 0
cTime = 0

#set GPIO mode
GPIO.setmode(GPIO.BCM)

#output pin
pin = 17

#reset GPIO pin
GPIO.cleanup(pin)

#set GPIO pin
GPIO.setup(pin, GPIO.OUT)


#detect the hands
def detectHands(frame):
    #convert frame to RGB
    imgGRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #process the image
    results = hands.process(imgGRAY)
    #print(results.multi_hand_landmarks)
    #if there are hands in the frame
    if results.multi_hand_landmarks:
        #for each hand in the frame
        for handLms in results.multi_hand_landmarks:
            #get the x and y coordinates of the thumb and index finger
            x_thumb = handLms.landmark[4].x
            y_thumb = handLms.landmark[4].y
            x_index = handLms.landmark[8].x
            y_index = handLms.landmark[8].y

            #draw the landmarks of the thumb and index finger
            cv2.circle(frame, (int(x_thumb*640), int(y_thumb*480)), 10, (255,0,0), cv2.FILLED)
            cv2.circle(frame, (int(x_index*640), int(y_index*480)), 10, (255,0,0), cv2.FILLED)
            
            #draw a straight line between the thumb and index finger
            cv2.line(frame, (int(x_thumb*640), int(y_thumb*480)), (int(x_index*640), int(y_index*480)), (255,0,0), 3)

            #calculate the distance between the thumb and index finger
            distance = math.sqrt((x_thumb - x_index)**2 + (y_thumb - y_index)**2)
            
            #map the distance to the range 0 to 100
            distance = int(distance * 100)
            print(distance)

            #if the distance is less than 50, switch off the bulb
            if distance < 50:
                GPIO.output(pin, GPIO.LOW)
            
            #if the distance is greater than 50, switch on the bulb
            else:
                GPIO.output(pin, GPIO.HIGH)
            
            #display the frame
            cv2.imshow('frame', frame)





#main function
def main():
    while True:
        ret, frame = cap.read()
        #detect the hands
        frame = detectHands(frame)
        
        
        '''
        #calculate fps
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        #display fps
        cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        '''

        
        #press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    #cleanup
    GPIO.cleanup()
