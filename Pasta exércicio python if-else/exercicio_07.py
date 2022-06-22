"""7. Fac¸a um programa que receba dois numeros e mostre o maior. Se por acaso, os dois ´
numeros forem iguais, imprima a mensagem ´ N´umeros iguais."""

num1 = float(input("Entre com um número: "))
num2 = float(input("Entre com outro número: "))

if num1 > num2:
    print("Número 1 é maior")
elif num1 == num2:
    print("Números iguais")
else:
    print("Número 2 é maior")
