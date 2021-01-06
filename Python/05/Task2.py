"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


def lines_word_count(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        result_dict = {}
        line_counter = 0
        for i in f:
            line_counter += 1
            word_counter = len(i.split())
            result_dict[line_counter] = word_counter

    result = ''
    for key, value in result_dict.items():
        if key == 2:
            result += f'Во {key} строке {value} слов(а)\n'
        else:
            result += f'В {key} строке {value} слов(а)\n'

    return result


print(lines_word_count('t2'))
