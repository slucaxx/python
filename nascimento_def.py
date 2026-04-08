import os
os.system ("cls")

anot=2026
nascimento=int(input("digite seu ano de nascimento: "))
def ano(n1):
    return  anot - nascimento 

ano_nas=ano(nascimento)
print(f"sua idade é {ano_nas}")