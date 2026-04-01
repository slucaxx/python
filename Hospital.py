import os
os.system("cls")

vetor= []
total = 0

print("--------------MENU HOSPITAL------------")
while True:
    print("""
 
 CODIGO |          NOME                 |        PREÇO     | 
------------------------------------------------------------   
    1   |   HOMOGRAFIA COMPLETA         |    R$ 70,00  
    2   |         Raio-X                |    R$ 80,00
    3   |     Ultrassonografia          |    R$ 100,00
    4   |     Eletrocardiograma         |    R$ 120,00
    5   |        Tomografia             |    R$ 85,00
    6   |    Ressonância Magnética      |    R$ 150,00
    7   |     Exame de Glicose          |    R$ 50,00
-------------------------------------------------------------   
    """)

    esc=int(input("digite o codigo desejado para realizar o agendamento ou (0) para finalizar o atendimento .: "))
    
    if esc == 0:
        break
    
    
    match esc:
        case 1:
            print("você agendou  a  HOMOGRAFIA COMPLETA (R$ 70,00)")
            total += 70.00
            vetor.append("HOMOGRAFIA COMPLETA")
        case 2:
            print("você agendou  o  Raio-X   (R$ 80,00)")
            total += 80.00
            vetor.append("Raio-X ")
        case 3:
            print("você agendou  a Ultrassonografia   (R$ 100,00)")
            total += 100.00
            vetor.append("Ultrassonografia  ")
        case 4:
            print("você agendou  o Eletrocardiograma (R$ 120,00)")
            total += 120.00
            vetor.append("Eletrocardiograma ")
        case 5:
            print("você agendou  a Tomografia (R$ 85,00)")
            total += 85.00
            vetor.append("Tomografia ")
        case 6:
            print("você agendou  a Ressonância Magnética(R$ 150,00)")
            total += 150.00
            vetor.append("Ressonância Magnética   ")
        case 7:
            print("você agendou  oa Exame de Glicose   (R$ 50,00)")
            total += 50.00
            vetor.append("Exame de Glicose  ")
        case _:
            print("opção invalida")
            print("tente novamente........")
            
    continuar =input("\ndeseja escolher outro exame (S/N): ").upper ()
    if continuar != "S": 
        break
    
print("\nexames escolhidos:")

for exame in vetor:
    print("-", exame)

print(f"\nvalor total: R$ {total:.2f}")

    
print("""
formas de pagamento:
1 |Convênio (desconto de 15 porcento sobre o valor total).
2 |Particular (sem desconto).
3 |Cartão de crédito (acréscimo de 8 porcento sobre o valor total). """)
    
pagamento=float(input("digite o codigo desejado para realizar o pagamento: "))
if pagamento == 1:
    total= total * 0.15
    print("\ndesconto de 15% aplicado. ")
elif pagamento == 2:
    print("\nsem desconto")
elif pagamento == 3:
    total= total * 0.8
    print("\ndesconto de 8% aplicado")
else:
    print("\nopçao invalida")

print(f"a forma de pagamento escolhida foi {pagamento}")
print(f"\nvalor final a pagar: R$ {total:.2f}")

print ("--------FIM---------")
                    
    
    