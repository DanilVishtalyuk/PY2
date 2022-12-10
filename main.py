import doctest
# TODO Написать 3 класса с документацией и аннотацией типов


class Computer:
    def __init__(self, brand: str, price: (float, int)):
        """
        Создание и подготовка к работе объекта компютер
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


class Vase:
    def __init__(self, color: str, form: str, volume: (float, int)):
        """
               Создание и подготовка к работе объекта ваза
               :param color: цвет вазы
               :param form: форма вазы
               """
        if not isinstance(color, str):
            raise TypeError("Цвет вазы должен быть типа str")
        self.color = color

        if not isinstance(form, str):
            raise TypeError("Форма вазы должна быть типа str")
        self.form = form

        if not isinstance(volume, (float, int)):
            raise TypeError("Объем вазы должен быть типа float или int")
        if volume <= 0:
            raise ValueError("Объем вазы должен быть положительным")
        self.volume = volume

    def change_flower(self) -> None:
        """Смена цветов в вазе"""
        ...

    def add_water(self, water: float) -> None:
        """
        Добавляем воду в вазу
        :param water: объем воды добавляемой в вазу
        >>>vase = Vase("желтая", "круглая", 12)
        >>>vase.add_water(5)
        """
        if not isinstance(water, (float, int)):
            raise TypeError("Объем добавляемой воды должен быть типа float или int")
        if water < 0:
            raise ValueError("Объем добавляемой воды не должен быть отрицательным")
        ...


class StudyGroup:
    def __init__(self, name: str, number: int):
        """
         Создание и подготовка к работе объекта учебная группа, который создает список учебной группы
         :param name: Имя студента
         :param number: Номер студента в списке группы
         """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Номер студента в списке группы должно быть типа str ")
        if number < 0:
            raise ValueError("Номер не может быть отрицательным")
        self.number = number

    def add_student(self, name: str, number: int) -> None:
        """
        Добавление нового студента в список группы
        :param name: Имя нового студента
        :param number: Номер в списке нового студента
        >>> group1 = StudyGroup("Иван", 1)
        >>> group1.add_student("Игорь", 2)
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Номер студента в списке группы должно быть типа str ")
        if number < 0:
            raise ValueError("Номер не может быть отрицательным")
        self.number = number
        ...


    def delete_student(self, name: str, number: int) -> None:
        """
        удаление студента из списка группы
        :param name: Имя студента, которого нужно убрать из списка
        :param number: Номер студенда, которого нужно убрать из списка
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Номер студента в списке группы должно быть типа str ")
        if number < 0:
            raise ValueError("Номер не может быть отрицательным")
        self.number = number
        ...


if __name__ == "__main__":
     doctest.testmod()

    # TODO работоспособность экземпляров класса проверить с помощью doctest
