import os
os.system("cls")

# ENTRADA
aposentadoria:int
tp_trab:int
matricula:str

aposentadoria =int(input("digite sua idade para saber se estar apto para se aposentar: "))
print("--------------------------")

tp_trab =int(input("digite seu tempo de trabalho: "))
print("--------------------------")
matricula =int(input("digite sua matricula de empregado: "))
print("--------------------------")
nascimento =str(input("digite seu ano de nascimento: "))
print("--------------------------")
# PROCESSAMENTO
if aposentadoria >= 65 or tp_trab >= 30:
    resultado =("você pode se aposentar")
    
else:
    resultado =("você não  pode se aposentar")


# SAIDA

print("---RESULTADO----")
print("você tem {} anos,\no resesultado da aposentadoria foi que {} \no tempo de trabalho foi {}".format(aposentadoria,resultado,tp_trab))



