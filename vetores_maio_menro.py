import os
os.system("cls")

vetor_n= []
QUANTIDADE_NU=5


for i in range(QUANTIDADE_NU):
    n=int(input(f"digite {i+1}ª numero: "))
    vetor_n.append(n)
    maior=max(vetor_n)
    menor=min(vetor_n)
          
print(f"o maior é {maior} e o menor numero é {menor}")