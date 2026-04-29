import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class cleinte:
    nome:str
    email:str
    telefone:str

print("==SOLICITANDOS DADOS DO CLIENTE===")

cliente=cleinte(
    nome=input("digite seu nome: "),
    email=input("digite seu email: "),
    telefone=input("digite seu telefone: "),)

print("\n=EXINBINDO RESULTADOS=")
print(f"nome: {cliente.nome} \nemail: {cliente.email} \ntelefone: {cliente.telefone}")