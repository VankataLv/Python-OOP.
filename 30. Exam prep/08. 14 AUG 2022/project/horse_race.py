from project.jockey import Jockey


class HorseRace:
    VALID_HORSE_RACES = ("Winter", "Spring", "Autumn", "Summer")

    def __init__(self, race_type):
        self.race_type = race_type
        self.jockeys: list[Jockey] = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value not in self.VALID_HORSE_RACES:
            raise ValueError("Race type does not exist!")
        self.__race_type = value
