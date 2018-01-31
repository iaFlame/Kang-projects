# Light Up Guessing Game
# Tristan Kang
# January 3, 2018
# Gues the number (1 to 20), shows blue if too low, red if
# too high, green if correct. You get five tries.

import random
import time
import RPi.GPIO as GPIO

def game_over():
    '''My game over function'''
    print("You ran out of guesses! So sad!")
    print("You are a banana")

def LED(pin):
    for i in range(5):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(.2)
    
    
GPIO.setmode(GPIO.BCM) # Sets the numbering scheme to Broadcom numbering
LED_pin_red = 21
LED_pin_green = 22
LED_pin_blue = 23

GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)
GPIO.setup(LED_pin_blue, GPIO.OUT)

# Title and instructions
print("Light Up Guessing Game")
print(""" You have five guesses to guess a number between 1 and 20
Blue = Too Low
Red = Too High
Green = Correct
""")
print("Copyright Flame Incorporated")

play_again = "Y"

while play_again == "Y":

    # Get a random number (1 and 20)


    num = random.randint(1,20)

    # Start a loop (5 tries)
    guesses = 0
    while guesses <= 4:
    # Get a guess from the user
        guess = input("Guess a number from 1 to 20: ")
        if guess == ("Cam Newton is da best!"):
            print("OHHH U FOUND AN EASTER EGG MISTA MAN OHHHHHHHHHHH YOU WIN!!")
            LED(LED_pin_green)
            time.sleep(0.1)
            LED(LED_pin_red)
            time.sleep(0.1)
            LED(LED_pin_blue)
            break
        guess = int(guess)
        guesses += 1
    # Check if correct, too low or too high
        if guess == num:
            print("You are correct!")
            # TODO: Blink Green
            LED(LED_pin_green)
            break
        elif guess < num:
            print("Tooo low!")
            # TODO: Blink Blue
            LED(LED_pin_blue)
        else: # Must be too high
            print("Too high")
            # TODO: Blink Red
            LED(LED_pin_red)

    else:
        game_over()
        print("Thank you for playing!")
    play_again = input("Do you want to play again? Y or N? ")    
    
    
    # Flash the appropriate color for three seconds

    GPIO.cleanup()

