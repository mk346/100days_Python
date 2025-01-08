# hangman game loop
import random
hangman_logo = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

print(hangman_logo)
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra' ,'cougar','coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat','goose', 'hawk', 'lion', 'lizard', 'llama' 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt ','otter', 'owl', 'panda', 'parrot', 'pigeon','python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake','spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey','turtle', 'weasel','whale', 'wolf', 'zebra']

# print(random.choice(word_list))
#choose a random word from the list
random_word = random.choice(word_list)

# print(random_word)
word_letters = list(random_word) #split the guessed word into letters
# print(word_letters)
blanks = []
x = 0
while x < len(word_letters):
    blanks += "-"
    x += 1
# print(blanks)
stage = len(stages) # to help loop over stages
#intialize a set to keep track of guessed letters
guessed_letters = set()
while "-" in blanks and stage > 0:
    # take guess letter from the user
    guess_letter = input("Guess a Letter: ").lower()
    
    # check if the letter has been guessed before
    if guess_letter in guessed_letters:
        print("You have already guessed that letter, Try again!")
        continue
    else:
        guessed_letters.add(guess_letter)
    
    # check if the guessed letter is in the word
    if guess_letter in random_word:
        index = 0
        #replace dashes with the correct letter
        for letter in random_word:
            if letter == guess_letter:
                blanks[index] = guess_letter
            index += 1
        print(blanks)
    else:
        print("You guessed " + guess_letter + " thats not in the word. You lose a life")
        #generate hangman ascii if the letter guessed is wrong
        stage -= 1
        print(stages[stage])
        if stage == 0:
            print("You Lose!")
            break
        
if "-" not in blanks:
    print("You Win!")

