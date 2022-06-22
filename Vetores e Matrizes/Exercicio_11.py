# 11. Faca um programa que preencha um vetor com 10 numeros reais, 
# calcule e mostre a
# quantidade de numeros negativos e a 
# soma dos numeros positivos desse veto

vetor = []
negativos = 0
positivos = 0

for c in range(10):
    vetor.append(float(input("Entre com os valores reais: ")))

for i in range(10):
    if vetor[i] < 0:
        negativos += 1
    elif vetor[i] >= 0:
        positivos += vetor[i]

print(f"A quantidade de Negativos é {negativos}")
print(f"A soma dos positivos no vetor é igual a {positivos}")
