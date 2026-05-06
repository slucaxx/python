import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class livraria:
    nome:str
    autor:str
    categoria:str
    preco:float

    def mostra_dados(self):
        print(f"nome: {self.nome}")
        print(f"autor: {self.autor}")
        print(f"categoria: {self.categoria}")
        print(f"preço: {self.preco}")

print("------SISTEMA DE CADASTRO------")
print("1- adicionar livro")
print("2- listar livros")
print("3-sair")

QUANTIDADEL=3
livros= []

print("==solicitando dados===")
while True:
    for i in range(QUANTIDADEL):
        livro = livraria(
            nome=input(f"digite o nome do {i+1} livro: "),
            autor=input(f"digite o nome do {i+1} autor do livro: "),
            categoria=input(f"digite a {i+1} categoria: "),
            preco=float(input(f"digite o preço do {i+1} livro: "))
        )

        print()
        livros.append(livro)

        usuario=int(input("deseja adicionar mais um livro?")) 
        if usuario == 3:
                break

    print("==salvando dados==")
    with open("catalogo_livros.csv", "a" , encoding= "utf-8") as arquivo:
        for salva_livros in livros:
            arquivo.write(f"{salva_livros.nome} , {salva_livros.autor}, {salva_livros.categoria}, {salva_livros.preco}\n")

        print("salvo com sucesso!")

for salva_livros in livros:
    salva_livros.mostrar_dados()

print("=fim do programa")


