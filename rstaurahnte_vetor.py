import os
os.system("cls")
total = 0
vetor= []

while True:
    print("""
=============== MENU ===================
 Código     Prato                 Valor

  1         Picanha               25.00
  2         Lasanha               20.00 
  3         Strogonoff            18.00 
  4         Bife Acebolado        15.00
  5         Pao com ovo           5.00       
========================================
    """)
    
    esc=int(input("digite o numero do prato desejado ou digite 0 para finalizar: "))
    
    if esc == 0:
        break
    
    match esc:
        case 1:
            print("Você adicionou Picanha (R$ 25,00)")
            total += 25.00
            vetor.append("picanha")
        case 2:
            print("Você adicionou lasanha (R$ 20.00)")
            total += 20.00
            vetor.append("lasanha")
        case 3:
            print("Você adicionou Strogonoff (R$ 18,00)")
            total += 18.00
            vetor.append("Strogonoff")
        case 4:
            print("Você adicionou Bife Acebolado (R$ 15,00)")
            total += 15.00
            vetor.append("Bife Acebolado")
        case 5:
            print("Você adicionou Pão com ovo (R$ 5,00)")
            total += 5.00
            vetor.append("Pão com ovo")
        case _:
            print("Opção inválida!")
            

    continuar = input("\nDeseja escolher outro prato? (S/N): ").upper()
    if continuar != "S":
        break
 
print("---------------------------------------------------------------")   
print("os pratos escolhidos por você foi")
for prato in vetor:
    print(f"- {prato}")
print(f"O valor total a ser pago é: R$ {total:.2f}")
print("====== FIM DO ATENDIMENTO =====")