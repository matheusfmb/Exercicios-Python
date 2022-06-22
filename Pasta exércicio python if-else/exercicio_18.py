
num1 = float(input("Entre com um número: "))
num2 = float(input("Entre com outro número: "))
operacao = int(input("""Entre com o número da operação desejada:
*************************
1. soma
2. subtração2
3. multiplicação
4. divisão
*************************-: """ ))

if operacao == 1:
    soma = num1  + num2
    print(f"Soma é igual a: {soma:.2f}")
elif operacao == 2:
    subtracao = num1  - num2
    print(f"Subtração é igual a: {subtracao:.2f}")
elif operacao == 3:
    multiplicacao = num1  * num2
    print(f"multiplicação é igual a: {multiplicacao:.2f}")
elif operacao == 4:
    if num2 == 0:
        print("Não existe divisor por 0. Entre com um outro número")
    else: 
        divisao = num1/num2
        print(f"Divisão é igual a: {divisao:.2f}")
else: 
    print("Entre com um número de operação válido entre 1 e 4.")

