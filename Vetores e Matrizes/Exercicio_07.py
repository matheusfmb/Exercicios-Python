#7. Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor.
#Imprima
#o vetor, o maior elemento e a posic ̧  ̃ao que ele se encontra.

lista = []

for c in range(5):
    list = int(input("Entre com valores do vetor: "))
    lista.append(list)

maior = max(lista)

print(lista.index(maior))
print(lista)
print(maior)




