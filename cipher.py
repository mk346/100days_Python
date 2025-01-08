# caesar cipher encryption
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#PRO VERSION
# Encryption and Decryption Function
def cipher(start_text,cipher_direction,shift_number):
    start_text = list(start_text)
    end_text = ""
    if cipher_direction == 'decode':
            shift_number *= -1 % 26
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_number
            if new_position > 26:
                new_position = new_position % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt the message, or 'decode' to decrypt the message: \n")
    if direction != 'encode' and direction != 'decode':
        print("Invalid Selection, Try Again!")
        continue
    
    text = input("Type your message: \n").lower()

    shift = int(input("Type the shift number:\n"))


    cipher(cipher_direction=direction, start_text=text, shift_number=shift)
    
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if choice == 'no':
        should_continue = False
        print("GoodBye!")

     
#STARTER VERSION
    # if choice == 1:
    #     for letter in message:
    #         if letter in alphabet:
    #             position = alphabet.index(letter) 
    #             # print(position)
    #             new_position = (position + shift_number) % 26
    #             new_letter = alphabet[new_position]
    #             # print(new_letter)
    #             cipher_text  += new_letter
    #         else:
    #             cipher_text += letter
    #     print(f"Here's the encoded result: {cipher_text}")
    #decrypting the message
    # elif choice == 2:
    #     for letter in message:
    #         if letter in alphabet:
    #             position = alphabet.index(letter)
    #             new_position = (position - shift_number)
    #             new_letter = alphabet[new_position]
    #             plain_text += new_letter
    #         else:
    #             plain_text += letter
    #     print(f"Here is the decoded result: {plain_text}")


        
        
    
    


# def encrypt(message, shift_number):
#     message = list(text)
#     shift_number = shift
#     # print(message)
#     encrypted_message = ""
#     for letter in message:
#         if letter in alphabet:
#             position = alphabet.index(letter) 
#             # print(position)
#             new_position = (position + shift_number) % 26
#             new_letter = alphabet[new_position]
#             # print(new_letter)
#             encrypted_message += new_letter
#         else:
#             encrypted_message += letter
#     print(f"Here's the encoded result: {encrypted_message}")

# def decrypt(message, shift_number):
#     message = list(text)
#     shift_number = shift
#     decrypted_message = ""
#     for letter in message:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position - shift_number)
#             new_letter = alphabet[new_position]
#             decrypted_message += new_letter
#         else:
#             decrypted_message += letter
#     print(f"Here is the decoded result: {decrypted_message}")
     
# if direction == 1:
#     encrypt(text,shift)
#     # reply = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
#     # if reply == "yes":
#     #     direction = int(input("Type 1 to encrypt the message, or 2 to decrypt the message: \n"))
#     #     text = input("Type your message: \n").lower()
#     #     shift = int(input("Type the shift number:\n"))
#     # elif reply == "no":
#     #     direction = int(input("Type 1 to encrypt the message, or 2 to decrypt the message: \n"))
#     #     text = input("Type your message: \n").lower()
#     #     shift = int(input("Type the shift number:\n"))
#     # else:
#     #     print("Invalid Selection!")
# elif direction == 2:
#     decrypt(text,shift)

# else:
#     print("Invalid Selection, Try Again!") 
