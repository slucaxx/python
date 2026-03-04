import os
os.system("cls")

# MENU

print("""
===============MENU===================
 Código     Prato                 Valor

  1         Picanha               25,00
  2         Lasanha               20,00 
  3         Strogonoff            18,00 
  4         Bife Acebolado        15,00
  5         Pao com ovo           5,00       
""")
prato =int(input("escolha o prato desejado digitando o codigo: "))

match prato:
    case 1:
       print("você escolheu picanha e o valor do prato é 25,00" )
    case 2:
       print("você escolheu lasanha e o valor do prato é 20,00" )
    case 3:
       print("você escolheu strogonoff e o valor do prato é 18,00" )
    case 4:
       print("você escolheu bife acebolado e o valor do prato é 15,00" )
    case 5:
       print("você escolheu pao com ovo e o valor do prato é 5,00" )
    case _:
       print("opção invalida" )
    
print("======FIM=====")


