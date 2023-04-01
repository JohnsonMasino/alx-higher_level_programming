#!/usr/bin/python3

#This code prints a square with "#"

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for number in range(size):
        print(("#" * size + "\n") * size, end="")
print("\nCode developed by Masino")        
