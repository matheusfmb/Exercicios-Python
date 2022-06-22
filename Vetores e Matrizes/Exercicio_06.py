#6. Faca um programa que receba do usuario um vetor 
# com 10 posicoes. Em seguida devera
#ser impresso o maior e o menor elemento do vetor

lista = []

for c in range(10):
    list = int(input("Entre com valores do vetor: "))
    lista.append(list)

maior = max(lista)
menor = min(lista)

print(f"{maior} = Maior")
print(f"{menor} = Menor")