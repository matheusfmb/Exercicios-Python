#3. Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado das
#componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos t ˆem
#10 elementos cada. Imprimir todos os conjuntos

lista_reais = []
quadrados = []

for c in range(6):
    reais = int(input("Entre com os valores reais do vetor: "))
    lista_reais.append(reais)
for i in lista_reais:
    quadrados.append(i**2)

print("Vetor",lista_reais)
print("Vetor ao Quadrado", quadrados)