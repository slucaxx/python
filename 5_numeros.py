import os
os.system("cls")

print("----------------ANALISE DE DADOS------------------")

soma = 0

for i in range(1, 6):
    n = int(input(f"Digite o {i}º número: "))
    soma = soma + n 
print(f"\nA soma de todos os números lidos é: {soma}")
