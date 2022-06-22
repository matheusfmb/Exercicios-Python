#8. Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor ´
#lido.

cont = 2
num = float(input("Digite o valor do numero 1: "))
guarda_maior = num
guarda_menor = num


while cont <= 10:
    num = float(input(f"Digite o valor do numero {cont:.0f}: "))

    if num > guarda_maior:
        guarda_maior = num

    elif num < guarda_menor: 
        guarda_menor = num
        print(f" guarda menor passou a ser = {guarda_menor}")

    cont+=1
    
print(f"O Maior é {guarda_maior} e o menor é {guarda_menor}")



    