import os
os.system("cls")
import time

print("---------APROVADO ou REPROVADO----------")
soma=0

for i in range(1,4):
    n=float(input(f"digite a {i} nota: "))
    soma += n

media=soma / 3       
if media >= 7:
        print(f"APROVADO,sua media é ({media}) parabens")
elif media <= 6.9:
        print(f"RECUPERAÇÃO,sua media é ({media}) sinto muito")
elif media <4:
        print(f"REPROVADO,sua media é ({media})")

