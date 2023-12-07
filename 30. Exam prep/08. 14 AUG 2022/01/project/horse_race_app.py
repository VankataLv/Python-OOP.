from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    VALID_HORSE_RACE_TYPES = ("Winter", "Spring", "Autumn", "Summer")

    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.VALID_HORSE_TYPES:
            horse_to_add = self._find_horse_by_name(horse_name)
            if horse_to_add:
                raise Exception(f"Horse {horse_name} has been already added!")
            horse_to_add = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(horse_to_add)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey_to_add = self._find_jockey_by_name(jockey_name)
        if jockey_to_add:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey_to_add = Jockey(jockey_name, age)
        self.jockeys.append(jockey_to_add)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        horse_race_to_add = self._find_horse_race_by_type(race_type)
        if horse_race_to_add:
            raise Exception(f"Race {race_type} has been already created!")
        horse_race_to_add = HorseRace(race_type)
        self.horse_races.append(horse_race_to_add)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self._find_last_horse_saved_by_type_that_is_free(horse_type)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self._find_horse_race_by_type(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self._find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self._find_horse_race_by_type(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jockey_name = None
        winner_horse_name = None
        highest_speed = 0

        for j in horse_race.jockeys:
            if j.horse.speed > highest_speed:
                winner_jockey_name = j.name
                winner_horse_name = j.horse.name
                highest_speed = j.horse.speed

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner_jockey_name}!\
 Winner's horse: {winner_horse_name}."

    def _find_last_horse_saved_by_type_that_is_free(self, given_horse_type: str):
        return [h for h in self.horses if h.__class__.__name__ == given_horse_type and not h.is_taken][-1]

    def _find_horse_race_by_type(self, given_horse_race_type: str):
        return next((h_r for h_r in self.horse_races if h_r.race_type == given_horse_race_type), None)

    def _find_jockey_by_name(self, given_name: str):
        return next((j for j in self.jockeys if j.name == given_name), None)

    def _find_horse_by_name(self, given_name: str):
        return next((h for h in self.horses if h.name == given_name), None)
