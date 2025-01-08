import random
names = input("Enter friends name separated by commas: ")

names_list = names.split(",")
# print(names_list)
# print(len(names_list))

#random_name = random.choice(names_list)
num_items = len(names_list)


random_choice = random.randint(0, num_items - 1)
print(random_choice)
#random_name = names[random_choice]

#print(random_name)