# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(text: str):
    """
    >>> int_func('test')
    'Test'
    >>> int_func('another test of this func')
    'Another Test Of This Func'
    """
    result = ""
    for i in text.split():
        result += i.capitalize() + ' '

    return result.rstrip()


print(int_func('string'))
print(int_func('another string'))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
