#!/usr/bin/python3
#This code multiplies two matrices

def matrix_mul(m_a, m_b):
    # m_a == first matrix and a list of lists
    # m_b == second matrix and a list of lists

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # To check that both m_a and m_b can be multiplied
    num_colum1 = 0
    num_row2 = 0

    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row1 in m_a:
        if type(row1) is not list:
            raise TypeError("m_a must be a list of lists")
        len1 = len(m_a[0])
        if row1 == []:
            raise ValueError("m_a can't be empty")
        if len1 != len(row1):
            raise TypeError("each row of m_a must be of the same size")
        num_colum1 = len(row1)
        for column1 in row1:
            if type(column1) is not int and type(column1) is not float:
                raise TypeError("m_a should contain only integers or floats")

    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row2 in m_b:
        if type(row2) != list:
            raise TypeError("m_b must be a list of lists")
        len2 = len(m_b[0])
        if row2 == []:
            raise ValueError("m_b can't be empty")
        if len2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")
        num_row2 += 1
        for column2 in row2:
            if type(column2) != int and type(column2) != float:
                raise TypeError("m_b should contain only integers or floats")

    if num_colum1 != num_row2:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row_1 in m_a:
        l = 0
        l_row = []
        while l < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in row_1:
                result += column_1 * m_b[k][l]
                k += 1
            l_row.append(result)
            l += 1
        mul_matrix.append(l_row)

    return mul_matrix
#print("\nCode by Masino")
