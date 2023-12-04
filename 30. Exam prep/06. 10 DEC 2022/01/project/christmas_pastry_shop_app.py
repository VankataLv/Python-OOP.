from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_TYPES_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_TYPES_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy_to_add = self.find_delicacy_by_name(name)
        if delicacy_to_add:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.VALID_TYPES_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        delicacy_to_add = self.VALID_TYPES_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy_to_add)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth_to_add = self.find_booth_by_booth_number(booth_number)
        if booth_to_add:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_TYPES_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        booth_to_add = self.VALID_TYPES_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth_to_add)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        proper_booth = self.find_not_reserved_booth_with_enough_capacity(number_of_people)
        if not proper_booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        proper_booth.reserve(number_of_people)
        return f"Booth {proper_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_booth_by_booth_number(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy = self.find_delicacy_by_name(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth_by_booth_number(booth_number)
        bill = booth.price_for_reservation
        for ordered_delicacy in booth.delicacy_orders:
            bill += ordered_delicacy.price
        self.income += bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"""Booth {booth_number}:
Bill: {bill:.2f}lv."""

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def find_not_reserved_booth_with_enough_capacity(self, number_seats_needed):
        return next((b for b in self.booths if not b.is_reserved and
                                                  b.capacity >= number_seats_needed), None)

    def find_booth_by_booth_number(self, given_booth_number: int):
        return next((b for b in self.booths if b.booth_number == given_booth_number), None)

    def find_delicacy_by_name(self, given_name: str):
        return next((d for d in self.delicacies if d.name == given_name), None)
