#!/usr/bin/python3
"""
This Function Appends a String
"""


def append_write(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
