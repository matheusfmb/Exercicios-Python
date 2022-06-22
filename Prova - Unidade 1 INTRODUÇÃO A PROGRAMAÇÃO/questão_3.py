
indice_participantes = []
numero_jogadas = []
cont = 0
cont2 = 0

while True:
    participantes = int(input("Entre com o número de participantes: "))
    if participantes <= 1:
        print("Número de participantes inválidos")
        continue
    else:
        indice_participantes = [i for i in range(1,participantes+1)]
        break
    
while cont < participantes:
    jogadas = int(input(f"Entre com a jogada do particiapante {cont+1} : "))
    if jogadas < 0 or jogadas > 10:
        print("Jogada Inválida")
        continue
    else:
        numero_jogadas.append(jogadas)
        cont+=1

total_jogadas = sum(numero_jogadas)
print(f"Total {total_jogadas}")
while total_jogadas != 0:
    cont2 += 1
    if cont2 > len(indice_participantes):
        cont2 = 0
        cont2 += 1 
    total_jogadas -= 1


print(f"O ganhador é o participante {indice_participantes[cont2-1]}")

















    





