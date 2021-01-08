"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""


import json


def read_data(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        average_profit = 0
        counter = 0
        profit_list = [{}, {}]
        for line in f:
            firm, _, receipts, costs = line.split()
            profit = float(receipts) - float(costs)
            if profit > 0:
                average_profit += profit
                counter += 1
            profit_list[0][firm] = profit
        try:
            profit_list[1]['average_profit'] = round(average_profit / counter, 2)
        except ZeroDivisionError:
            profit_list[1]['average_profit'] = 0
    return profit_list


def write_data_to_json(filename, jsonfile):
    with open(jsonfile, 'w', encoding="utf-8") as f:
        json.dump(read_data(filename), f)


write_data_to_json('t7', 't7.json')
