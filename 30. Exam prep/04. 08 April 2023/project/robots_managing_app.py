from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {'MainService': MainService,
                      'SecondaryService': SecondaryService}
    VALID_ROBOTS = {'MaleRobot': MaleRobot,
                    'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")
        self.services.append(self.VALID_SERVICES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        self.robots.append(self.VALID_ROBOTS[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._robot_search_by_name(robot_name)
        service = self._service_search_by_name(service_name)
        if robot.ROBOT_GENDER == "Female":
            if service.SERVICE_TYPE == "Main":
                return "Unsuitable service."
        if robot.ROBOT_GENDER == "Male":
            if service.SERVICE_TYPE == "Secondary":
                return "Unsuitable service."
        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        robot = None
        service = self._service_search_by_name(service_name)
        for robot_in_service in service.robots:
            if robot_in_service.name == robot_name:
                robot = robot_in_service
                break
        if robot:
            service.robots.remove(robot)
            self.robots.append(robot)
            return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = self._service_search_by_name(service_name)
        for robot_in_service in service.robots:
            robot_in_service.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        total_price = 0
        service = self._service_search_by_name(service_name)
        for robot_in_service in service.robots:
            total_price += robot_in_service.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(s.details() for s in self.services)

    def _robot_search_by_name(self, r_name):
        return [r for r in self.robots if r.name == r_name][0]

    def _service_search_by_name(self, s_name):
        return [s for s in self.services if s.name == s_name][0]


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
