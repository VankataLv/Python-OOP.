from typing import List
from pokemon import Pokemon


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
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            return"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"
