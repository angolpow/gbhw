"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary == 0:
            return str(self.real)
        sign = "-" if self.imaginary < 0 else "+"
        imaginary = "" if abs(self.imaginary) == 1 else abs(self.imaginary)
        return f'{self.real}{sign}{imaginary}i'

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNum(real, imaginary)


first = ComplexNum(1, -4)
second = ComplexNum(4, 4)
print(first + second)
print(first * second)
first = ComplexNum(1, -1)
second = ComplexNum(3, 6)
print(first + second)
print(first * second)