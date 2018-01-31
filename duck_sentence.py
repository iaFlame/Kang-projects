# Tristan Kang
# 10-11-17
# Duck Sentence Generator 21000
# Makes duck sentences like a madlib

# Getting the Player Name
print ("*" * 48)
print ("* Welcome to the duck sentence generator 21000 * ")
print ("*" * 48)
player_name = input("Please enter your name: ")
print (player_name)

# + can also add or join strings together
message = "Yo, " + player_name + "! Let's make a duck sentence!"
print (message.upper())

# Gather input from the user
famous_person = input("Enter the name of a famous person: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter anoter adjective: ")
verb = input("Enter a verb ending in _ING: ")

duck_sentence = ("The " + adjective1 + " " + player_name + " is " +
                 verb + " the " + adjective2 + " " + famous_person)
print(duck_sentence)
