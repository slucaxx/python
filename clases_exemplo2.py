import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class cliente:
    nome:str
    email:str
    telefone:int


@dataclass
class funcionario:
    nome:str
    matricula:int
    email:str
    setor:str


cliente1= cliente("lucas", "lucassa1609@gmail.com", 71987810078)
funcionario1=funcionario("laise", 11021345 , "laiselindadms@gmail.com" , "norte")


print("======INFO CLIENTE======")
print(f"nome: {cliente1.nome} \nemail: {cliente1.email} \ntelefone: {cliente1.telefone}")
print()
print("======INFO FUNCIONARIO======")
print(f"nome: {funcionario1.nome} \nemail: {funcionario1.email} \nmatricula: {funcionario1.matricula} \nsetor: {funcionario1.setor}")