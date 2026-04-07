import os 
os.system("cls")

def cal_medias(n1,n2):
    soma = num1 + num2
    media=soma /2
    return media

def veri_resultados(media):
    if media >= 7:
        resultado ="APROVADO"
    else:
        resultado ="REPROVADO"
        return resultado

print("------------------------------")
num1=int(input("digite a primeira nota: "))
num2=int(input("digite a segunda nota: "))


media=cal_medias(num1,num2)
resultado = veri_resultados (media)

print(f"media {media}")
print(f"resultados {resultado}")

