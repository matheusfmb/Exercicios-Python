#19. Escreva um algoritmo que leia um numero inteiro entre 100 e 999 e imprima na sa ́ıda
#cada um dos algarismos que compoem o número



while True:
    num = int(input("Entre com um número entre 100 e 999: ")) 
    if num < 100 or num > 999:
        print("Número inválido")
    elif num >= 100 and num <= 999:

        unidade = num % 10
        num = (num - unidade)/10

        dezena = num % 10

        numero = (num - dezena)/10
        centena = numero

        print(f"{centena:.0f} -- {dezena:.0f} -- {unidade} ")
        sair = input("Deseja sair? S/N: ").upper()
        if sair == "N":
            continue
        else:
            break





