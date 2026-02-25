# 🦗 Projeto POO em Python – Exercício 01

Este projeto foi desenvolvido como o **primeiro exercício prático de Programação Orientada a Objetos (POO)** em Python.

O objetivo foi aplicar os conceitos básicos aprendidos durante os estudos iniciais de orientação a objetos.

---

## 📚 Conceitos Aplicados

Neste exercício foram utilizados:

- ✅ Declaração de Classe
- ✅ Método Construtor (`__init__`)
- ✅ Atributos de Instância
- ✅ Métodos de Instância
- ✅ Criação de Objetos
- ✅ Manipulação de atributos

---

## 🧠 Estrutura da Classe

A classe criada foi:
```python
class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"


Objetivo do Exercício

O foco foi entender:

Como funciona a criação de uma classe

Como o método construtor inicializa atributos

Como métodos modificam o estado do objeto

Como instanciar objetos na prática

Por se tratar do primeiro exercício, a implementação foi mantida simples para reforçar os fundamentos antes de avançar para conceitos mais complexos como herança, encapsulamento avançado e polimorfismo.

📌 Status do Projeto

✔ Exercício concluído
📖 Projeto voltado para aprendizado