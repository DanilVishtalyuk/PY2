class Computer:
    def __init__(self, brand: str, price: (float, int)):
        """
        Создание и подготовка к работе объекта компьютер
        :param brand: марка компьютера
        :param price: цена компьютера
        """
        if not isinstance(brand, str):
            raise TypeError("Марка комьютера должна быть типа str")
        self.brand = brand

        if not isinstance(price, (float, int)):
            raise TypeError("Цена компьютера должна быть типа float или int")
        if price <= 0:
            raise ValueError("Цена не может быть равно нулю или быть отрицательной")
        self.price = price

    def comp_start(self) -> None:
        """ запуск комьютера """
        ...

    def comp_stop(self) ->None:
        """
        выключение компьютера
        Примеры:
        >>> comp1 = Computer("Lenovo", 50000)
        >>> comp1.comp_start()
        """
        ...

    def __str__(self):
        return f"Компьютер. Марка {self.brand}. Цена {self.price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, price={self.price!r})"


class Laptop(Computer):
    def __init__(self, brand: str, price: (float, int), battery_power: (float, int)):
        super().__init__(brand, price)
        self.battery_power = battery_power

        """
            Создание и подготовка к работе объекта ноутбук
            :param brand: марка ноутбука
            :param price: цена ноутбука
            :param battery_power: емкость батареи ноутбука
        """

        if not isinstance(battery_power, (float, int)):
            raise TypeError("Мощность баттареи ноутбука должна быть типа float или int")
        if battery_power < 0:
            raise ValueError("Мощность баттареи ноутбука не можеn быть отрицательной")

    def comp_start(self, battery_power) -> None:
        """ запуск ноутбука. если батарея разряжена, ноутбук не включится """
        if battery_power == 0:
            print("Батарея разряжена(")

    def comp_stop(self) -> None:

        super().comp_stop()
        """
               выключение ноутбука
        """

    def __str__(self):
        return f"Ноутбук. Марка {self.brand}. Цена {self.price}. Емкость батареи {self.battery_power}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, price={self.price!r}, battery power = {self.battery_power})"


