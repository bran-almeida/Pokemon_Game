class Pokemon:

    def __init__(self, especie, level=1, nome=None):
        if nome:
            self.nome = nome
        else:
            self.nome = especie
            
        self.especie = especie
        self.level = level
    
    def __str__(self):
        return f"{'_'*50}\nNome: {self.nome}\nEspecie: {self.especie}\nLevel: {self.level}"

    def atacar(self, adversario):
        print(f"{self.especie} atacou! {adversario.especie}")


class PokemonEletrico(Pokemon):
    tipo = "Elétrico"
    def ataque(self, alvo):
        print(f"{self.especie} lançou um ataque elétrico em {alvo.especie}")

class PokemonFogo(Pokemon):
    tipo = "Fogo"
    def ataque(self, alvo):
        print(f"{self.especie} lançou um ataque de fogo em {alvo.especie}")

class PokemonAgua(Pokemon):
    tipo = "Agua"
    def ataque(self, alvo):
        print(f"{self.especie} lançou um ataque de agua em {alvo.especie}")

meupokemon = PokemonEletrico(nome="Frigg", especie="Pikachu")
advpokemon = PokemonFogo("Charisard", level=1, nome="Akira")

meupokemon.ataque(advpokemon)
advpokemon.ataque(meupokemon)