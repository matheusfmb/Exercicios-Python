
#14. Faca um programa que leia um numero inteiro positivo par N e imprima todos os numeros
#pares de 0 ate N em ordem decrescente.

import contextlib


cont = 0
num = int(input("Entre com um número par: "))


while cont <= 50:
    if num % 2 !=0:
        num = int(input("Entre com um número par: "))
    else:
        break
    cont += 1

while num >= cont:
    if num % 2 == 0:
        par = num
        print(par,end =" ")
    num-=1

