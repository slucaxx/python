import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []
imcs= []
classificoes=[]


def cal_imc(altura,peso):
    imc = peso / (altura * altura)
    return imc

def classi_imc(imc):
    if imc < 18.5:
        return  "abaixo do peso"
    elif  imc < 25:
        return "peso ideal"
    elif imc >= 25.0 and imc < 30:
        return "acima do peso  "
    elif imc >= 30.0 and imc < 35:
        return "obesidade grau 1 "
    elif imc >= 35 and imc < 40:
        return "obesidade grau 2, "
    else:
        return "obesidade 3(mórbida), "
    

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o seu sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))

    
    resultado=cal_imc(altura,peso)
    classificação=classi_imc(resultado)

    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)
    imcs.append(resultado)
    classificoes.append(classificação)

resultado=cal_imc(altura,peso)
classificação=classi_imc(resultado)



# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print()
    print(f"O imc foi, {imcs[i]:.2f}")
    print("A classificação foi ", classificoes[i])
    print()