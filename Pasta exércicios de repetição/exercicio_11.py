#11. Faca um programa que leia um numero inteiro positivo N e imprima todos os numeros
#naturais de 0 ate N em ordem crescente.

num = int(input("Entre com um número: "))
cont = 0

if num <= 0:
    print("Entre com um número maior que 0.")

while cont <= num:
    print(cont, end= " ")
    cont += 1




