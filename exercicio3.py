import os
os.system("cls")


n1 = int(input("informe um numero: "))
n2 = int(input("informe outro numero: "))

maiorN = max(n1,n2)
menorN = min(n1,n2)

print("os numeros informados foram {} e {} \no maior numero é {} e o menor é {}".format(n1,n2,maiorN,menorN))