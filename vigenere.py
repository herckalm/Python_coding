# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 07:36:05 2019

@author: Iraklis Kalamas
"""

def main():

    # Getting user input and testing for validity
    plain_text = input("Encryption text: ")
    while True:
        if plain_text == "" or plain_text.isdigit():
            print("Not a valid input")
            plain_text = input("Encryption text: ")
        else:
            break
    
    cipher= input("Cipher word: ")
    while True:
        if not cipher.isalpha():
            print("Not a valid input")
            cipher = input("Cipher word: ")
        else:
            break
    
    #Mapping letters to numbers (26 elements)
    letters = {"A":0, "a":0, "B":1, "b":1, "C":2, "c":2, "D":3, "d":3, "E":4, "e":4,
               "F":5, "f":5, "G":6, "g":6, "H":7, "h":7, "I":8, "i":8, "J":9, "j":9,
               "K":10, "k":10, "L":11, "l":11, "M":12, "m":12, "N":13, "n":13, "O":14,
               "o":14, "P":15, "p":15, "Q":16, "q":16, "R":17, "r":17, "S":18, "s":18,
               "T":19, "t":19, "U":20, "u":20, "V":21, "v":21, "W":22, "w":22, "X":23,
               "x":23, "Y":24, "y":24, "Z":25, "z":25
                }
                
    #setting needed variables
    temp_cipher = cipher
    plain_char_len = 0
    cipher_len = len(cipher)
    n = 0
    c_text = ""
    
    #finding how many letters is in the input text
    for char in plain_text:
        if char.isalpha():
            plain_char_len += 1
    
    #checking if the cipher word is smaller than plain text and 
    #creating a temp cipher long as number of letters in plain text
    if plain_char_len > cipher_len:
        dif = plain_char_len - cipher_len
        for i in range(dif):
            temp_cipher += temp_cipher[i]
    
    #Main loop for the encryption of plain text
    for c in plain_text:
        if c.isalpha():
            if c.islower():
                c = (ord(c) - 97 + letters[temp_cipher[n]]) % 26 + 97
                c_text += chr(c)
                n += 1
            elif c.isupper():
                c = (ord(c) - 65 + letters[temp_cipher[n]]) % 26 + 65
                c_text += chr(c)
                n += 1
        else:
            c_text += c
      
    print(c_text)

if __name__ == "__main__":
    main()
