import random
# Welcome banner
import pyfiglet
import sys

scoreboard = []

def start_game():
    while True:
        name = input("Good day!, please enter your 'NAME' to start (or QUIT to exit): ")
        if name.lower() == "quit":
            sys.exit()
        elif name.isnumeric():
            print("{}?, that's an invalid input but you may provide a combination of numbers & letters.".format(name))
        else:
            greetings = pyfiglet.figlet_format("Welcome! {}!".format(name), font= "bubble")
            banner = pyfiglet.figlet_format("Let's Play the Number Guessing Game!")
            print(greetings)
            print (banner)
            if name.isalpha():
                break

    answer = random.randrange(1,10)
    attempt = 0
    guess = -1
    player = name

    while guess != answer:
        attempt += 1
        try:
            guess = input("Pick a number range from 1 to 10: ")
            guess = int(guess)
            if guess > 10: # guesses should not be outside this range
                print("Your guess of --> {} <-- is out of range.\nPlease try again!".format(guess))
            elif guess == 0:
                print("Your guess of --> {} <-- is not within the range of 1 to 10.\nPlease try again!".format(guess))

        except (ValueError, TypeError):
            print("--> {} <-- is an invalid input please enter a number.".format(guess))

        else:
            if guess == answer:
                print("Got it you made {} attempt/s to guess the correct number!".format(attempt))
                scoreboard.append(attempt)
            elif guess > answer:
                print("It's lower!")
            elif guess < answer:
                print("It's higher!")
# Displaying amount of tries and the high score to beat and ask player if he wants a remnatch also show ending message
    else:
        play = ''
        while True:
            try:
                play = input("You won the game do you want to a rematch!? (Enter Yes/No only): ")
                if play.isnumeric():
                    print("--> {} <-- that's an invalid input please enter a (Yes or No only).".format(play))
            except (ValueError, TypeError):
                print("--> {} <-- that's an invalid input please enter a (Yes or No only).".format(play))
            else:
                if play.lower() == "yes":
                    least_score = min(scoreboard)
                    print("\nThe least amount of {}! guesstimate(s) is the score to beat!".format(least_score))
                    start_game()
                elif play.lower() == "no":
                    print("Thank you for playing the Number guessing game {}!, See you again!".format(name))
                    sys.exit()

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    try:
        start_game()
    except SystemExit:
         print("Terminating program.")
