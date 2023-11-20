from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def add_player(self, *players_to_add):
        successfully_added_players = []
        for cur_player in players_to_add:
            if cur_player not in self.players:
                self.players.append(cur_player)
                successfully_added_players.append(cur_player)
        return f"Successfully added: {', '.join([p.name for p in successfully_added_players])}"

    def add_supply(self, *supplies_to_add):
        for cur_supply in supplies_to_add:
            self.supplies.append(cur_supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player_needed = next(p for p in self.players if p.name == player_name)
        if player_needed:
            if not player_needed.need_sustenance:
                return f"{player_name} have enough stamina."

            if sustenance_type not in ["Food", "Drink"]:
                return None

            supply_needed = None
            if self.supplies:
                for i in range(-1, -len(self.supplies) - 1, -1):
                    cur_supply = self.supplies[i]
                    if cur_supply.__class__.__name__ == sustenance_type:
                        supply_needed = cur_supply
                        self.supplies.remove(cur_supply)
                        break
            else:
                return None

            if supply_needed:
                if player_needed.stamina + supply_needed.energy <= 100:
                    player_needed.stamina += supply_needed.energy
                else:
                    player_needed.stamina = 100
                return f"{player_name} sustained successfully with {supply_needed.name}."

            else:
                if sustenance_type == "Food":
                    raise Exception("There are no food supplies left!")
                elif sustenance_type == "Drink":
                    raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        player_one_class = None
        player_two_class = None
        for cur_player in self.players:
            if cur_player.name == first_player_name:
                player_one_class = cur_player
            elif cur_player.name == second_player_name:
                player_two_class = cur_player
            else:
                continue

        if player_one_class and player_two_class:
            if player_one_class.stamina == 0:
                return f"Player {first_player_name} does not have enough stamina."
            if player_one_class.stamina == 0:
                return f"Player {second_player_name} does not have enough stamina."

        # first_attacker = None
        # second_attacker = None
        # winner = None
        if player_one_class.stamina < player_two_class.stamina:
            first_attacker = player_one_class
            second_attacker = player_two_class
        else:
            first_attacker = player_two_class
            second_attacker = player_one_class

        second_attacker.stamina -= first_attacker.stamina / 2
        if second_attacker.stamina <= 0:
            return f"Winner: {first_attacker.name}"
        else:
            first_attacker.stamina -= second_attacker.stamina / 2
            if first_attacker.stamina <= 0:
                return f"Winner: {second_attacker.name}"

        if first_attacker.stamina > second_attacker.stamina:
            return f"Winner: {first_attacker.name}"
        else:
            return f"Winner: {second_attacker.name}"

    def next_day(self):
        for cur_player in self.players:
            if cur_player.stamina - (cur_player.age * 2) < 0:
                cur_player.stamina = 0
            else:
                cur_player.stamina -= (cur_player.age * 2)

            self.sustain(cur_player.name, "Food")
            self.sustain(cur_player.name, "Drink")

    def __str__(self):
        return '\n'.join([p.__str__() for p in self.players] +
                 [s.details() for s in self.supplies])
