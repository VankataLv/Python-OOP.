from typing import List
from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, cust_id: int):
        self.name = name
        self.age = age
        self.cust_id = cust_id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        lst_dvd_name = []
        for dvd_instance in self.rented_dvds:
            lst_dvd_name.append(dvd_instance.name)
        return f"{self.cust_id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({','.join(lst_dvd_name)})"
