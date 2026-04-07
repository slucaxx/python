import os
os.system("cls")

def somar(n1,n2):
    soma = n1 + n2
    return soma   
        
n1=int(input("digite o primeiro numero : "))
n2=int(input("digite o segundo numero : "))
resultado = somar(n1,n2)
print(f"soma {resultado}")