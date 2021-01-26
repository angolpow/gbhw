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


class Warehouse:
    def __init__(self):
        self.__storage = {}

    # TODO: сделать геттеры/сеттеры
    def add_item(self, item):
        pass

    def pass_item_to_dep(self, item):
        pass


class OfficeEquipment:
    def __init__(self, model, price, demy, page_in_min):
        self.model = model
        self.page_in_min = page_in_min
        self.price = price
        self.demy = demy


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


