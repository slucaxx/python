import os
os.system("cls")

altura =float(input("informe sua altura pra saber seu IMC: "))
peso =float(input("informe seu peso: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("abaixo do peso")
elif imc >= 18.6 or 24.9:
    print(f"seu imc é {imc:.2f} peso ideal(PARABENS)")
elif imc >= 25.0 or imc <= 29.9:
    print(f"seu imc é {imc:.2f} levemente acima do peso")
elif imc >= 30.0 or imc <= 34.9:
    print(f"seu imc é {imc:.2f} obesidade grau 1")
elif imc >= 35.5 or 39.9:
    print(f"seu imc é {imc:.2f} obesidade grau 2(severa)")
else:
    print(f"seu imc é {imc:.2f} obesidade 3(mórbida)")

