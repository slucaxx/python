import os
os.system("cls")

nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota: "))

media = (nota1 + nota2) /2

if media >= 9:
    print(f"APROVADO! sua media é {media} você tirou um A")
elif media >= 7.5 or media < 9:
    print(f"APROVADO! sua média é {media} você tirou um B")
elif media >= 6 or media < 7.5:
    print (f"APROVADO! sua media é {media} você tirou um C")
elif media >= 4 or media  < 6:
    print(f"REPROVADO! sua media é {media} você tirou um D")
else:
    print(f"REPROVADO! sua média {media} você tirou um E")

