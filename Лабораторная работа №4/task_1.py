class Car:
    """ Базовый класс автомобиль """
    def __init__(self, brand: str, speed: float, mileage: int):
        """
                Создание и подготовка к работе объекта "Автомобиль"

                :param brand: Марка автомобиля
                :param speed: Скорость автомобиля в км/ч
                :param mileage: Пробег автомобиля в км

                Примеры:
                >>> car = Car("BMW", 84.2, 5550)  # инициализация экземпляра класса
                """
        self._brand = brand
        self.speed = speed
        self.mileage = mileage
        """Проверка атбирутов"""
        if not isinstance(brand, str):
            raise TypeError("Марка автомобилей должна быть типа str")
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость автомобиля должна быть типа int или float")
        if speed < 0:
            raise ValueError("Скорость автомобиля должна быть неотриательным числом")
        if not isinstance(mileage, int):
            raise TypeError("Скорость автомобиля должна быть типа int")
        if mileage < 0:
            raise ValueError("Пробег автомобиля не может быть отрицательным числом")

    """Непубличность для атрибута brand"""
    @property
    def brand(self):
        return self._brand

    def is_moves(self) -> bool:
        """
            Функция, которая проверяет движется ли автомобиль в данный момент

            :return: Движется ли автомобиль

            Примеры:
            >>> car = Car("BMW", 84.2, 5550)
            >>> car.is_moves()
            """
        ...

    def travel_time(self) -> float:
        """
            Функция для определения времени экспуатации автомобиля в движении

            :return: Значение времени в пути

            Примеры:
            >>> car = Car("BMW", 84.2, 5550)
            >>> car.travel_time()
        """
        ...

    def __str__(self) -> str:
        """
                Магический метод для просмотра инициализации экземпляра класса

                :return: Строка, предназначенная для чтения людьми
        """
        return f"Автомобиль марки: {self.brand}. Средняя скорость: {self.speed}. Пробег: {self.mileage}"

    def __repr__(self) -> str:
        """
                Магический метод для просмотра инициализации экземпляра класса

                :return: Строка, показывающая, как может быть инициализирован экземпляр (валидный код)
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, speed={self.speed!r}, mileage={self.mileage})"


class PassengerCar(Car):
    """ Дочерний класс легковой автомобиль """
    def __init__(self, brand: str, speed: float, mileage: int, body_type: str, passengers: int):
        """
                Создание и подготовка к работе объекта "Легковой автомобиль"

                Наследуется от базового класса "Автомобиль":
                :param brand: Марка автомобиля
                :param speed: Скорость автомобиля в км/ч
                :param mileage: Пробег автомобиля в км

                :param body_type: Тип кузова
                :param passengers: Число пассажиров

                Примеры:
                >>> passenger_car = PassengerCar("BMW", 44.3, 1945, "hatchback", 3000)  # инициализация экземпляра класса
                """
        super().__init__(brand, speed, mileage)
        self.body_type = body_type
        self.passengers = passengers
        """Проверка атбирутов"""
        if not isinstance(body_type, str):
            raise TypeError("Тип кузова должен быть типа str")
        if not isinstance(passengers, int):
            raise TypeError("Число пассажиров должно быть типа int")
        if passengers < 0:
            raise ValueError("Число пассажиров не может быть отрицательным числом")

    def __str__(self) -> str:
        """
                Магический метод для просмотра инициализации экземпляра класса

                :return: Строка, предназначенная для чтения людьми
        """
        return f"Автомобиль марки: {self.brand}. Средняя скорость: {self.speed}. Пробег: {self.mileage}. Тип кузова: {self.body_type}. Число пассажиров: {self.passengers}"

    def __repr__(self) -> str:
        """
                Магический метод для просмотра инициализации экземпляра класса

                :return: Строка, показывающая, как может быть инициализирован экземпляр (валидный код)
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, speed={self.speed!r}, mileage={self.mileage}, body_type={self.body_type}, passengers={self.passengers})"


class Truck(Car):
    """ Дочерний класс грузовай автомобиль """
    def __init__(self, brand: str, speed: float, mileage: int, load_capacity: int, cargo_volume: int):
        """
                Создание и подготовка к работе объекта "Грузовой автомобиль"

                Наследуется от базового класса "Автомобиль":
                :param brand: Марка автомобиля
                :param speed: Скорость автомобиля в км/ч
                :param mileage: Пробег автомобиля в км

                :param load_capacity: Грузоподъемность автомобиля в т
                :param cargo_volume: Максимальный объем груза для транспортировки в м^3

                Примеры:
                >>> truck = Truck("BMW", 44.3, 1945, 18, 3000)  # инициализация экземпляра класса
                """
        super().__init__(brand, speed, mileage)
        self.load_capacity = load_capacity
        self.cargo_volume = cargo_volume
        """Проверка атбирутов"""
        if not isinstance(load_capacity, int):
            raise TypeError("Грузоподъемность автомобиля должна быть типа int")
        if load_capacity < 0:
            raise ValueError("Грузоподъемность автомобиля не может быть отрицательным числом")
        if not isinstance(cargo_volume, int):
            raise TypeError("Максимальный объем груза для транспортировки должен быть типа int")
        if cargo_volume < 0:
            raise ValueError("Максимальный объем груза для транспортировки не может быть отрицательным числом")

    def __str__(self) -> str:
        """
                Магический метод для просмотра инициализации экземпляра класса

                :return: Строка, предназначенная для чтения людьми
        """
        return f"Автомобиль марки: {self.brand}. Средняя скорость: {self.speed}. Пробег: {self.mileage}. Грузоподъемность: {self.load_capacity}. Максимальный объем груза: {self.cargo_volume}"

    def __repr__(self) -> str:
        """
                Магический метод для просмотра инициализации экземпляра класса

                :return: Строка, показывающая, как может быть инициализирован экземпляр (валидный код)
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, speed={self.speed!r}, mileage={self.mileage}, load_capacity={self.load_capacity}, cargo_volume={self.cargo_volume})"

    def cargo_dimensions(self, dimensions: int) -> bool:
        """
                Функция для проверки вместимости грузов в грузовой автомобиль для дальнейшей транспортировки

                :return: Значение времени в пути

                Примеры:
                >>> truck = Truck("BMW", 44.3, 1945, 18, 3000)
                >>> truck.cargo_dimensions(249)
                """
        ...
