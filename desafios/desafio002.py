from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto: 
    """
Classe Produto aonde podemos cadastrar o nome e o preço do produto e mostrando uma etiqueta do preoço do produto
    """
    def __init__(self, nome='', preco=0):
        self.nome = nome
        self.preco = preco 

    def etiqueta(self):
        conteudo = f"{self.nome} \n {self.preco:,.2f}"
        painel = Panel(
            Align.center(conteudo, vertical="middle"),
            title="Produto",
            title_align="center",
            width=25
        )
        print(painel)
    
p1 = Produto(nome="Iphone 17 Pro", preco=25_000.85)
p2 = Produto(nome="Notebook", preco=8_000)
p1.etiqueta()
p2.etiqueta()