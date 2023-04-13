#!/usr/bin/python3
"""
This Module contains the Class 'BaseGeometry'
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
