import os
os.system("cls")

pares=0
impares=0
vetor=[]
NOTAS=6

for i in range(NOTAS):
    n=int(input(f"digite o {i+1}ª numero: "))
    vetor.append(n)
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"total de pares {pares} \ne o total de impartes {impares}")
    
