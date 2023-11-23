from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED = None
    STRING_HORSE_TYPE = None

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            return ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.MAX_SPEED:
            return ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        pass
