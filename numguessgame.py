from random import randrange
import os, sys


def new_game():
    answer = input("Do you want to start a new game? ").lower()
    #If Player answers yes, a new game is started. Otherwise, the screen is cleared, the player is thanked, and the game can be exited by pressing enter.
    if answer == 'yes':
        main()
    elif answer == 'no':
        os.system('cls')
        print("Thank you for playing!")
        input("Press the 'Enter' key to exit the game.")
        quit

def main():
    os.system('cls')

    guesses_left = 5

    #Randomly generates a number from 1 through 50
    r = randrange(1, 51)

    print("A random number between 1 and 50 has been generated.\n\nYou have 5 guesses to find it!")

    #While the Player has any guesses left, they will be prompted to guess again. Once they run out of guesses, the game is over, they are told the number, and new_game is called.
    while guesses_left > 0:
        guess = int(input("\nYou have %s guess(es) left: " % guesses_left))
        
        #Checks if the Player's input is between 1 and 50. If not, the Player is prompted to enter a new choice.
        if (guess > 50) or (guess < 1):
            guess = int(input("\n%s is not a valid entry. Please input a number between 1 and 50: " % guess))

        guesses_left -= 1
                           
        if guess == r:
            print("\nYou win!\n")
            guesses_left = 0
            new_game()
            return
        else:
            print("Wrong!")
    else:
        print("\nYou lose. The number was: %s" % r)
        new_game()

new_game()
