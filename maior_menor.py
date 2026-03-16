import os
os.system("cls")

print("------MAIOR,MENOR E IGUAL----------")

n1=int(input("digite um numero: "))
n2=int(input("digite outro numero: "))

maior = max(n1,n2)
nao_existe = (n1 == n2)

if n1 > n2:
    print(f" entre {n1} e {n2} o maior numero é o primeiro ({maior}) ")
elif n2 > n1:
    print(f"entre {n1} e {n2} o maior numero é o segundo ({maior}) ")
elif nao_existe :
    print("nao existe valor maior os dois são iguas")

print("=====FIM=====")
