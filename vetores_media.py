import os
os.system("cls")

# criando um vetor
vetor_notas = []
QUANTIDADE_NOTAS=3

print("a,dicionando 3 notas")
# adicionando tres notas
for i in range(QUANTIDADE_NOTAS):
    nota=float(input(f"digite a {i+1}ª nota: "))
    vetor_notas.append(nota)
    
media=sum(vetor_notas) / QUANTIDADE_NOTAS
    
print("\nexibindo as notas informadas")
# ForEach
for i,uma_nota in enumerate(vetor_notas, start=1):
    print(f"{i}ª nota: {uma_nota}")
    
print(f"media {media}")
