#2. Crie um programa que l ˆe 6 valores inteiros e, em seguida, mostre
#  na tela os valores lidos

lista = []

for c in range(6):
    lista_add = int(input("Entre com os 6 valores: "))
    lista.append(lista_add)

print("Os valores lidos foram", lista)