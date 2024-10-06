#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats cast to integers.

    Args:
        a (int or float): The first number to be added. Must be an integer or float.
        b (int or float, optional): The second number to be added. Defaults to 98. Must be an integer or float.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or float.

    Returns:
        int: The sum of 'a' and 'b', after both have been cast to integers (if necessary).

    Example:
        >>> add_integer(3, 5)
        8

        >>> add_integer(3.5, 2)
        5

        >>> add_integer(100)
        198
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return a + b

