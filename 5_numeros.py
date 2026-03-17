import os
os.system("cls")
import time

print("---------ANALISE DE DADOS------------")
soma=0

for i in range(1,6):
    n=int(input("digite um numero: "))
    soma=soma + n

print("a soma de todos os numeros informados é {soma}")