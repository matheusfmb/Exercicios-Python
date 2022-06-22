# 12. Fazer um programa para ler 5 valores e, 
# em seguida, mostrar todos os valores lidos
# juntamente com o maior, o menor e a m  ́edia dos valores

lista = []
media = 0

for i in range(5):
    valores = int(input("Entre com os valores: "))
    lista.append(valores)
    media += valores
maior = max(lista)
menor = min(lista)

print(lista)
print("Maior = ",maior)
print("Menor = ", menor)
print("Média = ", media/5)


