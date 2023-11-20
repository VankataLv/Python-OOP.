from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad,
                       "ElbowPad": ElbowPad}

    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam,
                   "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.VALID_EQUIPMENT[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        self.teams.append(self.VALID_TEAMS[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self._find_team_by_name(team_name)
        equipment = self._find_last_equipment_by_type(equipment_type)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)
        if not team:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        counter = 0
        for equipment in self.equipment:
            if equipment.TYPE_EQ == equipment_type:
                equipment.increase_price()
                counter += 1
        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)
        if team1.TEAM_TYPE != team2.TEAM_TYPE:
            Exception("Game cannot start! Team types mismatch!")

        team1_protection = sum([e for e in team1.equipment])
        team1_data = team1.advantage + team1_protection
        team2_protection = sum([e.protection for e in team2.equipment])
        team2_data = team2.advantage + team2_protection

        if team1_data > team2_data:
            winner = team1
        elif team1_data < team2_data:
            winner = team2
        else:
            return "No winner in this game."

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        return f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:
{''.join([team.get_statistics() for team in self.teams])}"""

# -------------Support Methods-----------------

    def _find_team_by_name(self, name_search: str):
        searched_team = [team for team in self.teams if team.name == name_search]
        return searched_team[0] if searched_team else None

    def _find_last_equipment_by_type(self, type_search):
        searched_equipment = [e for e in self.equipment if e.TYPE_EQ == type_search]
        # searched_equipment = [e for e in self.equipment if e.__class__.__name__ == type_search]
        return searched_equipment[-1] if searched_equipment else None


t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))
#
print(t.sell_equipment('KneePad', 'Spartak'))
#
print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))
#
print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))
#
print(t.play('Lokomotiv', 'Spartak'))
#
print(t.get_statistics())
