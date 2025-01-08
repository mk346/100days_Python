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
#player move
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

#computer move
computer_choice = random.randint(0,2)

if player_choice == 0 or computer_choice == 2:
    print ("You Chose "+ "\n" + rock)
    print ("Computer Chose "+ "\n" + scissors)
    print("You Win!")
elif player_choice == 2 or computer_choice == 0:
    print ("You Chose "+ "\n" +scissors)
    print ("Computer Chose "+ "\n" + rock)
    print("You Lose!")
elif player_choice == 2 or computer_choice == 1:
    print ("You Chose "+ "\n" +scissors)
    print ("Computer Chose "+ "\n" + paper)
    print("You Win!")
elif player_choice == 1 or computer_choice == 2:
    print ("You Choose "+ "\n" +paper)
    print ("Computer Chose "+ "\n" + scissors)
    print("You Lose!")
elif player_choice == 1 or computer_choice == 0:
    print ("You Chose "+ "\n" +paper)
    print ("Computer Chose "+ "\n" + rock)
    print("You Win!")
elif player_choice == 0 or computer_choice == 1:
    print ("You Chose "+ "\n" +rock)
    print ("Computer Chose "+ "\n" + paper)
    print("You Lose!")
elif player_choice == 0 or computer_choice == 0:
    print ("You Chose "+ "\n" +rock)
    print ("Computer Chose "+ "\n" + rock)
    print("Draw!")
elif player_choice == 1 or computer_choice == 1:
    print ("You Chose "+ "\n" +paper)
    print ("Computer Chose "+ "\n" + paper)
    print("Draw!")
elif player_choice == 2 or computer_choice == 2:
    print ("You Chose "+ "\n" +scissors)
    print ("Computer Chose "+ "\n" + scissors)
    print("Draw!")



# if computer_choice == 0:
#     print ("Computer Choose "+ "\n" + rock)
# elif computer_choice == 1:
#     print ("Computer Choose "+ "\n" +paper)
# elif computer_choice == 2:
#     print ("Computer Choose "+ "\n" +scissors)


