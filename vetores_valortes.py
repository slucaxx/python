import os
os.system("cls")

vetor=[]
NU=5

for i in range(NU):
    num = int(input(f"Digite o {i+1}º número: "))
    
    if num < 0:
        num = 0
    
    vetor.append(num)

print("\n--- Valores do Vetor ---")
print(vetor)