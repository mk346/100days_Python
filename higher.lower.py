#guided solution
import random, os
from art import logo, vs
from game_data import data

#clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#display art
print(logo)
score = 0
game_over = False
account_b = random.choice(data)

def format_data(account):
    '''format account data into printable format'''
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return (f"{account_name}, a {account_desc}, from {account_country}")

def check_answer(guess, a_followes, b_followers):
    '''take the user guess and followers count and check if user guess is correct'''
    if a_followes > b_followers:
        return guess == 'a' 
    else:
        return guess == 'b'
    

#make game repeatable
while not game_over:
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
        score += 1
        print(f"You're right!. Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True


