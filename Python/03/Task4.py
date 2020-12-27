# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def pow2(x, y):
    """
    >>> pow2(3, -3)
    0.037
    >>> pow2(2, -2)
    0.25
    >>> pow2(4, -4)
    0.0039
    """
    x_pow = x
    for i in range(-y - 1):
        x_pow *= x

    return round(1/x_pow, 4)


def pow3(x, y):
    """
    >>> pow3(3, -3)
    0.037
    >>> pow3(2, -2)
    0.25
    >>> pow3(4, -4)
    0.0039
    """

    return round(x**y, 4)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

