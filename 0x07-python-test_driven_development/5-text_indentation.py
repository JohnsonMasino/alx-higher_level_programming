#!/usr/bin/python3

#This function prints a text with 2 new lines after each of these characters: '.' ',' '?' and ':'

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    variable = 0
    for letter in text:
        if variable == 0:
            if text == " ":
                continue
            else:
                variable = 1
        if variable == 1:
            if letter == "?" or letter == "." or letter == ":":
                print(letter)
                print()
                variable = 0
            else:
                print(letter, end="")
print("\nCode developed by Masino")                
