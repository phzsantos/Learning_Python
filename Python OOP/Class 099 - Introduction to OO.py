from datetime import datetime

class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        
        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True


    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True


    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('Paulo', 20)
p2 = Pessoa('Joao', 25)

p1.falar('POO')
p2.falar('Python')
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
