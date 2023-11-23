from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES = {"Appaloosa": Appaloosa,
                    "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.VALID_HORSES:
            horse_to_create = self.VALID_HORSES[horse_type](horse_name, horse_speed)

            if horse_to_create in self.horses:
                raise Exception(f"Horse {horse_name} has been already added!")

            self.horses.append(horse_to_create)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey_to_create = Jockey(jockey_name, age)
        if jockey_to_create in self.jockeys:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(jockey_to_create)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for saved_race in self.horse_races:
            if saved_race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        race_to_save = HorseRace(race_type)
        self.horse_races.append(race_to_save)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        searched_jockey = self.find_jockey_from_given_name(jockey_name)
        if not searched_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        searched_horse = self.find_last_horse_from_given_type_which_is_free(horse_type)
        if not searched_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if searched_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        searched_horse.is_taken = True
        searched_jockey.horse = searched_horse
        return f"Jockey {jockey_name} will ride the horse {searched_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        searched_race = self.find_race_from_given_type(race_type)
        if not searched_race:
            raise Exception(f"Race {race_type} could not be found!")

        searched_jockey = self.find_jockey_from_given_name(jockey_name)
        if not searched_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not searched_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if searched_jockey in searched_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        searched_race.jockeys.append(searched_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        searched_race = self.find_race_from_given_type(race_type)
        if not searched_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(searched_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_speed = 0
        winner_jockey = None
        for racer in searched_race.jockeys:
            if racer.horse.speed > winner_speed:
                winner_speed = racer.horse.speed
                winner_jockey = racer

        return f"The winner of the {race_type} race, with a speed of {winner_speed}km/h is {winner_jockey.name}\
! Winner's horse: {winner_jockey.horse.name}."

# -------------------------HELPER METHODS ----------------------------------
    def find_race_from_given_type(self, type_given: str):
        saved_race = None
        for race in self.horse_races:
            if race.race_type == type_given:
                saved_race = race
        return saved_race

    def find_last_horse_from_given_type_which_is_free(self, type_given: str):
        collection = [horse for horse in self.horses if
                      horse.STRING_HORSE_TYPE == type_given and not horse.is_taken]
        if collection:
            return collection[-1]

    def find_jockey_from_given_name(self, name_given: str):
        jockey = None
        for jockey_saved in self.jockeys:
            if jockey_saved.name == name_given:
                jockey = jockey_saved
        return jockey
