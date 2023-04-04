#!/usr/bin/python3
#Defines
#a class
#rectangle

class Rectangle:
    #Represents a rectangle
    def __init__(self, width = 0, height = 0):
        #Initialising the rectangle
        self.height = height
        self.width = width

    @property
    def width(self):
        #gets the private instance attribute, width.
        return self.width

    @width.setter
    def width(self, value):
        #sets the private instance attribute, width.
        if type(value) is not int:
            raise TypeError("Width must be an Integer")
        if value < 0:
            raise ValueError("Width must be greater or equal to 0")
        self.width = value

    @property
    def height(self):
        #gets the private instatnce attribute, height
        return self.__height

    @height.setter
    def height(self, value):
        #Sets the private instance attribute, height
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater or equl to 0")
        self.__height = value
