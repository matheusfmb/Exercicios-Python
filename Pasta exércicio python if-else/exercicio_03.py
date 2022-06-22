#3. Leia um numero real. Se o numero for positivo imprima a raiz quadrada. Do contr ´ ario, ´
#mprima o numero ao quadrado.'''
import math

num = float(input("Entre com um número real: "))

if num >= 0:
    raiz = math.sqrt(num)
    print(f"A raiz quadrada desse número é: {raiz:.2f}")
else:
    quadrado = num**2
    print(f"O quadrado desse número é: {quadrado:.2f}")

