# Tristan Kang 10-24-17
# Norweign Blye Guessing Game
# A guessing game
import random


print("*" * 80)
print("* WELCOME TO THE NORWEIGN BLUE GUESSING GAME")
print("*" * 80)

instructions = """You walk into a pet
store and need to guess the age of a Norweign Blue parrot
in order to take it home.
:) 
You only get 5 guesses!!
"""

print(instructions)
# Make up the parrot's age
# TODO: make it random
parrot_age = random.randint(1,22)

# Set the number of guesses to 0
number_of_guesses = 0

while number_of_guesses < 5:
    # Get a guess from the user
    guess = input("Guess the age of the parrot [1 to 21]:")
    guess = int(guess) # Converts a string to an integer and stores in back tnto guess
    number_of_guesses = number_of_guesses + 1
    print(number_of_guesses)
    if guess == parrot_age:
        print("You Win!")
        break
    else:
        # TODO: Add higher or lower
        if guess < parrot_age:
            print("Too low")
        else:
            print("Too high")
        print("Omg that was the worst guess in the entire world, YOU CAN DO BETTERRRR!")
print("Thank you for playing!")
if number_of_guesses == 5:
    print ("Its actual age was" , parrot_age, "years old. Jk, it was 22 lelelel")
                       
