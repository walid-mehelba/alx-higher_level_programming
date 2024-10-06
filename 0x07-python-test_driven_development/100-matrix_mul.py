#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists): The first matrix to multiply.
        m_b (list of lists): The second matrix to multiply.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, or contains non-numeric elements.
        ValueError: If m_a or m_b is empty, not a rectangle, or can't be multiplied.

    Returns:
        list of lists: The resulting matrix after multiplication.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
