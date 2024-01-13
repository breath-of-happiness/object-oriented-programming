import doctest

# 1 пример класса
class Car:
    def __init__(self, car_color: str, car_speed: float, car_mileage: float):
        """
        Создание и подготовка к работе объекта "Машина"

        :param car_color: Цвет машины
        :param car_speed: Скорость автомобиля в км/ч
        :param car_mileage: Пробег автомобиля в км

        Примеры:
        >>> car = Car("Желтый", 84.2, 55500)  # инициализация экземпляра класса
        """
        if not isinstance(car_color, str):
            raise TypeError("Цвет автомобиля должен быть типа str")

        if not isinstance(car_speed, (int, float)):
            raise TypeError("Скорость автомобиля должна быть типа int или float")
        if car_speed < 0:
            raise ValueError("Скорость должна быть неотриательным числом")
        self.car_speed = car_speed

        if not isinstance(car_mileage, (int, float)):
            raise TypeError("Пробег автомобиля должен быть int или float")
        if car_mileage < 0:
            raise ValueError("Пробег не может быть отрицательным числом")
        self.car_mileage = car_mileage

    def is_moves(self) -> bool:
        """
        Функция, которая проверяет движется ли автомобиль в данный момент

        :return: Движется ли автомобиль

        Примеры:
        >>> car = Car("Желтый", 84.2, 55500)
        >>> car.is_moves()
        """
        ...

    def mileage_determination(self, distance: float) -> None:
        """
        Функция для определения пробега автомобиля

        :param distance: Объем добавляемой жидкости
        :raise ValueError: Если значение прибавляемого пробега отрицательное, то возвращается ошибка
        :return: Обновленное значение пробега

        Примеры:
        >>> car = Car("Желтый", 84.2, 55500)
        >>> car.mileage_determination(200)
        """
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

# 2 пример класса
class Ski:
    def __init__(self, ski_company: str, temperature_regime: str, ski_size: float):
        """
        Создание и подготовка к работе объекта "Беговые лыжи"

        :param ski_company: Производитель лыж
        :param temperature_regime: Подходящий температурный режим
        :param ski_size: Ростовка лыж


        Примеры:
        >>> ski = Ski("Fisher","-5", 194.5)  # инициализация экземпляра класса
        """
        if not isinstance(ski_company, str):
            raise TypeError("Компания-производитель лыж должен быть типа str")

        if not isinstance(temperature_regime, str):
            raise TypeError("Подходящий температурный режим лыж должен быть типа str")

        if not isinstance(ski_size, (int, float)):
            raise TypeError("Ростовка лыж должна быть типа int или float")
        if ski_size < 0:
            raise ValueError("Ростовка должна быть неотриательным числом")
        self.ski_size = ski_size


    def suitable_for_temperature(self, temperature: str) -> None:
        """
        Функция, которая проверяет удовлетворяют ли лыжи погодным условиям

        :param temperature: Погодные условия
        :return: Подходят лыжи или нет

        Примеры:
        >>> ski = Ski("Fisher","-5", 194.5)
        >>> ski.suitable_for_temperature("-1")

        """
        ...

    def choice_of_skis(self, man_height: float) -> None:
        """
        Функция, которая определяет подходят ли лыжи для человека данного роста

        :param man_height: Рост человека
        :raise ValueError: Если значение прибавляемого роста человека отрицательное, то возвращается ошибка
        :return: True or False

        Примеры:
        >>> ski = Ski("Fisher","-5", 194.5)
        >>> ski.choice_of_skis(180)
        """
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

# 3 пример класса
class Closet:
    def __init__(self, material: str, capacity: float, size: str):
        """
        Создание и подготовка к работе объекта "Беговые лыжи"

        :param material: Материал, из которого сделан шкаф
        :param capacity: Вместимость шкафа в литрах
        :param size: Габариты шкафа: МхМхМ


        Примеры:
        >>> closet= Closet("дуб", 100, "3х2,4х0,9")  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал шкафа должен быть типа str")

        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость шкафа должна быть типа int или float")
        if capacity < 0:
            raise ValueError("Вместимость шкафа должна быть неотриательным числом")
        self.capacity = capacity

        if not isinstance(size, str):
            raise TypeError("Габариты шкафа должны быть типа str")




    def closet_volume(self, volume: int) -> None:
        """
        Функция, которая проверяет сможет ли поместится объект, определенного объема в шкаф

        :param volume: Объем объекта
         :raise ValueError: Если значение объема объекта отрицательное, то возвращается ошибка
        :return: Вместится или нет

        Примеры:
        >>> closet= Closet("дуб", 100, "3х2,4х0,9")
        >>> closet.closet_volume(10)

        """
        ...

    def choice_of_skis(self, furniture_surrounding_material: "str") -> None:
        """
        Функция, которая будет сравнивать материал окружающей мебели и шкафа

        :param furniture_surrounding_material: Рост человека
        :raise ValueError: Если значение материала другого типа данных, то выводит ошибку
        :return: Совпадает или отличается материал

        Примеры:
        >>> closet= Closet("дуб", 100, "3х2,4х0,9")
        >>> closet.choice_of_skis("сосна")
        """
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
