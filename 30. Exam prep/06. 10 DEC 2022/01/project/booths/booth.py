from abc import ABC, abstractmethod

from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number: int = booth_number
        self.capacity: int = capacity
        self.delicacy_orders: list[Delicacy] = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass
