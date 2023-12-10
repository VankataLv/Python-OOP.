from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list[BaseFish] = []   # stores BaseFish
        self.competition_points: float = 0.0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level >= fish.time_to_catch:
            self.catch.append(fish)
            points_to_add = round(fish.points, 1)
            self.competition_points += points_to_add
            self.oxygen_level -= fish.time_to_catch
        else:
            self.oxygen_level = 0.0

        if self.oxygen_level == 0.0:
            BaseDiver.update_health_status(self)

    def update_health_status(self):
        if self.has_health_issue:           # True
            self.has_health_issue = False
        else:
            self.has_health_issue = True

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
