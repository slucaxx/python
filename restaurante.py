import os
os.system("cls")
total_pagar = 0

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
    
    escolha = int(input("Escolha o prato desejado (código) ou 0 para finalizar: "))
    
    if escolha == 0:
        break

    match escolha:
        case 1:
            print("Você adicionou Picanha (R$ 25,00)")
            total_pagar += 25.00
        case 2:
            print("Você adicionou Lasanha (R$ 20,00)")
            total_pagar += 20.00
        case 3:
            print("Você adicionou Strogonoff (R$ 18,00)")
            total_pagar += 18.00
        case 4:
            print("Você adicionou Bife Acebolado (R$ 15,00)")
            total_pagar += 15.00
        case 5:
            print("Você adicionou Pão com ovo (R$ 5,00)")
            total_pagar += 5.00
        case _:
            print("Opção inválida!")
            

    continuar = input("\nDeseja escolher outro prato? (S/N): ")
    if continuar != "S":
        break
    

print(f"O valor total a ser pago é: R$ {total_pagar:.2f}")
print("====== FIM DO ATENDIMENTO =====")