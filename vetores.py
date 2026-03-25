import os
os.system("cls")

# criando um vetor
vetor_notas = []
QUANTIDADE_NOTAS=3

print("a dicionando 3 notas")
# adicionando tres notas
for i in range(QUANTIDADE_NOTAS):
    nota=float(input(f"digite a {i+1}ª nota: "))
    vetor_notas.append(nota)
    
print("\nexibindo as notas informadas")
# ForEach
for uma_nota in vetor_notas:
    print(f"nota: {uma_nota}")
