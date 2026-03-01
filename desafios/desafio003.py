from rich import print
from rich.panel import Panel
from rich.align import Align 

class Churrasco:
    """
    Cria uma classe chamada churrasco e pergunta quantas pessoas vao participar e o qaunto de carne deve ser comprado
    """
    def __init__(self, quant = 0, titulo = ''):
        self.quant = quant
        self.titulo = titulo

    def churrasco(self, kg_carne = 0):
        kg_carne= 0.4 * self.quant 
        valor_total = kg_carne * 82.40
        valor_por_pessoa = valor_total / self.quant

        texto = f"Analisando o {self.titulo} com [bold green]{self.quant} convidados[/]:\n\n"
        #utilizei o texto como variavel para armazernar os recados pois o print  nao pode ser utilziado dentro do Panel 
        texto += f"Cada participante irá comer 0.4kg e cada KG custa R$82.40\n"
        texto += f"Recomendo [bold blue]comprar {kg_carne:.1f}kg[/] de carne.\n"
        texto += f"O custo total será de [bold yellow]R${valor_total:.2f}[/]\n"
        texto += f"Cada pessoa irá pagar [bold red]R${valor_por_pessoa:.2f}[/]"
        painel = Panel(
            texto,
            title= self.titulo,
            title_align="center",
            width=70,
        )
        print(painel)

c1 = Churrasco(titulo="Churrasco dos Amigos", quant=100)
c1.churrasco()
#CONSIDERE:
#Consumo padrão por pessoa: 400g -> transformando em kg: 0.4kg
#Preço do kg da carne: 82.40kg