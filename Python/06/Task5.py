"""
5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from Task4 import *

cars = [PoliceCar(120, 'blue', 'Car1', True),
        WorkCar(50, 'yellow', 'Car2', False),
        SportCar(150, 'red', 'Car3', False),
        TownCar(80, 'grey', 'Car4', False),
        Car(60, 'white', 'Car5', False)]

for i in cars:
    i.go()
    if i.is_police:
        print('Это полицейская машина')
    print(f'Цвет машины {i.color}')
    i.show_speed()
    i.turn('направо')
    i.stop()
    print()
