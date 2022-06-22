#9. Crie um programa que 
#le 6 valores inteiros pares e, 
#em seguida, mostre na tela os valores
#lidos na ordem inversa

lista = []
pares = 0


while pares < 6:
    valores = int(input("Entre com os Valores: "))
    if valores % 2 ==0:
        lista.append(valores)
        pares+=1
    else:
        print("Apenas valores pares!")
        continue
    
lista.reverse()
print(lista)

