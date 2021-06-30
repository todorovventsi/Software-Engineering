from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        pokemon_is_in_the_list = False
        poky = ""
        for name in self.pokemons:
            if name.name == pokemon_name:
                pokemon_is_in_the_list = True
                poky = name

        if pokemon_is_in_the_list:
            self.pokemons.remove(poky)
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    # This should be refactored as it is not working properly
    def trainer_data(self):
        details = []
        for catch in self.pokemons:
            result = catch.pokemon_details
            details.append(result)
        return details






pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())