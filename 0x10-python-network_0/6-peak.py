#!/usr/bin/python3
""" Finds the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find highest value in list of unsorted integers"""

    my_list = list_of_integers

    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
