import os
os.system("cls")

vetor_n = []
QUANTIDADES_DE_NOTAS = 4

for i in range(QUANTIDADES_DE_NOTAS):
    n=float(input(f"digite a {i+1}ª nota: "))
    vetor_n.append(n)
media=sum(vetor_n) / QUANTIDADES_DE_NOTAS  
if media >= 7:
        print(f"APROVADO,media{media}")
elif media >= 5 and media <=6.9:
        print(f"RECUPERAÇÃO,media{media}")
else:
        print(f"REPROVADO,media{media}")
    
    
    
for i,uma_nota in enumerate(vetor_n, start =1):
     print(f"{i}ª nota {uma_nota}")
   


