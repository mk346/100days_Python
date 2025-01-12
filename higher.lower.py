'''import needed functions'''
import random
import os
from art import logo, vs
from game_data import data

#clear the screen
def clear():
    '''clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

#display art
print(logo)
SCORE = 0
GAME_OVER = False
account_b = random.choice(data)

def format_data(account):
    '''format account data into printable format'''
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return (f"{account_name}, a {account_desc}, from {account_country}")

def check_answer(user_guess, a_followes, b_followers):
    '''take the user guess and followers count and check if user guess is correct'''
    if a_followes > b_followers:
        return user_guess == 'a'
    return user_guess == 'b'


#make game repeatable
while not GAME_OVER:
    #generate random account
    #make account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    #ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if user guess is correct
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    #clear the screen between rounds
    clear()
    print(logo)

    #give user a feedback on their guess and score keeping
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        SCORE += 1
        print(f"You're right!. Current score: {SCORE}")
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        GAME_OVER = True
