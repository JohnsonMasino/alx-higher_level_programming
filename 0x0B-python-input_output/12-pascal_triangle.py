#!/usr/bin/python3
"""
Defines A Pascal's Triangle Module
"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of Size n.
    Returns a List of Lists of Integers Representing the Triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
