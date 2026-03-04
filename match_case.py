import os
os.system("cls")

# EXEMPLO DE ESTRUTURA CONDICIONNAL ANINHADA
#MATH CASE SUBISTITUI O USO DO IF-ELIF-ELSE

dia = input("digiti o dia da semana")

match dia:
    case"segunda":
        print("hoje é segunda feira.")
    case"terça":
        print("hoje é terça feira.")
    case"quarta":
        print("hoje é qurta feira.")
    case"quinta":
        print("hoje é quinta feira.")
    case"sexta":
        print("hoje é sexta feira.")
    case"sabado" | "domingo":
        print("hoje é fim de semana")
    case_:
        print("dia invalido")
        
        
print(dia)
print("===fim==")
        