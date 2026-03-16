import os
os.system("cls")

print("------APROVAÇÃO BANCARIA PARA COMPRA DE CASA---------")

Vcasa =float(input("digite o valor da casa desejada: "))
salario =float(input("digie o seu salário aual: "))
anos =int(input("em quantos anos dejesa pagar a casa? "))

parcela = anos * 12
prestacao =Vcasa / parcela
minimo = salario * 0.3
print(f"para pagar um casa de R${Vcasa} em {anos} anos a prestação será de R${prestacao:.2f}")
if prestacao <= minimo:
    print("Empresimo pode ser concedido")
else:
    print("emprestimo negado")