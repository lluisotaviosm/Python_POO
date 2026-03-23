from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [white on blue]{self.nome}[/]"
        conteudo += f'\n Jogos favoritos: '
        for num, game in enumerate(self.favoritos):
            conteudo+= f"\n:video_game: [green]{game}[/]"
        painel = Panel(conteudo, title=f"jogador <{self.nick}>", width=40)
        print(painel)   

j1 = Gamer("Luis Otavio Silva", "lluisotaviosm")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God Of Wars")
j1.add_favoritos("Fifa")
j1.ficha()

j2 = Gamer("Pedro", "PedrinMatador")
j2.add_favoritos("Fifa")
j2.add_favoritos("Minecraft")
j2.add_favoritos("Clash Royale")
j2.add_favoritos("CS")
j2.ficha()