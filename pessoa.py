from pokemon import *
from time import sleep

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
    
    def __init__(self, nome=None, pokemons=[], money=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.money = money
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
        pokemon_escolhido = random.choice(self.pokemons)
        print(f"{self} escolheu {pokemon_escolhido.nome}")
        return pokemon_escolhido

    def gain_money(self, quantity):
        self.money += quantity
        print(f"Você ganhou $ {quantity}")
        self.mostrar_dinheiro()

    def mostrar_dinheiro(self):
        print(f"Você possui {self.money}")

    def batalhar(self, pessoa):
        print(f"{self} iniciou uma batalha com {pessoa}!!!")
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        meu_pokemon = self.escolher_pokemon()

        if pokemon_inimigo and meu_pokemon:
            while True:
                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f"{self} e {meu_pokemon.especie} venceram")
                    self.gain_money(pokemon_inimigo.level * 100)
                    break
                
                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)
                if vitoria_inimiga:
                    print(f"{pessoa} e {pokemon_inimigo.especie} venceram")
                    break
        else:
            print("Essa batalha não pode ocorrer.")

class Player(Pessoa):
    tipo = "player"
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self.nome}, capturou um pokemon: {pokemon.especie}")
    
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
    
    def explorar(self):
        while True:
            print("_"*50)
            print("Explorando >>> ",end="")
            for i in range(1,4):
                if i < 3:
                    print(i, end="")
                    sleep(1)
                else: 
                    print(i)
                    sleep(1)
            print("_"*50)

            if random.random() <= 0.3:
                pokemon_encontrado = random.choice(POKEMONS)
                print("Você encontrou um pokemon selvagem!")
                print(">>>", pokemon_encontrado)
                while True:
                    escolha = input(f"{self} deseja capturar {pokemon_encontrado.especie}?\n(s/n) >>>")
                    sleep(0.5)
                    if escolha in "Ss":
                        if random.random() <= 0.5:
                            print("_"*50)
                            print(f"Você conseguiu capturar {pokemon_encontrado.especie}")
                            self.capturar(pokemon_encontrado)
                            break
                        else:
                            print(f"Infelizmente você não conseguiu capturar {pokemon_encontrado.especie}")
                            print("Continuando exploração!")
                            break
                    elif escolha in "Nn":
                        print("Ok boa viagem!")
                        break
                    else: 
                        print("Valor inválido, informe \"s\" ou \"n\"")       

            else:
                print("Nenhum pokemon encontrado durante a exploração!")
                continuar = input(f"{self}, você deseja continuar explorando?\n(s/n) >>> ")
                sleep(0.5)
                if continuar in "Ss":
                    print("_"*50)
                    print("Continuando exploração!")
                elif continuar in "Nn":
                    print("Voltando para casa!")
                    break
                else: 
                    print("Valor inválido, informe \"s\" ou \"n\"")

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for p in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons)

    
