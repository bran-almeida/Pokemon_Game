import random
class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        
        self.especie = especie
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        if level:
            self.level = level
        else:            
            self.level = random.randint(1,100)
        
        self.ataque = self.level * 5
        self.vida = self.level * 10
        
    def __str__(self):
        return f"Especie: {self.especie} | Level: {self.level} | Tipo: {self.tipo}"

    def atacar(self, alvo):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        alvo.vida -= ataque_efetivo
        
        print(f"{alvo.especie} perdeu {ataque_efetivo} pontos de vida")

        if alvo.vida <= 0:
            print(f"{alvo.especie}, foi derrotado.")
            return True
        else:
            return False

class PokemonEletrico(Pokemon):
    tipo = "Elétrico"
 
    def atacar(self, alvo):
        print(f"{self.especie} lançou um ataque elétrico em {alvo.especie}")
        return super().atacar(alvo)

class PokemonFogo(Pokemon):
    tipo = "Fogo"
    
    def atacar(self, alvo):
        print(f"{self.especie} lançou um ataque de fogo em {alvo.especie}")
        return super().atacar(alvo)

class PokemonAgua(Pokemon):
    tipo = "Agua"
    
    def atacar(self, alvo):
        print(f"{self.especie} lançou um ataque de agua em {alvo.especie}")
        return super().atacar(alvo)