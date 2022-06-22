'''6. Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, ´
assim como a diferenc¸a existente entre ambos'''

num1 = int(input("Entre com um número1 inteiro: "))
num2 = int(input("Entre com um número2 inteiro: "))

if num1 > num2:
    dif = num1 - num2
    print(f"Num 1 é maior e a diferença é igual a: {dif}")
else:
    dif = num2 - num1
    print(f"Num 2 é maior e a diferença é igual a: {dif}")
