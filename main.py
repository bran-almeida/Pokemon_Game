from pokemon import *
from pessoa import *

def escolher_pokemon_incial(player):
    print(f"Olá {player}, agora você deve escolher o pokemon que lhe acompanhará nessa jornada!")

    pk1 = PokemonAgua("Squirtle", level=1)
    pk2 = PokemonFogo("Charmander", level=1)
    pk3 = PokemonEletrico("Pikachu", level=1)

    print("Você pode escolher entre estes três pokemons:")
    print(f"[1] - {pk1.especie}\n[2] - {pk2.especie}\n[3] - {pk3.especie}")
    
    while True:
        escolha = str(input("Sua escolha >>> "))
        if escolha == "1":
            player.capturar(pk1)
            break
        elif escolha == "2":
            player.capturar(pk2)
            break
        elif escolha == "3":
            player.capturar(pk3)
            break
        else:
            print("Você deve escolher 1, 2 ou 3!!!")

player = Player("Brandon")
escolher_pokemon_incial(player)