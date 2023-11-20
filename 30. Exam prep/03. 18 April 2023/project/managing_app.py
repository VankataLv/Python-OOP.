from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {'PassengerCar': PassengerCar,
                           'CargoVan': CargoVan}

    def __init__(self):
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and \
                    route.end_point == end_point and \
                    route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            elif (route.start_point == start_point and route.end_point == end_point) and \
                    route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            elif (route.start_point == start_point and route.end_point == end_point) and \
                    route.length > length:
                route.is_locked = True

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        searched_user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        searched_vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        searched_route = self.routes[route_id - 1]
        if searched_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if searched_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if searched_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        searched_vehicle.drive(searched_route.length)

        if is_accident_happened:
            searched_vehicle.change_status()
            searched_user.decrease_rating()
        else:
            searched_user.increase_rating()

        return str(searched_vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        ordered_damaged_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))
        if count > len(ordered_damaged_vehicles):
            vehicles_to_repair = ordered_damaged_vehicles
        else:
            vehicles_to_repair = ordered_damaged_vehicles[0:count]
        for d_v in vehicles_to_repair:
            d_v.change_status()
            d_v.recharge()
        return f"{len(vehicles_to_repair)} vehicles were successfully repaired!"

    def users_report(self):
        ordered_users = sorted(self.users, key=lambda x: -x.rating)
        result = "*** E-Drive-Rent ***\n"
        result += '\n'.join([str(u) for u in ordered_users])
        return result


app = ManagingApp()
print(app.register_user('Tisha', 'Reenie', '7246506'))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
