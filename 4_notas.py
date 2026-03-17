import os
os.system("cls")
import time

print("-----------ANILISE DE DADOS---------")
soma=0
for i in range(1,5):
    n=float(input(f"digite a {i} nota: "))
    soma += n

media=soma /4
print(f"a media das suas notas é ({media}) ")