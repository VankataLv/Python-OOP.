from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self) -> str:

        unpacked_skills = '\n'.join([f"==={k} - {v}" for k, v in self.skills.items()])

        return f"Name: {self.name}\n" + \
               f"Guild: {self.guild}\n" + \
               f"HP: {self.hp}\n" + \
               f"MP: {self.mp}\n" + \
               f"{unpacked_skills}"

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
