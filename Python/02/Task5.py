# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.


rates = [9, 6, 5, 5, 2, 1]

while True:
    new_rate = int(input("Введите новый результат, -1 для выхода: "))
    if new_rate == -1:
        break
    else:
        rates.append(new_rate)
        rates.sort(reverse=True)
        print(f"Текущие рейтинги: {', '.join(map(str, rates))}")
