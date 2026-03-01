from rich import print

class Funcionario:
    """
Cria uma classe Funcionario aonde cadastra nome, setor e cargo
    """
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def __str__(self):
        return f":wave: Olá, me chamo {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo "
    
n = str(input("digite seu nome: "))
s = str(input("digite qual setor vc trabalha: "))
c = str(input("digite seu cargo em seu trabalho "))
f1 = Funcionario(n, s, c)
print(str(f1))