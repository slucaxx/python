import os
os.system("cls")

# ENTRADA

nota1 =float(input("digite sua primeira nota: "))
nota2 =float(input("digite sua segunda nota: "))
faltas =int(input("quantas faltas você teve? "))

media =(nota1 + nota2) /2
faltas_maximas = 40

if media >= 7 and faltas <= 40:
    print(f"sua média é {media},suas faltas {faltas}")
    print("APROVADO,meus parabens")
else:
    print(f"sua média é {media},sua faltas é {faltas}")
    print("REPROVADO,que pena")