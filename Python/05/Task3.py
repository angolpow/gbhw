"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def analyze_pay(filename):
    result = 'Сотрудники с окладом ниже 20000:'  # длина строки 32, ниже это используется
    result_dict = {}
    average = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            key, value = line.split()
            result_dict[key] = float(value)

    for key, value in result_dict.items():
        if value < 20000:
            result += ' ' + key + ','
        average += value

    average = f'\nСредний доход сотрудников: {round(average / len(result_dict), 2)}'
    result = result[:-1] + average if len(result) > 32 \
        else 'Сотрудников с окладом меньше 20к нет' + average
    return result


print(analyze_pay('t3-1'))
print(analyze_pay('t3-2'))
