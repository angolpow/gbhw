"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, value):
        self.value = value

    @property
    @abstractmethod
    def calculate(self):
        pass

    def __add__(self, other):
        return self.calculate + other.calculate

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value <= 0:
            raise ValueError("Не может быть меньше или равно нулю")
        else:
            self.__value = value


class Suit(Clothing):
    @property
    def calculate(self):
        return self.value * 2 + 0.3


class Coat(Clothing):
    @property
    def calculate(self):
        return self.value / 6.5 + 0.5


cloth1 = Coat(13)
print(cloth1.calculate)
cloth2 = Suit(4)
print(cloth2.calculate)
print(cloth1 + cloth2)
