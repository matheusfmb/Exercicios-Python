'''15. Leia um ˆangulo em radianos e apresente-o convertido em graus. A f  ́ormula de convers  ̃ao
 ́e: G = R ∗180/π, sendo G o ˆangulo em graus e R em radianos e π = 3.14.
'''
R = float(input("Entre com o valor em radianos: "))
graus = (R*3.14)/180

print("O resultado em graus: ", "%.2f" %graus)