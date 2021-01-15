"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
 который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name} {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} едет с превышением разрешенной ей скорости на {self.speed - 60} км/ч')
        else:
            print(f'Скорость машины {self.name} {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} едет с превышением разрешенной ей скорости на {self.speed - 40} км/ч')
        else:
            print(f'Скорость машины {self.name} {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, True)
