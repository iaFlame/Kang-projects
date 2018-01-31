# PIR Motion Test
# Tristan 1-24-18
# chez

import RPi.GPIO as GPIO
import time

#Setting up my LED pins
GPIO.setmode(GPIO.BCM) # Sets the numbering scheme to Broadcom numbering
LED_pin_green = 19
GPIO.setup(LED_pin_green, GPIO.OUT)
PIR_pin = 12
GPIO.setup(PIR_pin, GPIO.IN)
button_pin = 6
GPIO.setup(PIR_pin, GPIO.OUT)
#Forever loop that checks if the sensor is detecting motion
mdm = False
while True:
    if mdm == True:
        if GPIO.input(PIR_pin):
            print("yo yo yo ma name is sensor and me is detecting motion oOHHHHHYH")
            time.sleep(.5)
            GPIO.output(LED_pin_green,GPIO.HIGH)
        else:
            GPIO.output(LED_pin_green,GPIO.LOW)
    if GPIO.input(button_pin):
        if mdm == True:
            mdm = False
        else:
            mdm = True


        

    
    



