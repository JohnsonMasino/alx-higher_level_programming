#!/usr/bin/python3

#This function adds two integers.

def add_integer(a, b = 98):
    #This prototype will return (a + b)
    #a and b must be typecasted into int before addition
    #if a or b or both is not int, raise a typeError
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
print("\nCode developed by Masino")
