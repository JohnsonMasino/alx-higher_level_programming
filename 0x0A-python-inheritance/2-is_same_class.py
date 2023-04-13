#!/usr/bin/python3
"""
Contains The Function "is_same_class"
"""


def is_same_class(obj, a_class):
    """returns true if obj is the exact class of a_class, or else, returns false"""
    if type(obj) == a_class:
        return True
    else:
        return False
