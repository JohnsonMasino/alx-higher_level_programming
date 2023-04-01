#!/usr/bin/python3

#This code defines a function[matrix_divided(matrix, div)] to divide a matrix.

def matrix_divided(matrix, div):
    #This will divide a matrix by scaler integer.
    import decimal

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        length_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_count += 1
    if len(set(length_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    generate_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return generate_matrix
print("\nCode developed by Masino")
