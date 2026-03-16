import os
os.system("cls")
import time

print("-------------TABUADA-------------")
n1=int(input("digite um numero: "))

for i in range(1,11):
    tabuada= n1 * i
    print(f"{n1} x {i} = {tabuada}")
    time.sleep(0.5)
