'''9. Leia o salario de um trabalhador e o valor da prestac¸ ´ ao de um empr ˜ estimo. Se a ´
prestac¸ao for maior que 20% do sal ˜ ario imprima: ´ Empr´estimo n~ao concedido, caso
contrario imprima: ´ Empr´estimo concedido.'''

salario = float(input("Entre com seu salário: "))
prestacao = float(input("Entre com o valor da prestação: "))



if prestacao < salario * 0.2:
    print("Empréstimo concedido")
else:
    print("Empréstimo não concedido.")