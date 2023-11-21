from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_TYPES_EQUIPMENT = {"KneePad": KneePad,
                             "ElbowPad": ElbowPad}
    VALID_TYPES_TEAM = {"OutdoorTeam": OutdoorTeam,
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
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_TYPES_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.VALID_TYPES_EQUIPMENT[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TYPES_TEAM:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.VALID_TYPES_TEAM[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_to_sell = self.find_equipment_by_type(equipment_type)
        team_to_buy = self.find_team_by_name(team_name)
        if equipment_to_sell and team_to_buy:
            if team_to_buy.budget < equipment_to_sell.price:
                raise Exception("Budget is not enough!")

            self.equipment.remove(equipment_to_sell)
            team_to_buy.equipment.append(equipment_to_sell)
            team_to_buy.budget -= equipment_to_sell.price
            return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_to_remove = self.find_team_by_name(team_name)
        if team_to_remove not in self.teams:
            raise Exception("No such team!")

        if team_to_remove.wins > 0:
            raise Exception(f"The team has {team_to_remove.wins} wins! Removal is impossible!")

        self.teams.remove(team_to_remove)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        counter = 0
        for eq in self.equipment:
            if eq.EQUIPMENT_TYPE == equipment_type:
                counter += 1
                eq.increase_price()
        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = self.find_team_by_name(team_name1)
        team_2 = self.find_team_by_name(team_name2)
        if team_1.TEAM_TYPE != team_2.TEAM_TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        rating_1 = team_1.advantage + sum([x.protection for x in team_1.equipment])
        rating_2 = team_2.advantage + sum([x.protection for x in team_2.equipment])

        winner = None
        if rating_1 == rating_2:
            return "No winner in this game."
        elif rating_1 > rating_2:
            winner = team_1
        elif rating_2 > rating_1:
            winner = team_2

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        team_stats = '\n'.join(team.get_statistics() for team in self.teams)
        return f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:
{team_stats}"""

#  ___HELPER METHODS_____________________________________________________

    def find_equipment_by_type(self, type_given):  # LAST equipment in list!!!
        collection_of_equipments = [equipment for equipment in self.equipment if equipment.EQUIPMENT_TYPE == type_given]
        if collection_of_equipments:
            return collection_of_equipments[0]

        return None

    def find_team_by_name(self, name_given):
        for team in self.teams:
            if team.name == name_given:
                return team
        return None

#
# t = Tournament('SoftUniada2023', 2)
#
# print(t.add_equipment('KneePad'))
# print(t.add_equipment('ElbowPad'))
#
# print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
# print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
# print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))
#
# print(t.sell_equipment('KneePad', 'Spartak'))
#
# print(t.remove_team('Levski'))
# print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))
#
# print(t.increase_equipment_price('ElbowPad'))
# print(t.increase_equipment_price('KneePad'))
#
# print(t.play('Lokomotiv', 'Spartak'))
#
# print(t.get_statistics())
