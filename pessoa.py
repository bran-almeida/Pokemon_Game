from pokemon import *
import random

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
        return f'PLAYER: {self.nome}'

    def mostrar_pokemons(self):
        if self.pokemons:
            c=1
            for p in self.pokemons:
                print("_"*50)
                print(f'Pokemon {c}:') 
                print(p)
                c+=1
        else:
            print(f"{self} não possui pokemons")

class Player(Pessoa):
    tipo = "player"
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self.nome}, capturou um pokemon! {pokemon}:")

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for p in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons)


Meu_inimigo = Inimigo()
print(Meu_inimigo)
Meu_inimigo.mostrar_pokemons()
