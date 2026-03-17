import os
os.system("cls")

while True:
   idade=int(input("digite sua idade: "))
   if idade <18:
      print("Acesso negado!")
      print("Tente novamente... \n")
   else:
      print("Acesso permitido.")
      break #para a repetição
   
print("FIM")