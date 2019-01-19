#A simple python program that rolls die and returns the number that has been rolled. Made by Hunter Oreair.

from random import randint # imports randint. duh.

min = 1 #sets the minimum value on the dice that you can roll
max = 6 #sets the maximum value

def die(): # Creates a method called die
    rollDie = randint(min, max) # sets what number you rolled
    print("You rolled a", rollDie) # prints the number you rolled

def rollAgain():
    again = True

    while again: #while 'again' is True, do the following:
        die() # calls the die method.
        print("Would you like to roll again? y/n") #asks if you would like to roll again.
        ans = input() #takes your input

        if ans == "y": #if your input equals 'y' then run the while loop again
            again = True
        else: #anything will end the program
            again = False

rollAgain() # calls rollAgain method, running the program.
