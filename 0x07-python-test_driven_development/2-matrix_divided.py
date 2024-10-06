#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    
    Args:
        matrix (list of lists of int/float): The matrix to be divided. Each row must be of the same size.
        div (int/float): The number to divide each matrix element by.
        
    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats, or if each row is not the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    
    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimal places.
    
    Example:
        >>> matrix_divided([[4, 6], [8, 10]], 2)
        [[2.0, 3.0], [4.0, 5.0]]
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix)
        or not all(isinstance(el, (int, float)) for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(el / div, 2) for el in row] for row in matrix]
