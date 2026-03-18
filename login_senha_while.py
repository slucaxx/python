import os
os.system("cls")

login = "lucassa"
senha= "lucassa.x1"
while True:
    log=str(input("digite seu login: "))
    sen=input("digite sua senha: ")
    if  sen == senha and  log == login:
        print("Acesso permitido") 
        break
    else:
        print("acesso negado \ntente novamente........")
    