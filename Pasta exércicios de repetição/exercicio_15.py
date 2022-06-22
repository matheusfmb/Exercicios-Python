#15. Faca um programa que leia um n  ́umero inteiro positivo  ́ımpar N e imprima todos os
#numeros  ́ımpares de 1 at  ́e N em ordem crescente.



cont = 0
while 0 <= 100:
    num = int(input("Entre com um número impar: "))
    if num % 2 != 1:
        print("Número inválido. (par) ")
    else:
        break

while cont <= num:
    if cont % 2 == 1:
        impar = cont
        print(impar, end= " ")
    cont +=1
    


