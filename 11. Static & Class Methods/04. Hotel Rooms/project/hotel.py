from typing import List


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List = [int]
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):