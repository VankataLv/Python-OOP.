from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread,
                        "Stolen": Stolen}
    VALID_BOOTHS = {"Open Booth": OpenBooth,
                    "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for added_delicacies in self.delicacies:
            if added_delicacies.name == name:
                raise Exception(f"{type_delicacy} already exists!")
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        delicacy_obj = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy_obj)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for added_booth in self.booths:
            if added_booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        booth_obj = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth_obj)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for i in range(0, len(self.booths)):
            cur_booth = self.booths[i]
            if not cur_booth.is_reserved:
                if cur_booth.capacity >= number_of_people:
                    cur_booth.reserve(number_of_people)
                    return f"Booth {cur_booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_booth_by_number(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy = self.find_delicacy_by_name(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth_by_number(booth_number)
        bill = booth.price_for_reservation
        for ordered_meal in booth.delicacy_orders:
            bill += ordered_meal.price
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"""Booth {booth_number}:
Bill: {bill:.2f}lv."""

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def find_booth_by_number(self, number_given: int):
        for b in self.booths:
            if b.booth_number == number_given:
                return b

    def find_delicacy_by_name(self, name_given: str):
        for d in self.delicacies:
            if d.name == name_given:
                return d


# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
