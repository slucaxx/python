import os
os.system("cls")


soma = 0
QAUNTIDADE_NOTAS = 3
for i in range(QAUNTIDADE_NOTAS):
  while True:
      no=float(input(f"digite a {i+i}º nota: "))
      if   no >= 0 and no <= 10:
       soma +=no
       break
      else:
          print("nota invalidao")
          print("tente novamente.......")
        
media = soma /QAUNTIDADE_NOTAS
print(f"media {media}")       
print("parabens")   
print("======FIM======")