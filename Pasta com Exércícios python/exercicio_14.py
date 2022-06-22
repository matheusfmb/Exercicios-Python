'''14. Leia um ˆangulo em graus e apresente-o convertido em radianos. A f  ́ormula de convers  ̃ao
 ́e: R = G ∗π/180, sendo G o ˆangulo em graus e R em radianos e π = 3.14. '''

graus = float(input("Entre com o Ângulo em graus º: "))
radianos = (graus*3.14)/180

print("O Resultado em radianos é:", "%.3f" %radianos)