'''2. Leia um numero fornecido pelo usu ´ ario. Se esse n ´ umero for positivo, calcule a raiz ´
quadrada do numero. Se o n ´ umero for negativo, mostre uma mensagem dizendo que o ´
numero ´ e inv ´ alido'''
import math

num = int(input("Entre com um número: "))

if num >= 0:
    raiz = math.sqrt(num)
    print(f"A raiz quadrada é: {raiz:.3f}")
else:
    print("Número inválido")