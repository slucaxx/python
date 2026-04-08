import os
os.system ("cls")

def conversão(n1):
    return n1 * 100

print("=SOLICITANDO DADOS= ")
num1=int(input("digite o numero em metros para converter para centimetros: "))
multi=conversão(num1)
print(f"a conversão é {multi}")