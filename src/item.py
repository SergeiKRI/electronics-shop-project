import csv

from settings import NAME_DIR


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        print("Файл item.csv поврежден")


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Не является экземпляром Phone или Item классов')
        return self.quantity + other.quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            # print("Длина наименования товара превышает 10 символов")
            self.__name = name[:10]
        else:
            self.__name = name


        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, file=NAME_DIR):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/item.csv
        """
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not (row['name'] and row['price'] and row['quantity']) is '':
                        name = row['name']
                        price = row['price']
                        quantity = row["quantity"]
                        cls(name, price, quantity)
                    else:
                        raise InstantiateCSVError

            return cls

        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(x):
        """
        возвращающий число из числа-строки
        """
        return int(float(x))