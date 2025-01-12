# number guessing game
import random

LOGO = r"""

 _______           _______  _______  _______   _________          _______    _                 _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  \__   __/|\     /|(  ____ \  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/     ) (   | )   ( || (    \/  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |     | |   | )   ( || (____/\  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)     )_(   |/     \|(_______/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/
                                                                                                                                  

"""
print(LOGO)
number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    ATTEMPTS = 10
elif difficulty == 'hard':
    ATTEMPTS  = 5
else:
    print("Invalid input. Defaulting to 'easy' mode.")
    ATTEMPTS = 10

while ATTEMPTS  > 0:
    print(f"You have {ATTEMPTS} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    ATTEMPTS  -= 1
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    if guess < number and ATTEMPTS  > 0:
        print("Too low. \nGuess again.")
    elif guess > number and ATTEMPTS  > 0:
        print("Too high. \nGuess again.")
if ATTEMPTS  == 0:
    print(f"You've run out of guesses. The number was {number}.")
