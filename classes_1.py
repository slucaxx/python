import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade:int

@dataclass
class Pet:
    nome:str
    idade:int

pessoa1=Pessoa("Alice",30)
pessoa2=Pessoa("bob",20)
pet1=Pet("lua",5)
pet2=Pet("Milli", 11)


print(f"Nome: {pessoa1.nome} \nIdade: {pessoa1.idade} ")
print()
print(f"Nome: {pessoa2.nome}  \nIdade: {pessoa2.idade} ")
print()
print(f"Nome: {pet1.nome}  \nIdade: {pet1.idade} ")
print()
print(f"Nome: {pet2.nome}  \nIdade: {pet2.idade} ")
