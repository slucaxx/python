import os 
os.system("cls")

matriculas = 11021345
senhas = "lczinx.x1"

def sistema():
    os.system("cls")
    print("="*30)
    print("SISTEMA DE PAGAMENTO")
    print("="*30)

sistema()

def login(mat, sen):

        matricula = int(input("Digite sua matrícula: "))
        senha = input("Digite sua senha: ")

        if matricula == mat and senha == sen:
            print("ACESSO PERMITIDO \nBEM VINDO!")
            return True
        else:
            print("ACESSO NEGADO")
            return False

def calcular_inss(salario):
    if salario <= 1518:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09
    elif salario <= 4190.83:
        return salario * 0.12
    elif salario <= 8157.41:
        return salario * 0.14
    else:
        return 951.62 
    
def calcular_irrf(base):
    if base <= 2428.80:
        return 0
    elif base <= 2826.65:
        return base * 0.075
    elif base <= 3751.05:
        return base * 0.15
    elif base <= 4664.68:
        return base * 0.225
    else:
        return base * 0.275

sistema ()
def pagamento():
    if entra:
        salariob= int(input("Qual seu salário? "))
        vale_trans = input("Deseja receber vale transporte? (s/n): ").upper()
        vale_refe=int(input("Qual o valor do vale refeições? "))
        dependentes=int(input("qual a qauntidade de dependente? "))

        plan_saude=dependentes * 150
        
        valor_refe_total=vale_refe * 0.20

        if vale_trans == "S":
                descontov=salariob * 0.06
        else:
                descontov=0


        inss = calcular_inss(salariob)

    
        base_irrf = salariob - inss

  
        irrf = calcular_irrf(base_irrf)

    
        total_desc = plan_saude + descontov + valor_refe_total + inss + irrf


        salario_liquido = salariob - total_desc

    
        print("\n===== HOLERITE =====")
        print(f"Salário bruto: R$ {salariob:.2f}")
        print(f"INSS: R$ {inss:.2f}")
        print(f"IRRF: R$ {irrf:.2f}")
        print(f"Vale transporte: R$ {valor_refe_total:.2f}")
        print(f"Vale refeição (20%): R$ {dependentes:.2f}")
        print(f"Plano de saúde: R$ {plan_saude:.2f}")
        print(f"Total de descontos: R$ {total_desc:.2f}")
        print(f"Salário líquido: R$ {salario_liquido:.2f}")


entra = login(matriculas, senhas)
if entra:
    sistema()
    pagamento()




