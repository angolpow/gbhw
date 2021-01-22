"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, mtrx: list):
        self.mtrx = mtrx

    def __len__(self):
        return len(self.mtrx)

    def __getitem__(self, key):
        return self.mtrx[key]

    def __str__(self):
        result = ''
        for i in self.mtrx:
            for j in i:
                result += f'{j: 4}'
            result += '\n'
        return result

    def __add__(self, other):
        new_mtrx = []
        height = max(len(other), len(self.mtrx))
        width = max(len(other[0]), len(self.mtrx[0]))
        for j in range(height):
            line = []
            for i in range(width):
                try:
                    line.append(self.mtrx[j][i] + other[j][i])
                except IndexError:
                    try:
                        line.append(self.mtrx[j][i])
                    except IndexError:
                        line.append(other[j][i])
            new_mtrx.append(line)
        return Matrix(new_mtrx)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix1)
matrix2 = Matrix([[4, 6, 2, 3], [1, 8, 4, 2], [3, 11, 2, 4], [4, 9, 0, 1]])
print(matrix2)
print(matrix1 + matrix2)
print(matrix2 + matrix1)
print(matrix1 + matrix1)
