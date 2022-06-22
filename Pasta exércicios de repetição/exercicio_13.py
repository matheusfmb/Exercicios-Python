#13. Faca um programa que leia um numero inteiro positivo par N e imprima todos os numeros
#pares de 0 ate N em ordem crescente.

cont = 0
num = int(input("Entre com um número par: "))


while cont <= 50:
    if num % 2 !=0:
        num = int(input("Entre com um número par: "))
    else:
        break
    cont += 1

while cont <= num:
    if cont % 2 == 0:
        par = cont
        print(par,end =" ")
    cont+=1



