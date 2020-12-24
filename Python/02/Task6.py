# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


import pprint as p


params = ["название", "цена", "количество", "eд"]
store = []
proceed = True
statistics = {}

while proceed:
    store.append((len(store) + 1, {}))
    for i in params:
        value = input(f"Введите параметр '{i}': ")
        value = int(value) if value.isdigit() else value
        store[len(store) - 1][1][i] = value

    proceed = input("Введите любой символ для продолжения заполнения, Enter для завершения. ")

p.pprint(store)
print()

for i in params:
    statistics[i] = []
    for j in store:
        if not (i == 'eд' and j[1][i] in statistics[i]):  # проверка уникальности ед измерения
            statistics[i].append(j[1][i])

p.pprint(statistics)
