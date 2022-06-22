#21. Escreva o menu de opcoes abaixo. Leia a opcao do usu  ́ario e execute a operacao esco-
#lhida. Escreva uma mensagem de erro se a opcao for invalida.
#scolha a op ̧c~ao:
#1- Soma de 2 n ́umeros.
#2- Diferenca entre 2 n ́umeros (maior pelo menor).
#3- Produto entre 2 numeros.
#4- Divis~ao entre 2 numeros (o denominador n~ao pode ser zero).
#opçãO

operacao = int(input(""" Entre com a operação 
 *******************************
 1. soma de 2 números.
 2. diferença entre dois números.
 3. produto entre dois números.
 4. divisão entre dois números.
 ******************************--:"""))
 

num1 = float(input("Entre com o primeiro numero: "))
num2 = float(input("Entre com o primeiro numero: "))


if operacao == 1:
    resultado = (num1+num2)
    print(f"O resultado da operação soma  de 2 números é: {resultado:.2f}")
elif operacao == 2:
    resultado = (num1-num2)
    print(f"O resultado da operação diferença entre os 2 números é: {resultado:.2f}")
elif operacao == 3:
    resultado = (num1*num2)
    print(f"O resultado da operação produto entre dois números é: {resultado:.2f}")
elif operacao == 4:
    if num2 == 0:
        print("O denominador não pode ser 0.")
    else: 
        resultado = (num1/num2)
        print(f"O resultado da operação divisão entre dois números é: {resultado:.2f}")
else:
    print("Entre com um uma valor de operação entre 1 a 4.")