from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam,  "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name: str = name
        self.capacity: int = capacity
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
        self.equipment.append(self.VALID_EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."
        self.teams.append(self.VALID_TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_to_sell = self._find_last_equipment_by_type(equipment_type)
        team_to_get = self._find_team_by_name(team_name)
        if team_to_get.budget < equipment_to_sell.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment_to_sell)
        team_to_get.equipment.append(equipment_to_sell)
        team_to_get.budget -= equipment_to_sell.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_to_remove = self._find_team_by_name(team_name)
        if team_to_remove is None:
            raise Exception("No such team!")
        if team_to_remove.wins > 0:
            raise Exception(f"The team has {team_to_remove.wins} wins! Removal is impossible!")
        self.teams.remove(team_to_remove)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_to_increase_price = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        for e in equipment_to_increase_price:
            e.increase_price()
        return f"Successfully changed {len(equipment_to_increase_price)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)
        if not team1.__class__.__name__ == team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        point1 = self._summed_points_for_team(team1)
        point2 = self._summed_points_for_team(team2)

        if point1 > point2:
            winner = team1
        elif point1 < point2:
            winner = team2
        else:
            return "No winner in this game."

        winner.win()
        return f"The winner is {winner.name}."  # -5

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

    def _summed_points_for_team(self, given_team: BaseTeam):
        return sum(eq.protection for eq in given_team.equipment) + given_team.advantage

    def _find_team_by_name(self, given_name: str):
        return next((t for t in self.teams if t.name == given_name), None)

    def _find_last_equipment_by_type(self, given_type: str):
        collection = [e for e in self.equipment if e.__class__.__name__ == given_type]
        if collection:
            return collection[-1]
