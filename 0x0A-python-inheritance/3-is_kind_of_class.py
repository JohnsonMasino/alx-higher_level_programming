#!/usr/bin/python3
"""
This Module Contains the 'is_kind_of_class' function
"""


def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance or inherited from a_class, else return False"""
    return (isinstance(obj, a_class))
