#19. Faca um programa para verificar se um determinado numero inteiro e divisıvel por 3 ou
#5, mas nao simultaneamente pelos dois.

num1 = int(input("Entre com um número inteiro: "))

if num1%3 == 0 and num1%5 ==0:
    print("É divisivel por 5 e 3")
elif num1%3 == 0:
    print("É divisível por 3")
elif num1%5 == 0:
    print("É divisível por 5")
