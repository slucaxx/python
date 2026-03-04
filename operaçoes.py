import os
os.system("cls")


n1=int(input("digite um numero: "))
n2=int(input("digite outro numero: "))
oper =input("escolha operação dejesada (+ ,-,*,/): ")

soma =n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisao = n1 / n2

match oper:
    case"+":
        print(f"o resultado foi {soma}")
    case"-":
        print(f"o resultado foi {subtração}")
    case"*":
        print(f"o resultado foi {multiplicação}")
    case"/":
        print(f"o resultado foi {divisao}")
    case _:
        print("opção invalida")
        

print("====FIM====")