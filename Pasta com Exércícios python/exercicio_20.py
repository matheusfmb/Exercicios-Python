'''20. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A f  ́ormula
de convers  ̃ao  ́e: L = K
0,45, sendo K a massa em quilogramas e L a massa em libras.'''

K = float(input("Entre com o valor em quilogramas: "))
L = K/0.45

print(f"A conversão para libras é {L:.2f} Lb")
