import os
os.system("cls")

altura =float(input("informe sua altura em metros(m): "))
peso =float(input("informe seu peso em kilos (kg): "))

def cal_imc(peso,altura):
    imc = peso / (altura * altura)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return  "abaixo do peso"," Consulte um nutricionista para orientação"
    elif  imc < 25:
        return "peso ideal, " ," Mantenha hábitos saudáveis!"
    elif imc >= 25.0 and imc < 30:
        return "acima do peso  " ," Considere uma dieta balanceada e atividade física."
    elif imc >= 30.0 and imc < 35:
        return "obesidade grau 1, " , "Procure orientação de um profissional de saúde." 
    elif imc >= 35 and imc < 40:
        return "obesidade grau 2, " , "Consulte um médico para avaliação e orientação."
    else:
        return "obesidade 3(mórbida), " ,"Busque assistência médica imediatamente."
    
resultado=cal_imc(peso,altura)
classificaçao,recomedação = classificar_imc(resultado)


print(f"o seu imc foi {resultado:.2f}")
print(f"a sua classificação foi {classificaçao}")
print(f"a sua recomendação  foi {recomedação}")
