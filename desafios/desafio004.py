from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class Livro:
    def __init__(self, titulo, paginas):
        self.console = Console()
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        
        # Painel de boas-vindas
        mensagem = Text.assemble(
            ("📖 Você abriu o livro ", "italic white"),
            (f"'{self.titulo}'", "bold magenta"),
            (f"\nTotal de páginas: {self.total_paginas}", "cyan"),
            (f"\nVocê está na página {self.pagina_atual}", "green")
        )
        self.console.print(Panel(mensagem, expand=False, border_style="blue"))

    def avancar_paginas(self, qtd):
        if self.pagina_atual >= self.total_paginas:
            self.console.print(f"[bold red]🚩 Você já terminou '{self.titulo}'![/]")
            return

        paginas_saltadas = 0
        texto_progresso = Text() # Objeto do Rich para acumular texto colorido

        for _ in range(qtd):
            if self.pagina_atual < self.total_paginas:
                self.pagina_atual += 1
                paginas_saltadas += 1
                
                # Adiciona a página com cor
                texto_progresso.append(f"Pág{self.pagina_atual}", style="bold yellow")
                
                if self.pagina_atual < self.total_paginas:
                    texto_progresso.append(" ▶ ", style="white")
            else:
                break
        
        # Exibe o rastro das páginas
        self.console.print(texto_progresso)
        
        # Painel de resumo do avanço
        resumo = f"✅ Avançou {paginas_saltadas} páginas. Agora na [bold green]página {self.pagina_atual}[/]"
        self.console.print(Panel(resumo, border_style="green", expand=False))

        if self.pagina_atual == self.total_paginas:
            self.console.print(f"[bold reverse red] 📕 FIM DO LIVRO: {self.titulo.upper()} [/]\n")

# --- Testando com Rich ---
l1 = Livro("10 coisas que aprendi", 120)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)