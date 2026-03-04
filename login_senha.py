import os
os.system("cls")

# ENTRADA

print("-----ANALISE DE LOGIN E SENHA-----")
login =input("digite seu login: ")
senha =input("digite sua senha: ")

login_correto = ("lucassa")
senha_correta = ("lczinx.x1")

print("-----SAIDA DE DADOS-----")
if login == login_correto and senha == senha_correta:
    print(f"ola {login} bem vindo")
else:
    print("login ou senha invalidos")