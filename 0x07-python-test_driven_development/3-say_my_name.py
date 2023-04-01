#!/usr/bin/python3

#This code defines a funtion that prints: My name is <first name> <last name>

def say_my_name(first_name, last_name=""):
    #This prints a first name and a subsequent last name.
    # All arguments must be strings.
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
print('\nCode developed by Masino')    
