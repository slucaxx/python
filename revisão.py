import os
os.system ("cls")

import os

# Inicializando a lista para armazenar os resultados
resultados = []

def logo():
    os.system("cls")
    print("======== ========")
    print("====  SENAI  ====")
    print("======== ========")

def somar(a, b):
    resultado = a + b
    resultados.append(f"Soma: {resultado}") 
    return resultado

def subtrair(a, b):
    resultado = a - b
    resultados.append(f"Subtração: {resultado}")
    return resultado

def multiplicar(a, b):
    resultado = a * b
    resultados.append(f"Multiplicação: {resultado}")
    return resultado

def dividir(a, b):
    resultado = a / b
    resultados.append(f"Divisão: {resultado}")
    return resultado

# --- Fluxo Principal ---
logo()
print("= SOLICITANDO DADOS =")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


somar(n1, n2)
subtrair(n1, n2)
multiplicar(n1, n2)
dividir(n1, n2)

logo()
print("= EXIBINDO RESULTADOS DO VETOR =")


for item in resultados:
    print("\n---------------------------------------------------------")
    print(item)