import RPi.GPIO as GPIO
import time

#Variable for the GPIO pin number
LED_pin_blue = 21
LED_pin_green = 22
LED_pin_yellow = 23 

#Tell the Pi we are using the breakout board pin numbering
GPIO.setmode(GPIO.BCM)

#Set up the GPIO pin for output
GPIO.setup(LED_pin_blue, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)
GPIO.setup(LED_pin_yellow, GPIO.OUT)

GPIO.setwarnings (False)

#Loop to blink our led
while True:

    GPIO.cleanup()
    
    #print("Blue!")
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    time.sleep(.02)
    GPIO.output(LED_pin_blue, GPIO.LOW)
    time.sleep(.02)

    #print("Yellow!")
    GPIO.output(LED_pin_yellow, GPIO.HIGH)
    time.sleep(.02)
    GPIO.output(LED_pin_yellow, GPIO.LOW)
    time.sleep(.02)

    #print("Green!")
    GPIO.output(LED_pin_green, GPIO.HIGH)
    time.sleep(.02)
    GPIO.output(LED_pin_green, GPIO.LOW)
    time.sleep(.02)

    #print("Yellow!")
    #GPIO.output(LED_pin_yellow, GPIO.HIGH)
    #time.sleep(.0005)
    #GPIO.output(LED_pin_yellow, GPIO.LOW)
    #time.sleep(.05)



