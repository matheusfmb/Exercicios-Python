
import statistics

notas = []
acima_media = 0

print("Digite um número negativo para interromper a leitura de notas.")

while True:
    notas_alunos = float(input("Entre com as notas: "))
    if notas_alunos > 10:
        print("nota inválida")
        continue
    elif notas_alunos < 0:
        break
    else:
        notas.append(notas_alunos)

for i in range(len(notas)):
    if notas[i] >= 7:
        acima_media+=1
        


media = sum(notas)/len(notas)
desvio = statistics.pstdev(notas)


print(notas)
print(f"Soma das notas: {sum(notas)}")
print(f"Média das notas: {media:.2f}")
print(f"As notas acima da média {acima_media}")
print(f"O Desvio padrão foi {desvio:.3f}")

