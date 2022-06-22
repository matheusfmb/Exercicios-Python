#7. Faca um programa que leia 10 inteiros positivos, ignorando n  ̃ao positivos, e imprima sua
#media

n = 1
soma = 0

while n <= 10:
    if n > 0:
        num = int(input(f"Entre com {n} número: "))
        soma += num
    elif n <= 0:
        soma += 0
    n +=1
print(f"A média é {soma/10}")