#!/usr/bin/python3
"""
This Function Returns True if the Object is an instance of the class
"""
def is_same_class(obj, a_class):
    """defines this 'is_same_class' function"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
is_same_class()    
