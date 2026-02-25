import os
os.system('cls')

idade = int(input("informe sua idade: "))

if  idade < 16: 
    print("você não pode votar")
elif idade == 16 or idade == 17 or idade  >65:
    print("seu voto é opcional")
else:
    print("seu voto é obrigatorio")
            