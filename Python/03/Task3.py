# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.


def sum_of_max_two(a, b, c):
    """
    >>> sum_of_max_two(5, 2, 1)
    7
    >>> sum_of_max_two(1, 4, 8)
    12
    >>> sum_of_max_two(0, 11, 3)
    14
    >>> sum_of_max_two(6, 1, 3)
    9
    >>> sum_of_max_two(5, 5, 3)
    10
    >>> sum_of_max_two(3, 3, 3)
    6
    >>> sum_of_max_two(5, 3, 5)
    10
    >>> sum_of_max_two(2, 5, 5)
    10
    """
    if a >= b:
        if c >= b:
            return a + c
        else:
            return a + b
    else:
        if a >= c:
            return a + b
        else:
            return c + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
