#9. Faca um programa que leia um numero inteiro N e depois imprima os N primeiros
#numeros naturais  ́ımpares


print("Gerador do n primeiros números ímpares positivos\n") 
n = int(input("Digite o valor de n: "))    
i = 0
ímpar = 1



while i < n:
    print(ímpar)
    ímpar = ímpar + 2
    i+=1