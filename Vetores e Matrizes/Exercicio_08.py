#8. Crie um programa que l ˆe 6 valores 
# inteiros e, em seguida, mostre na tela
#  os valores lidos
#na ordem inversa.

lista = []

for c in range(1,7):
    lista.append(int(input("Entre com os valores do vetor: ")))
print(lista)
lista.reverse()
print(lista)
    
