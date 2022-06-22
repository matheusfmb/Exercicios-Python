#12. Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem “Numero
#invalido”. Se o numero for positivo, calcular o logaritmo deste numero.

import math

num = int(input("Entre com o número inteiro: "))

if num > 0:
    logaritimo = math.log10(num)
    print(f"O logarítimo é {logaritimo:.2f}")
else:
    print("Número inválido.")

