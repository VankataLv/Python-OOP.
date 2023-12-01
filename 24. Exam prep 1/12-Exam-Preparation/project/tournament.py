from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        equipment_to_add = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment_to_add)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        team_to_add = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team_to_add)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self.find_last_equipment_by_type(equipment_type)
        team = self.find_team_by_team_name(team_name)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.budget -= equipment.price
        team.equipment.append(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.find_team_by_team_name(team_name)
        if not team:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        counter = 0
        for eq in self.equipment:
            if eq.__class__.__name__ == equipment_type:
                eq.increase_price()
                counter += 1
        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first_team = self.find_team_by_team_name(team_name1)
        second_team = self.find_team_by_team_name(team_name2)
        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_points = 0
        for eq1 in first_team.equipment:
            first_team_points += eq1.protection
        first_team_points += first_team.advantage

        second_team_points = 0
        for eq2 in second_team.equipment:
            second_team_points += eq2.protection
        second_team_points += second_team.advantage

        winner = ""
        if first_team_points > second_team_points:
            winner = first_team
        elif second_team_points > first_team_points:
            winner = second_team
        else:
            return "No winner in this game."

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda t: -t.wins)
        result = f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:\n"""
        for team in teams:
            result += team.get_statistics()
        return result

    def find_last_equipment_by_type(self, given_type: str):
        equipment_collection = [eq for eq in self.equipment if eq.__class__.__name__ == given_type]
        if equipment_collection:
            return equipment_collection[-1]

    def find_team_by_team_name(self, given_name):
        return next((team for team in self.teams if team.name == given_name), None)

t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
