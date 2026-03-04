import os
os.system("cls")

print("----SOLICITANDO DADOS------")
ano_nascimento =int(input("digite seu ano de nascimento "))
sexo = input("digite seu sexo: ").lower()

idade =  2026 - ano_nascimento

id_obrig = idade >= 18
sexo_obrigatorio = sexo =="masculino"

if idade >= id_obrig and sexo == sexo_obrigatorio:
    print(f"{idade} anos deve se apresentar aos serviços militares")
else:
    print(f"{idade} anos nao é necessario se apresentar aos serviços militares")