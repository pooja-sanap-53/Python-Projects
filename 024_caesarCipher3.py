# Caesar Cipher
# Reorganizing code
'''
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

'''


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_number, cipher_direction):
    end_text =""
    for char in start_text:
        position = alphabet.index(char)
        if cipher_direction == "decode":
            new_positon = position -shift_number
        elif cipher_direction == "encode":
            new_positon = position + shift_number
        end_text += alphabet[new_positon]
    print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text = text, shift_number = shift, cipher_direction = direction)
