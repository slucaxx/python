import os
os.system("cls")
import time

print("--------------------CONTAGEM REGRESSIVA---------------------")
n=int(input("digite um numero: "))
for i in range(n,0,-1):
    print(i)
    time.sleep(1)

print("============FIM================")