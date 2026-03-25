import os
import time

soma=0
opção=0
contador=0
somaf=0
maiors=0
menors=0

while True:
    os.system("cls")
    print("""
---MENU DA PESQUISA---
1- ADICIONAR FAMILIA
2-SAIR E EXIBIR RESULTADOS
""")
    opção=int(input("digite a opção desejada: "))
    
    match opção:
        case 1:
            print("--CADASTRO-----=")
            familias=int(input("quntos filhos tem na cidade? "))
            salario=int(input("digite o salario: "))
            
            soma += salario
            contador += 1
            somaf =+familias
            
            if contador ==1:
                maiors =salario
                menors=salario
            else:
                if salario > maiors:
                    maiors = salario
                if  salario > menors:
                    menors = salario
                
            print("---FAMILIA ADICIONADA----")
            time.sleep(5)
        case 2:
            if contador == 0:
                print("\nnenhuma pessoa cadastrada.\n") 
            
            else:
                medias=soma / contador
                mediaf=somaf / contador
                print(f"o total de filhos foi {familias}")
                print(f"a media de salario da população é {medias} e a media de familia é {mediaf}")
                print(f"o maior salario foi {maiors}")
                print(f"o menor salario foi {menors}")
                print("=========FIM==========")
                break
        case _:
            print("\nopção invalida\n")
   