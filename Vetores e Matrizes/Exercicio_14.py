
# 14. Faca um programa que leia um vetor de 10 posicoes e 
# verifique se existem valores iguais
# e os escreva na tela.

lista = []
repetidos = []
rep = 0 

for i in range(5):
    valor = int(input("Entre com os valores: "))
    lista.append(valor)

lista.sort()

for j in range(0,len(lista)-1):
    print(lista)
    if lista[j] == lista [j+1]:
        valor = lista[j]
        repetidos.append(valor)
        valor = 0
    else:
        continue

print(lista)
print("------------")
print(repetidos)

