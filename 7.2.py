# Store the word
word = "calf"
# Generate a list of dashes
hidden_word = ["-"] * len(word)
# Initialize the counter
index = 0

while "-" in hidden_word:
    # Take user input
    guess = input("Guess a letter: ").lower()
    # Check if the input is in the word
    if guess in word:
        # Replace dashes with the correct letter
        index = 0
        for letter in word:
            if letter == guess:
                hidden_word[index] = guess
            index += 1
        print("".join(hidden_word))
    else:
        print("Wrong letter.")
print("Congratulations! You've guessed the word:", word)
