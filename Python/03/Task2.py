# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def get_info(name, surname, year, city, email, phone):
    """
    >>> get_info(name='Вася', surname="Иванов", year="1960", city="Москва", email="vi@mail.ru", phone="+79991234567")
    'Вася Иванов 1960 года рождения из города Москва. Контактные данныe: vi@mail.ru, +79991234567.'
    >>> get_info(name='Петя', surname="Смирнов", year="1971", city="Архангельск", email="ps@mail.ru", phone="+79991234567")
    'Петя Смирнов 1971 года рождения из города Архангельск. Контактные данныe: ps@mail.ru, +79991234567.'
    """

    return f"{name} {surname} {year} года рождения из города {city}. Контактные данныe: {email}, {phone}."


print(get_info(name='Вася', surname="Иванов", year="1960", city="Москва", email="vi@mail.ru",
               phone="+79991234567"))
print(get_info(name='Петя', surname="Смирнов", year="1971", city="Архангельск", email="ps@mail.ru",
               phone="+79991234567"))

if __name__ == "__main__":
    import doctest
    doctest.testmod()