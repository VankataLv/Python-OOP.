import math
from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
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
        total_price_of_team_equipment = sum([e.price for e in self.equipment])
        avg_team_protection = 0
        if self.equipment:
            avg_team_protection = sum([e.protection for e in self.equipment]) / len(self.equipment)
        return f"""Name: {self.name}
Country: {self.country}
Advantage: {self.advantage} points
Budget: {self.budget:.2f}EUR
Wins: {self.wins}
Total Equipment Price: {total_price_of_team_equipment:.2f}
Average Protection: {math.floor(avg_team_protection)}\n"""
