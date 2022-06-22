# 35. Fac ̧ a um programa que some os n  ́umeros impares contidos em um intervalo definido
# pelo usu  ́ario. O usu  ́ario define o valor inicial do intervalo e o valor final deste intervalo
# e o programa deve somar todos os n  ́umeros  ́ımpares contidos neste intervalo. Caso o
# usu  ́ario digite um intervalo inv  ́alido (comec ̧ando por um valor maior que o valor final) deve
# ser escrito uma mensagem de erro na tela, “Intervalo de valores inv  ́alido” e o programa
# termina. Exemplo de tela de sa ́ıda: Digite o valor inicial e valor final: 5
# 10
# Soma dos  ́ımpares neste intervalo: 21
while True:
    num1 = int(input("Entre com o início do intervalo: "))
    num2 = int(input("Entre com o final do intervalo: "))
    soma_i = 0
    soma_p = 0
    multi_i = 1
    multi_p = 1
    x = num1

    if num1 >= num2:
        print("intervalo Inválido")
        continue
    else:
        while x <= num2:
            if x%2 != 0:
                soma_i+=x
                multi_i*=x
            else:
                soma_p+=x
                multi_p*=x
            x+=1

        print(f"..A soma dos impares do intervalo é {soma_i} e a multiplicação dos ímpares é {multi_i}")
        print(f"..A soma dos pares do intervalo é {soma_p} e a multiplicação dos pares é {multi_p}")
        break

    

