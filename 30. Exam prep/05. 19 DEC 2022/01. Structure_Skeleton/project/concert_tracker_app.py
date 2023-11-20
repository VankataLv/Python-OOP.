from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist,
                            "Drummer": Drummer,
                            "Singer": Singer}

    def __init__(self):
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        for musician_already_enrolled in self.musicians:
            if musician_already_enrolled.name == name:
                raise Exception(f"{name} is already a musician!")
        obj = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(obj)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for created_bands in self.bands:
            if created_bands.name == name:
                raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for already_created_concerts in self.concerts:
            if already_created_concerts.place == place:
                raise Exception(f"{place} is already registered for {already_created_concerts.genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        band = self.find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = None
        for musician_in_band in band.members:
            if musician_in_band.name == musician_name:
                musician = musician_in_band
                break
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_band_by_name(band_name)

        musicians_in_band_roster = {"Guitarist": 0,
                                    "Drummer": 0,
                                    "Singer": 0}
        for musician_in_band in band.members:
            if musician_in_band.MUSICIAN_TYPE == "Guitarist":
                musicians_in_band_roster["Guitarist"] += 1
            elif musician_in_band.MUSICIAN_TYPE == "Drummer":
                musicians_in_band_roster["Drummer"] += 1
            elif musician_in_band.MUSICIAN_TYPE == "Singer":
                musicians_in_band_roster["Singer"] += 1
        all_musician_types_present = True
        for key in musicians_in_band_roster:
            if musicians_in_band_roster[key] < 1:
                all_musician_types_present = False
        if not all_musician_types_present:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = self.find_concert_by_place(concert_place)
        appropriate_skills_present = True
        if concert.genre == "Rock":
            for m in band.members:
                if m.MUSICIAN_TYPE == "Drummer":
                    if "play the drums with drumsticks" not in m.skills:
                        appropriate_skills_present = False
                elif m.MUSICIAN_TYPE == "Singer":
                    if "sing high pitch notes" not in m.skills:
                        appropriate_skills_present = False
                elif m.MUSICIAN_TYPE == "Guitarist":
                    if "play rock" not in m.skills:
                        appropriate_skills_present = False

        elif concert.genre == "Metal":
            for m in band.members:
                if m.MUSICIAN_TYPE == "Drummer":
                    if "play the drums with drumsticks" not in m.skills:
                        appropriate_skills_present = False
                elif m.MUSICIAN_TYPE == "Singer":
                    if "sing low pitch notes" not in m.skills:
                        appropriate_skills_present = False
                elif m.MUSICIAN_TYPE == "Guitarist":
                    if "play metal" not in m.skills:
                        appropriate_skills_present = False

        elif concert.genre == "Jazz":
            for m in band.members:
                if m.MUSICIAN_TYPE == "Drummer":
                    if "play the drums with drum brushes" not in m.skills:
                        appropriate_skills_present = False
                elif m.MUSICIAN_TYPE == "Singer":
                    if "sing high pitch notes" not in m.skills or "sing low pitch notes" not in m.skills:
                        appropriate_skills_present = False
                elif m.MUSICIAN_TYPE == "Guitarist":
                    if "play jazz" not in m.skills:
                        appropriate_skills_present = False

        if not appropriate_skills_present:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def find_concert_by_place(self, place_given: str):
        for c in self.concerts:
            if c.place == place_given:
                return c
        return None

    def find_musician_by_name(self, name_given: str):
        for m in self.musicians:
            if m.name == name_given:
                return m
        return None

    def find_band_by_name(self, name_given: str):
        for b in self.bands:
            if b.name == name_given:
                return b
        return None

# ______________________________________________________
#
#
# musician_types = ["Singer", "Drummer", "Guitarist"]
# names = ["George", "Alex", "Lilly"]
#
# app = ConcertTrackerApp()
#
# for i in range(3):
#     print(app.create_musician(musician_types[i], names[i], 20))
#
# print(app.musicians[0].learn_new_skill("sing high pitch notes"))
# print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
# print(app.musicians[2].learn_new_skill("play rock"))
#
# print(app.create_band("RockName"))
# for i in range(3):
#     print(app.add_musician_to_band(names[i], "RockName"))
#
# print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
#
# print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
# print(app.start_concert("Sofia", "RockName"))
