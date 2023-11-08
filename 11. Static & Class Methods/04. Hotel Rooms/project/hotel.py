from typing import List, TypeVar, Type

from project.room import Room

T = TypeVar("T", bound="TrivialClass")


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List = [Room]
        self.guests = 0

    @classmethod
    def from_stars(cls: Type[T], stars_count: int) -> T:
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = [r for r in self.rooms if r.number == room_number][0]  # ако има такава стая ако не гърми и пишем try/except
        res = room.take_room(people)
        if not res:
            self.guests += 1  # това е за хотела

    def free_room(self, room_number: int) -> None:
        room = [r for r in self.rooms if r.number == room_number][0]
        guest_count_that_free_room = room.guests
        room.free_room(room_number)
        self.guests -= guest_count_that_free_room

    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join([str(r.number) for r in free_rooms])}" \
                 f"Taken rooms: {', '.join([str(r.number) for r in taken_rooms])}"
