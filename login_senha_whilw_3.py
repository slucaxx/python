import os
os.system("cls")

login="lucassa"
senha="lczinx.x1"
tentativas=3

while True:
 for i in range(tentativas):
     log=str(input("digite seu login: "))
     sen=input("digite sua senha: ")
     if sen == senha and log == login:
        print("ACESSO PERMITIDO")
        break
     else:
      print("ACESSO NEGADO,login ou senha inválidos \ntente novamente........")
 print("acesso negado,numero de tentivas superada.")
 break