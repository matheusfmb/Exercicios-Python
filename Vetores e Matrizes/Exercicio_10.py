#10. Faca um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
#e imprima a m  ́edia geral

notas = []
media = 0

for c in range(15):
    nota = float(input("Entre com as notas: "))
    notas.append(nota)
    media += nota

print(media/15)
