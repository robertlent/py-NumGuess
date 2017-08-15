import os
from random import randrange

def new_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    answer = input("Do you want to start a new game? ").lower()

    if answer not in ['yes', 'y', 'no', 'n']:
        new_game()
    else:
        if answer == 'yes' or answer == 'y':
            main()
        elif answer == 'no' or answer == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thank you for playing!")
            input("Press the 'Enter' key to exit the game.")
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    guesses_left = 5
    guessed = []

    # Randomly generates a number from 1 through 50
    rand_num = randrange(1, 51)

    print("A random number between 1 and 50 has been generated.\n\nYou have 5 guesses to find it!")

    # While the Player has any guesses left, they will be prompted to guess again. Once they run out of guesses,
    # the game is over, they are told the number, and new_game is called.
    while guesses_left > 0:
        while True:
            try:
                guess = int(input("\nYou have %s guess(es) left: " % guesses_left))
                if guess not in range(1, 51):
                    raise ValueError()
            except ValueError:
                print("Enter a number between 1 and 50!")
                continue
            else:
                break

        guesses_left -= 1
        guessed.append(str(guess))

        if guess == rand_num:
            os.system('cls' if os.name == 'nt' else 'clear')
            input("You win! The number was %s!\n" % rand_num)
            new_game()
            return
        else:
            print("Wrong!")
            os.system('cls' if os.name == 'nt' else 'clear')
            if guess < rand_num:
                print("Your guess was too low!\n")
                print("You have previously guessed: " + (", ".join(guessed)))
            else:
                print("Your guess was too high!\n")
                print("You have previously guessed: " + (", ".join(guessed)))
    else:
        input("\nYou lose. The number was: %s" % rand_num)
        new_game()

new_game()
