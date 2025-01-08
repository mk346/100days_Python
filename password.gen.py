import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

symbols = ["!", "\"", "#", "$", "%", "&","(", ")", "*", "+","-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_","{", "|", "}"]

numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

for x in range(0, len(letters)):
    random_letters = random.sample(letters, nr_letters)
# print(random_letters)
for x in range(0, len(symbols)):
    random_symbols = random.sample(symbols, nr_symbols)

for x in range(0, len(numbers)):
    random_numbers = random.sample(numbers, nr_numbers)

gen_password = ''.join(random_letters + random_symbols + random_numbers)
combined_list = list(gen_password)
# print(combined_list)
random.shuffle(combined_list)
new_password = ''.join(combined_list)

print("Here is your password: "+ str(new_password))



