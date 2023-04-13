#!/usr/bin/python3
"""
This Module Contains the 'inherits_from' function
"""


def inherits_from(obj, a_class):
    """Rreturns True if obj is a subclass of a_class, otherwise False"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
