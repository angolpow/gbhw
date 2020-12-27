# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def str_to_sum():
    result = 0
    while True:
        list_of_nums = input("Введите строку чисел для суммирования, символ окончания @: ").split()
        summ = 0
        try:
            for i in list_of_nums:
                summ += float(i)
            result += summ
        except ValueError:
            result += summ
            break
    return result


print(str_to_sum())


