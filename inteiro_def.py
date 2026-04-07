import os 
os.system("cls")

def inteiros(n1):
    if n1 < 0:
        print(f"o numero é negativo ({numero})")
    else:
        print(f"o numero é positivo ({numero})")

numero=int(input("digite o numero para saber se é positivo ou negativo: "))
inteiros(numero)
