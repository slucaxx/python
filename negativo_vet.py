import os
os.system("cls")

soma = 0
vetor= []
NU = 5
negativo=0

for i in range(NU):
    n=int(input(f"digite  o {i+1}ª numnero: "))
    vetor.append(n)
    
for n in vetor:
    if n < 0:
       negativo += 1
    elif n > 0:
        soma +=  n                          

print(f"a quantidade de numeros negativos é {negativo} \ne a somna dos numeros positivfos é {soma}") 