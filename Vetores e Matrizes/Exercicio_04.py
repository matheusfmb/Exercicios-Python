#4. Faca um programa que leia um vetor de 8 posicoes e, em seguida, leia tamb  ́em dois va-
#lores X e Y quaisquer correspondentes a duas posicoes no vetor. Ao final seu programa
#devera escrever a soma dos valores encontrados nas respectivas posicoes X e Y .

A = []

for c in range(8):
    adicionar = int(input("Entre com os números do vetor: "))
    A.append(adicionar)
print(A)
valor = int(input("Entre com um posição do vetor: 0-7: "))
valor1 = int(input("Entre com outro posição do vetor: 0-7: "))

soma = A[valor] + A[valor1]

print(soma)