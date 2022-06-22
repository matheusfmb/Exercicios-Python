import math
import numpy
print("Calculadora de raízes de uma equação de 2º Grau.")
print("Ex: equação de 2º Grau - x**2+bx+c")
a = float(input("Entre com o valor de A: "))
b = float(input("Entre com o valor de B: "))
c = float(input("Entre com o valor de C: "))

delta= (b**2) - (4*a*c)
raiz_p =  (- b + (delta**(0.5)))/2*a
raiz_n =  (- b - (delta**(0.5)))/2*a

if delta < 0:
    print("Não existe raiz.")
elif delta == 0:
    print("Existe uma raiz")
    print(f"{raiz_p}")
else:
    print(f""" raiz+ = {raiz_p:.2f}
    raiz- = {raiz_n:.2f}""")

