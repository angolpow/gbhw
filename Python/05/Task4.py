"""
4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


def translate_nums(filename):
    ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open(filename, 'r', encoding='utf-8') as r:
        with open(filename+'_russian', 'w', encoding='utf-8') as w:
            for line in r:
                key, _, value = line.split()
                w.write(ru_dict[key] + ' — ' + value + '\n')


translate_nums('t4-1')
