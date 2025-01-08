#rock paper scissors game
import random
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#game images
game_images = [rock,paper,scissors]

#player move
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
#print(game_images[user_choice])


#computer move
computer_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("Computer chose: \n" + game_images[computer_choice])
    print("Invalid choice, You Lose!")
else:
    print("You Chose: \n "+ game_images[user_choice])
    print("Computer chose: \n" + game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
        #print(game_images[user_choice])
    elif computer_choice > user_choice:
        print("You Lose!")
        #print(game_images[user_choice])
    elif user_choice > computer_choice:
        print("You Win!")
        #print(game_images[user_choice])
    elif computer_choice == user_choice:
        print("Its a Draw!")
        #print(game_images[user_choice])
