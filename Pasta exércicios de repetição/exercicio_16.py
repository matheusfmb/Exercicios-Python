#16. Fac ̧ a um programa que leia um n  ́umero inteiro positivo  ́ımpar N e imprima todos os
#numeros  ́ımpares de 1 ate N em ordem decrescente.

from multiprocessing.pool import IMapIterator


cont = 0
while 0 <= 100:
    num = int(input("Entre com um número impar: "))
    if num % 2 != 1:
        print("Número inválido.")
    else:
        break

while num >= cont:
    if num % 2 == 1:
        impa = num
        print(impa, end =" ")
    num -=1


