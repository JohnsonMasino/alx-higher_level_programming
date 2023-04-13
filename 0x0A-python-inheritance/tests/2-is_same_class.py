#!/usr/bin/python3
"""
Contains The Function "is_same_class"
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class of a_class, else, return false"""
    return (type(obj) == a_class)
