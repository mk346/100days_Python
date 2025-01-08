# higher and lower game
import random
from art import logo, vs
from game_data import data

# print(art.logo)
# print(art.vs)
comparison = []
count_list = []

def get_data(data):
    '''Returns a random data from the list'''
    return random.choice(data)

def game():
    '''game function'''
    is_game_over = False
    score = 0
    while not is_game_over:
        get_another_data()
        print(logo)
        print(f"Compare A: {comparison[0]['name']}, a {comparison[0]['description']}, from {comparison[0]['country']}")
        print(vs)
        print(f"Againts B: {comparison[1]['name']}, a {comparison[1]['description']}, from {comparison[1]['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ")
        count_list.append(comparison[0]['follower_count'])
        count_list.append(comparison[1]['follower_count'])
        max_count = max(count_list)
        if choice == "A":
            your_choice = comparison[0]['follower_count']
        elif choice == "B":
            your_choice = comparison[1]['follower_count']
        if your_choice < max_count:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_game_over = True
        elif your_choice == max_count:
            score += 1
            get_another_data()
            print(f"You're right!. Current score: {score}")
    

def get_another_data():
    for _ in range(2):
        comparison.append(get_data(data))
        #print(comparison)
game()



