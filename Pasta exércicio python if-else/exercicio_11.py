# 11. Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a ´
# soma de todos os seus algarismos. Por exemplo, ao numero 251 corresponder ´ a o valor ´
# 8 (2 + 5 + 1). Se o numero lido n ´ ao for maior do que zero, o programa terminar ˜ a com a ´
# mensagem “Numero inv ´ alido”.

from re import U
import uu


num = int(input("Entre com um número inteiro: "))
u = num //1 %10
d = num //10 %10
c = num //100 %10
m = num //1000 %10


if num <= 0:
    print("Número Inválido")
elif num >= 1 and num <= 99:
    print (f"{d} + {u}")
elif num >= 100 and num <= 999:
    print(f"{c} + {d} + {u}")
elif num >= 1000:
    print(f"{m} + {c} + {d} + {u}")



