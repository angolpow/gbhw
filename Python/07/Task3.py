"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и целочисленное (с округлением до целого) деление клеток, соответственно.
"""


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            print('Нельзя вычесть из меньшей большую клетку')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_in_row):
        result = ''
        for i in range(self.cells // cells_in_row):
            result += '*' * cells_in_row + '\n'
        add = self.cells % cells_in_row
        if add:
            result += '*' * add
        return result.rstrip()


print('Клетка с 14-ю ячейками в ряд по 7')
test = Cell(14)
print(test.make_order(7))
print()
print('Клетка с 16-ю ячейками в ряд по 7')
test = Cell(16)
print(test.make_order(7))
print()
print('Сумма клеток с 16-ю и 7-ю ячейками в ряд по 7')
test = Cell(16) + Cell(7)
print(test.make_order(7))
print()
print('Деление клеток с 16-ю ячейками на клетку с 3-мя ячейками в ряд по 5')
test = Cell(16) / Cell(3)
print(test.make_order(5))
print()
print('Перемножение клеток с 2-мя и 4-мя ячейками в ряд по 5')
test = Cell(2) * Cell(4)
print(test.make_order(5))
print()
print('Разность клеток с 16-ю и 7-ю ячейками в ряд по 7')
test = Cell(16) - Cell(7)
print(test.make_order(7))
print()
print('Разность клеток с 1-й и 7-ю ячейками')
test = Cell(1) - Cell(7)
