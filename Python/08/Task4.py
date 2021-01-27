"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class OfficeEquipment:
    def __init__(self, model, price, demy, page_in_min):
        self.model = model
        self.page_in_min = page_in_min
        self.price = price
        self.demy = demy

    def show_info(self):
        return f'Модель:     {self.model}\n' \
               f'Цена:       {self.price}\n' \
               f'Формат:     {self.demy}\n' \
               f'Стр. в мин: {self.page_in_min}\n'


class Printer(OfficeEquipment):
    def __init__(self, model, price, demy, page_in_min, is_color: bool, is_double_sided: bool):
        self.is_color = is_color
        self.is_double_sided = is_double_sided
        super().__init__(model, price, demy, page_in_min)


class Scanner(OfficeEquipment):
    def __init__(self, model, price, demy, page_in_min, dpi):
        self.dpi = dpi
        super().__init__(model, price, demy, page_in_min)


class Xerox(OfficeEquipment):
    def __init__(self, model, price, demy, page_in_min, is_double_sided: bool):
        self.is_double_sided = is_double_sided
        super().__init__(model, price, demy, page_in_min)


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.__storage = {}

    def add_item(self, item: OfficeEquipment, quantity):
        if Warehouse.check_quantity(quantity):
            self.__storage[item] = quantity
        else:
            print('Количество должно быть числом')

    def pass_item_to_dep(self, item, dep):
        if self.__storage[item] > 1:
            self.__storage[item] -= 1
        else:
            self.__storage.pop(item)
        dep.add_item(item, 1)

    @staticmethod
    def check_quantity(quantity):
        if isinstance(quantity, int):
            return True
        return False

    @property
    def show_stored(self):
        result = f'На складе {self.name} следующие позиции:\n'
        for i in self.__storage:
            result += f"{i.show_info()}Кол-во:     {self.__storage[i]}\n----------------------\n"

        return result


store = Warehouse('Склад')
department = Warehouse('Отдел IT')
printer = Printer('HP1001', 1000, 'A4', 30, False, False)
scanner = Scanner('Scanjet 5590', 900, 'A4', 10, 2000)
store.add_item(printer, 2)
store.add_item(scanner, 1)
print(store.show_stored)
print('=========================')
store.pass_item_to_dep(printer, department)
print(store.show_stored)
print(department.show_stored)
