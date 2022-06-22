#17. Faca um programa que leia um numero inteiro positivo n e calcule a soma dos n primeiros
#numeros naturais
cont = 0
soma = 0
while True:
    num = int(input("Entre com um número: "))
    if num < 0: 
        print ("Ente com um número positivo.")
    else:
        break  

while cont <= num:
    soma = soma + cont
    cont +=1

print(F"A soma nos (N) primeiros números de (N) é = {soma}")