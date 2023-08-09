#program to blink a led connected to GPIO 18

import RPi.GPIO as GPIO
import time

#set GPIO warnings to false
GPIO.setwarnings(False)

#set GPIO mode
GPIO.setmode(GPIO.BCM)

#output pin
pin = 18

#set GPIO pin
GPIO.setup(pin, GPIO.OUT)

#blink the led
while True:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

#cleanup
GPIO.cleanup()

#end of program
