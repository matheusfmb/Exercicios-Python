#22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
#uma sequencia arbitraria de notas (validas no intervalo de 10 a 20) e que mostre na tela,
#como resultado, a correspondente media aritmetica. O numero de notas com que o aluno
#pretenda efetuar o calculo nao será fornecido ao programa, o qual terminara quando for
#introduzido um valor que nao seja valido como nota de aprovacao
import time

soma_notas = 0
divisao_notas = 0
nota_invalida = 0
nota_valida = 0

while 0 < 10:
    print("Notas Válidas [10,20]")
    nota = float(input("Entre com a nota: "))
    if nota < 10 or nota > 20:
        print("Nota Inválida. Na próxima nota inválida o programa irá fechar.")
        nota_invalida = nota_invalida + 1
        time.sleep(0.5)
    else:
        nota_valida +=1

    if nota_invalida == 1:
        nota = 0
        
    elif nota_invalida == 2:
        break

    elif nota_valida >= 1:
        soma_notas = soma_notas + nota
        divisao_notas += 1
    
    if divisao_notas >= 2:
        media = soma_notas/divisao_notas
        print(f"A média ponderada é {media:.2f} ")
    

    

    
    


    
    