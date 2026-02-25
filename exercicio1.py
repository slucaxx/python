import os
os.system("cls")

# ENTRADA

n1 = int(input("por favor informe um numero: "))
n2 = int(input("informe outro numero: "))

# PROCESSAMENTO

s = n1 + n2
m = (n1 + n2) /2
p = n1 * n2

# SAIDA

print("a soma é {}".format(s))
print("a média é {}".format(m))
print("o produto é {}".format(p))
print("-----------------------------------------")

if n1 == n2:
   print("os numero informados são iguais \nportanto não tem maior ou menor numero")
else:
   maiorV = max(n1,n2)
   menorV = min(n1,n2)
 
   print("o maior valor é {} \n o menor valor é {}".format(maiorV,menorV))

 
