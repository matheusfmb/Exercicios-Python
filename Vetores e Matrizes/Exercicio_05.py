#5. Leia um vetor de 10 posicoes.
#Contar e escrever quantos valores pares ele possui.

lista = []
pares = 0

for c in range(10):
    valor = int(input("Entre com os valores do vetor: "))
    lista.append(valor)
print(lista)

for i in lista:
    if i%2 == 0:
        pares+=1

print(pares)
