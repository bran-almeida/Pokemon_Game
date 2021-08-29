from pokemon import *

NOMES = ["Miau", "Jack", "Jane"]
POKEMONS = [
    PokemonFogo("Chamander"),
    PokemonFogo("Charmeleon"),
    PokemonFogo("Charisard"),
    PokemonFogo("Vulpix"),
    PokemonFogo("Ninetails"),
    PokemonFogo("Growlithe"),
    PokemonFogo("Arcanine"),
    PokemonFogo("Rapidash"),
    PokemonFogo("Ponyta"),
    PokemonAgua("Krabby"),
    PokemonAgua("Kingler"),
    PokemonAgua("Poliwag"),
    PokemonAgua("Poliwhirl"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Wartortle"),
    PokemonAgua("Blastoise"),
    PokemonAgua("Psyduck"),
    PokemonAgua("Golduck"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonEletrico("Voltorb"),
    PokemonEletrico("Electrode"),
    PokemonEletrico("Jolteon"),
    PokemonEletrico("Zapdos"),
    PokemonEletrico("Pichu"),
    PokemonEletrico("Mareep"),
    PokemonEletrico("Flaafy"),
    PokemonEletrico("Ampharos")
]
class Pessoa:
    
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons
    
    def __str__(self):
        return f'{self.nome}'

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"Esses são os pokemons de {self}")
            for e, p in enumerate(self.pokemons):
                print(f'[{e+1}] - {p}') 
        
        else:
            print(f"{self} não possui pokemons")

    def escolher_pokemon(self):
        while True:
            print(f"{self} escolha um de seus pokemons para batalhar: ")
            self.mostrar_pokemons()
            try:
                escolha = int(input(">>> "))-1
                pokemon_escolhido = self.pokemons[escolha]
                print(f"{pokemon_escolhido.nome} eu escolho você!!!")
                return pokemon_escolhido
            except:
                print(f"Valor informado é invalido, escolha um numero entre 1 e {len(self.pokemons)} para selecionar um pokemon para batalha")

    def batalhar(self, pessoa):
        print(f"{self} iniciou uma batalha com {pessoa}!!!")
        pessoa.mostrar_pokemons()
        pessoa.escolher_pokemon()
        self.escolher_pokemon()

class Player(Pessoa):
    tipo = "player"
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self.nome}, capturou um pokemon! {pokemon}")

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for p in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        pokemon_escolhido = random.choice(self.pokemons)
        print(f"{self} escolheu {pokemon_escolhido.nome}")
        return pokemon_escolhido
