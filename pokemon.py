import random
class Pokemon:

    def __init__(self, especie, level=None, nome=None, tipo=None):
        self.especie = especie
        
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        if level:
            self.level = level
        else:            
            self.level = random.randint(1,100)
        
    def __str__(self):
        return f"\nEspecie: {self.especie}\nLevel: {self.level}\nTipo: {self.tipo}"

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