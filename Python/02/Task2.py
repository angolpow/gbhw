# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


elements = [x for x in input("Введите список элементов через запятую: ").split(",")]
new_elements = []
elements_length = len(elements) if len(elements) % 2 == 0 else len(elements) - 1

for i in range(0, elements_length, 2):
    new_elements.append(elements[i + 1])
    new_elements.append(elements[i])

if elements_length < len(elements):
    new_elements.append(elements[-1])

print(new_elements)

# Можно не использовать новый список, а менять сразу текущий, но это плохая практика, хоть код и будет короче.

# for i in range(0, elements_length, 2):
#     elements[i], elements[i + 1] = elements[i + 1], elements[i]
#
# print(elements)
