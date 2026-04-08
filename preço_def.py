import os
os.system ("cls")

numero=int(input("digite o preço de um produto para saber a inflação: "))
def produto(n1):
    if numero <= 100:
        return numero * 1.10
    else:
        return numero * 1.20
    
preço =produto(numero)
print(f"o preço foi {preço} ")