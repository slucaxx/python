import os 
os.system("cls")

def pares(n1):
    if n1 % 2 == 0:
        print("o numero é pár")
    else:
        print("o numero é impar")

numero=int(input("digite o numero para saber se é par ou impar: "))
pares(numero)
