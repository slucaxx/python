import os 
os.system("cls")

def tabuada(n1):
   for i in range(0,11):
      tabua = n1 * i
      print(f"{n1} x {i} = {tabua}")
num1=int(input("digite um numero para saber sua tabuada: "))
tabuada(num1)
