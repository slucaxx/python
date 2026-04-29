import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class paciente:
    nome:str
    idade:int
    peso:float
    altura:float

print("====PEDINDO DADOS====")i0uiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii89cjjjjjj

pacientes=paciente(
    nome=input("digite seu nome: "),
    idade=int(input("digite sua idade: ")),
    peso=float(input("digite seu peso: ")),
    altura=float(input("digite sua altura: ")))

print("===INFORMAÇÕES DO PACIENTE====")
print(f"nome: {pacientes.nome} \nidade {pacientes.idade} \npeso {pacientes.peso} \naltura {pacientes.altura}")