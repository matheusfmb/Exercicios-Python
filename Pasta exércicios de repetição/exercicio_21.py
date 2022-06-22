#21. Faca um programa que receba dois numeros. Calcule e mostre:
#•a soma dos numeros pares desse intervalo de n  ́umeros, incluindo os n  ́umeros digitados;
#•a multiplicacao dos numeros  ́ımpares desse intervalo, incluindo os digitado

from socket import SOCK_DGRAM


num1 = int(input("Entre com o número 1. começo do intervalo: "))
num2 = int(input("Entre com o número 2. final do intervalo: "))
cont = num1

if num1 %2 == 0 and num2 %2 ==0:
    soma = num1 + num2
elif num1 %2 == 0:
    soma = num1
elif num2 %2 == 0:
    soma = num2
else:
    soma = 0

if num1 %2 != 0 and num2 %2 != 0:
    multi = num1 * num2
elif num1 %2 != 0:
    multi = num1
elif num2 %2 != 0:
    multi = num2
else:
    multi = 1



while cont <= num2:
    if cont % 2 == 0:
        soma+=num1
        print(cont)
    elif cont % 2 !=0:
        multi*=cont
    cont+=1


print(f"A Soma dos pares do intervalo é {soma}")
print(f"multiplicação dos impares no invervalo é {multi:,.2f}")

