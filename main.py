import pickle
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

def save_game(player):

    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo Salvo com sucesso!")
    except Exception as erro:
        print("Erro ao salvar")        
        print(erro)

def load_game():
    try:
        with open ("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso!")
            return player
    except Exception as error:
        print("Save não encontrado")

if __name__ == '__main__':

    print("_"*50)
    print("Bem Vindo ao pokemon RPG de terminal!")
    print("_"*50)
    
    player = load_game()

    if not player:

        nome = str(input("Olá, qual é o seu nome?\n>>>"))
        player = Player(nome)
        print("Olá esse é um mundo habitado por pokemons, sua missão é se tornar um mestre pokemon!")
        print("Capture pokemons, batalhe, viva essa aventura!")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Vejo que você já possui pokemons!")
            player.mostrar_pokemons()
        
        else:
            print("Vejo que você não possui pokemons! Para começar escolha um destes!")
            escolher_pokemon_incial(player)
        
        print("Pronto, agora que você já possui pokemon, está na hora da sua primeira batalha!")
        gary = Inimigo("Gary", pokemons=[PokemonAgua("Squirtle", 1)])
        player.batalhar(gary)
        
        save_game(player)
    
    while True:
        print("_"*50)
        print("O que deseja fazer?")
        print("[1] Explorar")
        print("[2] Batalhar")
        print("[3] Mostrar Pokeagenda")
        print("[0] Sair do Jogo")
        escolha = str(input(">>>"))
        
        if escolha == "0":
            print("Saindo do Jogo!")
            sleep(1)
            break
        elif escolha == "1":
            player.explorar()
            save_game(player)
        elif escolha == "2":
            player.batalhar(Inimigo())
            save_game(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        else:
            print("Escolha inválida!")     
         



