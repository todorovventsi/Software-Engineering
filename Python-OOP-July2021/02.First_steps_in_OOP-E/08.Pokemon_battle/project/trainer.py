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
        details = ["- " + catch.pokemon_details() + "\n" for catch in self.pokemons]
        display_name = f"Pokemon Trainer {self.name}\n"
        pokemon_numbers = f"Pokemon count {len(self.pokemons)}\n"
        return f"{display_name}{pokemon_numbers}{''.join(details)}"
