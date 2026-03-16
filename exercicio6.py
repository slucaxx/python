import os
os.system("cls")

altura =float(input("informe sua altura pra saber seu IMC: "))
peso =float(input("informe seu peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"abaixo do peso")
elif  imc >= 18.5 and imc < 25:
    print(f"seu imc é {imc:.2f} peso ideal(PARABENS)")
elif imc >= 25.0 and imc < 30:
    print(f"seu imc é {imc:.2f} levemente acima do peso")
elif imc >= 30.0 and imc < 35:
    print(f"seu imc é {imc:.2f} obesidade grau 1")
elif imc >= 35 and imc < 40:
    print(f"seu imc é {imc:.2f} obesidade grau 2(severa)")
else:
    print(f"seu imc é {imc:.2f} obesidade 3(mórbida)")
