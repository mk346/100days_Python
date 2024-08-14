print("Welcome to Treasure Island. \n Your mission is to find the treasure")
choice_1 = input("You're are at a cross road.Where do you want to go? Type \"left\" or \"right\": ")
if choice_1 == "left":
    choice_2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across: ")
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island  unharmed. There is a house with 3 doors. One red, one yellow, and one blue.  Which color do you choose?: ")
        if choice_3 == "red":
            print("Burned by fire. Game Over")
        elif choice_3 == "blue":
            print("Eaten by beasts. Game Over")
        elif choice_3 == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. Game Over")
