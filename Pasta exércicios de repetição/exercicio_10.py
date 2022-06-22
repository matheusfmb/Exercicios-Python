#0. Faca um programa que calcule e mostre a soma dos 50 primeiros numeros pares
#  

cont = 1
soma = 0

while cont <= 100:
    if cont % 2 == 0:
        par = cont
        soma += cont
        print(par, end = " ")
    cont +=1
print(f" A soma dos 50 valores pares é {soma}")





'''#include <stdio.h>  

int main() {  

int num, i, soma=0;  

for (i=1; i<=100; i++) {  

if (i % 2 == 0)

soma += i;  

}  

printf("Soma dos 50 primeiros números é: %d\n", soma);  

return 0;  

}
        '''

