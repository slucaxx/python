import os
os.system("cls")

quantidade = int(input("informe a quantidade de maçãs desejadas: "))

if quantidade < 12:
   preco = 1.30
else:
  preco = 1.00

valor =  quantidade * preco

print("a quantidade foi {} maçãs, o preço por unidade foi R$ {:.2f}".format(quantidade,preco))
print("o valor total é R${}".format(valor))

 