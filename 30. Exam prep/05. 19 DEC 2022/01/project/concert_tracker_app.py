from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        musician_to_add = self.find_musician_by_name(name)
        if musician_to_add:
            raise Exception(f"{name} is already a musician!")
        musician_to_add = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician_to_add)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_to_add = self.find_band_by_name(name)
        if band_to_add:
            raise Exception(f"{name} band is already created!")
        band_to_add = Band(name)
        self.bands.append(band_to_add)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_to_add = self.find_concert_by_place(place)
        if concert_to_add:
            raise Exception(f"{place} is already registered for {concert_to_add.genre} concert!")
        concert_to_add = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert_to_add)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician_to_add = self.find_musician_by_name(musician_name)
        if not musician_to_add:
            raise Exception(f"{musician_name} isn't a musician!")
        band_to_receive_musician = self.find_band_by_name(band_name)
        if not band_to_receive_musician:
            raise Exception(f"{band_name} isn't a band!")
        band_to_receive_musician.members.append(musician_to_add)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band_to_lose_musician = self.find_band_by_name(band_name)
        if not band_to_lose_musician:
            raise Exception(f"{band_name} isn't a band!")
        musician_to_remove = next((m for m in band_to_lose_musician.members if m.name == musician_name), None)
        if not musician_to_remove:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band_to_lose_musician.members.remove(musician_to_remove)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = self.find_concert_by_place(concert_place)
        band = self.find_band_by_name(band_name)

        current_band_member_types = {"Guitarist": 0, "Drummer": 0, "Singer": 0}
        for musician in band.members:
            if musician.__class__.__name__ == "Guitarist":
                current_band_member_types["Guitarist"] += 1
            elif musician.__class__.__name__ == "Drummer":
                current_band_member_types["Drummer"] += 1
            elif musician.__class__.__name__ == "Singer":
                current_band_member_types["Singer"] += 1
        for type_musician_value in current_band_member_types.values():
            if type_musician_value < 1:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        needed_skills = {}
        if concert.genre == "Rock":
            needed_skills = {"play the drums with drumsticks": 0, "sing high pitch notes": 0, "play rock": 0}
        elif concert.genre == "Metal":
            needed_skills = {"play the drums with drumsticks": 0, "sing low pitch notes": 0, "play metal": 0}
        elif concert.genre == "Jazz":
            needed_skills = {"play the drums with drum brushes": 0, "sing high pitch notes": 0, "sing low pitch notes": 0, "play jazz": 0}

        for musician in band.members:
            for skill in musician.skills:
                if skill in needed_skills:
                    needed_skills[skill] += 1

        for skill_value in needed_skills.values():
            if skill_value < 1:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

# _________________________________________________________________________________________________________________________________
    def find_concert_by_place(self, given_place: str):
        return next((c for c in self.concerts if c.place == given_place), None)

    def find_band_by_name(self, given_band_name: str):
        return next((b for b in self.bands if b.name == given_band_name), None)

    def find_musician_by_name(self, given_musician_name: str):
        return next((m for m in self.musicians if m.name == given_musician_name), None)
