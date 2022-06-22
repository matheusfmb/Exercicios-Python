#4. Fac¸a um programa que leia um numero e, caso ele seja positivo, calcule e mostre: ´
#• O numero digitado ao quadrado ´
#• A raiz quadrada do numero digitado
import math

num = float(input("Entre com um número: "))

if num >= 0:
    quadrado = num**2
    raiz = math.sqrt(num)
    print (f"O número ao quadrado é: {quadrado} e sua raiz é: {raiz:.2f}") 
else:
    print("Número inválido")

