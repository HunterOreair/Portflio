#A Python program that has the user guess what number the computer is thinking. Made by Hunter Oreair

from random import *

min = 1 # Sets the lowest possible number the comp can think of
max = 100 # Sets the highest number

def Guess(): #  Creates a method called Guess
    num = randint(min, max) # Sets what number the comp is thinking of
    print("Im thinking of a number between 1 and 100. Try to guess it :)")
    again = True
    while again: # while again is True, do the following code.
        guess = (int(input())) # Takes the users input, aka 'guess'

        if guess < num: # if guess is less than num, try again.
            print("you guessed", guess, "which is too low, try again.")
        elif guess > num: # if guess is more than num, try again.
            print("you guessed", guess, "which is too high, try again.")
        else: # otherwise, you've guessed correctly. Congrats
            print("You guessed", guess, "which is CORRECT!")
            again = False

    print("High five!")

Guess()
