import os
os.system("cls")
import time

pares=0
imparares=0

print("--------NUMEROS IMPARES E PARES-----------")
for i in range(1,6):
    n=int(input(f"{i} digite um numero: "))
    if n % 2 == 0:
      pares += 1
    else:
      imparares += 1

print(f"Total de números PARES:   {pares}")
print(f"Total de números ÍMPARES: {imparares}")