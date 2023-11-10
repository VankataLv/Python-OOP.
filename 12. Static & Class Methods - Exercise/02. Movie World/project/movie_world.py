from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        s_customer = next((c for c in self.customers if c.cust_id == customer_id), None)
        s_dvd = next((d for d in self.dvds if d.dvd_id == dvd_id), None)
        if s_dvd in s_customer.rented_dvds:
            return f"{s_customer.name} has already rented {s_dvd.name}"
        elif s_dvd.is_rented:
            return "DVD is already rented"  # because the dvd is rented, but it is not in the above-mentioned customer
        elif not s_dvd.is_rented:
            if s_customer.age < s_dvd.age_restriction:
                return f"{s_customer.name} should be at least {s_dvd.age_restriction} to rent this movie"
            else:
                s_customer.rented_dvds.append(s_dvd)
                s_dvd.is_rented = True
                return f"{s_customer.name} has successfully rented {s_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        s_customer = next((c for c in self.customers if c.cust_id == customer_id), "Wrong ID")
        s_dvd = next((d for d in self.dvds if d.dvd_id == dvd_id), "Wrong ID")
        if s_dvd in s_customer.rented_dvds:
            s_customer.rented_dvds.remove(s_dvd)
            s_dvd.is_rented = False
            return f"{s_customer.name} has successfully returned {s_dvd.name}"
        else:
            return f"{s_customer.name} does not have that DVD"

    def __repr__(self):
        result = "\n".join([c.__repr__() for c in self.customers]) + "\n"
        result += "\n".join([d.__repr__() for d in self.dvds])
        return result
