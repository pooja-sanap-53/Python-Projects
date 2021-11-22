# Caesar Cipher
# Decryption 
'''
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
'''


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_number):
    cipher_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_number
        new_char = alphabet[new_position]
        cipher_text += new_char
    print(f"The encoded test is {cipher_text}")

def decrypt(cipher_text, shift_number):
    plain_text = ""
    for char in cipher_text:
        position = alphabet.index(char)
        new_position = position - shift_number
        plain_text += alphabet[new_position]
        
    print(f"The decoded text is {plain_text}")



if direction == "encode":
    encrypt(plain_text=text, shift_number= shift)
elif direction =="decode":
    decrypt(cipher_text=text, shift_number = shift)

