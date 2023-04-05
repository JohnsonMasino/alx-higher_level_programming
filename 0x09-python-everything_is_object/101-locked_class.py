#!/usr/bin/python3
# Locked_class

"""Defines a class that is locked"""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes called "first_name"
    """

    __slots__ = ["first_name"]
