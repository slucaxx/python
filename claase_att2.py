import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome:str
    cnpj: int
    telefone:int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}"),
        print(f"telefone: {self.telefone}")
        print(f"cnpj: {self.cnpj}\n")

QUANTIDADE_FUNCIONARIOS = 1
lista_funcionarios = []


print("=Solicitando dados=")
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionario(
        nome=input("Digite  nome da empresa: "),
        telefone=int(input("Digite o telefone da empresa: ")),
        cnpj=int(input("Digite o cnpj da empresa: ")),
    )
    print('')
    lista_funcionarios.append(novo_funcionario)



    print("= Exibindo dados =")
    for funcionario in lista_funcionarios:
        funcionario.mostrar_dados()

    print("= Salvando dados = ")
    with open("contrato_empresa.csv", "a" , encoding="utf-8") as arquivo:
        for funcionario in lista_funcionarios:
            arquivo.write(f"{funcionario.nome}, {funcionario.cnpj} , {funcionario.telefone}\n")
        print("Salvo com sucesso!!")

print("= Fim do programa =")