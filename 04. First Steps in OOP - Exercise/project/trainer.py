from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        searched_pokemon = self.find_pokemon_by_name(pokemon_name)
        if searched_pokemon:
            self.pokemons.remove(searched_pokemon)
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def find_pokemon_by_name(self, given_name):
        for pokemon in self.pokemons:
            if pokemon.name == given_name:
                return pokemon

    def trainer_data(self):
        pok_data = "\n".join([f"- {x.pokemon_details()}" for x in self.pokemons])
        return f"""Pokemon Trainer {self.name}
Pokemon count {len(self.pokemons)}
{pok_data}"""

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.add_pokemon(Pokemon("TEST_P", 99)))
# print(trainer.trainer_data())
