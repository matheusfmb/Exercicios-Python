'''8. Fac¸a um programa que leia 2 notas de um aluno, verifique se as notas sao v ˜ alidas e ´
exiba na tela a media destas notas. Uma nota v ´ alida deve ser, obrigatoriamente, um ´
valor entre 0.0 e 10.0, onde caso a nota nao possua um valor v ˜ alido, este fato deve ser ´
informado ao usuario e o programa termina.'''

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))

if nota1 < 0 or nota2 < 0:
    print("Nota inválida. informe um valor acima de 0")
elif nota1 or nota2 >= 0:
    media = (nota1+nota2)/2
print(f"Sua média é: {media}")