#47. Fac ̧ a um programa que apresente um menu de opc ̧  ̃oes para o c  ́alculo das seguintes
#operac ̧  ̃oes entre dois n  ́umeros:
#•adic ̧  ̃ao (opc ̧  ̃ao 1)
#•subtrac ̧  ̃ao (opc ̧  ̃ao 2)
#•multiplicac ̧  ̃ao (opc ̧  ̃ao 3)
#•divis  ̃ao (opc ̧  ̃ao 4).
#•sa ́ıda (opc ̧  ̃ao 5)
#O programa deve possibilitar ao usu  ́ario a escolha da operac ̧  ̃ao desejada, a exibic ̧  ̃ao do
#resultado e a volta ao menu de opc ̧  ̃oes. O programa s  ́o termina quando for escolhida a
#opc ̧  ̃ao de sa ́ıda (opc ̧  ̃ao 5)

while True:

    menu = int(input("""Menu Calculadora
    1 - Adição
    2 - Subtração
    3 - multiplicação
    4 - divisão
    5 - saída ---:  """))

    num1 = float(input("Entre com o primeiro número: "))
    num2 = float(input("Entre com o segundo número: "))

    if menu != 1 or menu != 2 or menu != 3 or menu != 4 or menu != 5:
        print("Escolha uma opção válida")

    elif menu == 1:
        print("Adição")
        soma = num1 + num2
        print(f"Soma = {soma}")

    elif menu == 2:
        print("Subtração")
        sub = num1 = num2
        print(f"Subtração = {sub}")

    elif menu == 3:
        print("Multiplicação")
        mult = num1 * num2
        print(f"Multiplicação = {mult}")

    elif menu == 4:
        print("Divisão")
        div = num1/num2
        print(f"Divisão = {div}")
    else:
        break








