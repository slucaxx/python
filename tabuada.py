import os
os.system("cls")
import time

print("--------------TABUADA----------------")
n=int(input("digite um, numero: "))

for i in range(1,11):
    tabuada=n * i
    print("-----")
    print(f"{n} x {i} = {tabuada}")
    time.sleep(0.5)