from abc import ABC, abstractmethod

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name: str = name
        self.country: str = country
        self.advantage: int = advantage
        self.budget: float = budget
        self.wins: int = 0
        self.equipment: list[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_equipment_price = sum([eq.price for eq in self.equipment])
        avg_protection = sum([eq.protection for eq in self.equipment]) / len(self.equipment) if self.equipment else 0
        return f"""Name: {self.name}
Country: {self.country}
Advantage: {self.advantage} points
Budget: {self.budget:.2f}EUR
Wins: {self.wins}
Total Equipment Price: {total_equipment_price:.2f}
Average Protection: {int(avg_protection)}"""
