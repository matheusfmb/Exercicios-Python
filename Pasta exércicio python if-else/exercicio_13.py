#13. Faca um algoritmo que calcule a m  ́edia ponderada das notas de 3 provas. A primeira e
#a segunda prova t ˆem peso 1 e a terceira tem peso 2. Ao final, mostrar a m  ́edia do aluno
#e indicar se o aluno foi aprovado ou reprovado. A nota para aprovac ̧  ̃ao deve ser igual ou
#superior a 60 pontos.


print("************************************************************")
print("************CALCULADORA DE MÉDIA PONDERADA******************")
print("************************************************************")

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))

media_ponderada = (nota1*1 + nota2*1 + nota3*2)/4

if media_ponderada > 6.0:
    print(f"Você está aprovado, sua média foi: {media_ponderada:.2f}")
else:
    print(f"Você foi reprovado sua média foi: {media_ponderada:.2f}")


